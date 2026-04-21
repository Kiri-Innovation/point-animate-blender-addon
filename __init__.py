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

bl_info = {
    "name" : "Point Animate by KIRI Engine",
    "author" : "BLUE NILE 3D", 
    "description" : "",
    "blender" : (4, 2, 0),
    "version" : (1, 0, 3),
    "location" : "N Panel",
    "warning" : "Uninstall before updating",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "Animation" 
}


import bpy
import bpy.utils.previews
import os
import webbrowser


addon_keymaps = {}
_icons = None


def sna_update_start_frame_325FE(self, context):
    sna_updated_prop = self.start_frame
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_14'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_14'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Mesh_To_Points_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Mesh_To_Points_GN']['Socket_4'] = sna_updated_prop
    bpy.context.view_layer.objects.active.update_tag(refresh={'OBJECT'}, )
    if bpy.context and bpy.context.screen:
        for a in bpy.context.screen.areas:
            a.tag_redraw()


def sna_update_point_scale_min_A5ACF(self, context):
    sna_updated_prop = self.point_scale_min
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Mesh_To_Points_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Mesh_To_Points_GN']['Socket_7'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_11'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_67'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_95'] = sna_updated_prop
    bpy.context.view_layer.objects.active.update_tag(refresh={'OBJECT'}, )
    if bpy.context and bpy.context.screen:
        for a in bpy.context.screen.areas:
            a.tag_redraw()


def sna_update_point_scale_attribute_2C65A(self, context):
    sna_updated_prop = self.point_scale_attribute
    input_attribute = sna_updated_prop
    output_value = None
    # Define the dictionary with 'attribute_string' as the key and 'attribute_int' as the value
    attribute_mapping = {
        'No Attribute Influence': 0,
        'Timeline:1-0': 1,
        'Timeline:0-1': 2,
        'Timeline:20%-80%=1-0': 3,
        'Timeline:20%-80%=0-1': 4,
        'Timeline:0%-50%=1-0': 5,
        'Timeline:0%-50%=0-1': 6,
        'Timeline:1-0-1': 7,
        'Timeline:0-1-0': 8,
        'Timeline:20%-50%-80%=1-0-1': 9,
        'Timeline:20%-50%-80%=0-1-0': 10,
        'Isactive (if using Wind)': 11,
        'Age (if using Wind)': 12
    }
    output_value = attribute_mapping.get(input_attribute, None)  # Returns None if not found
    # Now you can use `output_value` directly in your script
    print(f"The corresponding integer value for '{input_attribute}' is {output_value}")
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_72'] = output_value
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_69'] = output_value
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_97'] = output_value
    bpy.context.view_layer.objects.active.update_tag(refresh={'OBJECT'}, )
    if bpy.context and bpy.context.screen:
        for a in bpy.context.screen.areas:
            a.tag_redraw()


def sna_update_end_frame_22369(self, context):
    sna_updated_prop = self.end_frame
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_28'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_28'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Mesh_To_Points_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Mesh_To_Points_GN']['Socket_5'] = sna_updated_prop
    bpy.context.view_layer.objects.active.update_tag(refresh={'OBJECT'}, )
    if bpy.context and bpy.context.screen:
        for a in bpy.context.screen.areas:
            a.tag_redraw()


def sna_update_point_scale_max_0E8A0(self, context):
    sna_updated_prop = self.point_scale_max
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Mesh_To_Points_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Mesh_To_Points_GN']['Socket_8'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_71'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_68'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_96'] = sna_updated_prop
    bpy.context.view_layer.objects.active.update_tag(refresh={'OBJECT'}, )
    if bpy.context and bpy.context.screen:
        for a in bpy.context.screen.areas:
            a.tag_redraw()


def sna_update_scale_random_5C353(self, context):
    sna_updated_prop = self.scale_random
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Mesh_To_Points_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Mesh_To_Points_GN']['Socket_6'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_10'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_10'] = sna_updated_prop
    if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers):
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_94'] = sna_updated_prop
    bpy.context.view_layer.objects.active.update_tag(refresh={'OBJECT'}, )
    if bpy.context and bpy.context.screen:
        for a in bpy.context.screen.areas:
            a.tag_redraw()


def property_exists(prop_path, glob, loc):
    try:
        eval(prop_path, glob, loc)
        return True
    except:
        return False


def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id


def sna_update_enable_decimate_897F9(self, context):
    sna_updated_prop = self.enable_decimate
    sna_turn_modifier_on_off_function_execute_C4736(sna_updated_prop, 'KIRI_Point_Animate_Decimate_GN')


def sna_update_enable_crop_box_C5D8F(self, context):
    sna_updated_prop = self.enable_crop_box
    sna_turn_modifier_on_off_function_execute_C4736(sna_updated_prop, 'KIRI_Point_Animate_Crop_Box_GN')


def sna_update_enable_wind_0B2A0(self, context):
    sna_updated_prop = self.enable_wind
    sna_turn_modifier_on_off_function_execute_C4736(sna_updated_prop, 'KIRI_Point_Animate_Wind_GN')
    if sna_updated_prop:
        sna_turn_modifier_on_off_function_execute_C4736(False, 'KIRI_Point_Animate_Morph_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_morph = False


def sna_update_enable_morph_2583F(self, context):
    sna_updated_prop = self.enable_morph
    sna_turn_modifier_on_off_function_execute_C4736(sna_updated_prop, 'KIRI_Point_Animate_Morph_GN')
    if sna_updated_prop:
        sna_turn_modifier_on_off_function_execute_C4736(False, 'KIRI_Point_Animate_Wind_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wind = False


def sna_update_enable_noise_19878(self, context):
    sna_updated_prop = self.enable_noise
    sna_turn_modifier_on_off_function_execute_C4736(sna_updated_prop, 'KIRI_3DGS_Point_Animate_Noise_GN')


def sna_update_enable_snap_141CD(self, context):
    sna_updated_prop = self.enable_snap
    sna_turn_modifier_on_off_function_execute_C4736(sna_updated_prop, 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN')


def sna_update_enable_wireframe_CAA02(self, context):
    sna_updated_prop = self.enable_wireframe
    sna_turn_modifier_on_off_function_execute_C4736(sna_updated_prop, 'KIRI_Point_Animate_Wireframe_GN')


def sna_crop_function_interface_7E647(layout_function, ):
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_crop_box:
        pass
    else:
        box_39A95 = layout_function.box()
        box_39A95.alert = True
        box_39A95.enabled = True
        box_39A95.active = True
        box_39A95.use_property_split = False
        box_39A95.use_property_decorate = False
        box_39A95.alignment = 'Expand'.upper()
        box_39A95.scale_x = 1.0
        box_39A95.scale_y = 1.0
        if not True: box_39A95.operator_context = "EXEC_DEFAULT"
        box_39A95.label(text='Crop Box is disabled', icon_value=0)
    box_7D30A = layout_function.box()
    box_7D30A.alert = False
    box_7D30A.enabled = bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_crop_box
    box_7D30A.active = True
    box_7D30A.use_property_split = False
    box_7D30A.use_property_decorate = False
    box_7D30A.alignment = 'Expand'.upper()
    box_7D30A.scale_x = 1.0
    box_7D30A.scale_y = 1.0
    if not True: box_7D30A.operator_context = "EXEC_DEFAULT"
    box_7D30A.label(text='Crop Method', icon_value=0)
    attr_9667D = '["' + str('Socket_4' + '"]') 
    box_7D30A.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Crop_Box_GN'], attr_9667D, text='', icon_value=0, emboss=True, slider=True)
    if ((bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Crop_Box_GN']['Socket_4'] == 2) or (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Crop_Box_GN']['Socket_4'] == 1)):
        attr_F6B6F = '["' + str('Socket_3' + '"]') 
        box_7D30A.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Crop_Box_GN'], attr_F6B6F, text='Crop Object', icon_value=0, emboss=True, slider=True)
    if ((bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Crop_Box_GN']['Socket_4'] == 3) or (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Crop_Box_GN']['Socket_4'] == 4)):
        attr_31C1B = '["' + str('Socket_5' + '"]') 
        box_7D30A.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Crop_Box_GN'], attr_31C1B, text='Distance Threshold', icon_value=0, emboss=True, slider=True)


def sna_decimate_function_interface_36876(layout_function, ):
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_decimate:
        pass
    else:
        box_F44E9 = layout_function.box()
        box_F44E9.alert = True
        box_F44E9.enabled = True
        box_F44E9.active = True
        box_F44E9.use_property_split = False
        box_F44E9.use_property_decorate = False
        box_F44E9.alignment = 'Expand'.upper()
        box_F44E9.scale_x = 1.0
        box_F44E9.scale_y = 1.0
        if not True: box_F44E9.operator_context = "EXEC_DEFAULT"
        box_F44E9.label(text='Decimate is disabled', icon_value=0)
    box_9BCC5 = layout_function.box()
    box_9BCC5.alert = False
    box_9BCC5.enabled = bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_decimate
    box_9BCC5.active = True
    box_9BCC5.use_property_split = False
    box_9BCC5.use_property_decorate = False
    box_9BCC5.alignment = 'Expand'.upper()
    box_9BCC5.scale_x = 1.0
    box_9BCC5.scale_y = 1.0
    if not True: box_9BCC5.operator_context = "EXEC_DEFAULT"
    box_9BCC5.label(text='Decimate Percentage', icon_value=0)
    attr_5D31E = '["' + str('Socket_25' + '"]') 
    box_9BCC5.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Decimate_GN'], attr_5D31E, text='', icon_value=0, emboss=True, slider=True)


def sna_add_point_animate_modifiers_button_CA918(layout_function, ):
    if (bpy.context.view_layer.objects.active == None):
        pass
    else:
        if ((property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Mesh_To_Points_GN' in bpy.context.view_layer.objects.active.modifiers) and (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Color_Convert_GN' in bpy.context.view_layer.objects.active.modifiers) and (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Decimate_GN' in bpy.context.view_layer.objects.active.modifiers) and (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Crop_Box_GN' in bpy.context.view_layer.objects.active.modifiers) and (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers) and (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers) and (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers) and (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN' in bpy.context.view_layer.objects.active.modifiers) and (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wireframe_GN' in bpy.context.view_layer.objects.active.modifiers) and (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Viewport_Display_GN' in bpy.context.view_layer.objects.active.modifiers) and (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Set_Material_GN' in bpy.context.view_layer.objects.active.modifiers)):
            pass
        else:
            if bpy.context.view_layer.objects.active.type == 'MESH':
                box_D6EEB = layout_function.box()
                box_D6EEB.alert = True
                box_D6EEB.enabled = True
                box_D6EEB.active = True
                box_D6EEB.use_property_split = False
                box_D6EEB.use_property_decorate = False
                box_D6EEB.alignment = 'Expand'.upper()
                box_D6EEB.scale_x = 1.0
                box_D6EEB.scale_y = 2.0
                if not True: box_D6EEB.operator_context = "EXEC_DEFAULT"
                op = box_D6EEB.operator('sna.add_point_edit_modifiers_aafc2', text='Add Point Animate Modifiers', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'plus.svg')), emboss=True, depress=False)


class SNA_OT_Add_Point_Edit_Modifiers_Aafc2(bpy.types.Operator):
    bl_idname = "sna.add_point_edit_modifiers_aafc2"
    bl_label = "Add Point Edit Modifiers"
    bl_description = "Adds a series of animation modifiers to the selected object with deafult settings."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_add_point_edit_modifiers_function_execute_D32BB()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_append_and_add_geo_nodes_function_execute_9EF47(modifier_name, Assetpath, Nodegroupname):
    if (property_exists("bpy.data.node_groups", globals(), locals()) and modifier_name in bpy.data.node_groups):
        pass
    else:
        before_data = list(bpy.data.node_groups)
        bpy.ops.wm.append(directory=Assetpath + r'\NodeTree', filename=Nodegroupname, link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.node_groups)))
        appended_F282A = None if not new_data else new_data[0]
    modifier_0D938 = bpy.context.view_layer.objects.active.modifiers.new(name=modifier_name, type='NODES', )
    modifier_0D938.node_group = bpy.data.node_groups[Nodegroupname]


def sna_turn_modifier_on_off_function_execute_C4736(onoff, modifier_name):
    bpy.context.view_layer.objects.active.modifiers[modifier_name].show_on_cage = onoff
    bpy.context.view_layer.objects.active.modifiers[modifier_name].show_in_editmode = onoff
    bpy.context.view_layer.objects.active.modifiers[modifier_name].show_viewport = onoff
    bpy.context.view_layer.objects.active.modifiers[modifier_name].show_render = onoff
    bpy.context.view_layer.objects.active.update_tag(refresh={'OBJECT'}, )
    if bpy.context and bpy.context.screen:
        for a in bpy.context.screen.areas:
            a.tag_redraw()


def sna_add_point_edit_modifiers_function_execute_D32BB():
    if (len(bpy.context.view_layer.objects.selected) > 1):
        self.report({'ERROR'}, message='Only select 1 object please.')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_Point_Animate_Mesh_To_Points_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_Point_Animate_Mesh_To_Points_GN')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_Point_Animate_Color_Convert_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_Point_Animate_Color_Convert_GN')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_Point_Animate_Decimate_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_Point_Animate_Decimate_GN')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_Point_Animate_Crop_Box_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_Point_Animate_Crop_Box_GN')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_Point_Animate_Wind_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_Point_Animate_Wind_GN')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_Point_Animate_Morph_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_Point_Animate_Morph_GN')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_3DGS_Point_Animate_Noise_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_3DGS_Point_Animate_Noise_GN')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_3DGS_Point_Animate_Snap_To_Shape_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_Point_Animate_Wireframe_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_Point_Animate_Wireframe_GN')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_Point_Animate_Viewport_Display_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_Point_Animate_Viewport_Display_GN')
    sna_append_and_add_geo_nodes_function_execute_9EF47('KIRI_3DGS_Point_Animate_Set_Material_GN', os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend'), 'KIRI_3DGS_Point_Animate_Set_Material_GN')
    sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_Point_Animate_Mesh_To_Points_GN')
    sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_Point_Animate_Color_Convert_GN')
    sna_turn_modifier_on_off_function_execute_C4736(False, 'KIRI_Point_Animate_Decimate_GN')
    sna_turn_modifier_on_off_function_execute_C4736(False, 'KIRI_Point_Animate_Crop_Box_GN')
    sna_turn_modifier_on_off_function_execute_C4736(False, 'KIRI_Point_Animate_Wind_GN')
    sna_turn_modifier_on_off_function_execute_C4736(False, 'KIRI_Point_Animate_Morph_GN')
    sna_turn_modifier_on_off_function_execute_C4736(False, 'KIRI_3DGS_Point_Animate_Noise_GN')
    sna_turn_modifier_on_off_function_execute_C4736(False, 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN')
    sna_turn_modifier_on_off_function_execute_C4736(False, 'KIRI_Point_Animate_Wireframe_GN')
    sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_Point_Animate_Viewport_Display_GN')
    sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_3DGS_Point_Animate_Set_Material_GN')
    bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_72'] = 0
    bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_69'] = 0
    bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_97'] = 0
    bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.point_scale_attribute = 'No Attribute Influence'
    bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Color_Convert_GN']['Socket_33'] = 0.0020000000949949026
    bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_11'] = 0.0020000000949949026
    bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_67'] = 0.0020000000949949026
    bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Color_Convert_GN']['Socket_34'] = 0.029999999329447746
    bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_71'] = 0.029999999329447746
    bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_68'] = 0.029999999329447746
    bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_96'] = 0.029999999329447746
    bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.point_scale_min = 0.0020000000949949026
    bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.point_scale_max = 0.029999999329447746
    bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_decimate = False
    bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_crop_box = False
    bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wind = False
    bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_morph = False
    bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_noise = False
    bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_snap = False
    bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wireframe = False
    for i_AC295 in range(len(bpy.context.view_layer.objects.active.modifiers)):
        for i_9F9B2 in range(len(bpy.context.view_layer.objects.active.modifiers[i_AC295].bakes)):
            bpy.context.view_layer.objects.active.modifiers[i_AC295].bakes[i_9F9B2].bake_mode = 'ANIMATION'
    bpy.ops.object.material_slot_add('INVOKE_DEFAULT', )
    if (property_exists("bpy.data.materials", globals(), locals()) and 'POINTANIMATE_MATERIAL' in bpy.data.materials):
        pass
    else:
        before_data = list(bpy.data.materials)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'KIRI_Point_Animate_1.0.0_APPEND.blend') + r'\Material', filename='POINTANIMATE_MATERIAL', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.materials)))
        appended_8D816 = None if not new_data else new_data[0]
    bpy.context.view_layer.objects.active.material_slots[bpy.context.view_layer.objects.active.active_material_index].material = bpy.data.materials['POINTANIMATE_MATERIAL']
    bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Set_Material_GN']['Socket_6'] = bpy.data.materials['POINTANIMATE_MATERIAL']
    bpy.context.view_layer.objects.active.update_tag(refresh={'OBJECT'}, )
    if bpy.context and bpy.context.screen:
        for a in bpy.context.screen.areas:
            a.tag_redraw()


def sna_run_bake_node_function_execute_00810(Modifier):
    bpy.ops.object.geometry_node_bake_single('INVOKE_DEFAULT', session_uid=bpy.context.view_layer.objects.active.modifiers[Modifier].bakes[int(len(bpy.context.view_layer.objects.active.modifiers[Modifier].bakes) - 1.0)].id_data.session_uid, modifier_name=Modifier, bake_id=bpy.context.view_layer.objects.active.modifiers[Modifier].bakes[int(len(bpy.context.view_layer.objects.active.modifiers[Modifier].bakes) - 1.0)].bake_id)


def sna_remove_bake_node_function_execute_80F90(Modifier):
    for i_95102 in range(len(bpy.context.view_layer.objects.active.modifiers[Modifier].bakes)):
        bpy.ops.object.geometry_node_bake_delete_single('INVOKE_DEFAULT', session_uid=bpy.context.view_layer.objects.active.modifiers[Modifier].bakes[i_95102].id_data.session_uid, modifier_name=Modifier, bake_id=bpy.context.view_layer.objects.active.modifiers[Modifier].bakes[i_95102].bake_id)


