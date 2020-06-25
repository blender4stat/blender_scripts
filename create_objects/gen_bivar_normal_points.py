# Generate the points on the density function.

from scipy.stats import multivariate_normal
import numpy as np

x, y = np.mgrid[-3:3.25:.25, -3:3.25:.25]
side_size = x.shape[0]
coord = np.empty(x.shape + (2, ))
coord[:, :, 0] = x
coord[:, :, 1] = y
cov_xy = .8
var = multivariate_normal([0.0, 0.0], [[1.0, cov_xy], [cov_xy, 1.0]])
z = var.pdf(coord)

z_scale = 10

import bpy

mesh        = bpy.data.meshes.new("bivar_normal_curve")
object      = bpy.data.objects.new(mesh.name, mesh)
collection  = bpy.data.collections.get("Collection")
collection.objects.link(object)
bpy.context.view_layer.objects.active = object

vertices_all = list(zip(x.flatten(), y.flatten(), z_scale*z.flatten()))
edges_all = []

face_index = np.array(range(0, (side_size * side_size)))
face_index = face_index.reshape((side_size, side_size))
face_index = face_index[0:(side_size - 1),0:(side_size - 1)].flatten()
face_vertices = list()
for i in face_index:
    face_vertices.append((i, i + 1, i + side_size + 1, i + side_size))
faces_all = face_vertices

mesh.from_pydata(vertices_all, edges_all, faces_all)
