# Generate random vertices along direction.

import numpy as np

n   = 500
x1  = np.random.uniform(-1.5, 1.5, n)
y00 = np.maximum(np.absolute(x1/10), .075)
y01 = np.random.normal(np.full(n, 0), y00)
y1  = 1.5 + (x1 + y01)**4
y2  = np.random.uniform(0, 3, n)
x2  = np.random.normal(
        np.full(n, 0), 
        np.maximum(
            (np.absolute(y2 - 3/2)**4)/20, .025))
xall = np.concatenate((x1, x2))
yall = np.concatenate((y1, y2))
selected = yall < 3
x = xall[selected]
y = yall[selected]
n_final = x.size  
z = np.random.uniform(-0.1, 0.1, n_final)

import bpy

mesh        = bpy.data.meshes.new("sample_points")
object      = bpy.data.objects.new(mesh.name, mesh)
collection  = bpy.data.collections.get("Collection")
collection.objects.link(object)
bpy.context.view_layer.objects.active = object

vertices_all = list(zip(x, z, y))
edges_all = []
faces_all = []

mesh.from_pydata(vertices_all, edges_all, faces_all)