class SNA_OT_Append_Wire_Sphere_F21B7(bpy.types.Operator):
    bl_idname = "sna.append_wire_sphere_f21b7"
    bl_label = "Append Wire Sphere"
    bl_description = "Appends an object for use as a modifier effector. The object will not render."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        before_data = list(bpy.data.objects)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Wireframe Objects.blend') + r'\Object', filename='Wire Sphere', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
        appended_CD42E = None if not new_data else new_data[0]
        appended_CD42E.location = bpy.context.scene.cursor.location
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Append_Wire_Cube_D69Fb(bpy.types.Operator):
    bl_idname = "sna.append_wire_cube_d69fb"
    bl_label = "Append Wire Cube"
    bl_description = "Appends an object for use as a modifier effector. The object will not render."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        before_data = list(bpy.data.objects)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Wireframe Objects.blend') + r'\Object', filename='Wire Cube', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
        appended_DE242 = None if not new_data else new_data[0]
        appended_DE242.location = bpy.context.scene.cursor.location
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Append_Wind_Controller_14Ef6(bpy.types.Operator):
    bl_idname = "sna.append_wind_controller_14ef6"
    bl_label = "Append Wind Controller"
    bl_description = "Appends an object for use as a modifier effector. The object will not render."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        before_data = list(bpy.data.objects)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Wireframe Objects.blend') + r'\Object', filename='Wind Controller', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
        appended_688C7 = None if not new_data else new_data[0]
        appended_688C7.location = bpy.context.scene.cursor.location
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_effectors_menu_20819(layout_function, ):
    box_3CE1A = layout_function.box()
    box_3CE1A.alert = False
    box_3CE1A.enabled = True
    box_3CE1A.active = True
    box_3CE1A.use_property_split = False
    box_3CE1A.use_property_decorate = False
    box_3CE1A.alignment = 'Expand'.upper()
    box_3CE1A.scale_x = 1.0
    box_3CE1A.scale_y = 1.0
    if not True: box_3CE1A.operator_context = "EXEC_DEFAULT"
    box_3CE1A.label(text='Add Effectors', icon_value=0)
    grid_D7834 = box_3CE1A.grid_flow(columns=3, row_major=False, even_columns=False, even_rows=False, align=True)
    grid_D7834.enabled = True
    grid_D7834.active = True
    grid_D7834.use_property_split = False
    grid_D7834.use_property_decorate = False
    grid_D7834.alignment = 'Expand'.upper()
    grid_D7834.scale_x = 1.0
    grid_D7834.scale_y = 1.0
    if not True: grid_D7834.operator_context = "EXEC_DEFAULT"
    op = grid_D7834.operator('sna.append_wire_sphere_f21b7', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'noun-sphere-7915480-FFFFFF.svg')), emboss=True, depress=False)
    op = grid_D7834.operator('sna.append_wire_cube_d69fb', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'noun-cube-7915485-FFFFFF.svg')), emboss=True, depress=False)
    op = grid_D7834.operator('sna.append_wind_controller_14ef6', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'direction-arrow-straight.svg')), emboss=True, depress=False)


def sna_active_modifier_settings_function_interface_D3061(layout_function, ):
    if (bpy.context.view_layer.objects.active == None):
        pass
    else:
        if ((property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Decimate_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Crop_Box_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wireframe_GN' in bpy.context.view_layer.objects.active.modifiers)):
            col_0C24F = layout_function.column(heading='', align=True)
            col_0C24F.alert = False
            col_0C24F.enabled = True
            col_0C24F.active = True
            col_0C24F.use_property_split = False
            col_0C24F.use_property_decorate = False
            col_0C24F.scale_x = 1.0
            col_0C24F.scale_y = 1.0
            col_0C24F.alignment = 'Expand'.upper()
            col_0C24F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            box_44258 = col_0C24F.box()
            box_44258.alert = False
            box_44258.enabled = True
            box_44258.active = True
            box_44258.use_property_split = False
            box_44258.use_property_decorate = False
            box_44258.alignment = 'Expand'.upper()
            box_44258.scale_x = 1.0
            box_44258.scale_y = 1.0
            if not True: box_44258.operator_context = "EXEC_DEFAULT"
            box_44258.label(text='Active Settings', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'nine-points-connected.svg')))
            grid_7328C = box_44258.grid_flow(columns=2, row_major=False, even_columns=False, even_rows=False, align=True)
            grid_7328C.enabled = True
            grid_7328C.active = True
            grid_7328C.use_property_split = False
            grid_7328C.use_property_decorate = False
            grid_7328C.alignment = 'Expand'.upper()
            grid_7328C.scale_x = 1.0
            grid_7328C.scale_y = 1.0
            if not True: grid_7328C.operator_context = "EXEC_DEFAULT"
            grid_7328C.prop(bpy.context.scene.sna_kiri_pa_scene_properties, 'active_settings', text='.', icon_value=0, emboss=True, expand=True)
            box_D08B3 = col_0C24F.box()
            box_D08B3.alert = False
            box_D08B3.enabled = True
            box_D08B3.active = True
            box_D08B3.use_property_split = False
            box_D08B3.use_property_decorate = False
            box_D08B3.alignment = 'Expand'.upper()
            box_D08B3.scale_x = 1.0
            box_D08B3.scale_y = 1.0
            if not True: box_D08B3.operator_context = "EXEC_DEFAULT"
            if bpy.context.scene.sna_kiri_pa_scene_properties.active_settings == "Decimate":
                if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Decimate_GN' in bpy.context.view_layer.objects.active.modifiers):
                    layout_function = box_D08B3
                    sna_decimate_function_interface_36876(layout_function, )
                else:
                    box_61770 = box_D08B3.box()
                    box_61770.alert = True
                    box_61770.enabled = True
                    box_61770.active = True
                    box_61770.use_property_split = False
                    box_61770.use_property_decorate = False
                    box_61770.alignment = 'Expand'.upper()
                    box_61770.scale_x = 1.0
                    box_61770.scale_y = 1.0
                    if not True: box_61770.operator_context = "EXEC_DEFAULT"
                    box_61770.label(text='Decimate modifier is missing', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'alert-circle.svg')))
            elif bpy.context.scene.sna_kiri_pa_scene_properties.active_settings == "Crop Box":
                if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Crop_Box_GN' in bpy.context.view_layer.objects.active.modifiers):
                    layout_function = box_D08B3
                    sna_crop_function_interface_7E647(layout_function, )
                else:
                    box_834CE = box_D08B3.box()
                    box_834CE.alert = True
                    box_834CE.enabled = True
                    box_834CE.active = True
                    box_834CE.use_property_split = False
                    box_834CE.use_property_decorate = False
                    box_834CE.alignment = 'Expand'.upper()
                    box_834CE.scale_x = 1.0
                    box_834CE.scale_y = 1.0
                    if not True: box_834CE.operator_context = "EXEC_DEFAULT"
                    box_834CE.label(text='Crop Box modifier is missing', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'alert-circle.svg')))
            elif bpy.context.scene.sna_kiri_pa_scene_properties.active_settings == "Wind":
                if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers):
                    layout_function = box_D08B3
                    sna_wind_function_interface_178D5(layout_function, )
                else:
                    box_94DC1 = box_D08B3.box()
                    box_94DC1.alert = True
                    box_94DC1.enabled = True
                    box_94DC1.active = True
                    box_94DC1.use_property_split = False
                    box_94DC1.use_property_decorate = False
                    box_94DC1.alignment = 'Expand'.upper()
                    box_94DC1.scale_x = 1.0
                    box_94DC1.scale_y = 1.0
                    if not True: box_94DC1.operator_context = "EXEC_DEFAULT"
                    box_94DC1.label(text='Wind modifier is missing', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'alert-circle.svg')))
            elif bpy.context.scene.sna_kiri_pa_scene_properties.active_settings == "Morph":
                if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers):
                    layout_function = box_D08B3
                    sna_morph_function_interface_BAD21(layout_function, )
                else:
                    box_B23F5 = box_D08B3.box()
                    box_B23F5.alert = True
                    box_B23F5.enabled = True
                    box_B23F5.active = True
                    box_B23F5.use_property_split = False
                    box_B23F5.use_property_decorate = False
                    box_B23F5.alignment = 'Expand'.upper()
                    box_B23F5.scale_x = 1.0
                    box_B23F5.scale_y = 1.0
                    if not True: box_B23F5.operator_context = "EXEC_DEFAULT"
                    box_B23F5.label(text='Morph modifier is missing', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'alert-circle.svg')))
            elif bpy.context.scene.sna_kiri_pa_scene_properties.active_settings == "Noise":
                if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers):
                    layout_function = box_D08B3
                    sna_noise_function_interface_05231(layout_function, )
                else:
                    box_8AEBC = box_D08B3.box()
                    box_8AEBC.alert = True
                    box_8AEBC.enabled = True
                    box_8AEBC.active = True
                    box_8AEBC.use_property_split = False
                    box_8AEBC.use_property_decorate = False
                    box_8AEBC.alignment = 'Expand'.upper()
                    box_8AEBC.scale_x = 1.0
                    box_8AEBC.scale_y = 1.0
                    if not True: box_8AEBC.operator_context = "EXEC_DEFAULT"
                    box_8AEBC.label(text='Noise modifier is missing', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'alert-circle.svg')))
            elif bpy.context.scene.sna_kiri_pa_scene_properties.active_settings == "Snap To Shape":
                if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN' in bpy.context.view_layer.objects.active.modifiers):
                    layout_function = box_D08B3
                    sna_snap_function_interface_8E0BA(layout_function, )
                else:
                    box_F925D = box_D08B3.box()
                    box_F925D.alert = True
                    box_F925D.enabled = True
                    box_F925D.active = True
                    box_F925D.use_property_split = False
                    box_F925D.use_property_decorate = False
                    box_F925D.alignment = 'Expand'.upper()
                    box_F925D.scale_x = 1.0
                    box_F925D.scale_y = 1.0
                    if not True: box_F925D.operator_context = "EXEC_DEFAULT"
                    box_F925D.label(text='Snap To Shape modifier is missing', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'alert-circle.svg')))
            elif bpy.context.scene.sna_kiri_pa_scene_properties.active_settings == "Wireframe":
                if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wireframe_GN' in bpy.context.view_layer.objects.active.modifiers):
                    layout_function = box_D08B3
                    sna_wireframe_function_interface_67E1B(layout_function, )
                else:
                    box_78EB9 = box_D08B3.box()
                    box_78EB9.alert = True
                    box_78EB9.enabled = True
                    box_78EB9.active = True
                    box_78EB9.use_property_split = False
                    box_78EB9.use_property_decorate = False
                    box_78EB9.alignment = 'Expand'.upper()
                    box_78EB9.scale_x = 1.0
                    box_78EB9.scale_y = 1.0
                    if not True: box_78EB9.operator_context = "EXEC_DEFAULT"
                    box_78EB9.label(text='Wireframe modifier is missing', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'alert-circle.svg')))
            else:
                pass


def sna_all_functions_main_function_interface_AECE6(layout_function, ):
    col_0FD77 = layout_function.column(heading='', align=True)
    col_0FD77.alert = False
    col_0FD77.enabled = True
    col_0FD77.active = True
    col_0FD77.use_property_split = False
    col_0FD77.use_property_decorate = False
    col_0FD77.scale_x = 1.0
    col_0FD77.scale_y = 1.0
    col_0FD77.alignment = 'Expand'.upper()
    col_0FD77.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    layout_function = col_0FD77
    sna_add_point_animate_modifiers_button_CA918(layout_function, )
    layout_function = col_0FD77
    sna_quick_control_function_interface_80AF1(layout_function, )
    layout_function = col_0FD77
    sna_add_effectors_menu_20819(layout_function, )
    layout_function = col_0FD77
    sna_global_properties_55201(layout_function, )
    layout_function = col_0FD77
    sna_layer_stack_menu_D2063(layout_function, )
    layout_function = col_0FD77
    sna_active_modifier_settings_function_interface_D3061(layout_function, )


class SNA_OT_Refresh_Changes_Ce548(bpy.types.Operator):
    bl_idname = "sna.refresh_changes_ce548"
    bl_label = "Refresh changes"
    bl_description = "Refreshes modifier changes on the active object"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.view_layer.objects.active.update_tag(refresh={'OBJECT'}, )
        if bpy.context and bpy.context.screen:
            for a in bpy.context.screen.areas:
                a.tag_redraw()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_global_properties_55201(layout_function, ):
    if (bpy.context.view_layer.objects.active == None):
        pass
    else:
        if ((property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wireframe_GN' in bpy.context.view_layer.objects.active.modifiers)):
            box_5B50C = layout_function.box()
            box_5B50C.alert = False
            box_5B50C.enabled = True
            box_5B50C.active = True
            box_5B50C.use_property_split = False
            box_5B50C.use_property_decorate = False
            box_5B50C.alignment = 'Expand'.upper()
            box_5B50C.scale_x = 1.0
            box_5B50C.scale_y = 1.0
            if not True: box_5B50C.operator_context = "EXEC_DEFAULT"
            col_9E35D = box_5B50C.column(heading='', align=True)
            col_9E35D.alert = False
            col_9E35D.enabled = True
            col_9E35D.active = True
            col_9E35D.use_property_split = False
            col_9E35D.use_property_decorate = False
            col_9E35D.scale_x = 1.0
            col_9E35D.scale_y = 1.0
            col_9E35D.alignment = 'Expand'.upper()
            col_9E35D.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            if ((property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wireframe_GN' in bpy.context.view_layer.objects.active.modifiers)):
                col_8BA56 = col_9E35D.column(heading='', align=False)
                col_8BA56.alert = False
                col_8BA56.enabled = True
                col_8BA56.active = True
                col_8BA56.use_property_split = False
                col_8BA56.use_property_decorate = False
                col_8BA56.scale_x = 1.0
                col_8BA56.scale_y = 1.0
                col_8BA56.alignment = 'Expand'.upper()
                col_8BA56.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                if ((bpy.context.view_layer.objects.active.rotation_euler[0] == 0.0) and (bpy.context.view_layer.objects.active.rotation_euler[1] == 0.0) and (bpy.context.view_layer.objects.active.rotation_euler[2] == 0.0)):
                    pass
                else:
                    box_23735 = col_8BA56.box()
                    box_23735.alert = True
                    box_23735.enabled = True
                    box_23735.active = True
                    box_23735.use_property_split = False
                    box_23735.use_property_decorate = False
                    box_23735.alignment = 'Expand'.upper()
                    box_23735.scale_x = 1.0
                    box_23735.scale_y = 1.0
                    if not True: box_23735.operator_context = "EXEC_DEFAULT"
                    box_23735.label(text='Rotation is not applied', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'alert-circle.svg')))
                if ((bpy.context.view_layer.objects.active.scale[0] == 1.0) and (bpy.context.view_layer.objects.active.scale[1] == 1.0) and (bpy.context.view_layer.objects.active.scale[2] == 1.0)):
                    pass
                else:
                    box_51618 = col_8BA56.box()
                    box_51618.alert = True
                    box_51618.enabled = True
                    box_51618.active = True
                    box_51618.use_property_split = False
                    box_51618.use_property_decorate = False
                    box_51618.alignment = 'Expand'.upper()
                    box_51618.scale_x = 1.0
                    box_51618.scale_y = 1.0
                    if not True: box_51618.operator_context = "EXEC_DEFAULT"
                    box_51618.label(text='Scale is not applied', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'alert-circle.svg')))
            if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Mesh_To_Points_GN' in bpy.context.view_layer.objects.active.modifiers):
                if (len(bpy.context.active_object.data.id_data.edges) > 0):
                    box_CF306 = col_9E35D.box()
                    box_CF306.alert = False
                    box_CF306.enabled = True
                    box_CF306.active = True
                    box_CF306.use_property_split = False
                    box_CF306.use_property_decorate = False
                    box_CF306.alignment = 'Expand'.upper()
                    box_CF306.scale_x = 1.0
                    box_CF306.scale_y = 1.0
                    if not True: box_CF306.operator_context = "EXEC_DEFAULT"
                    box_CF306.label(text='Mesh colour texture', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'image.svg')))
                    row_FCD17 = box_CF306.row(heading='', align=True)
                    row_FCD17.alert = False
                    row_FCD17.enabled = True
                    row_FCD17.active = True
                    row_FCD17.use_property_split = False
                    row_FCD17.use_property_decorate = False
                    row_FCD17.scale_x = 1.0
                    row_FCD17.scale_y = 1.0
                    row_FCD17.alignment = 'Expand'.upper()
                    row_FCD17.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    row_FCD17.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Mesh_To_Points_GN'], '["Socket_2"]', bpy.data, 'images', text='', icon='NONE', item_search_property="name")
                    op = row_FCD17.operator('sna.refresh_changes_ce548', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'refresh.svg')), emboss=True, depress=False)
            if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Set_Material_GN' in bpy.context.view_layer.objects.active.modifiers):
                box_D0222 = col_9E35D.box()
                box_D0222.alert = False
                box_D0222.enabled = True
                box_D0222.active = True
                box_D0222.use_property_split = False
                box_D0222.use_property_decorate = False
                box_D0222.alignment = 'Expand'.upper()
                box_D0222.scale_x = 1.0
                box_D0222.scale_y = 1.0
                if not True: box_D0222.operator_context = "EXEC_DEFAULT"
                box_D0222.label(text='Materials', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'nine-points-connected.svg')))
                grid_F259F = box_D0222.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=True)
                grid_F259F.enabled = True
                grid_F259F.active = True
                grid_F259F.use_property_split = False
                grid_F259F.use_property_decorate = False
                grid_F259F.alignment = 'Expand'.upper()
                grid_F259F.scale_x = 1.0
                grid_F259F.scale_y = 1.0
                if not True: grid_F259F.operator_context = "EXEC_DEFAULT"
                box_76853 = grid_F259F.box()
                box_76853.alert = False
                box_76853.enabled = True
                box_76853.active = True
                box_76853.use_property_split = False
                box_76853.use_property_decorate = False
                box_76853.alignment = 'Expand'.upper()
                box_76853.scale_x = 1.0
                box_76853.scale_y = 1.0
                if not True: box_76853.operator_context = "EXEC_DEFAULT"
                box_76853.label(text='Point', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'material.svg')))
                box_76853.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Set_Material_GN'], '["Socket_6"]', bpy.data, 'materials', text='', icon='NONE', item_search_property="name")
                box_F2B60 = grid_F259F.box()
                box_F2B60.alert = False
                box_F2B60.enabled = True
                box_F2B60.active = True
                box_F2B60.use_property_split = False
                box_F2B60.use_property_decorate = False
                box_F2B60.alignment = 'Expand'.upper()
                box_F2B60.scale_x = 1.0
                box_F2B60.scale_y = 1.0
                if not True: box_F2B60.operator_context = "EXEC_DEFAULT"
                box_F2B60.label(text='Mesh', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'material.svg')))
                box_F2B60.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Set_Material_GN'], '["Socket_7"]', bpy.data, 'materials', text='', icon='NONE', item_search_property="name")
            if ((property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wireframe_GN' in bpy.context.view_layer.objects.active.modifiers)):
                box_92E9D = col_9E35D.box()
                box_92E9D.alert = False
                box_92E9D.enabled = True
                box_92E9D.active = True
                box_92E9D.use_property_split = False
                box_92E9D.use_property_decorate = False
                box_92E9D.alignment = 'Expand'.upper()
                box_92E9D.scale_x = 1.0
                box_92E9D.scale_y = 1.0
                if not True: box_92E9D.operator_context = "EXEC_DEFAULT"
                box_92E9D.label(text='Timing', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'nine-points-connected.svg')))
                grid_2745E = box_92E9D.grid_flow(columns=2, row_major=False, even_columns=False, even_rows=False, align=True)
                grid_2745E.enabled = True
                grid_2745E.active = True
                grid_2745E.use_property_split = False
                grid_2745E.use_property_decorate = False
                grid_2745E.alignment = 'Expand'.upper()
                grid_2745E.scale_x = 1.0
                grid_2745E.scale_y = 1.0
                if not True: grid_2745E.operator_context = "EXEC_DEFAULT"
                grid_2745E.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'start_frame', text='Start Frame', icon_value=0, emboss=True)
                grid_2745E.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'end_frame', text='End Frame', icon_value=0, emboss=True)
            if ((property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers)):
                box_477AE = col_9E35D.box()
                box_477AE.alert = False
                box_477AE.enabled = True
                box_477AE.active = True
                box_477AE.use_property_split = False
                box_477AE.use_property_decorate = False
                box_477AE.alignment = 'Expand'.upper()
                box_477AE.scale_x = 1.0
                box_477AE.scale_y = 1.0
                if not True: box_477AE.operator_context = "EXEC_DEFAULT"
                box_477AE.label(text='Point Scale', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'nine-points-connected.svg')))
                col_6575B = box_477AE.column(heading='', align=True)
                col_6575B.alert = False
                col_6575B.enabled = True
                col_6575B.active = True
                col_6575B.use_property_split = False
                col_6575B.use_property_decorate = False
                col_6575B.scale_x = 1.0
                col_6575B.scale_y = 1.0
                col_6575B.alignment = 'Expand'.upper()
                col_6575B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_D35D5 = col_6575B.row(heading='', align=True)
                row_D35D5.alert = False
                row_D35D5.enabled = True
                row_D35D5.active = True
                row_D35D5.use_property_split = False
                row_D35D5.use_property_decorate = False
                row_D35D5.scale_x = 1.0
                row_D35D5.scale_y = 1.0
                row_D35D5.alignment = 'Expand'.upper()
                row_D35D5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_D35D5.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'point_scale_min', text='Min', icon_value=0, emboss=True)
                row_D35D5.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'point_scale_max', text='Max', icon_value=0, emboss=True)
                col_6575B.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'scale_random', text='Randomize', icon_value=0, emboss=True)
            if ((property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers)):
                if ((not bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wind) and (not bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_morph) and (not bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_noise)):
                    pass
                else:
                    box_FB041 = col_9E35D.box()
                    box_FB041.alert = False
                    box_FB041.enabled = True
                    box_FB041.active = True
                    box_FB041.use_property_split = False
                    box_FB041.use_property_decorate = False
                    box_FB041.alignment = 'Expand'.upper()
                    box_FB041.scale_x = 1.0
                    box_FB041.scale_y = 1.0
                    if not True: box_FB041.operator_context = "EXEC_DEFAULT"
                    box_FB041.label(text='Attribute Influence', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'nine-points-connected.svg')))
                    box_FB041.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'point_scale_attribute', text='', icon_value=0, emboss=True)
            if (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Viewport_Display_GN' in bpy.context.view_layer.objects.active.modifiers):
                box_B1C84 = col_9E35D.box()
                box_B1C84.alert = False
                box_B1C84.enabled = True
                box_B1C84.active = True
                box_B1C84.use_property_split = False
                box_B1C84.use_property_decorate = False
                box_B1C84.alignment = 'Expand'.upper()
                box_B1C84.scale_x = 1.0
                box_B1C84.scale_y = 1.0
                if not True: box_B1C84.operator_context = "EXEC_DEFAULT"
                box_B1C84.label(text='Viewport Display', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'nine-points-connected.svg')))
                attr_695C7 = '["' + str('Socket_2' + '"]') 
                box_B1C84.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Viewport_Display_GN'], attr_695C7, text='', icon_value=0, emboss=True)


