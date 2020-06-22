# Generate the points on the density function.

from scipy.stats import norm
import numpy as np

n = 100
scale_x = 3
scale_z = 12

x = np.linspace(-9, 9, n)
z = scale_z * norm.pdf(x / scale_x)

import bpy

mesh        = bpy.data.meshes.new("newmesh")
object      = bpy.data.objects.new(mesh.name, mesh)
collection  = bpy.data.collections.get("Collection")
collection.objects.link(object)
bpy.context.view_layer.objects.active = object

vertices_all = list(zip(x, [0] * n, z))
edges_all = list(zip(range(0, n - 1), range(1, n)))
faces_all = []

mesh.from_pydata(vertices_all, edges_all, faces_all)
