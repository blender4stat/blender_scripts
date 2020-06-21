# Generate random vertices along direction.

import numpy as np
import statistics

rseed = 8594375
xmin  = -10
xmax  =  10
n     =  20
ymin  =   0
ymax  =  10

np.random.seed(rseed)
xmean = statistics.mean([xmin, xmax])
xmidrange = (xmax - xmin)/2
ydelta = (ymax - ymin)/n

xall = []
for i in range(0, n):
    xall.append(round(np.random.normal(xmean, xmidrange/3.5), 0))
    
yall = []
for i in range(0, n):
    yall.append(i * ydelta)

import bpy

mesh        = bpy.data.meshes.new("newmesh")
object      = bpy.data.objects.new(mesh.name, mesh)
collection  = bpy.data.collections.get("Collection")
collection.objects.link(object)
bpy.context.view_layer.objects.active = object

vertices_all = list(zip(xall, yall, [0] * n))
edges_all = []
faces_all = []

mesh.from_pydata(vertices_all, edges_all, faces_all)