def sna_about_and_external_links_interface_function_8E1B8(layout_function, ):
    box_DD590 = layout_function.box()
    box_DD590.alert = False
    box_DD590.enabled = True
    box_DD590.active = True
    box_DD590.use_property_split = False
    box_DD590.use_property_decorate = False
    box_DD590.alignment = 'Expand'.upper()
    box_DD590.scale_x = 1.0
    box_DD590.scale_y = 1.0
    if not True: box_DD590.operator_context = "EXEC_DEFAULT"
    col_7EB57 = box_DD590.column(heading='', align=True)
    col_7EB57.alert = False
    col_7EB57.enabled = True
    col_7EB57.active = True
    col_7EB57.use_property_split = False
    col_7EB57.use_property_decorate = False
    col_7EB57.scale_x = 1.0
    col_7EB57.scale_y = 1.0
    col_7EB57.alignment = 'Expand'.upper()
    col_7EB57.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    box_8183E = col_7EB57.box()
    box_8183E.alert = False
    box_8183E.enabled = True
    box_8183E.active = True
    box_8183E.use_property_split = False
    box_8183E.use_property_decorate = False
    box_8183E.alignment = 'Center'.upper()
    box_8183E.scale_x = 1.0
    box_8183E.scale_y = 1.0
    if not True: box_8183E.operator_context = "EXEC_DEFAULT"
    box_8183E.label(text='About KIRI Engine', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'nine-points-connected.svg')))
    box_8183E.template_icon(icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Addon speel 2.png')), scale=10.0)
    op = box_8183E.operator('sna.dgs_render_launch_kiri_site_84772', text='Learn More', icon_value=0, emboss=True, depress=False)
    box_63F09 = col_7EB57.box()
    box_63F09.alert = False
    box_63F09.enabled = True
    box_63F09.active = True
    box_63F09.use_property_split = False
    box_63F09.use_property_decorate = True
    box_63F09.alignment = 'Expand'.upper()
    box_63F09.scale_x = 1.0
    box_63F09.scale_y = 1.2000000476837158
    if not True: box_63F09.operator_context = "EXEC_DEFAULT"
    row_786FB = box_63F09.row(heading='', align=True)
    row_786FB.alert = False
    row_786FB.enabled = True
    row_786FB.active = True
    row_786FB.use_property_split = False
    row_786FB.use_property_decorate = False
    row_786FB.scale_x = 1.0
    row_786FB.scale_y = 1.0
    row_786FB.alignment = 'Expand'.upper()
    row_786FB.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_786FB.label(text='Documentation', icon_value=0)
    split_7852F = row_786FB.split(factor=0.30000001192092896, align=True)
    split_7852F.alert = False
    split_7852F.enabled = True
    split_7852F.active = True
    split_7852F.use_property_split = False
    split_7852F.use_property_decorate = False
    split_7852F.scale_x = 1.0
    split_7852F.scale_y = 1.0
    split_7852F.alignment = 'Expand'.upper()
    if not True: split_7852F.operator_context = "EXEC_DEFAULT"
    op = split_7852F.operator('sna.pa_open_documentation_3b870', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'documentation.svg')), emboss=True, depress=False)
    op = split_7852F.operator('sna.pa_open_tutorial_video_d0cd5', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'video.svg')), emboss=True, depress=False)
    box_C5949 = col_7EB57.box()
    box_C5949.alert = False
    box_C5949.enabled = True
    box_C5949.active = True
    box_C5949.use_property_split = False
    box_C5949.use_property_decorate = False
    box_C5949.alignment = 'Expand'.upper()
    box_C5949.scale_x = 1.0
    box_C5949.scale_y = 1.0
    if not True: box_C5949.operator_context = "EXEC_DEFAULT"
    row_7C27F = box_C5949.row(heading='', align=False)
    row_7C27F.alert = False
    row_7C27F.enabled = True
    row_7C27F.active = True
    row_7C27F.use_property_split = False
    row_7C27F.use_property_decorate = False
    row_7C27F.scale_x = 1.0
    row_7C27F.scale_y = 1.2000000476837158
    row_7C27F.alignment = 'Expand'.upper()
    row_7C27F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_7C27F.label(text='Get More Addons', icon_value=0)
    split_57202 = row_7C27F.split(factor=0.5, align=True)
    split_57202.alert = False
    split_57202.enabled = True
    split_57202.active = True
    split_57202.use_property_split = False
    split_57202.use_property_decorate = False
    split_57202.scale_x = 1.0
    split_57202.scale_y = 1.0
    split_57202.alignment = 'Expand'.upper()
    if not True: split_57202.operator_context = "EXEC_DEFAULT"
    op = split_57202.operator('sna.pa_launch_superhive_store_0bcb5', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'SuperHive Logo White.png')), emboss=True, depress=False)
    op = split_57202.operator('sna.pa_launch_kiri_blender_addons_page_9427f', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'kiriengine blender addon icon color.svg')), emboss=True, depress=False)


class SNA_OT_Dgs_Render_Launch_Kiri_Site_84772(bpy.types.Operator):
    bl_idname = "sna.dgs_render_launch_kiri_site_84772"
    bl_label = "3DGS Render: Launch KIRI Site"
    bl_description = "Launches a browser for the KIRI Engine main site"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        url = 'https://www.kiriengine.app/'
        # Open the web browser and go to the specified URL
        webbrowser.open(url)
        print(f"Opening web browser to {url}")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Pa_Launch_Superhive_Store_0Bcb5(bpy.types.Operator):
    bl_idname = "sna.pa_launch_superhive_store_0bcb5"
    bl_label = "PA: Launch SuperHive Store"
    bl_description = "Launches a browser for the KIRI Engine SuperHive store"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        url = 'https://blendermarket.com/creators/blender-addon-from-kiri-engine'
        # Open the web browser and go to the specified URL
        webbrowser.open(url)
        print(f"Opening web browser to {url}")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Pa_Launch_Kiri_Blender_Addons_Page_9427F(bpy.types.Operator):
    bl_idname = "sna.pa_launch_kiri_blender_addons_page_9427f"
    bl_label = "PA: Launch KIRI Blender Addons page"
    bl_description = "Launches a browser for the KIRI Engine Blender Market store"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        url = 'https://www.kiriengine.app/blender-addon'
        # Open the web browser and go to the specified URL
        webbrowser.open(url)
        print(f"Opening web browser to {url}")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Pa_Open_Documentation_3B870(bpy.types.Operator):
    bl_idname = "sna.pa_open_documentation_3b870"
    bl_label = "PA: Open Documentation"
    bl_description = "Launches a browser with the addon documentation"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        url = 'https://www.kiriengine.app/blender-addon'
        # Open the web browser and go to the specified URL
        webbrowser.open(url)
        print(f"Opening web browser to {url}")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Pa_Open_Tutorial_Video_D0Cd5(bpy.types.Operator):
    bl_idname = "sna.pa_open_tutorial_video_d0cd5"
    bl_label = "PA: Open Tutorial Video"
    bl_description = "Launches a browser with the addon documentation video"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        url = 'https://www.youtube.com/@BlenderAddon-fromKIRI'
        # Open the web browser and go to the specified URL
        webbrowser.open(url)
        print(f"Opening web browser to {url}")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_layer_stack_menu_D2063(layout_function, ):
    if (bpy.context.view_layer.objects.active == None):
        pass
    else:
        if ((property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Mesh_To_Points_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Color_Convert_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Decimate_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Crop_Box_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wireframe_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Viewport_Display_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Set_Material_GN' in bpy.context.view_layer.objects.active.modifiers)):
            box_4A42B = layout_function.box()
            box_4A42B.alert = False
            box_4A42B.enabled = True
            box_4A42B.active = True
            box_4A42B.use_property_split = False
            box_4A42B.use_property_decorate = False
            box_4A42B.alignment = 'Expand'.upper()
            box_4A42B.scale_x = 1.0
            box_4A42B.scale_y = 1.0
            if not True: box_4A42B.operator_context = "EXEC_DEFAULT"
            col_B74D3 = box_4A42B.column(heading='', align=True)
            col_B74D3.alert = False
            col_B74D3.enabled = True
            col_B74D3.active = True
            col_B74D3.use_property_split = False
            col_B74D3.use_property_decorate = False
            col_B74D3.scale_x = 1.0
            col_B74D3.scale_y = 1.0
            col_B74D3.alignment = 'Expand'.upper()
            col_B74D3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_B74D3.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'enable_decimate', text='Enable Decimate', icon_value=0, emboss=True, toggle=True)
            col_B74D3.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'enable_crop_box', text='Enable Crop Box', icon_value=0, emboss=True, toggle=True)
            grid_2EA86 = col_B74D3.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=True)
            grid_2EA86.enabled = True
            grid_2EA86.active = True
            grid_2EA86.use_property_split = False
            grid_2EA86.use_property_decorate = False
            grid_2EA86.alignment = 'Expand'.upper()
            grid_2EA86.scale_x = 1.0
            grid_2EA86.scale_y = 1.0
            if not True: grid_2EA86.operator_context = "EXEC_DEFAULT"
            grid_2EA86.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'enable_wind', text='Enable Wind', icon_value=0, emboss=True, toggle=True)
            grid_2EA86.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'enable_morph', text='Enable Morph', icon_value=0, emboss=True, toggle=True)
            col_B74D3.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'enable_noise', text='Enable Noise', icon_value=0, emboss=True, toggle=True)
            col_B74D3.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'enable_snap', text='Enable Snap To Shape', icon_value=0, emboss=True, toggle=True)
            col_B74D3.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'enable_wireframe', text='Enable Wireframe', icon_value=0, emboss=True, toggle=True)


class SNA_PT_POINT_ANIMATE_BY_KIRI_ENGINE_B94F8(bpy.types.Panel):
    bl_label = 'Point Animate by KIRI Engine'
    bl_idname = 'SNA_PT_POINT_ANIMATE_BY_KIRI_ENGINE_B94F8'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Point Animate'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout
        layout.template_icon(icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'kiriengine icon.png')), scale=0.0)

    def draw(self, context):
        layout = self.layout
        layout_function = layout
        sna_all_functions_main_function_interface_AECE6(layout_function, )
        layout_function = layout
        sna_about_and_external_links_interface_function_8E1B8(layout_function, )


def sna_quick_control_function_interface_80AF1(layout_function, ):
    if (bpy.context.view_layer.objects.active == None):
        pass
    else:
        if ((property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Mesh_To_Points_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Color_Convert_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Decimate_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Crop_Box_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wind_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Morph_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Noise_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Wireframe_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_Point_Animate_Viewport_Display_GN' in bpy.context.view_layer.objects.active.modifiers) or (property_exists("bpy.context.view_layer.objects.active.modifiers", globals(), locals()) and 'KIRI_3DGS_Point_Animate_Set_Material_GN' in bpy.context.view_layer.objects.active.modifiers)):
            pass
        else:
            if bpy.context.view_layer.objects.active.type == 'MESH':
                box_4F7E4 = layout_function.box()
                box_4F7E4.alert = False
                box_4F7E4.enabled = True
                box_4F7E4.active = True
                box_4F7E4.use_property_split = False
                box_4F7E4.use_property_decorate = False
                box_4F7E4.alignment = 'Expand'.upper()
                box_4F7E4.scale_x = 1.0
                box_4F7E4.scale_y = 1.0
                if not True: box_4F7E4.operator_context = "EXEC_DEFAULT"
                grid_E5771 = box_4F7E4.grid_flow(columns=2, row_major=False, even_columns=False, even_rows=False, align=True)
                grid_E5771.enabled = True
                grid_E5771.active = True
                grid_E5771.use_property_split = False
                grid_E5771.use_property_decorate = False
                grid_E5771.alignment = 'Expand'.upper()
                grid_E5771.scale_x = 1.0
                grid_E5771.scale_y = 1.0
                if not True: grid_E5771.operator_context = "EXEC_DEFAULT"
                op = grid_E5771.operator('sna.setup_quick_dissolve_94289', text='Quick Dissolve', icon_value=0, emboss=True, depress=False)
                op = grid_E5771.operator('sna.setup_quick_morph_dc267', text='Quick Morph', icon_value=0, emboss=True, depress=False)
                op = grid_E5771.operator('sna.setup_quick_magic_ce2cf', text='Quick Magic', icon_value=0, emboss=True, depress=False)
                op.sna_input_ = 'Input = Points'
                op = grid_E5771.operator('sna.setup_quick_tech_af450', text='Quick Tech', icon_value=0, emboss=True, depress=False)


class SNA_OT_Setup_Quick_Dissolve_94289(bpy.types.Operator):
    bl_idname = "sna.setup_quick_dissolve_94289"
    bl_label = "Setup Quick Dissolve"
    bl_description = "Adds Point Animate modifiers and sets values for a dissolve effect."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_76'] == 1):
            bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.point_scale_attribute = 'Timeline:0%-50%=0-1'
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_72'] = 6
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_69'] = 6
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_97'] = 6
        else:
            bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.point_scale_attribute = 'Timeline:1-0'
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_72'] = 1
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_69'] = 1
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_97'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_50'] = 1.0
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_69'] = 1
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_76'] == 1):
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_98'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_57'] = 12
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_55'] = 5.0
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_60'] = 10.0
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_63'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_61'] = 0.20000000298023224
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wind = True
        sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_Point_Animate_Wind_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_noise = True
        sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_3DGS_Point_Animate_Noise_GN')
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        box_14FE2 = layout.box()
        box_14FE2.alert = False
        box_14FE2.enabled = True
        box_14FE2.active = True
        box_14FE2.use_property_split = False
        box_14FE2.use_property_decorate = False
        box_14FE2.alignment = 'Expand'.upper()
        box_14FE2.scale_x = 1.0
        box_14FE2.scale_y = 1.0
        if not True: box_14FE2.operator_context = "EXEC_DEFAULT"
        box_14FE2.label(text='Quick Dissolve Settings', icon_value=0)
        box_14FE2.separator(factor=1.0)
        box_32231 = box_14FE2.box()
        box_32231.alert = False
        box_32231.enabled = True
        box_32231.active = True
        box_32231.use_property_split = False
        box_32231.use_property_decorate = False
        box_32231.alignment = 'Expand'.upper()
        box_32231.scale_x = 1.0
        box_32231.scale_y = 1.0
        if not True: box_32231.operator_context = "EXEC_DEFAULT"
        grid_BF280 = box_32231.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=False)
        grid_BF280.enabled = True
        grid_BF280.active = True
        grid_BF280.use_property_split = False
        grid_BF280.use_property_decorate = False
        grid_BF280.alignment = 'Expand'.upper()
        grid_BF280.scale_x = 1.0
        grid_BF280.scale_y = 1.0
        if not True: grid_BF280.operator_context = "EXEC_DEFAULT"
        grid_BF280.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'start_frame', text='Start Frame', icon_value=0, emboss=True)
        grid_BF280.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'end_frame', text='End Frame', icon_value=0, emboss=True)
        box_DF46D = box_14FE2.box()
        box_DF46D.alert = False
        box_DF46D.enabled = True
        box_DF46D.active = True
        box_DF46D.use_property_split = False
        box_DF46D.use_property_decorate = False
        box_DF46D.alignment = 'Expand'.upper()
        box_DF46D.scale_x = 1.0
        box_DF46D.scale_y = 1.0
        if not True: box_DF46D.operator_context = "EXEC_DEFAULT"
        attr_A7470 = '["' + str('Socket_76' + '"]') 
        box_DF46D.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_A7470, text='', icon_value=0, emboss=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_76'] == 1):
            box_0A56D = box_DF46D.box()
            box_0A56D.alert = False
            box_0A56D.enabled = True
            box_0A56D.active = True
            box_0A56D.use_property_split = False
            box_0A56D.use_property_decorate = False
            box_0A56D.alignment = 'Expand'.upper()
            box_0A56D.scale_x = 1.0
            box_0A56D.scale_y = 1.0
            if not True: box_0A56D.operator_context = "EXEC_DEFAULT"
            box_0A56D.label(text='Input Mesh Colour Texture', icon_value=0)
            box_0A56D.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Mesh_To_Points_GN'], '["Socket_2"]', bpy.data, 'images', text='', icon='NONE', item_search_property="name")

    def invoke(self, context, event):
        sna_add_point_edit_modifiers_function_execute_D32BB()
        return context.window_manager.invoke_props_dialog(self, width=500)


