def add_children(name = "children", subdivisions = 2, diameter = .25):
    "Add vertice instancing with an icosphere child"

    import bpy
    import bmesh

    obj_p = bpy.context.active_object

    mesh = bpy.data.meshes.new(name)
    children = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(children)
    bpy.context.view_layer.objects.active = children

    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions = subdivisions, diameter = diameter)
    bm.to_mesh(mesh)
    bm.free()

    obj_p.select_set(True)
    children.select_set(True)
    bpy.context.view_layer.objects.active = obj_p

    bpy.ops.object.parent_set()

    obj_p.instance_type = "VERTS"
    obj_p.show_instancer_for_render = False
    obj_p.show_instancer_for_viewport = False
