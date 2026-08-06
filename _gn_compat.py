# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import re


__all__ = (
    "kiri_gn_get",
    "kiri_gn_set",
    "kiri_gn_has",
    "kiri_gn_layout_prop",
    "kiri_gn_layout_prop_search",
    "kiri_gn_property_exists",
)


_MISSING = object()
_SOCKET_PATH = re.compile(
    r"^(?P<base>.+)\[(?P<quote>['\"])(?P<identifier>Socket_\d+(?:_(?:use_attribute|attribute_name))?)(?P=quote)\]$"
)


def _socket_identifier(prop):
    if not isinstance(prop, str):
        return None
    if prop.startswith("Socket_"):
        return prop
    if len(prop) >= 5 and prop[:2] == '["' and prop[-2:] == '"]':
        identifier = prop[2:-2]
        return identifier if identifier.startswith("Socket_") else None
    if len(prop) >= 5 and prop[:2] == "['" and prop[-2:] == "']":
        identifier = prop[2:-2]
        return identifier if identifier.startswith("Socket_") else None
    return None


def _split_identifier(identifier):
    if identifier.endswith("_use_attribute"):
        return identifier[: -len("_use_attribute")], "use_attribute"
    if identifier.endswith("_attribute_name"):
        return identifier[: -len("_attribute_name")], "attribute_name"
    return identifier, "value"


def _interface_item(modifier, identifier):
    interface = getattr(modifier, "properties", None)
    if interface is None:
        return None, None

    base_identifier, member = _split_identifier(identifier)
    for collection_name in ("inputs", "outputs"):
        collection = getattr(interface, collection_name, None)
        if collection is not None and hasattr(collection, base_identifier):
            return getattr(collection, base_identifier), member
    return None, member


def _enum_property(item):
    try:
        prop = item.bl_rna.properties["value"]
    except (AttributeError, KeyError, TypeError):
        return None
    return prop if prop.type == "ENUM" else None


def _legacy_menu_value(item, value):
    enum_prop = _enum_property(item)
    if enum_prop is None:
        return value
    if not value:
        return -1
    for enum_item in enum_prop.enum_items:
        if enum_item.identifier == value:
            return enum_item.value
    return -1


def _modern_menu_value(item, value):
    enum_prop = _enum_property(item)
    if enum_prop is None:
        return value
    if isinstance(value, int):
        for enum_item in enum_prop.enum_items:
            if enum_item.value == value:
                return enum_item.identifier
        if value == -1:
            return ""
    if isinstance(value, str):
        for enum_item in enum_prop.enum_items:
            if value in {enum_item.identifier, enum_item.name}:
                return enum_item.identifier
    return value


def kiri_gn_get(modifier, identifier, default=_MISSING):
    item, member = _interface_item(modifier, identifier)
    if item is None:
        if getattr(modifier, "properties", None) is not None:
            if default is not _MISSING:
                return default
            raise KeyError(identifier)
        try:
            return modifier[identifier]
        except (KeyError, TypeError):
            if default is not _MISSING:
                return default
            raise

    try:
        if member == "use_attribute":
            return item.type == "ATTRIBUTE"
        if member == "attribute_name":
            return item.attribute_name
        return _legacy_menu_value(item, item.value)
    except AttributeError:
        if default is not _MISSING:
            return default
        raise KeyError(identifier)


def kiri_gn_set(modifier, identifier, value):
    item, member = _interface_item(modifier, identifier)
    if item is None:
        if getattr(modifier, "properties", None) is not None:
            return value
        modifier[identifier] = value
        return value

    if member == "use_attribute":
        item.type = "ATTRIBUTE" if value else "VALUE"
    elif member == "attribute_name":
        item.attribute_name = value
    else:
        item.value = _modern_menu_value(item, value)
    return value


def kiri_gn_has(modifier, identifier):
    item, member = _interface_item(modifier, identifier)
    if item is not None:
        if member == "value":
            return hasattr(item, "value")
        return hasattr(item, member if member != "use_attribute" else "type")
    try:
        return identifier in modifier
    except TypeError:
        return False


def kiri_gn_layout_prop(layout, data, prop, *args, **kwargs):
    identifier = _socket_identifier(prop)
    if identifier is not None:
        item, member = _interface_item(data, identifier)
        if item is not None:
            target_prop = {
                "value": "value",
                "use_attribute": "type",
                "attribute_name": "attribute_name",
            }[member]
            if hasattr(item, target_prop):
                return layout.prop(item, target_prop, *args, **kwargs)
    return layout.prop(data, prop, *args, **kwargs)


def kiri_gn_layout_prop_search(layout, data, prop, search_data, search_property, *args, **kwargs):
    identifier = _socket_identifier(prop)
    if identifier is not None:
        item, member = _interface_item(data, identifier)
        if item is not None:
            target_prop = "attribute_name" if member == "attribute_name" else "value"
            if hasattr(item, target_prop):
                return layout.prop_search(
                    item,
                    target_prop,
                    search_data,
                    search_property,
                    *args,
                    **kwargs,
                )
    return layout.prop_search(data, prop, search_data, search_property, *args, **kwargs)


def kiri_gn_property_exists(prop_path, glob, loc):
    try:
        eval(prop_path, glob, loc)
        return True
    except Exception:
        match = _SOCKET_PATH.match(prop_path)
        if match is None:
            return False
        try:
            modifier = eval(match.group("base"), glob, loc)
        except Exception:
            return False
        return kiri_gn_has(modifier, match.group("identifier"))