class SNA_OT_Setup_Quick_Morph_Dc267(bpy.types.Operator):
    bl_idname = "sna.setup_quick_morph_dc267"
    bl_label = "Setup Quick Morph"
    bl_description = "Adds Point Animate modifiers and sets values for a morph effect."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_60'] == 1):
            bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.point_scale_attribute = 'Timeline:0-1-0'
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_72'] = 8
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_69'] = 8
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_97'] = 8
        else:
            bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.point_scale_attribute = 'No Attribute Influence'
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_72'] = 0
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_69'] = 0
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_97'] = 0
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_60'] == 5):
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_98'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_57'] = 10
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_60'] = 10.0
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_63'] = 10
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_61'] = 0.20000000298023224
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_morph = True
        sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_Point_Animate_Morph_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_noise = True
        sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_3DGS_Point_Animate_Noise_GN')
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        box_12C4C = layout.box()
        box_12C4C.alert = False
        box_12C4C.enabled = True
        box_12C4C.active = True
        box_12C4C.use_property_split = False
        box_12C4C.use_property_decorate = False
        box_12C4C.alignment = 'Expand'.upper()
        box_12C4C.scale_x = 1.0
        box_12C4C.scale_y = 1.0
        if not True: box_12C4C.operator_context = "EXEC_DEFAULT"
        box_12C4C.label(text='Quick Morph Settings', icon_value=0)
        box_12C4C.separator(factor=1.0)
        box_9470F = box_12C4C.box()
        box_9470F.alert = False
        box_9470F.enabled = True
        box_9470F.active = True
        box_9470F.use_property_split = False
        box_9470F.use_property_decorate = False
        box_9470F.alignment = 'Expand'.upper()
        box_9470F.scale_x = 1.0
        box_9470F.scale_y = 1.0
        if not True: box_9470F.operator_context = "EXEC_DEFAULT"
        grid_A4BB5 = box_9470F.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=False)
        grid_A4BB5.enabled = True
        grid_A4BB5.active = True
        grid_A4BB5.use_property_split = False
        grid_A4BB5.use_property_decorate = False
        grid_A4BB5.alignment = 'Expand'.upper()
        grid_A4BB5.scale_x = 1.0
        grid_A4BB5.scale_y = 1.0
        if not True: grid_A4BB5.operator_context = "EXEC_DEFAULT"
        grid_A4BB5.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'start_frame', text='Start Frame', icon_value=0, emboss=True)
        grid_A4BB5.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'end_frame', text='End Frame', icon_value=0, emboss=True)
        box_04555 = box_12C4C.box()
        box_04555.alert = False
        box_04555.enabled = True
        box_04555.active = True
        box_04555.use_property_split = False
        box_04555.use_property_decorate = False
        box_04555.alignment = 'Expand'.upper()
        box_04555.scale_x = 1.0
        box_04555.scale_y = 1.0
        if not True: box_04555.operator_context = "EXEC_DEFAULT"
        attr_0100F = '["' + str('Socket_60' + '"]') 
        box_04555.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_0100F, text='', icon_value=0, emboss=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_60'] == 0):
            col_E9ECA = box_04555.column(heading='', align=False)
            col_E9ECA.alert = False
            col_E9ECA.enabled = True
            col_E9ECA.active = True
            col_E9ECA.use_property_split = False
            col_E9ECA.use_property_decorate = False
            col_E9ECA.scale_x = 1.0
            col_E9ECA.scale_y = 1.0
            col_E9ECA.alignment = 'Expand'.upper()
            col_E9ECA.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_E9ECA.label(text='Target Type', icon_value=0)
            attr_38058 = '["' + str('Socket_66' + '"]') 
            col_E9ECA.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_38058, text='', icon_value=0, emboss=True)
            if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_66'] == 0):
                col_1C9D4 = col_E9ECA.column(heading='', align=False)
                col_1C9D4.alert = False
                col_1C9D4.enabled = True
                col_1C9D4.active = True
                col_1C9D4.use_property_split = False
                col_1C9D4.use_property_decorate = False
                col_1C9D4.scale_x = 1.0
                col_1C9D4.scale_y = 1.0
                col_1C9D4.alignment = 'Expand'.upper()
                col_1C9D4.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                col_1C9D4.label(text='Target Object', icon_value=0)
                attr_79675 = '["' + str('Socket_20' + '"]') 
                col_1C9D4.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_79675, text='', icon_value=0, emboss=True)
            else:
                col_E5D49 = col_E9ECA.column(heading='', align=False)
                col_E5D49.alert = False
                col_E5D49.enabled = True
                col_E5D49.active = True
                col_E5D49.use_property_split = False
                col_E5D49.use_property_decorate = False
                col_E5D49.scale_x = 1.0
                col_E5D49.scale_y = 1.0
                col_E5D49.alignment = 'Expand'.upper()
                col_E5D49.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                col_E5D49.label(text='Target Object', icon_value=0)
                attr_56139 = '["' + str('Socket_57' + '"]') 
                col_E5D49.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_56139, text='', icon_value=0, emboss=True)
                col_E5D49.label(text='Target Mesh Colour Texture', icon_value=0)
                col_E5D49.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], '["Socket_59"]', bpy.data, 'images', text='', icon='NONE', item_search_property="name")
        else:
            col_29F93 = box_04555.column(heading='', align=False)
            col_29F93.alert = False
            col_29F93.enabled = True
            col_29F93.active = True
            col_29F93.use_property_split = False
            col_29F93.use_property_decorate = False
            col_29F93.scale_x = 1.0
            col_29F93.scale_y = 1.0
            col_29F93.alignment = 'Expand'.upper()
            col_29F93.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            box_CA767 = col_29F93.box()
            box_CA767.alert = False
            box_CA767.enabled = True
            box_CA767.active = True
            box_CA767.use_property_split = False
            box_CA767.use_property_decorate = False
            box_CA767.alignment = 'Expand'.upper()
            box_CA767.scale_x = 1.0
            box_CA767.scale_y = 1.0
            if not True: box_CA767.operator_context = "EXEC_DEFAULT"
            box_CA767.label(text='Input Mesh Colour Texture', icon_value=0)
            box_CA767.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Mesh_To_Points_GN'], '["Socket_2"]', bpy.data, 'images', text='', icon='NONE', item_search_property="name")
            box_EB96F = col_29F93.box()
            box_EB96F.alert = False
            box_EB96F.enabled = True
            box_EB96F.active = True
            box_EB96F.use_property_split = False
            box_EB96F.use_property_decorate = False
            box_EB96F.alignment = 'Expand'.upper()
            box_EB96F.scale_x = 1.0
            box_EB96F.scale_y = 1.0
            if not True: box_EB96F.operator_context = "EXEC_DEFAULT"
            box_EB96F.label(text='Target Object', icon_value=0)
            attr_B3D74 = '["' + str('Socket_57' + '"]') 
            box_EB96F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_B3D74, text='', icon_value=0, emboss=True)
            box_EB96F.label(text='Target Mesh Colour Texture', icon_value=0)
            box_EB96F.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], '["Socket_59"]', bpy.data, 'images', text='', icon='NONE', item_search_property="name")

    def invoke(self, context, event):
        sna_add_point_edit_modifiers_function_execute_D32BB()
        return context.window_manager.invoke_props_dialog(self, width=500)


class SNA_OT_Setup_Quick_Magic_Ce2Cf(bpy.types.Operator):
    bl_idname = "sna.setup_quick_magic_ce2cf"
    bl_label = "Setup Quick Magic"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_input__enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_input_: bpy.props.EnumProperty(name='Input =', description='', items=[('Input = Points', 'Input = Points', '', 0, 0), ('Input = Mesh', 'Input = Mesh', '', 0, 1)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_98'] == 1):
            bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.point_scale_attribute = 'Timeline:0-1-0'
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_72'] = 8
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_69'] = 8
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_97'] = 8
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_100'] = 2
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_82'] = 1
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_76'] = 6
        else:
            bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.point_scale_attribute = 'Timeline:1-0'
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_72'] = 1
            bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_69'] = 1
            bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_97'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_57'] = 8
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_60'] = 3.0
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_63'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_61'] = 0.20000000298023224
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_noise = True
        sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_3DGS_Point_Animate_Noise_GN')
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        box_28423 = layout.box()
        box_28423.alert = False
        box_28423.enabled = True
        box_28423.active = True
        box_28423.use_property_split = False
        box_28423.use_property_decorate = False
        box_28423.alignment = 'Expand'.upper()
        box_28423.scale_x = 1.0
        box_28423.scale_y = 1.0
        if not True: box_28423.operator_context = "EXEC_DEFAULT"
        box_28423.label(text='Quick Magic Settings', icon_value=0)
        box_28423.separator(factor=1.0)
        box_BF2E0 = box_28423.box()
        box_BF2E0.alert = False
        box_BF2E0.enabled = True
        box_BF2E0.active = True
        box_BF2E0.use_property_split = False
        box_BF2E0.use_property_decorate = False
        box_BF2E0.alignment = 'Expand'.upper()
        box_BF2E0.scale_x = 1.0
        box_BF2E0.scale_y = 1.0
        if not True: box_BF2E0.operator_context = "EXEC_DEFAULT"
        grid_8D9FB = box_BF2E0.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=False)
        grid_8D9FB.enabled = True
        grid_8D9FB.active = True
        grid_8D9FB.use_property_split = False
        grid_8D9FB.use_property_decorate = False
        grid_8D9FB.alignment = 'Expand'.upper()
        grid_8D9FB.scale_x = 1.0
        grid_8D9FB.scale_y = 1.0
        if not True: grid_8D9FB.operator_context = "EXEC_DEFAULT"
        grid_8D9FB.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'start_frame', text='Start Frame', icon_value=0, emboss=True)
        grid_8D9FB.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'end_frame', text='End Frame', icon_value=0, emboss=True)
        box_85484 = box_28423.box()
        box_85484.alert = False
        box_85484.enabled = True
        box_85484.active = True
        box_85484.use_property_split = False
        box_85484.use_property_decorate = False
        box_85484.alignment = 'Expand'.upper()
        box_85484.scale_x = 1.0
        box_85484.scale_y = 1.0
        if not True: box_85484.operator_context = "EXEC_DEFAULT"
        attr_CC27F = '["' + str('Socket_98' + '"]') 
        box_85484.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_CC27F, text='', icon_value=0, emboss=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_98'] == 1):
            box_0A1EF = box_85484.box()
            box_0A1EF.alert = False
            box_0A1EF.enabled = True
            box_0A1EF.active = True
            box_0A1EF.use_property_split = False
            box_0A1EF.use_property_decorate = False
            box_0A1EF.alignment = 'Expand'.upper()
            box_0A1EF.scale_x = 1.0
            box_0A1EF.scale_y = 1.0
            if not True: box_0A1EF.operator_context = "EXEC_DEFAULT"
            box_0A1EF.label(text='Input Mesh Colour Texture', icon_value=0)
            box_0A1EF.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Mesh_To_Points_GN'], '["Socket_2"]', bpy.data, 'images', text='', icon='NONE', item_search_property="name")

    def invoke(self, context, event):
        sna_add_point_edit_modifiers_function_execute_D32BB()
        return context.window_manager.invoke_props_dialog(self, width=500)


class SNA_OT_Setup_Quick_Tech_Af450(bpy.types.Operator):
    bl_idname = "sna.setup_quick_tech_af450"
    bl_label = "Setup Quick Tech"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_18'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_19'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_20'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_3'] = (5.0, 5.0, 5.0)
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_7'] = 7
        before_data = list(bpy.data.objects)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Wireframe Objects.blend') + r'\Object', filename='Tech Ball', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
        appended_CF0C6 = None if not new_data else new_data[0]
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_2'] = appended_CF0C6
        appended_CF0C6.hide_viewport = True
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_39'] = 2
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_28'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_5'] = 1.0
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_22'] = 10
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_15'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_32'] = 10
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_6'] = 0.029999999329447746
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_37'] = 8
        bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_24'] = 1
        bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_57'] = 8
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_snap = True
        sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_3DGS_Point_Animate_Snap_To_Shape_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wireframe = True
        sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_Point_Animate_Wireframe_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_noise = True
        sna_turn_modifier_on_off_function_execute_C4736(True, 'KIRI_3DGS_Point_Animate_Noise_GN')
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        box_323C5 = layout.box()
        box_323C5.alert = False
        box_323C5.enabled = True
        box_323C5.active = True
        box_323C5.use_property_split = False
        box_323C5.use_property_decorate = False
        box_323C5.alignment = 'Expand'.upper()
        box_323C5.scale_x = 1.0
        box_323C5.scale_y = 1.0
        if not True: box_323C5.operator_context = "EXEC_DEFAULT"
        box_323C5.label(text='Quick Tech Settings', icon_value=0)
        box_323C5.separator(factor=1.0)
        box_522C1 = box_323C5.box()
        box_522C1.alert = False
        box_522C1.enabled = True
        box_522C1.active = True
        box_522C1.use_property_split = False
        box_522C1.use_property_decorate = False
        box_522C1.alignment = 'Expand'.upper()
        box_522C1.scale_x = 1.0
        box_522C1.scale_y = 1.0
        if not True: box_522C1.operator_context = "EXEC_DEFAULT"
        grid_7ECED = box_522C1.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=False)
        grid_7ECED.enabled = True
        grid_7ECED.active = True
        grid_7ECED.use_property_split = False
        grid_7ECED.use_property_decorate = False
        grid_7ECED.alignment = 'Expand'.upper()
        grid_7ECED.scale_x = 1.0
        grid_7ECED.scale_y = 1.0
        if not True: grid_7ECED.operator_context = "EXEC_DEFAULT"
        grid_7ECED.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'start_frame', text='Start Frame', icon_value=0, emboss=True)
        grid_7ECED.prop(bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties, 'end_frame', text='End Frame', icon_value=0, emboss=True)

    def invoke(self, context, event):
        sna_add_point_edit_modifiers_function_execute_D32BB()
        return context.window_manager.invoke_props_dialog(self, width=500)


def sna_morph_function_interface_BAD21(layout_function, ):
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_morph:
        pass
    else:
        box_FCAAD = layout_function.box()
        box_FCAAD.alert = True
        box_FCAAD.enabled = True
        box_FCAAD.active = True
        box_FCAAD.use_property_split = False
        box_FCAAD.use_property_decorate = False
        box_FCAAD.alignment = 'Expand'.upper()
        box_FCAAD.scale_x = 1.0
        box_FCAAD.scale_y = 1.0
        if not True: box_FCAAD.operator_context = "EXEC_DEFAULT"
        box_FCAAD.label(text='Morph is disabled', icon_value=0)
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.morph_baked:
        box_05E9F = layout_function.box()
        box_05E9F.alert = True
        box_05E9F.enabled = True
        box_05E9F.active = True
        box_05E9F.use_property_split = False
        box_05E9F.use_property_decorate = False
        box_05E9F.alignment = 'Expand'.upper()
        box_05E9F.scale_x = 1.0
        box_05E9F.scale_y = 1.0
        if not True: box_05E9F.operator_context = "EXEC_DEFAULT"
        box_05E9F.label(text='Modifiers settings are baked', icon_value=0)
    col_A5668 = layout_function.column(heading='', align=False)
    col_A5668.alert = False
    col_A5668.enabled = True
    col_A5668.active = True
    col_A5668.use_property_split = False
    col_A5668.use_property_decorate = False
    col_A5668.scale_x = 1.0
    col_A5668.scale_y = 1.0
    col_A5668.alignment = 'Expand'.upper()
    col_A5668.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    box_1506D = col_A5668.box()
    box_1506D.alert = False
    box_1506D.enabled = (bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_morph and (not bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.morph_baked))
    box_1506D.active = True
    box_1506D.use_property_split = False
    box_1506D.use_property_decorate = False
    box_1506D.alignment = 'Expand'.upper()
    box_1506D.scale_x = 1.0
    box_1506D.scale_y = 1.0
    if not True: box_1506D.operator_context = "EXEC_DEFAULT"
    box_0976B = box_1506D.box()
    box_0976B.alert = False
    box_0976B.enabled = True
    box_0976B.active = True
    box_0976B.use_property_split = False
    box_0976B.use_property_decorate = False
    box_0976B.alignment = 'Expand'.upper()
    box_0976B.scale_x = 1.0
    box_0976B.scale_y = 1.0
    if not True: box_0976B.operator_context = "EXEC_DEFAULT"
    box_0976B.label(text='Input / Output', icon_value=0)
    attr_7F97D = '["' + str('Socket_60' + '"]') 
    box_0976B.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_7F97D, text='', icon_value=0, emboss=True, slider=True)
    if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_60'] == 5):
        box_306C3 = box_1506D.box()
        box_306C3.alert = False
        box_306C3.enabled = True
        box_306C3.active = True
        box_306C3.use_property_split = False
        box_306C3.use_property_decorate = False
        box_306C3.alignment = 'Expand'.upper()
        box_306C3.scale_x = 1.0
        box_306C3.scale_y = 1.0
        if not True: box_306C3.operator_context = "EXEC_DEFAULT"
        box_306C3.label(text='Target Mesh', icon_value=0)
        attr_9840A = '["' + str('Socket_57' + '"]') 
        box_306C3.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_9840A, text='', icon_value=0, emboss=True, slider=True)
        box_306C3.label(text='Target Mesh Texture', icon_value=0)
        box_306C3.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], '["Socket_59"]', bpy.data, 'images', text='', icon='NONE', item_search_property="name")
    else:
        box_DAAB6 = box_1506D.box()
        box_DAAB6.alert = False
        box_DAAB6.enabled = True
        box_DAAB6.active = True
        box_DAAB6.use_property_split = False
        box_DAAB6.use_property_decorate = False
        box_DAAB6.alignment = 'Expand'.upper()
        box_DAAB6.scale_x = 1.0
        box_DAAB6.scale_y = 1.0
        if not True: box_DAAB6.operator_context = "EXEC_DEFAULT"
        box_DAAB6.label(text='Target = ', icon_value=0)
        attr_E8645 = '["' + str('Socket_66' + '"]') 
        box_DAAB6.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_E8645, text='', icon_value=0, emboss=True, slider=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN']['Socket_66'] == 1):
            box_483DC = box_DAAB6.box()
            box_483DC.alert = False
            box_483DC.enabled = True
            box_483DC.active = True
            box_483DC.use_property_split = False
            box_483DC.use_property_decorate = False
            box_483DC.alignment = 'Expand'.upper()
            box_483DC.scale_x = 1.0
            box_483DC.scale_y = 1.0
            if not True: box_483DC.operator_context = "EXEC_DEFAULT"
            box_483DC.label(text='Target Mesh', icon_value=0)
            attr_02258 = '["' + str('Socket_57' + '"]') 
            box_483DC.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_02258, text='', icon_value=0, emboss=True, slider=True)
            box_483DC.label(text='Target Mesh Texture', icon_value=0)
            box_483DC.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], '["Socket_59"]', bpy.data, 'images', text='', icon='NONE', item_search_property="name")
        else:
            box_3AB7F = box_DAAB6.box()
            box_3AB7F.alert = False
            box_3AB7F.enabled = True
            box_3AB7F.active = True
            box_3AB7F.use_property_split = False
            box_3AB7F.use_property_decorate = False
            box_3AB7F.alignment = 'Expand'.upper()
            box_3AB7F.scale_x = 1.0
            box_3AB7F.scale_y = 1.0
            if not True: box_3AB7F.operator_context = "EXEC_DEFAULT"
            box_3AB7F.label(text='Target Points', icon_value=0)
            attr_6AB75 = '["' + str('Socket_20' + '"]') 
            box_3AB7F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_6AB75, text='', icon_value=0, emboss=True, slider=True)
            box_3AB7F.label(text='Target Mesh Texture', icon_value=0)
            attr_5BAB3 = '["' + str('Socket_70' + '"]') 
            box_3AB7F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Morph_GN'], attr_5BAB3, text='Linearize Colour', icon_value=0, emboss=True, slider=True, toggle=True)
    col_A5668.separator(factor=1.0)
    grid_FEFF5 = col_A5668.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=False)
    grid_FEFF5.enabled = bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_morph
    grid_FEFF5.active = True
    grid_FEFF5.use_property_split = False
    grid_FEFF5.use_property_decorate = False
    grid_FEFF5.alignment = 'Expand'.upper()
    grid_FEFF5.scale_x = 1.0
    grid_FEFF5.scale_y = 1.0
    if not True: grid_FEFF5.operator_context = "EXEC_DEFAULT"
    box_0ECA6 = grid_FEFF5.box()
    box_0ECA6.alert = True
    box_0ECA6.enabled = True
    box_0ECA6.active = True
    box_0ECA6.use_property_split = False
    box_0ECA6.use_property_decorate = False
    box_0ECA6.alignment = 'Expand'.upper()
    box_0ECA6.scale_x = 1.0
    box_0ECA6.scale_y = 2.0
    if not True: box_0ECA6.operator_context = "EXEC_DEFAULT"
    op = box_0ECA6.operator('sna.bake_morph_settings_29b13', text='BAKE', icon_value=0, emboss=True, depress=False)
    box_231E8 = grid_FEFF5.box()
    box_231E8.alert = True
    box_231E8.enabled = True
    box_231E8.active = True
    box_231E8.use_property_split = False
    box_231E8.use_property_decorate = False
    box_231E8.alignment = 'Expand'.upper()
    box_231E8.scale_x = 1.0
    box_231E8.scale_y = 2.0
    if not True: box_231E8.operator_context = "EXEC_DEFAULT"
    op = box_231E8.operator('sna.remove_bake_morph_settings_fdef2', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'trash.svg')), emboss=True, depress=False)


class SNA_OT_Bake_Morph_Settings_29B13(bpy.types.Operator):
    bl_idname = "sna.bake_morph_settings_29b13"
    bl_label = "Bake Morph Settings"
    bl_description = "Bakes current modifier settings."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_run_bake_node_function_execute_00810('KIRI_Point_Animate_Morph_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.morph_baked = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Remove_Bake_Morph_Settings_Fdef2(bpy.types.Operator):
    bl_idname = "sna.remove_bake_morph_settings_fdef2"
    bl_label = "Remove Bake Morph Settings"
    bl_description = "Removes baked data."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_remove_bake_node_function_execute_80F90('KIRI_Point_Animate_Morph_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.morph_baked = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_noise_function_interface_05231(layout_function, ):
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_noise:
        pass
    else:
        box_91B0E = layout_function.box()
        box_91B0E.alert = True
        box_91B0E.enabled = True
        box_91B0E.active = True
        box_91B0E.use_property_split = False
        box_91B0E.use_property_decorate = False
        box_91B0E.alignment = 'Expand'.upper()
        box_91B0E.scale_x = 1.0
        box_91B0E.scale_y = 1.0
        if not True: box_91B0E.operator_context = "EXEC_DEFAULT"
        box_91B0E.label(text='Noise is disabled', icon_value=0)
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.noise_baked:
        box_C0B76 = layout_function.box()
        box_C0B76.alert = True
        box_C0B76.enabled = True
        box_C0B76.active = True
        box_C0B76.use_property_split = False
        box_C0B76.use_property_decorate = False
        box_C0B76.alignment = 'Expand'.upper()
        box_C0B76.scale_x = 1.0
        box_C0B76.scale_y = 1.0
        if not True: box_C0B76.operator_context = "EXEC_DEFAULT"
        box_C0B76.label(text='Modifiers settings are baked', icon_value=0)
    col_ACF71 = layout_function.column(heading='', align=False)
    col_ACF71.alert = False
    col_ACF71.enabled = True
    col_ACF71.active = True
    col_ACF71.use_property_split = False
    col_ACF71.use_property_decorate = False
    col_ACF71.scale_x = 1.0
    col_ACF71.scale_y = 1.0
    col_ACF71.alignment = 'Expand'.upper()
    col_ACF71.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    box_C9C2C = col_ACF71.box()
    box_C9C2C.alert = False
    box_C9C2C.enabled = (bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_noise and (not bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.noise_baked))
    box_C9C2C.active = True
    box_C9C2C.use_property_split = False
    box_C9C2C.use_property_decorate = False
    box_C9C2C.alignment = 'Expand'.upper()
    box_C9C2C.scale_x = 1.0
    box_C9C2C.scale_y = 1.0
    if not True: box_C9C2C.operator_context = "EXEC_DEFAULT"
    box_2B794 = box_C9C2C.box()
    box_2B794.alert = False
    box_2B794.enabled = True
    box_2B794.active = True
    box_2B794.use_property_split = False
    box_2B794.use_property_decorate = False
    box_2B794.alignment = 'Expand'.upper()
    box_2B794.scale_x = 1.0
    box_2B794.scale_y = 1.0
    if not True: box_2B794.operator_context = "EXEC_DEFAULT"
    box_2B794.label(text='Input / Output', icon_value=0)
    attr_27B2B = '["' + str('Socket_98' + '"]') 
    box_2B794.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_27B2B, text='', icon_value=0, emboss=True, slider=True)
    box_51D21 = box_C9C2C.box()
    box_51D21.alert = False
    box_51D21.enabled = True
    box_51D21.active = True
    box_51D21.use_property_split = False
    box_51D21.use_property_decorate = False
    box_51D21.alignment = 'Expand'.upper()
    box_51D21.scale_x = 1.0
    box_51D21.scale_y = 1.0
    if not True: box_51D21.operator_context = "EXEC_DEFAULT"
    box_D934F = box_51D21.box()
    box_D934F.alert = False
    box_D934F.enabled = True
    box_D934F.active = True
    box_D934F.use_property_split = False
    box_D934F.use_property_decorate = False
    box_D934F.alignment = 'Expand'.upper()
    box_D934F.scale_x = 1.0
    box_D934F.scale_y = 1.0
    if not True: box_D934F.operator_context = "EXEC_DEFAULT"
    box_D934F.label(text='Points Noise Type', icon_value=0)
    attr_308FF = '["' + str('Socket_58' + '"]') 
    box_D934F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_308FF, text='', icon_value=0, emboss=True, slider=True)
    box_681AB = box_51D21.box()
    box_681AB.alert = False
    box_681AB.enabled = True
    box_681AB.active = True
    box_681AB.use_property_split = False
    box_681AB.use_property_decorate = False
    box_681AB.alignment = 'Expand'.upper()
    box_681AB.scale_x = 1.0
    box_681AB.scale_y = 1.0
    if not True: box_681AB.operator_context = "EXEC_DEFAULT"
    attr_73DC8 = '["' + str('Socket_55' + '"]') 
    box_681AB.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_73DC8, text='Points Noise Strength', icon_value=0, emboss=True)
    attr_08419 = '["' + str('Socket_59' + '"]') 
    box_681AB.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_08419, text='Points Noise Randomize', icon_value=0, emboss=True)
    box_681AB.label(text='Strength - Attribute Influence', icon_value=0)
    attr_503AF = '["' + str('Socket_57' + '"]') 
    box_681AB.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_503AF, text='', icon_value=0, emboss=True, slider=True)
    box_EA219 = box_51D21.box()
    box_EA219.alert = False
    box_EA219.enabled = True
    box_EA219.active = True
    box_EA219.use_property_split = False
    box_EA219.use_property_decorate = False
    box_EA219.alignment = 'Expand'.upper()
    box_EA219.scale_x = 1.0
    box_EA219.scale_y = 1.0
    if not True: box_EA219.operator_context = "EXEC_DEFAULT"
    attr_EE36C = '["' + str('Socket_60' + '"]') 
    box_EA219.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_EE36C, text='Points Noise Scale', icon_value=0, emboss=True)
    box_EA219.label(text='Scale - Attribute Influence', icon_value=0)
    attr_574A6 = '["' + str('Socket_63' + '"]') 
    box_EA219.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_574A6, text='', icon_value=0, emboss=True)
    box_CB573 = box_51D21.box()
    box_CB573.alert = False
    box_CB573.enabled = True
    box_CB573.active = True
    box_CB573.use_property_split = False
    box_CB573.use_property_decorate = False
    box_CB573.alignment = 'Expand'.upper()
    box_CB573.scale_x = 1.0
    box_CB573.scale_y = 1.0
    if not True: box_CB573.operator_context = "EXEC_DEFAULT"
    attr_E41AB = '["' + str('Socket_61' + '"]') 
    box_CB573.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_E41AB, text='Points Noise Phase', icon_value=0, emboss=True)
    box_CB573.label(text='Phase - Attribute Influence', icon_value=0)
    attr_16CDE = '["' + str('Socket_62' + '"]') 
    box_CB573.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_16CDE, text='', icon_value=0, emboss=True)
    if (bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_98'] == 0):
        pass
    else:
        box_11908 = box_C9C2C.box()
        box_11908.alert = False
        box_11908.enabled = True
        box_11908.active = True
        box_11908.use_property_split = False
        box_11908.use_property_decorate = False
        box_11908.alignment = 'Expand'.upper()
        box_11908.scale_x = 1.0
        box_11908.scale_y = 1.0
        if not True: box_11908.operator_context = "EXEC_DEFAULT"
        box_C47B5 = box_11908.box()
        box_C47B5.alert = False
        box_C47B5.enabled = True
        box_C47B5.active = True
        box_C47B5.use_property_split = False
        box_C47B5.use_property_decorate = False
        box_C47B5.alignment = 'Expand'.upper()
        box_C47B5.scale_x = 1.0
        box_C47B5.scale_y = 1.0
        if not True: box_C47B5.operator_context = "EXEC_DEFAULT"
        box_C47B5.label(text='Mesh Effects', icon_value=0)
        attr_639A7 = '["' + str('Socket_100' + '"]') 
        box_C47B5.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_639A7, text='', icon_value=0, emboss=True, slider=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_100'] == 0):
            pass
        else:
            box_1C85D = box_11908.box()
            box_1C85D.alert = False
            box_1C85D.enabled = True
            box_1C85D.active = True
            box_1C85D.use_property_split = False
            box_1C85D.use_property_decorate = False
            box_1C85D.alignment = 'Expand'.upper()
            box_1C85D.scale_x = 1.0
            box_1C85D.scale_y = 1.0
            if not True: box_1C85D.operator_context = "EXEC_DEFAULT"
            box_1C85D.label(text='Mesh Face Scale', icon_value=0)
            attr_29FD4 = '["' + str('Socket_82' + '"]') 
            box_1C85D.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_29FD4, text='', icon_value=0, emboss=True, slider=True)
            if (bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_82'] == 0):
                attr_3EDBE = '["' + str('Socket_83' + '"]') 
                box_1C85D.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_3EDBE, text='Face Scale', icon_value=0, emboss=True, slider=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN']['Socket_100'] == 2):
            col_CCBB0 = box_11908.column(heading='', align=False)
            col_CCBB0.alert = False
            col_CCBB0.enabled = True
            col_CCBB0.active = True
            col_CCBB0.use_property_split = False
            col_CCBB0.use_property_decorate = False
            col_CCBB0.scale_x = 1.0
            col_CCBB0.scale_y = 1.0
            col_CCBB0.alignment = 'Expand'.upper()
            col_CCBB0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            box_5C7CC = col_CCBB0.box()
            box_5C7CC.alert = False
            box_5C7CC.enabled = True
            box_5C7CC.active = True
            box_5C7CC.use_property_split = False
            box_5C7CC.use_property_decorate = False
            box_5C7CC.alignment = 'Expand'.upper()
            box_5C7CC.scale_x = 1.0
            box_5C7CC.scale_y = 1.0
            if not True: box_5C7CC.operator_context = "EXEC_DEFAULT"
            box_5C7CC.label(text='Mesh Noise Type', icon_value=0)
            attr_DB81E = '["' + str('Socket_75' + '"]') 
            box_5C7CC.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_DB81E, text='', icon_value=0, emboss=True, slider=True)
            box_BEB2C = col_CCBB0.box()
            box_BEB2C.alert = False
            box_BEB2C.enabled = True
            box_BEB2C.active = True
            box_BEB2C.use_property_split = False
            box_BEB2C.use_property_decorate = False
            box_BEB2C.alignment = 'Expand'.upper()
            box_BEB2C.scale_x = 1.0
            box_BEB2C.scale_y = 1.0
            if not True: box_BEB2C.operator_context = "EXEC_DEFAULT"
            attr_1725C = '["' + str('Socket_77' + '"]') 
            box_BEB2C.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_1725C, text='Mesh Noise Strength', icon_value=0, emboss=True)
            attr_C1E69 = '["' + str('Socket_78' + '"]') 
            box_BEB2C.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_C1E69, text='Mesh Noise Randomize', icon_value=0, emboss=True)
            box_BEB2C.label(text='Strength - Attribute Influence', icon_value=0)
            attr_39E1D = '["' + str('Socket_76' + '"]') 
            box_BEB2C.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_39E1D, text='', icon_value=0, emboss=True, slider=True)
            box_6A41F = col_CCBB0.box()
            box_6A41F.alert = False
            box_6A41F.enabled = True
            box_6A41F.active = True
            box_6A41F.use_property_split = False
            box_6A41F.use_property_decorate = False
            box_6A41F.alignment = 'Expand'.upper()
            box_6A41F.scale_x = 1.0
            box_6A41F.scale_y = 1.0
            if not True: box_6A41F.operator_context = "EXEC_DEFAULT"
            attr_425A3 = '["' + str('Socket_74' + '"]') 
            box_6A41F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_425A3, text='Mesh Noise Scale', icon_value=0, emboss=True)
            box_6A41F.label(text='Scale - Attribute Influence', icon_value=0)
            attr_E7DC5 = '["' + str('Socket_73' + '"]') 
            box_6A41F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_E7DC5, text='', icon_value=0, emboss=True)
            box_89A74 = col_CCBB0.box()
            box_89A74.alert = False
            box_89A74.enabled = True
            box_89A74.active = True
            box_89A74.use_property_split = False
            box_89A74.use_property_decorate = False
            box_89A74.alignment = 'Expand'.upper()
            box_89A74.scale_x = 1.0
            box_89A74.scale_y = 1.0
            if not True: box_89A74.operator_context = "EXEC_DEFAULT"
            attr_FC887 = '["' + str('Socket_72' + '"]') 
            box_89A74.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_FC887, text='Mesh Noise Phase', icon_value=0, emboss=True)
            box_89A74.label(text='Phase - Attribute Influence', icon_value=0)
            attr_7358D = '["' + str('Socket_68' + '"]') 
            box_89A74.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Noise_GN'], attr_7358D, text='', icon_value=0, emboss=True)
    col_ACF71.separator(factor=1.0)
    grid_F32FF = col_ACF71.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=False)
    grid_F32FF.enabled = bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_noise
    grid_F32FF.active = True
    grid_F32FF.use_property_split = False
    grid_F32FF.use_property_decorate = False
    grid_F32FF.alignment = 'Expand'.upper()
    grid_F32FF.scale_x = 1.0
    grid_F32FF.scale_y = 1.0
    if not True: grid_F32FF.operator_context = "EXEC_DEFAULT"
    box_23761 = grid_F32FF.box()
    box_23761.alert = True
    box_23761.enabled = True
    box_23761.active = True
    box_23761.use_property_split = False
    box_23761.use_property_decorate = False
    box_23761.alignment = 'Expand'.upper()
    box_23761.scale_x = 1.0
    box_23761.scale_y = 2.0
    if not True: box_23761.operator_context = "EXEC_DEFAULT"
    op = box_23761.operator('sna.bake_noise_settings_354ca', text='BAKE', icon_value=0, emboss=True, depress=False)
    box_6A8CD = grid_F32FF.box()
    box_6A8CD.alert = True
    box_6A8CD.enabled = True
    box_6A8CD.active = True
    box_6A8CD.use_property_split = False
    box_6A8CD.use_property_decorate = False
    box_6A8CD.alignment = 'Expand'.upper()
    box_6A8CD.scale_x = 1.0
    box_6A8CD.scale_y = 2.0
    if not True: box_6A8CD.operator_context = "EXEC_DEFAULT"
    op = box_6A8CD.operator('sna.remove_bake_noise_settings_714b1', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'trash.svg')), emboss=True, depress=False)


class SNA_OT_Bake_Noise_Settings_354Ca(bpy.types.Operator):
    bl_idname = "sna.bake_noise_settings_354ca"
    bl_label = "Bake Noise Settings"
    bl_description = "Bakes current modifier settings."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_run_bake_node_function_execute_00810('KIRI_3DGS_Point_Animate_Noise_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.noise_baked = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Remove_Bake_Noise_Settings_714B1(bpy.types.Operator):
    bl_idname = "sna.remove_bake_noise_settings_714b1"
    bl_label = "Remove Bake Noise Settings"
    bl_description = "Removes baked data."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_remove_bake_node_function_execute_80F90('KIRI_3DGS_Point_Animate_Noise_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.noise_baked = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_snap_function_interface_8E0BA(layout_function, ):
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_snap:
        pass
    else:
        box_23173 = layout_function.box()
        box_23173.alert = True
        box_23173.enabled = True
        box_23173.active = True
        box_23173.use_property_split = False
        box_23173.use_property_decorate = False
        box_23173.alignment = 'Expand'.upper()
        box_23173.scale_x = 1.0
        box_23173.scale_y = 1.0
        if not True: box_23173.operator_context = "EXEC_DEFAULT"
        box_23173.label(text='Snap To Shape is disabled', icon_value=0)
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.snap_baked:
        box_ACF4C = layout_function.box()
        box_ACF4C.alert = True
        box_ACF4C.enabled = True
        box_ACF4C.active = True
        box_ACF4C.use_property_split = False
        box_ACF4C.use_property_decorate = False
        box_ACF4C.alignment = 'Expand'.upper()
        box_ACF4C.scale_x = 1.0
        box_ACF4C.scale_y = 1.0
        if not True: box_ACF4C.operator_context = "EXEC_DEFAULT"
        box_ACF4C.label(text='Modifiers settings are baked', icon_value=0)
    col_7B974 = layout_function.column(heading='', align=False)
    col_7B974.alert = False
    col_7B974.enabled = True
    col_7B974.active = True
    col_7B974.use_property_split = False
    col_7B974.use_property_decorate = False
    col_7B974.scale_x = 1.0
    col_7B974.scale_y = 1.0
    col_7B974.alignment = 'Expand'.upper()
    col_7B974.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    box_3DB4C = col_7B974.box()
    box_3DB4C.alert = False
    box_3DB4C.enabled = (bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_snap and (not bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.snap_baked))
    box_3DB4C.active = True
    box_3DB4C.use_property_split = False
    box_3DB4C.use_property_decorate = False
    box_3DB4C.alignment = 'Expand'.upper()
    box_3DB4C.scale_x = 1.0
    box_3DB4C.scale_y = 1.0
    if not True: box_3DB4C.operator_context = "EXEC_DEFAULT"
    box_6FD5B = box_3DB4C.box()
    box_6FD5B.alert = False
    box_6FD5B.enabled = True
    box_6FD5B.active = True
    box_6FD5B.use_property_split = False
    box_6FD5B.use_property_decorate = False
    box_6FD5B.alignment = 'Expand'.upper()
    box_6FD5B.scale_x = 1.0
    box_6FD5B.scale_y = 1.0
    if not True: box_6FD5B.operator_context = "EXEC_DEFAULT"
    attr_5000D = '["' + str('Socket_6' + '"]') 
    box_6FD5B.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_5000D, text='Preview Shapes', icon_value=0, emboss=True, slider=False, toggle=True)
    col_58B32 = box_3DB4C.column(heading='', align=True)
    col_58B32.alert = False
    col_58B32.enabled = True
    col_58B32.active = True
    col_58B32.use_property_split = False
    col_58B32.use_property_decorate = False
    col_58B32.scale_x = 1.0
    col_58B32.scale_y = 1.0
    col_58B32.alignment = 'Expand'.upper()
    col_58B32.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    box_0EEB8 = col_58B32.box()
    box_0EEB8.alert = False
    box_0EEB8.enabled = True
    box_0EEB8.active = True
    box_0EEB8.use_property_split = False
    box_0EEB8.use_property_decorate = False
    box_0EEB8.alignment = 'Expand'.upper()
    box_0EEB8.scale_x = 1.0
    box_0EEB8.scale_y = 1.0
    if not True: box_0EEB8.operator_context = "EXEC_DEFAULT"
    box_0EEB8.label(text='Grid Movement', icon_value=0)
    attr_EC184 = '["' + str('Socket_28' + '"]') 
    box_0EEB8.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_EC184, text='', icon_value=0, emboss=True, slider=False, toggle=True)
    box_7973D = col_58B32.box()
    box_7973D.alert = False
    box_7973D.enabled = True
    box_7973D.active = True
    box_7973D.use_property_split = False
    box_7973D.use_property_decorate = False
    box_7973D.alignment = 'Expand'.upper()
    box_7973D.scale_x = 1.0
    box_7973D.scale_y = 1.0
    if not True: box_7973D.operator_context = "EXEC_DEFAULT"
    box_7973D.label(text='Grid Points', icon_value=0)
    grid_1DA3B = box_7973D.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=True)
    grid_1DA3B.enabled = True
    grid_1DA3B.active = True
    grid_1DA3B.use_property_split = False
    grid_1DA3B.use_property_decorate = False
    grid_1DA3B.alignment = 'Expand'.upper()
    grid_1DA3B.scale_x = 1.0
    grid_1DA3B.scale_y = 1.0
    if not True: grid_1DA3B.operator_context = "EXEC_DEFAULT"
    attr_4FC45 = '["' + str('Socket_18' + '"]') 
    grid_1DA3B.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_4FC45, text='X', icon_value=0, emboss=True, slider=False, toggle=True)
    attr_58551 = '["' + str('Socket_19' + '"]') 
    grid_1DA3B.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_58551, text='Y', icon_value=0, emboss=True, slider=False, toggle=True)
    attr_91332 = '["' + str('Socket_20' + '"]') 
    grid_1DA3B.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_91332, text='Z', icon_value=0, emboss=True, slider=False, toggle=True)
    box_4F5BF = col_58B32.box()
    box_4F5BF.alert = False
    box_4F5BF.enabled = True
    box_4F5BF.active = True
    box_4F5BF.use_property_split = False
    box_4F5BF.use_property_decorate = False
    box_4F5BF.alignment = 'Expand'.upper()
    box_4F5BF.scale_x = 1.0
    box_4F5BF.scale_y = 1.0
    if not True: box_4F5BF.operator_context = "EXEC_DEFAULT"
    box_4F5BF.label(text='Grid Translate', icon_value=0)
    row_02DB8 = box_4F5BF.row(heading='', align=False)
    row_02DB8.alert = False
    row_02DB8.enabled = True
    row_02DB8.active = True
    row_02DB8.use_property_split = False
    row_02DB8.use_property_decorate = False
    row_02DB8.scale_x = 1.0
    row_02DB8.scale_y = 1.0
    row_02DB8.alignment = 'Expand'.upper()
    row_02DB8.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    attr_6FB7F = '["' + str('Socket_25' + '"]') 
    row_02DB8.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_6FB7F, text='', icon_value=0, emboss=True, slider=False, toggle=False)
    box_F5EE6 = col_58B32.box()
    box_F5EE6.alert = False
    box_F5EE6.enabled = True
    box_F5EE6.active = True
    box_F5EE6.use_property_split = False
    box_F5EE6.use_property_decorate = False
    box_F5EE6.alignment = 'Expand'.upper()
    box_F5EE6.scale_x = 1.0
    box_F5EE6.scale_y = 1.0
    if not True: box_F5EE6.operator_context = "EXEC_DEFAULT"
    box_F5EE6.label(text='Grid Rotate', icon_value=0)
    row_896AD = box_F5EE6.row(heading='', align=False)
    row_896AD.alert = False
    row_896AD.enabled = True
    row_896AD.active = True
    row_896AD.use_property_split = False
    row_896AD.use_property_decorate = False
    row_896AD.scale_x = 1.0
    row_896AD.scale_y = 1.0
    row_896AD.alignment = 'Expand'.upper()
    row_896AD.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    attr_E2B7B = '["' + str('Socket_26' + '"]') 
    row_896AD.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_E2B7B, text='', icon_value=0, emboss=True, slider=False, toggle=False)
    box_C1DF4 = col_58B32.box()
    box_C1DF4.alert = False
    box_C1DF4.enabled = True
    box_C1DF4.active = True
    box_C1DF4.use_property_split = False
    box_C1DF4.use_property_decorate = False
    box_C1DF4.alignment = 'Expand'.upper()
    box_C1DF4.scale_x = 1.0
    box_C1DF4.scale_y = 1.0
    if not True: box_C1DF4.operator_context = "EXEC_DEFAULT"
    box_C1DF4.label(text='Grid Scale', icon_value=0)
    row_B8609 = box_C1DF4.row(heading='', align=False)
    row_B8609.alert = False
    row_B8609.enabled = True
    row_B8609.active = True
    row_B8609.use_property_split = False
    row_B8609.use_property_decorate = False
    row_B8609.scale_x = 1.0
    row_B8609.scale_y = 1.0
    row_B8609.alignment = 'Expand'.upper()
    row_B8609.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    attr_04162 = '["' + str('Socket_27' + '"]') 
    row_B8609.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_04162, text='', icon_value=0, emboss=True, slider=False, toggle=False)
    col_0215A = box_3DB4C.column(heading='', align=False)
    col_0215A.alert = False
    col_0215A.enabled = True
    col_0215A.active = True
    col_0215A.use_property_split = False
    col_0215A.use_property_decorate = False
    col_0215A.scale_x = 1.0
    col_0215A.scale_y = 1.0
    col_0215A.alignment = 'Expand'.upper()
    col_0215A.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    box_C5339 = col_0215A.box()
    box_C5339.alert = False
    box_C5339.enabled = True
    box_C5339.active = True
    box_C5339.use_property_split = False
    box_C5339.use_property_decorate = False
    box_C5339.alignment = 'Expand'.upper()
    box_C5339.scale_x = 1.0
    box_C5339.scale_y = 1.0
    if not True: box_C5339.operator_context = "EXEC_DEFAULT"
    box_C5339.label(text='Shape', icon_value=0)
    attr_B8B86 = '["' + str('Socket_7' + '"]') 
    box_C5339.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_B8B86, text='', icon_value=0, emboss=True, slider=False, toggle=True)
    if (bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_7'] == 7):
        box_F3CAB = box_C5339.box()
        box_F3CAB.alert = False
        box_F3CAB.enabled = True
        box_F3CAB.active = True
        box_F3CAB.use_property_split = False
        box_F3CAB.use_property_decorate = False
        box_F3CAB.alignment = 'Expand'.upper()
        box_F3CAB.scale_x = 1.0
        box_F3CAB.scale_y = 1.0
        if not True: box_F3CAB.operator_context = "EXEC_DEFAULT"
        box_F3CAB.label(text='Custom Object', icon_value=0)
        attr_7B0DD = '["' + str('Socket_2' + '"]') 
        box_F3CAB.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_7B0DD, text='', icon_value=0, emboss=True, slider=False, toggle=True)
    box_E1FDB = col_0215A.box()
    box_E1FDB.alert = False
    box_E1FDB.enabled = True
    box_E1FDB.active = True
    box_E1FDB.use_property_split = False
    box_E1FDB.use_property_decorate = False
    box_E1FDB.alignment = 'Expand'.upper()
    box_E1FDB.scale_x = 1.0
    box_E1FDB.scale_y = 1.0
    if not True: box_E1FDB.operator_context = "EXEC_DEFAULT"
    box_E1FDB.label(text='Shape Translate', icon_value=0)
    row_78FBC = box_E1FDB.row(heading='', align=False)
    row_78FBC.alert = False
    row_78FBC.enabled = True
    row_78FBC.active = True
    row_78FBC.use_property_split = False
    row_78FBC.use_property_decorate = False
    row_78FBC.scale_x = 1.0
    row_78FBC.scale_y = 1.0
    row_78FBC.alignment = 'Expand'.upper()
    row_78FBC.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    attr_A19B7 = '["' + str('Socket_29' + '"]') 
    row_78FBC.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_A19B7, text='', icon_value=0, emboss=True, slider=False, toggle=False)
    box_3889A = col_0215A.box()
    box_3889A.alert = False
    box_3889A.enabled = True
    box_3889A.active = True
    box_3889A.use_property_split = False
    box_3889A.use_property_decorate = False
    box_3889A.alignment = 'Expand'.upper()
    box_3889A.scale_x = 1.0
    box_3889A.scale_y = 1.0
    if not True: box_3889A.operator_context = "EXEC_DEFAULT"
    box_3889A.label(text='Shape Rotate', icon_value=0)
    row_8DE06 = box_3889A.row(heading='', align=False)
    row_8DE06.alert = False
    row_8DE06.enabled = True
    row_8DE06.active = True
    row_8DE06.use_property_split = False
    row_8DE06.use_property_decorate = False
    row_8DE06.scale_x = 1.0
    row_8DE06.scale_y = 1.0
    row_8DE06.alignment = 'Expand'.upper()
    row_8DE06.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    attr_252F8 = '["' + str('Socket_4' + '"]') 
    row_8DE06.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_252F8, text='', icon_value=0, emboss=True, slider=False, toggle=False)
    box_C9C71 = col_0215A.box()
    box_C9C71.alert = False
    box_C9C71.enabled = True
    box_C9C71.active = True
    box_C9C71.use_property_split = False
    box_C9C71.use_property_decorate = False
    box_C9C71.alignment = 'Expand'.upper()
    box_C9C71.scale_x = 1.0
    box_C9C71.scale_y = 1.0
    if not True: box_C9C71.operator_context = "EXEC_DEFAULT"
    box_C9C71.label(text='Shape Scale', icon_value=0)
    row_372D2 = box_C9C71.row(heading='', align=False)
    row_372D2.alert = False
    row_372D2.enabled = True
    row_372D2.active = True
    row_372D2.use_property_split = False
    row_372D2.use_property_decorate = False
    row_372D2.scale_x = 1.0
    row_372D2.scale_y = 1.0
    row_372D2.alignment = 'Expand'.upper()
    row_372D2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    attr_5CCCD = '["' + str('Socket_3' + '"]') 
    row_372D2.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_5CCCD, text='', icon_value=0, emboss=True, slider=False, toggle=False)
    box_5D225 = box_3DB4C.box()
    box_5D225.alert = False
    box_5D225.enabled = True
    box_5D225.active = True
    box_5D225.use_property_split = False
    box_5D225.use_property_decorate = False
    box_5D225.alignment = 'Expand'.upper()
    box_5D225.scale_x = 1.0
    box_5D225.scale_y = 1.0
    if not True: box_5D225.operator_context = "EXEC_DEFAULT"
    attr_809D9 = '["' + str('Socket_13' + '"]') 
    box_5D225.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_809D9, text='Selection', icon_value=0, emboss=True, toggle=True)
    box_5D225.label(text='Selection - Attribute Influence', icon_value=0)
    attr_C869B = '["' + str('Socket_22' + '"]') 
    box_5D225.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_C869B, text='', icon_value=0, emboss=True, toggle=True)
    box_CC43C = box_3DB4C.box()
    box_CC43C.alert = False
    box_CC43C.enabled = True
    box_CC43C.active = True
    box_CC43C.use_property_split = False
    box_CC43C.use_property_decorate = False
    box_CC43C.alignment = 'Expand'.upper()
    box_CC43C.scale_x = 1.0
    box_CC43C.scale_y = 1.0
    if not True: box_CC43C.operator_context = "EXEC_DEFAULT"
    box_CC43C.label(text='Masking', icon_value=0)
    attr_893EE = '["' + str('Socket_12' + '"]') 
    box_CC43C.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_893EE, text='', icon_value=0, emboss=True)
    if (bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_12'] == 0):
        pass
    else:
        col_9069F = box_CC43C.column(heading='', align=False)
        col_9069F.alert = False
        col_9069F.enabled = True
        col_9069F.active = True
        col_9069F.use_property_split = False
        col_9069F.use_property_decorate = False
        col_9069F.scale_x = 1.0
        col_9069F.scale_y = 1.0
        col_9069F.alignment = 'Expand'.upper()
        col_9069F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_9069F.label(text='Mask By:', icon_value=0)
        attr_6097D = '["' + str('Socket_14' + '"]') 
        col_9069F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_6097D, text='', icon_value=0, emboss=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_14'] == 0):
            attr_A8C05 = '["' + str('Socket_15' + '"]') 
            col_9069F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_A8C05, text='', icon_value=0, emboss=True)
        else:
            col_9069F.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], '["Socket_16"]', bpy.data, 'collections', text='', icon='NONE', item_search_property="name")
        if ((bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_12'] == 3) or (bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN']['Socket_12'] == 4)):
            attr_77D2D = '["' + str('Socket_11' + '"]') 
            col_9069F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_77D2D, text='Distance Threshold', icon_value=0, emboss=True)
    box_243C2 = box_3DB4C.box()
    box_243C2.alert = False
    box_243C2.enabled = True
    box_243C2.active = True
    box_243C2.use_property_split = False
    box_243C2.use_property_decorate = False
    box_243C2.alignment = 'Expand'.upper()
    box_243C2.scale_x = 1.0
    box_243C2.scale_y = 1.0
    if not True: box_243C2.operator_context = "EXEC_DEFAULT"
    attr_7C198 = '["' + str('Socket_5' + '"]') 
    box_243C2.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_7C198, text='Effect Strength', icon_value=0, emboss=True, toggle=True)
    box_243C2.label(text='Strength - Attribute Influence', icon_value=0)
    attr_D6520 = '["' + str('Socket_22' + '"]') 
    box_243C2.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_3DGS_Point_Animate_Snap_To_Shape_GN'], attr_D6520, text='', icon_value=0, emboss=True, toggle=True)
    col_7B974.separator(factor=1.0)
    grid_0E6D5 = col_7B974.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=False)
    grid_0E6D5.enabled = bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_snap
    grid_0E6D5.active = True
    grid_0E6D5.use_property_split = False
    grid_0E6D5.use_property_decorate = False
    grid_0E6D5.alignment = 'Expand'.upper()
    grid_0E6D5.scale_x = 1.0
    grid_0E6D5.scale_y = 1.0
    if not True: grid_0E6D5.operator_context = "EXEC_DEFAULT"
    box_3B050 = grid_0E6D5.box()
    box_3B050.alert = True
    box_3B050.enabled = True
    box_3B050.active = True
    box_3B050.use_property_split = False
    box_3B050.use_property_decorate = False
    box_3B050.alignment = 'Expand'.upper()
    box_3B050.scale_x = 1.0
    box_3B050.scale_y = 2.0
    if not True: box_3B050.operator_context = "EXEC_DEFAULT"
    op = box_3B050.operator('sna.bake_snap_settings_9226d', text='BAKE', icon_value=0, emboss=True, depress=False)
    box_3C394 = grid_0E6D5.box()
    box_3C394.alert = True
    box_3C394.enabled = True
    box_3C394.active = True
    box_3C394.use_property_split = False
    box_3C394.use_property_decorate = False
    box_3C394.alignment = 'Expand'.upper()
    box_3C394.scale_x = 1.0
    box_3C394.scale_y = 2.0
    if not True: box_3C394.operator_context = "EXEC_DEFAULT"
    op = box_3C394.operator('sna.remove_bake_snap_settings_a2139', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'trash.svg')), emboss=True, depress=False)


class SNA_OT_Bake_Snap_Settings_9226D(bpy.types.Operator):
    bl_idname = "sna.bake_snap_settings_9226d"
    bl_label = "Bake Snap Settings"
    bl_description = "Bakes current modifier settings."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_run_bake_node_function_execute_00810('KIRI_3DGS_Point_Animate_Snap_To_Shape_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.snap_baked = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Remove_Bake_Snap_Settings_A2139(bpy.types.Operator):
    bl_idname = "sna.remove_bake_snap_settings_a2139"
    bl_label = "Remove Bake Snap Settings"
    bl_description = "Removes baked data."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_remove_bake_node_function_execute_80F90('KIRI_3DGS_Point_Animate_Snap_To_Shape_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.snap_baked = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_wind_function_interface_178D5(layout_function, ):
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wind:
        pass
    else:
        box_B8D90 = layout_function.box()
        box_B8D90.alert = True
        box_B8D90.enabled = True
        box_B8D90.active = True
        box_B8D90.use_property_split = False
        box_B8D90.use_property_decorate = False
        box_B8D90.alignment = 'Expand'.upper()
        box_B8D90.scale_x = 1.0
        box_B8D90.scale_y = 1.0
        if not True: box_B8D90.operator_context = "EXEC_DEFAULT"
        box_B8D90.label(text='Wind is disabled', icon_value=0)
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.wind_baked:
        box_3E3AC = layout_function.box()
        box_3E3AC.alert = True
        box_3E3AC.enabled = True
        box_3E3AC.active = True
        box_3E3AC.use_property_split = False
        box_3E3AC.use_property_decorate = False
        box_3E3AC.alignment = 'Expand'.upper()
        box_3E3AC.scale_x = 1.0
        box_3E3AC.scale_y = 1.0
        if not True: box_3E3AC.operator_context = "EXEC_DEFAULT"
        box_3E3AC.label(text='Modifiers settings are baked', icon_value=0)
    col_EECF5 = layout_function.column(heading='', align=False)
    col_EECF5.alert = False
    col_EECF5.enabled = True
    col_EECF5.active = True
    col_EECF5.use_property_split = False
    col_EECF5.use_property_decorate = False
    col_EECF5.scale_x = 1.0
    col_EECF5.scale_y = 1.0
    col_EECF5.alignment = 'Expand'.upper()
    col_EECF5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    col_62BDC = col_EECF5.column(heading='', align=True)
    col_62BDC.alert = False
    col_62BDC.enabled = (bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wind and (not bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.wind_baked))
    col_62BDC.active = True
    col_62BDC.use_property_split = False
    col_62BDC.use_property_decorate = False
    col_62BDC.scale_x = 1.0
    col_62BDC.scale_y = 1.0
    col_62BDC.alignment = 'Expand'.upper()
    col_62BDC.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    box_AB2B5 = col_62BDC.box()
    box_AB2B5.alert = False
    box_AB2B5.enabled = True
    box_AB2B5.active = True
    box_AB2B5.use_property_split = False
    box_AB2B5.use_property_decorate = False
    box_AB2B5.alignment = 'Expand'.upper()
    box_AB2B5.scale_x = 1.0
    box_AB2B5.scale_y = 1.0
    if not True: box_AB2B5.operator_context = "EXEC_DEFAULT"
    box_AB2B5.label(text='Input / Output', icon_value=0)
    attr_B15E4 = '["' + str('Socket_76' + '"]') 
    box_AB2B5.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_B15E4, text='', icon_value=0, emboss=True, slider=True)
    if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_76'] == 1):
        box_297F2 = col_62BDC.box()
        box_297F2.alert = False
        box_297F2.enabled = True
        box_297F2.active = True
        box_297F2.use_property_split = False
        box_297F2.use_property_decorate = False
        box_297F2.alignment = 'Expand'.upper()
        box_297F2.scale_x = 1.0
        box_297F2.scale_y = 1.0
        if not True: box_297F2.operator_context = "EXEC_DEFAULT"
        box_297F2.label(text='Mesh Face Scale', icon_value=0)
        attr_8E6C5 = '["' + str('Socket_79' + '"]') 
        box_297F2.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_8E6C5, text='', icon_value=0, emboss=True, slider=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_79'] == 12):
            box_9675F = box_297F2.box()
            box_9675F.alert = False
            box_9675F.enabled = True
            box_9675F.active = True
            box_9675F.use_property_split = False
            box_9675F.use_property_decorate = False
            box_9675F.alignment = 'Expand'.upper()
            box_9675F.scale_x = 1.0
            box_9675F.scale_y = 1.0
            if not True: box_9675F.operator_context = "EXEC_DEFAULT"
            box_9675F.label(text='Face Scale', icon_value=0)
            attr_A4E72 = '["' + str('Socket_78' + '"]') 
            box_9675F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_A4E72, text='', icon_value=0, emboss=True, slider=True)
    box_EF746 = col_62BDC.box()
    box_EF746.alert = False
    box_EF746.enabled = True
    box_EF746.active = True
    box_EF746.use_property_split = False
    box_EF746.use_property_decorate = False
    box_EF746.alignment = 'Expand'.upper()
    box_EF746.scale_x = 1.0
    box_EF746.scale_y = 1.0
    if not True: box_EF746.operator_context = "EXEC_DEFAULT"
    box_EF746.label(text='Selection', icon_value=0)
    attr_76D16 = '["' + str('Socket_69' + '"]') 
    box_EF746.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_76D16, text='', icon_value=0, emboss=True, slider=True)
    if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_69'] == 0):
        box_190C4 = box_EF746.box()
        box_190C4.alert = False
        box_190C4.enabled = True
        box_190C4.active = True
        box_190C4.use_property_split = False
        box_190C4.use_property_decorate = False
        box_190C4.alignment = 'Expand'.upper()
        box_190C4.scale_x = 1.0
        box_190C4.scale_y = 1.0
        if not True: box_190C4.operator_context = "EXEC_DEFAULT"
        box_190C4.label(text='Selection Factor', icon_value=0)
        attr_741C8 = '["' + str('Socket_54' + '"]') 
        box_190C4.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_741C8, text='', icon_value=0, emboss=True, slider=True)
    box_63AD7 = col_62BDC.box()
    box_63AD7.alert = False
    box_63AD7.enabled = True
    box_63AD7.active = True
    box_63AD7.use_property_split = False
    box_63AD7.use_property_decorate = False
    box_63AD7.alignment = 'Expand'.upper()
    box_63AD7.scale_x = 1.0
    box_63AD7.scale_y = 1.0
    if not True: box_63AD7.operator_context = "EXEC_DEFAULT"
    box_63AD7.label(text='Masking', icon_value=0)
    attr_C4F74 = '["' + str('Socket_62' + '"]') 
    box_63AD7.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_C4F74, text='', icon_value=0, emboss=True, slider=True)
    if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_62'] == 0):
        pass
    else:
        col_6ECCB = box_63AD7.column(heading='', align=False)
        col_6ECCB.alert = False
        col_6ECCB.enabled = True
        col_6ECCB.active = True
        col_6ECCB.use_property_split = False
        col_6ECCB.use_property_decorate = False
        col_6ECCB.scale_x = 1.0
        col_6ECCB.scale_y = 1.0
        col_6ECCB.alignment = 'Expand'.upper()
        col_6ECCB.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_2BEB3 = col_6ECCB.box()
        box_2BEB3.alert = False
        box_2BEB3.enabled = True
        box_2BEB3.active = True
        box_2BEB3.use_property_split = False
        box_2BEB3.use_property_decorate = False
        box_2BEB3.alignment = 'Expand'.upper()
        box_2BEB3.scale_x = 1.0
        box_2BEB3.scale_y = 1.0
        if not True: box_2BEB3.operator_context = "EXEC_DEFAULT"
        box_2BEB3.label(text='Mask By:', icon_value=0)
        attr_1E5F2 = '["' + str('Socket_67' + '"]') 
        box_2BEB3.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_1E5F2, text='', icon_value=0, emboss=True, slider=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_67'] == 0):
            attr_47589 = '["' + str('Socket_66' + '"]') 
            box_2BEB3.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_47589, text='', icon_value=0, emboss=True, slider=True)
        else:
            box_2BEB3.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], '["Socket_59"]', bpy.data, 'collections', text='', icon='NONE', item_search_property="name")
        if ((bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_62'] == 3) or (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN']['Socket_62'] == 4)):
            box_B4972 = col_6ECCB.box()
            box_B4972.alert = False
            box_B4972.enabled = True
            box_B4972.active = True
            box_B4972.use_property_split = False
            box_B4972.use_property_decorate = False
            box_B4972.alignment = 'Expand'.upper()
            box_B4972.scale_x = 1.0
            box_B4972.scale_y = 1.0
            if not True: box_B4972.operator_context = "EXEC_DEFAULT"
            box_B4972.label(text='Distance Threshold', icon_value=0)
            attr_4BA90 = '["' + str('Socket_68' + '"]') 
            box_B4972.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_4BA90, text='', icon_value=0, emboss=True, slider=False)
    box_62887 = col_62BDC.box()
    box_62887.alert = False
    box_62887.enabled = True
    box_62887.active = True
    box_62887.use_property_split = False
    box_62887.use_property_decorate = False
    box_62887.alignment = 'Expand'.upper()
    box_62887.scale_x = 1.0
    box_62887.scale_y = 1.0
    if not True: box_62887.operator_context = "EXEC_DEFAULT"
    box_62887.label(text='Wind Controller', icon_value=0)
    attr_7A194 = '["' + str('Socket_81' + '"]') 
    box_62887.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_7A194, text='', icon_value=0, emboss=True, slider=True)
    box_62887.label(text='Wind Strength', icon_value=0)
    attr_B0FBF = '["' + str('Socket_50' + '"]') 
    box_62887.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_B0FBF, text='', icon_value=0, emboss=True, slider=False)
    box_62887.label(text='Random Mix', icon_value=0)
    attr_48DB0 = '["' + str('Socket_73' + '"]') 
    box_62887.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_48DB0, text='', icon_value=0, emboss=True, slider=False)
    box_62887.label(text='Random Divider', icon_value=0)
    attr_B044B = '["' + str('Socket_63' + '"]') 
    box_62887.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_B044B, text='', icon_value=0, emboss=True, slider=False)
    box_D6406 = col_62BDC.box()
    box_D6406.alert = False
    box_D6406.enabled = True
    box_D6406.active = True
    box_D6406.use_property_split = False
    box_D6406.use_property_decorate = False
    box_D6406.alignment = 'Expand'.upper()
    box_D6406.scale_x = 1.0
    box_D6406.scale_y = 1.0
    if not True: box_D6406.operator_context = "EXEC_DEFAULT"
    box_D6406.label(text='Delete By Age', icon_value=0)
    attr_2B9EA = '["' + str('Socket_90' + '"]') 
    box_D6406.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wind_GN'], attr_2B9EA, text='Age Threshold', icon_value=0, emboss=True, slider=True)
    col_EECF5.separator(factor=1.0)
    grid_14F4F = col_EECF5.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=False)
    grid_14F4F.enabled = bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wind
    grid_14F4F.active = True
    grid_14F4F.use_property_split = False
    grid_14F4F.use_property_decorate = False
    grid_14F4F.alignment = 'Expand'.upper()
    grid_14F4F.scale_x = 1.0
    grid_14F4F.scale_y = 1.0
    if not True: grid_14F4F.operator_context = "EXEC_DEFAULT"
    box_BA352 = grid_14F4F.box()
    box_BA352.alert = True
    box_BA352.enabled = True
    box_BA352.active = True
    box_BA352.use_property_split = False
    box_BA352.use_property_decorate = False
    box_BA352.alignment = 'Expand'.upper()
    box_BA352.scale_x = 1.0
    box_BA352.scale_y = 2.0
    if not True: box_BA352.operator_context = "EXEC_DEFAULT"
    op = box_BA352.operator('sna.bake_wind_settings_8567d', text='BAKE', icon_value=0, emboss=True, depress=False)
    box_C0C37 = grid_14F4F.box()
    box_C0C37.alert = True
    box_C0C37.enabled = True
    box_C0C37.active = True
    box_C0C37.use_property_split = False
    box_C0C37.use_property_decorate = False
    box_C0C37.alignment = 'Expand'.upper()
    box_C0C37.scale_x = 1.0
    box_C0C37.scale_y = 2.0
    if not True: box_C0C37.operator_context = "EXEC_DEFAULT"
    op = box_C0C37.operator('sna.remove_bake_wind_settings_3c21d', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'trash.svg')), emboss=True, depress=False)


class SNA_OT_Bake_Wind_Settings_8567D(bpy.types.Operator):
    bl_idname = "sna.bake_wind_settings_8567d"
    bl_label = "Bake Wind Settings"
    bl_description = "Bakes current modifier settings."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_run_bake_node_function_execute_00810('KIRI_Point_Animate_Wind_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.wind_baked = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Remove_Bake_Wind_Settings_3C21D(bpy.types.Operator):
    bl_idname = "sna.remove_bake_wind_settings_3c21d"
    bl_label = "Remove Bake Wind Settings"
    bl_description = "Removes baked data."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_remove_bake_node_function_execute_80F90('KIRI_Point_Animate_Wind_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.wind_baked = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_wireframe_function_interface_67E1B(layout_function, ):
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wireframe:
        pass
    else:
        box_68D2A = layout_function.box()
        box_68D2A.alert = True
        box_68D2A.enabled = True
        box_68D2A.active = True
        box_68D2A.use_property_split = False
        box_68D2A.use_property_decorate = False
        box_68D2A.alignment = 'Expand'.upper()
        box_68D2A.scale_x = 1.0
        box_68D2A.scale_y = 1.0
        if not True: box_68D2A.operator_context = "EXEC_DEFAULT"
        box_68D2A.label(text='Wireframe is disabled', icon_value=0)
    if bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.wireframe_baked:
        box_913EC = layout_function.box()
        box_913EC.alert = True
        box_913EC.enabled = True
        box_913EC.active = True
        box_913EC.use_property_split = False
        box_913EC.use_property_decorate = False
        box_913EC.alignment = 'Expand'.upper()
        box_913EC.scale_x = 1.0
        box_913EC.scale_y = 1.0
        if not True: box_913EC.operator_context = "EXEC_DEFAULT"
        box_913EC.label(text='Modifiers settings are baked', icon_value=0)
    col_1E0D3 = layout_function.column(heading='', align=False)
    col_1E0D3.alert = False
    col_1E0D3.enabled = True
    col_1E0D3.active = True
    col_1E0D3.use_property_split = False
    col_1E0D3.use_property_decorate = False
    col_1E0D3.scale_x = 1.0
    col_1E0D3.scale_y = 1.0
    col_1E0D3.alignment = 'Expand'.upper()
    col_1E0D3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    box_5C0DE = col_1E0D3.box()
    box_5C0DE.alert = False
    box_5C0DE.enabled = (bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wireframe and (not bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.wireframe_baked))
    box_5C0DE.active = True
    box_5C0DE.use_property_split = False
    box_5C0DE.use_property_decorate = False
    box_5C0DE.alignment = 'Expand'.upper()
    box_5C0DE.scale_x = 1.0
    box_5C0DE.scale_y = 1.0
    if not True: box_5C0DE.operator_context = "EXEC_DEFAULT"
    box_02E3E = box_5C0DE.box()
    box_02E3E.alert = False
    box_02E3E.enabled = True
    box_02E3E.active = True
    box_02E3E.use_property_split = False
    box_02E3E.use_property_decorate = False
    box_02E3E.alignment = 'Expand'.upper()
    box_02E3E.scale_x = 1.0
    box_02E3E.scale_y = 1.0
    if not True: box_02E3E.operator_context = "EXEC_DEFAULT"
    box_02E3E.label(text='Single / Multiple', icon_value=0)
    attr_35556 = '["' + str('Socket_15' + '"]') 
    box_02E3E.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_35556, text='', icon_value=0, emboss=True, slider=False, toggle=True)
    box_705F8 = box_5C0DE.box()
    box_705F8.alert = False
    box_705F8.enabled = True
    box_705F8.active = True
    box_705F8.use_property_split = False
    box_705F8.use_property_decorate = False
    box_705F8.alignment = 'Expand'.upper()
    box_705F8.scale_x = 1.0
    box_705F8.scale_y = 1.0
    if not True: box_705F8.operator_context = "EXEC_DEFAULT"
    box_705F8.label(text='Point Order', icon_value=0)
    attr_0331E = '["' + str('Socket_39' + '"]') 
    box_705F8.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_0331E, text='', icon_value=0, emboss=True, slider=False, toggle=True)
    if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_39'] == 5):
        col_9E062 = box_705F8.column(heading='', align=True)
        col_9E062.alert = False
        col_9E062.enabled = True
        col_9E062.active = True
        col_9E062.use_property_split = False
        col_9E062.use_property_decorate = False
        col_9E062.scale_x = 1.0
        col_9E062.scale_y = 1.0
        col_9E062.alignment = 'Expand'.upper()
        col_9E062.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_9E062.label(text='Custom Object', icon_value=0)
        attr_D33BD = '["' + str('Socket_40' + '"]') 
        col_9E062.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_D33BD, text='', icon_value=0, emboss=True, slider=False, toggle=True)
    box_D2AB5 = box_5C0DE.box()
    box_D2AB5.alert = False
    box_D2AB5.enabled = True
    box_D2AB5.active = True
    box_D2AB5.use_property_split = False
    box_D2AB5.use_property_decorate = False
    box_D2AB5.alignment = 'Expand'.upper()
    box_D2AB5.scale_x = 1.0
    box_D2AB5.scale_y = 1.0
    if not True: box_D2AB5.operator_context = "EXEC_DEFAULT"
    attr_706F4 = '["' + str('Socket_18' + '"]') 
    box_D2AB5.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_706F4, text='Selection', icon_value=0, emboss=True, slider=True, toggle=False)
    box_6F2D3 = box_5C0DE.box()
    box_6F2D3.alert = False
    box_6F2D3.enabled = True
    box_6F2D3.active = True
    box_6F2D3.use_property_split = False
    box_6F2D3.use_property_decorate = False
    box_6F2D3.alignment = 'Expand'.upper()
    box_6F2D3.scale_x = 1.0
    box_6F2D3.scale_y = 1.0
    if not True: box_6F2D3.operator_context = "EXEC_DEFAULT"
    box_6F2D3.label(text='Masking', icon_value=0)
    attr_B67DE = '["' + str('Socket_29' + '"]') 
    box_6F2D3.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_B67DE, text='', icon_value=0, emboss=True)
    if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_29'] == 0):
        pass
    else:
        col_A262E = box_6F2D3.column(heading='', align=True)
        col_A262E.alert = False
        col_A262E.enabled = True
        col_A262E.active = True
        col_A262E.use_property_split = False
        col_A262E.use_property_decorate = False
        col_A262E.scale_x = 1.0
        col_A262E.scale_y = 1.0
        col_A262E.alignment = 'Expand'.upper()
        col_A262E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_A262E.label(text='Mask By:', icon_value=0)
        attr_134BB = '["' + str('Socket_25' + '"]') 
        col_A262E.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_134BB, text='', icon_value=0, emboss=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_25'] == 0):
            attr_3706E = '["' + str('Socket_26' + '"]') 
            col_A262E.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_3706E, text='', icon_value=0, emboss=True)
        else:
            col_A262E.prop_search(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], '["Socket_27"]', bpy.data, 'collections', text='', icon='NONE', item_search_property="name")
        if ((bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_29'] == 3) or (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_29'] == 4)):
            attr_558A3 = '["' + str('Socket_28' + '"]') 
            col_A262E.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_558A3, text='Distance Threshold', icon_value=0, emboss=True)
    box_94A5B = box_5C0DE.box()
    box_94A5B.alert = False
    box_94A5B.enabled = True
    box_94A5B.active = True
    box_94A5B.use_property_split = False
    box_94A5B.use_property_decorate = False
    box_94A5B.alignment = 'Expand'.upper()
    box_94A5B.scale_x = 1.0
    box_94A5B.scale_y = 1.0
    if not True: box_94A5B.operator_context = "EXEC_DEFAULT"
    attr_B542F = '["' + str('Socket_3' + '"]') 
    box_94A5B.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_B542F, text='Curve Resolution', icon_value=0, emboss=True, slider=False, toggle=True)
    box_750F0 = box_5C0DE.box()
    box_750F0.alert = False
    box_750F0.enabled = True
    box_750F0.active = True
    box_750F0.use_property_split = False
    box_750F0.use_property_decorate = False
    box_750F0.alignment = 'Expand'.upper()
    box_750F0.scale_x = 1.0
    box_750F0.scale_y = 1.0
    if not True: box_750F0.operator_context = "EXEC_DEFAULT"
    attr_957C6 = '["' + str('Socket_5' + '"]') 
    box_750F0.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_957C6, text='Curve Radius Min', icon_value=0, emboss=True, slider=False, toggle=True)
    attr_EC169 = '["' + str('Socket_6' + '"]') 
    box_750F0.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_EC169, text='Curve Radius Max', icon_value=0, emboss=True, slider=False, toggle=True)
    box_750F0.label(text='Radius - Attribute Influence', icon_value=0)
    attr_F46C2 = '["' + str('Socket_32' + '"]') 
    box_750F0.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_F46C2, text='', icon_value=0, emboss=True, slider=False, toggle=True)
    box_750F0.label(text='Radius Taper', icon_value=0)
    attr_87F4F = '["' + str('Socket_17' + '"]') 
    box_750F0.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_87F4F, text='', icon_value=0, emboss=True, slider=False, toggle=True)
    box_FD97D = box_5C0DE.box()
    box_FD97D.alert = False
    box_FD97D.enabled = True
    box_FD97D.active = True
    box_FD97D.use_property_split = False
    box_FD97D.use_property_decorate = False
    box_FD97D.alignment = 'Expand'.upper()
    box_FD97D.scale_x = 1.0
    box_FD97D.scale_y = 1.0
    if not True: box_FD97D.operator_context = "EXEC_DEFAULT"
    attr_2294A = '["' + str('Socket_12' + '"]') 
    box_FD97D.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_2294A, text='Trim End', icon_value=0, emboss=True, slider=False, toggle=True)
    box_FD97D.label(text='Trim - Attribute Influence', icon_value=0)
    attr_70313 = '["' + str('Socket_37' + '"]') 
    box_FD97D.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_70313, text='', icon_value=0, emboss=True, slider=False, toggle=True)
    if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_15'] == 0):
        col_887B0 = box_5C0DE.column(heading='', align=True)
        col_887B0.alert = False
        col_887B0.enabled = True
        col_887B0.active = True
        col_887B0.use_property_split = False
        col_887B0.use_property_decorate = False
        col_887B0.scale_x = 1.0
        col_887B0.scale_y = 1.0
        col_887B0.alignment = 'Expand'.upper()
        col_887B0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_887B0.separator(factor=1.0)
        box_6F653 = col_887B0.box()
        box_6F653.alert = False
        box_6F653.enabled = True
        box_6F653.active = True
        box_6F653.use_property_split = False
        box_6F653.use_property_decorate = False
        box_6F653.alignment = 'Expand'.upper()
        box_6F653.scale_x = 1.0
        box_6F653.scale_y = 1.0
        if not True: box_6F653.operator_context = "EXEC_DEFAULT"
        box_6F653.label(text='Curve Type', icon_value=0)
        attr_38E26 = '["' + str('Socket_13' + '"]') 
        box_6F653.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_38E26, text='', icon_value=0, emboss=True, slider=False, toggle=True)
        col_887B0.separator(factor=1.0)
        box_47DF7 = col_887B0.box()
        box_47DF7.alert = False
        box_47DF7.enabled = True
        box_47DF7.active = True
        box_47DF7.use_property_split = False
        box_47DF7.use_property_decorate = False
        box_47DF7.alignment = 'Expand'.upper()
        box_47DF7.scale_x = 1.0
        box_47DF7.scale_y = 1.0
        if not True: box_47DF7.operator_context = "EXEC_DEFAULT"
        attr_A6165 = '["' + str('Socket_14' + '"]') 
        box_47DF7.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_A6165, text='Simplify', icon_value=0, emboss=True, slider=False, toggle=True)
        col_887B0.separator(factor=1.0)
        box_358B5 = col_887B0.box()
        box_358B5.alert = False
        box_358B5.enabled = True
        box_358B5.active = True
        box_358B5.use_property_split = False
        box_358B5.use_property_decorate = False
        box_358B5.alignment = 'Expand'.upper()
        box_358B5.scale_x = 1.0
        box_358B5.scale_y = 1.0
        if not True: box_358B5.operator_context = "EXEC_DEFAULT"
        box_358B5.label(text='Fillet Type', icon_value=0)
        attr_9BF33 = '["' + str('Socket_24' + '"]') 
        box_358B5.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_9BF33, text='', icon_value=0, emboss=True, slider=False, toggle=True)
        if (bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN']['Socket_24'] == 1):
            col_FAB4F = box_358B5.column(heading='', align=False)
            col_FAB4F.alert = False
            col_FAB4F.enabled = True
            col_FAB4F.active = True
            col_FAB4F.use_property_split = False
            col_FAB4F.use_property_decorate = False
            col_FAB4F.scale_x = 1.0
            col_FAB4F.scale_y = 1.0
            col_FAB4F.alignment = 'Expand'.upper()
            col_FAB4F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            attr_E1942 = '["' + str('Socket_21' + '"]') 
            col_FAB4F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_E1942, text='Fillet Resolution', icon_value=0, emboss=True, slider=False, toggle=True)
            attr_0E53D = '["' + str('Socket_21' + '"]') 
            col_FAB4F.prop(bpy.context.view_layer.objects.active.modifiers['KIRI_Point_Animate_Wireframe_GN'], attr_0E53D, text='Fillet Radius', icon_value=0, emboss=True, slider=False, toggle=True)
    col_1E0D3.separator(factor=1.0)
    grid_3FCF0 = col_1E0D3.grid_flow(columns=6, row_major=False, even_columns=False, even_rows=False, align=False)
    grid_3FCF0.enabled = bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.enable_wireframe
    grid_3FCF0.active = True
    grid_3FCF0.use_property_split = False
    grid_3FCF0.use_property_decorate = False
    grid_3FCF0.alignment = 'Expand'.upper()
    grid_3FCF0.scale_x = 1.0
    grid_3FCF0.scale_y = 1.0
    if not True: grid_3FCF0.operator_context = "EXEC_DEFAULT"
    box_EBB3C = grid_3FCF0.box()
    box_EBB3C.alert = True
    box_EBB3C.enabled = True
    box_EBB3C.active = True
    box_EBB3C.use_property_split = False
    box_EBB3C.use_property_decorate = False
    box_EBB3C.alignment = 'Expand'.upper()
    box_EBB3C.scale_x = 1.0
    box_EBB3C.scale_y = 2.0
    if not True: box_EBB3C.operator_context = "EXEC_DEFAULT"
    op = box_EBB3C.operator('sna.bake_wireframe_settings_3429e', text='BAKE', icon_value=0, emboss=True, depress=False)
    box_91BCA = grid_3FCF0.box()
    box_91BCA.alert = True
    box_91BCA.enabled = True
    box_91BCA.active = True
    box_91BCA.use_property_split = False
    box_91BCA.use_property_decorate = False
    box_91BCA.alignment = 'Expand'.upper()
    box_91BCA.scale_x = 1.0
    box_91BCA.scale_y = 2.0
    if not True: box_91BCA.operator_context = "EXEC_DEFAULT"
    op = box_91BCA.operator('sna.remove_bake_wireframe_settings_f1797', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'trash.svg')), emboss=True, depress=False)


class SNA_OT_Bake_Wireframe_Settings_3429E(bpy.types.Operator):
    bl_idname = "sna.bake_wireframe_settings_3429e"
    bl_label = "Bake Wireframe Settings"
    bl_description = "Bakes current modifier settings."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_run_bake_node_function_execute_00810('KIRI_Point_Animate_Wireframe_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.wireframe_baked = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Remove_Bake_Wireframe_Settings_F1797(bpy.types.Operator):
    bl_idname = "sna.remove_bake_wireframe_settings_f1797"
    bl_label = "Remove Bake Wireframe Settings"
    bl_description = "Removes baked data."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_remove_bake_node_function_execute_80F90('KIRI_Point_Animate_Wireframe_GN')
        bpy.context.view_layer.objects.active.sna_kiri_pa_object_properties.wireframe_baked = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_GROUP_sna_kiri_pa_scene_property_group(bpy.types.PropertyGroup):
    active_settings: bpy.props.EnumProperty(name='Active_Settings', description='', items=[('Decimate', 'Decimate', '', 0, 0), ('Crop Box', 'Crop Box', '', 0, 1), ('Wind', 'Wind', '', 0, 2), ('Morph', 'Morph', '', 0, 3), ('Noise', 'Noise', '', 0, 4), ('Snap To Shape', 'Snap To Shape', '', 0, 5), ('Wireframe', 'Wireframe', '', 0, 6)])
    show_full_controls: bpy.props.BoolProperty(name='Show_Full_Controls', description='', default=False)


class SNA_GROUP_sna_kiri_pa_object_property_group(bpy.types.PropertyGroup):
    start_frame: bpy.props.IntProperty(name='Start Frame', description='', default=1, subtype='NONE', update=sna_update_start_frame_325FE)
    end_frame: bpy.props.IntProperty(name='End Frame', description='', default=250, subtype='NONE', update=sna_update_end_frame_22369)
    point_scale_min: bpy.props.FloatProperty(name='Point_Scale_Min', description='', default=0.0020000000949949026, subtype='NONE', unit='NONE', min=0.0010000000474974513, max=100.0, step=3, precision=3, update=sna_update_point_scale_min_A5ACF)
    point_scale_max: bpy.props.FloatProperty(name='Point_Scale_Max', description='', default=0.029999999329447746, subtype='NONE', unit='NONE', min=0.0010000000474974513, max=100.0, step=3, precision=3, update=sna_update_point_scale_max_0E8A0)
    scale_random: bpy.props.FloatProperty(name='Scale_Random', description='', default=0.5, subtype='NONE', unit='NONE', min=0.0, max=1.0, step=3, precision=2, update=sna_update_scale_random_5C353)
    point_scale_attribute: bpy.props.EnumProperty(name='Point_Scale_Attribute', description='', items=[('No Attribute Influence', 'No Attribute Influence', '', 0, 0), ('Timeline:1-0', 'Timeline:1-0', '', 0, 1), ('Timeline:0-1', 'Timeline:0-1', '', 0, 2), ('Timeline:20%-80%=1-0', 'Timeline:20%-80%=1-0', '', 0, 3), ('Timeline:20%-80%=0-1', 'Timeline:20%-80%=0-1', '', 0, 4), ('Timeline:0%-50%=1-0', 'Timeline:0%-50%=1-0', '', 0, 5), ('Timeline:0%-50%=0-1', 'Timeline:0%-50%=0-1', '', 0, 6), ('Timeline:1-0-1', 'Timeline:1-0-1', '', 0, 7), ('Timeline:0-1-0', 'Timeline:0-1-0', '', 0, 8), ('Timeline:20%-50%-80%=1-0-1', 'Timeline:20%-50%-80%=1-0-1', '', 0, 9), ('Timeline:20%-50%-80%=0-1-0', 'Timeline:20%-50%-80%=0-1-0', '', 0, 10), ('Isactive (if using Wind)', 'Isactive (if using Wind)', '', 0, 11), ('Age (if using Wind)', 'Age (if using Wind)', '', 0, 12)], update=sna_update_point_scale_attribute_2C65A)
    enable_decimate: bpy.props.BoolProperty(name='Enable_Decimate', description='', default=False, update=sna_update_enable_decimate_897F9)
    enable_crop_box: bpy.props.BoolProperty(name='Enable_Crop_Box', description='', default=False, update=sna_update_enable_crop_box_C5D8F)
    enable_wind: bpy.props.BoolProperty(name='Enable_Wind', description='', default=False, update=sna_update_enable_wind_0B2A0)
    enable_morph: bpy.props.BoolProperty(name='Enable_Morph', description='', default=False, update=sna_update_enable_morph_2583F)
    enable_noise: bpy.props.BoolProperty(name='Enable_Noise', description='', default=False, update=sna_update_enable_noise_19878)
    enable_snap: bpy.props.BoolProperty(name='Enable_Snap', description='', default=False, update=sna_update_enable_snap_141CD)
    enable_wireframe: bpy.props.BoolProperty(name='Enable_Wireframe', description='', default=False, update=sna_update_enable_wireframe_CAA02)
    wind_baked: bpy.props.BoolProperty(name='Wind_Baked', description='', default=False)
    morph_baked: bpy.props.BoolProperty(name='Morph_Baked', description='', default=False)
    noise_baked: bpy.props.BoolProperty(name='Noise_Baked', description='', default=False)
    snap_baked: bpy.props.BoolProperty(name='Snap_Baked', description='', default=False)
    wireframe_baked: bpy.props.BoolProperty(name='Wireframe_Baked', description='', default=False)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_GROUP_sna_kiri_pa_scene_property_group)
    bpy.utils.register_class(SNA_GROUP_sna_kiri_pa_object_property_group)
    bpy.types.Scene.sna_kiri_pa_scene_properties = bpy.props.PointerProperty(name='KIRI_PA_Scene_Properties', description='', type=SNA_GROUP_sna_kiri_pa_scene_property_group)
    bpy.types.Object.sna_kiri_pa_object_properties = bpy.props.PointerProperty(name='KIRI_PA_Object_Properties', description='', type=SNA_GROUP_sna_kiri_pa_object_property_group)
    bpy.utils.register_class(SNA_OT_Add_Point_Edit_Modifiers_Aafc2)
    bpy.utils.register_class(SNA_OT_Append_Wire_Sphere_F21B7)
    bpy.utils.register_class(SNA_OT_Append_Wire_Cube_D69Fb)
    bpy.utils.register_class(SNA_OT_Append_Wind_Controller_14Ef6)
    bpy.utils.register_class(SNA_OT_Refresh_Changes_Ce548)
    bpy.utils.register_class(SNA_OT_Dgs_Render_Launch_Kiri_Site_84772)
    bpy.utils.register_class(SNA_OT_Pa_Launch_Superhive_Store_0Bcb5)
    bpy.utils.register_class(SNA_OT_Pa_Launch_Kiri_Blender_Addons_Page_9427F)
    bpy.utils.register_class(SNA_OT_Pa_Open_Documentation_3B870)
    bpy.utils.register_class(SNA_OT_Pa_Open_Tutorial_Video_D0Cd5)
    bpy.utils.register_class(SNA_PT_POINT_ANIMATE_BY_KIRI_ENGINE_B94F8)
    bpy.utils.register_class(SNA_OT_Setup_Quick_Dissolve_94289)
    bpy.utils.register_class(SNA_OT_Setup_Quick_Morph_Dc267)
    bpy.utils.register_class(SNA_OT_Setup_Quick_Magic_Ce2Cf)
    bpy.utils.register_class(SNA_OT_Setup_Quick_Tech_Af450)
    bpy.utils.register_class(SNA_OT_Bake_Morph_Settings_29B13)
    bpy.utils.register_class(SNA_OT_Remove_Bake_Morph_Settings_Fdef2)
    bpy.utils.register_class(SNA_OT_Bake_Noise_Settings_354Ca)
    bpy.utils.register_class(SNA_OT_Remove_Bake_Noise_Settings_714B1)
    bpy.utils.register_class(SNA_OT_Bake_Snap_Settings_9226D)
    bpy.utils.register_class(SNA_OT_Remove_Bake_Snap_Settings_A2139)
    bpy.utils.register_class(SNA_OT_Bake_Wind_Settings_8567D)
    bpy.utils.register_class(SNA_OT_Remove_Bake_Wind_Settings_3C21D)
    bpy.utils.register_class(SNA_OT_Bake_Wireframe_Settings_3429E)
    bpy.utils.register_class(SNA_OT_Remove_Bake_Wireframe_Settings_F1797)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Object.sna_kiri_pa_object_properties
    del bpy.types.Scene.sna_kiri_pa_scene_properties
    bpy.utils.unregister_class(SNA_GROUP_sna_kiri_pa_object_property_group)
    bpy.utils.unregister_class(SNA_GROUP_sna_kiri_pa_scene_property_group)
    bpy.utils.unregister_class(SNA_OT_Add_Point_Edit_Modifiers_Aafc2)
    bpy.utils.unregister_class(SNA_OT_Append_Wire_Sphere_F21B7)
    bpy.utils.unregister_class(SNA_OT_Append_Wire_Cube_D69Fb)
    bpy.utils.unregister_class(SNA_OT_Append_Wind_Controller_14Ef6)
    bpy.utils.unregister_class(SNA_OT_Refresh_Changes_Ce548)
    bpy.utils.unregister_class(SNA_OT_Dgs_Render_Launch_Kiri_Site_84772)
    bpy.utils.unregister_class(SNA_OT_Pa_Launch_Superhive_Store_0Bcb5)
    bpy.utils.unregister_class(SNA_OT_Pa_Launch_Kiri_Blender_Addons_Page_9427F)
    bpy.utils.unregister_class(SNA_OT_Pa_Open_Documentation_3B870)
    bpy.utils.unregister_class(SNA_OT_Pa_Open_Tutorial_Video_D0Cd5)
    bpy.utils.unregister_class(SNA_PT_POINT_ANIMATE_BY_KIRI_ENGINE_B94F8)
    bpy.utils.unregister_class(SNA_OT_Setup_Quick_Dissolve_94289)
    bpy.utils.unregister_class(SNA_OT_Setup_Quick_Morph_Dc267)
    bpy.utils.unregister_class(SNA_OT_Setup_Quick_Magic_Ce2Cf)
    bpy.utils.unregister_class(SNA_OT_Setup_Quick_Tech_Af450)
    bpy.utils.unregister_class(SNA_OT_Bake_Morph_Settings_29B13)
    bpy.utils.unregister_class(SNA_OT_Remove_Bake_Morph_Settings_Fdef2)
    bpy.utils.unregister_class(SNA_OT_Bake_Noise_Settings_354Ca)
    bpy.utils.unregister_class(SNA_OT_Remove_Bake_Noise_Settings_714B1)
    bpy.utils.unregister_class(SNA_OT_Bake_Snap_Settings_9226D)
    bpy.utils.unregister_class(SNA_OT_Remove_Bake_Snap_Settings_A2139)
    bpy.utils.unregister_class(SNA_OT_Bake_Wind_Settings_8567D)
    bpy.utils.unregister_class(SNA_OT_Remove_Bake_Wind_Settings_3C21D)
    bpy.utils.unregister_class(SNA_OT_Bake_Wireframe_Settings_3429E)
    bpy.utils.unregister_class(SNA_OT_Remove_Bake_Wireframe_Settings_F1797)
