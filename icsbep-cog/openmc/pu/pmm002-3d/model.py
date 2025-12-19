"""
TEX Experiment tex3di
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_element("P", 1.514340e+01)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("P", 7.900000e+00)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("P", 7.820000e+00)

# Si
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("P", 2.700000e+00)

# H
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("P", 9.640000e-01)
mat5.add_nuclide("H1", 1.437054e-01)
mat5.add_s_alpha_beta("c_H_in_CH2")

# Si
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("P", 2.700000e+00)

# Si
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("P", 2.700000e+00)

mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("P", 2.700000e+00)

# Si
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("P", 2.700000e+00)

# H
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("P", 9.610000e-01)
mat10.add_nuclide("H1", 1.437054e-01)
mat10.add_s_alpha_beta("c_H_in_CH2")

# H
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_element("P", 9.720000e-01)
mat11.add_nuclide("H1", 1.437054e-01)
mat11.add_s_alpha_beta("c_H_in_CH2")

# H
mat12 = openmc.Material(material_id=12)
mat12.set_density("sum")
mat12.add_element("P", 9.620000e-01)
mat12.add_nuclide("H1", 1.437054e-01)
mat12.add_s_alpha_beta("c_H_in_CH2")

# H
mat13 = openmc.Material(material_id=13)
mat13.set_density("sum")
mat13.add_element("P", 9.710000e-01)
mat13.add_nuclide("H1", 1.437054e-01)
mat13.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11, mat12, mat13])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.model.RectangularParallelepiped(-15.327376, 15.327376, -15.327376, 15.327376, -0.13608050000000002, 0.1614805)
surf2 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -0.14878049999999998, 0.1616455)
surf3 = openmc.model.RectangularParallelepiped(-15.327376, 15.327376, -15.327376, 15.327376, 0.1614805, 0.16164550000000003)
surf4 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, -0.1767205, -0.14878049999999998)
surf5 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -0.34073749999999997, -0.1767205)
surf6 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 0.22974260000000002, 0.5428646)
surf7 = openmc.model.RectangularParallelepiped(-24.445976, 24.445976, -24.445976, 24.445976, 4.57965462, 4.8953766199999995)
surf8 = openmc.model.RectangularParallelepiped(-57.15, 57.15, -57.15, 57.15, 2.03965462, 4.5796546199999995)
surf9 = openmc.model.RectangularParallelepiped(-24.13, 24.13, -24.13, 24.13, 2.03965462, 4.5796546199999995)
surf10 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 9.820146182, 10.133268182)
surf11 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -2.722843, -0.3407374999999999)
surf12 = openmc.model.RectangularParallelepiped(-27.94, 27.94, -27.94, 27.94, -2.7228429999999997, -2.087843)
surf13 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -2.7228429999999997, -2.087843)
surf14 = openmc.model.RectangularParallelepiped(-27.939999999999998, -22.86, -27.94, -17.145, -2.7228429999999997, -2.087843)
surf15 = openmc.model.RectangularParallelepiped(-27.939999999999998, -22.86, 17.145, 27.94, -2.7228429999999997, -2.087843)
surf16 = openmc.model.RectangularParallelepiped(-22.86, -15.875, 22.86, 27.939999999999998, -2.7228429999999997, -2.087843)
surf17 = openmc.model.RectangularParallelepiped(-30.48, 30.48, -30.48, 30.48, -3.9928429999999997, -2.722843)
surf18 = openmc.model.RectangularParallelepiped(-30.48, -25.400000000000002, -33.02, 33.02, -5.580343, -3.6753430000000002)
surf19 = openmc.model.RectangularParallelepiped(25.400000000000002, 30.48, -33.02, 33.02, -5.580343, -3.6753430000000002)
surf20 = openmc.model.RectangularParallelepiped(-39.37, 39.37, -39.37, 39.37, -9.390343, -5.580343)
surf41 = openmc.model.RectangularParallelepiped(-15.327376, 15.327376, -15.327376, 15.327376, -0.14878049999999998, -0.1360805)
surf50 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 10.13326818, 12.51537318)
surf51 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 11.4032725, 13.7853775)
surf60 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 4.8953766, 5.2084985999999995)
surf61 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 1.113344424, 1.426466424)
surf62 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 1.996946248, 2.310068248)
surf63 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 6.544906097999999, 7.483312098)
surf64 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 8.035683396, 8.974089396)
surf80 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, -0.3407375, 0.1616455)
surf81 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 0.54286432, 1.04524732)
surf82 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 1.42646615, 1.92884915)
surf83 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 2.31006797, 2.81245097)
surf84 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 3.1936698, 3.6960528)
surf85 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 4.07727162, 4.57965462)
surf86 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 5.20849832, 5.71088132)
surf87 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 6.02929325, 6.53167625)
surf88 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 6.85008817, 7.35247117)
surf89 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 7.6708831, 8.1732661)
surf93 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 2.880548072, 3.1936700719999997)
surf94 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 3.764149896, 4.077271896)
surf99 = openmc.model.RectangularParallelepiped(-95.0, 95.0, -95.0, 95.0, -10.0, 30.0, boundary_type="vacuum")
surf101 = openmc.XPlane(surface_id=101, x0=-2.23901)
surf102 = openmc.XPlane(surface_id=102, x0=2.23901)
surf103 = openmc.YPlane(surface_id=103, y0=-3.78466)
surf104 = openmc.YPlane(surface_id=104, y0=3.639757)
surf105 = openmc.ZPlane(surface_id=105, z0=-0.10668)
surf106 = openmc.ZPlane(surface_id=106, z0=0.10668)
surf107 = openmc.XPlane(surface_id=107, x0=-2.159635)
surf108 = openmc.XPlane(surface_id=108, x0=-1.60401)
surf109 = openmc.XPlane(surface_id=109, x0=1.60401)
surf110 = openmc.XPlane(surface_id=110, x0=2.159635)
surf111 = openmc.YPlane(surface_id=111, y0=-3.7052885)
surf112 = openmc.YPlane(surface_id=112, y0=-3.1496635)
surf113 = openmc.YPlane(surface_id=113, y0=3.0047565)
surf114 = openmc.YPlane(surface_id=114, y0=3.5603815)
surf115 = openmc.ZPlane(surface_id=115, z0=-0.027305)
surf116 = openmc.ZPlane(surface_id=116, z0=0.027305)
surf117 = openmc.ZCylinder(surface_id=117, x0=-1.60401, y0=3.0047565, r=0.555625)
surf118 = openmc.ZCylinder(surface_id=118, x0=-1.60401, y0=3.0047565, r=0.635)
surf119 = openmc.ZCylinder(surface_id=119, x0=1.60401, y0=3.0047565, r=0.555625)
surf120 = openmc.ZCylinder(surface_id=120, x0=1.60401, y0=3.0047565, r=0.635)
surf121 = openmc.ZCylinder(surface_id=121, x0=-1.60401, y0=-3.1496635, r=0.555625)
surf122 = openmc.ZCylinder(surface_id=122, x0=-1.60401, y0=-3.1496635, r=0.635)
surf123 = openmc.ZCylinder(surface_id=123, x0=1.60401, y0=-3.14966355, r=0.555625)
surf124 = openmc.ZCylinder(surface_id=124, x0=1.60401, y0=-3.14966355, r=0.635)
surf125 = openmc.YCylinder(surface_id=125, x0=-2.159635, y0=-0.0724535, r=0.079375)
surf126 = openmc.YCylinder(surface_id=126, x0=-2.159635, y0=-0.0724535, r=0.079375)
surf127 = openmc.YCylinder(surface_id=127, x0=2.159635, y0=-0.0724535, r=0.079375)
surf128 = openmc.YCylinder(surface_id=128, x0=2.159635, y0=-0.0724535, r=0.079375)
surf129 = openmc.ZCylinder(surface_id=129, x0=0.0, y0=3.5603815, r=0.079375)
surf130 = openmc.ZCylinder(surface_id=130, x0=0.0, y0=3.5603815, r=0.079375)
surf131 = openmc.ZCylinder(surface_id=131, x0=0.0, y0=-3.7052885, r=0.079375)
surf132 = openmc.ZCylinder(surface_id=132, x0=0.0, y0=-3.7052885, r=0.079375)
# surf133: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '-1.60401', '3.0047565', '-0.027305']
# surf134: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '-1.60401', '3.0047565', '0.027305']
# surf135: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '1.60401', '3.0047565', '-0.027305']
# surf136: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '1.60401', '3.0047565', '0.027305']
# surf137: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '-1.60401', '-3.0047565', '-0.027305']
# surf138: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '-1.60401', '-3.0047565', '-0.027305']
# surf139: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '1.60401', '-3.0047565', '-0.027305']
# surf140: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '1.60401', '-3.0047565', '0.027305']
surf161 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 5.716171527, 6.029293527)
surf162 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 6.536966454, 6.850088454)
surf163 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 7.357761381, 7.670883381)
surf164 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 8.178556308, 8.491678308)
surf165 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 8.999351235, 9.312473235)
surf180 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 8.49167803, 8.994061030000001)
surf181 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 9.312472960000001, 9.81485596)
surf201 = openmc.XPlane(surface_id=201, x0=-2.530729)
surf202 = openmc.XPlane(surface_id=202, x0=-2.287083795)
surf203 = openmc.XPlane(surface_id=203, x0=2.287083795)
surf204 = openmc.XPlane(surface_id=204, x0=2.530729)
surf205 = openmc.YPlane(surface_id=205, y0=-3.8128575)
surf206 = openmc.YPlane(surface_id=206, y0=-3.7846635)
surf209 = openmc.YPlane(surface_id=209, y0=3.7846635)
surf210 = openmc.YPlane(surface_id=210, y0=3.8128575)
surf211 = openmc.ZPlane(surface_id=211, z0=-0.1487805)
surf212 = openmc.ZPlane(surface_id=212, z0=-0.1205865)
surf215 = openmc.ZPlane(surface_id=215, z0=0.1205865)
surf216 = openmc.ZPlane(surface_id=216, z0=0.1487805)
surf300 = openmc.model.RectangularParallelepiped(-17.71682, 12.67318, -19.0645, 11.4387, -0.1487805, 0.1487805)
surf301 = openmc.model.RectangularParallelepiped(-0.142992, 4.918445999999999, 0.07594600000000007, 7.701661, -0.13608050000000002, 0.1614805)
surf302 = openmc.model.RectangularParallelepiped(-5.20443, -0.142992, 0.07594600000000007, 7.701661, -0.13608050000000002, 0.1614805)
surf303 = openmc.model.RectangularParallelepiped(-10.265868, -5.20443, 0.07594600000000007, 7.701661, -0.13608050000000002, 0.1614805)
surf304 = openmc.model.RectangularParallelepiped(-15.327306, -10.265868000000001, 0.07594600000000007, 7.701661, -0.13608050000000002, 0.1614805)
surf305 = openmc.model.RectangularParallelepiped(4.918445999999999, 9.979884, 0.07594600000000007, 7.701661, -0.13608050000000002, 0.1614805)
surf306 = openmc.model.RectangularParallelepiped(9.979884, 15.041322, 0.07594600000000007, 7.701661, -0.13608050000000002, 0.1614805)
surf307 = openmc.model.RectangularParallelepiped(-0.142992, 4.918445999999999, 7.701661, 15.327376, -0.13608050000000002, 0.1614805)
surf308 = openmc.model.RectangularParallelepiped(-5.20443, -0.142992, 7.701661, 15.327376, -0.13608050000000002, 0.1614805)
surf309 = openmc.model.RectangularParallelepiped(-10.265868, -5.20443, 7.701661, 15.327376, -0.13608050000000002, 0.1614805)
surf310 = openmc.model.RectangularParallelepiped(-15.327306, -10.265868000000001, 7.701661, 15.327376, -0.13608050000000002, 0.1614805)
surf311 = openmc.model.RectangularParallelepiped(4.918445999999999, 9.979884, 7.701661, 15.327376, -0.13608050000000002, 0.1614805)
surf312 = openmc.model.RectangularParallelepiped(9.979884, 15.041322, 7.701661, 15.327376, -0.13608050000000002, 0.1614805)
surf313 = openmc.model.RectangularParallelepiped(-0.142992, 4.918445999999999, -7.5497689999999995, 0.07594599999999962, -0.13608050000000002, 0.1614805)
surf314 = openmc.model.RectangularParallelepiped(-5.20443, -0.142992, -7.5497689999999995, 0.07594599999999962, -0.13608050000000002, 0.1614805)
surf315 = openmc.model.RectangularParallelepiped(-10.265868, -5.20443, -7.5497689999999995, 0.07594599999999962, -0.13608050000000002, 0.1614805)
surf316 = openmc.model.RectangularParallelepiped(-15.327306, -10.265868000000001, -7.5497689999999995, 0.07594599999999962, -0.13608050000000002, 0.1614805)
surf317 = openmc.model.RectangularParallelepiped(4.918445999999999, 9.979884, -7.5497689999999995, 0.07594599999999962, -0.13608050000000002, 0.1614805)
surf318 = openmc.model.RectangularParallelepiped(9.979884, 15.041322, -7.5497689999999995, 0.07594599999999962, -0.13608050000000002, 0.1614805)
surf319 = openmc.model.RectangularParallelepiped(-0.142992, 4.918445999999999, -15.175483999999999, -7.5497689999999995, -0.13608050000000002, 0.1614805)
surf320 = openmc.model.RectangularParallelepiped(-5.20443, -0.142992, -15.175483999999999, -7.5497689999999995, -0.13608050000000002, 0.1614805)
surf321 = openmc.model.RectangularParallelepiped(-10.265868, -5.20443, -15.175483999999999, -7.5497689999999995, -0.13608050000000002, 0.1614805)
surf322 = openmc.model.RectangularParallelepiped(-15.327306, -10.265868000000001, -15.175483999999999, -7.5497689999999995, -0.13608050000000002, 0.1614805)
surf323 = openmc.model.RectangularParallelepiped(4.918445999999999, 9.979884, -15.175483999999999, -7.5497689999999995, -0.13608050000000002, 0.1614805)
surf324 = openmc.model.RectangularParallelepiped(9.979884, 15.041322, -15.175483999999999, -7.5497689999999995, -0.13608050000000002, 0.1614805)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

universe1 = openmc.Universe(universe_id=1, cells=[])

universe2 = openmc.Universe(universe_id=2, cells=[])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell()
u4_cell0.region = +surf1 & -surf3
u4_cell1 = openmc.Cell(fill=mat5)
u4_cell1.region = +surf1 & +surf3 & +surf41 & -surf2
u4_cell2 = openmc.Cell(fill=mat6)
u4_cell2.region = -surf41
u4_cell3 = openmc.Cell(fill=mat4)
u4_cell3.region = -surf4
u4_cell4 = openmc.Cell(fill=mat10)
u4_cell4.region = -surf5
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

u5_cell0 = openmc.Cell(fill=mat9)
u5_cell0.region = +surf201 & -surf204 & +surf205 & -surf210 & +surf211 & -surf216
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0])

u6_cell0 = openmc.Cell()
u6_cell0.region = +surf1 & -surf3
u6_cell1 = openmc.Cell(fill=mat5)
u6_cell1.region = +surf1 & +surf3 & +surf41 & -surf2
u6_cell2 = openmc.Cell(fill=mat6)
u6_cell2.region = -surf41
u6_cell3 = openmc.Cell(fill=mat4)
u6_cell3.region = -surf4
u6_cell4 = openmc.Cell(fill=mat10)
u6_cell4.region = -surf5
universe6 = openmc.Universe(universe_id=6, cells=[u6_cell0, u6_cell1, u6_cell2, u6_cell3, u6_cell4])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# poly2
cell1 = openmc.Cell(cell_id=1, fill=mat12)
cell1.region = -surf6

# plat
cell2 = openmc.Cell(cell_id=2, fill=mat9)
cell2.region = -surf12 & +surf13 & +surf14 & +surf15 & +surf16

# plat2
cell3 = openmc.Cell(cell_id=3, fill=mat9)
cell3.region = -surf17

# plat
cell4 = openmc.Cell(cell_id=4, fill=mat9)
cell4.region = -surf20

# plat5
cell5 = openmc.Cell(cell_id=5, fill=mat9)
cell5.region = -surf18 & +surf17

# plat6
cell6 = openmc.Cell(cell_id=6, fill=mat9)
cell6.region = -surf19 & +surf17

# bott
cell7 = openmc.Cell(cell_id=7, fill=mat11)
cell7.region = -surf11

# layer1
cell8 = openmc.Cell(cell_id=8, fill=universe4)
cell8.translation = (0.0, 0.0, 0.0)
cell8.region = -surf80

# layer2
cell9 = openmc.Cell(cell_id=9, fill=universe4)
cell9.translation = (0.0, 0.0, 0.883610824)
cell9.region = -surf81

# layer3
cell10 = openmc.Cell(cell_id=10, fill=universe4)
cell10.translation = (0.0, 0.0, 1.767203648)
cell10.region = -surf82

# layer4
cell11 = openmc.Cell(cell_id=11, fill=universe4)
cell11.translation = (0.0, 0.0, 2.650805472)
cell11.region = -surf83

# layer5
cell12 = openmc.Cell(cell_id=12, fill=universe4)
cell12.translation = (0.0, 0.0, 3.534407296)
cell12.region = -surf84

# layer6
cell13 = openmc.Cell(cell_id=13, fill=universe4)
cell13.translation = (0.0, 0.0, 4.41800912)
cell13.region = -surf85

# imlayer2
cell14 = openmc.Cell(cell_id=14, fill=mat12)
cell14.region = -surf61

# imlayer3
cell15 = openmc.Cell(cell_id=15, fill=mat12)
cell15.region = -surf62

# imlayer4
cell16 = openmc.Cell(cell_id=16, fill=mat12)
cell16.region = -surf93

# imlayer5
cell17 = openmc.Cell(cell_id=17, fill=mat12)
cell17.region = -surf94

# dia
cell18 = openmc.Cell(cell_id=18, fill=mat8)
cell18.region = -surf7

# pla4
cell19 = openmc.Cell(cell_id=19, fill=mat7)
cell19.region = -surf8 & +surf9

# layer7
cell20 = openmc.Cell(cell_id=20, fill=universe4)
cell20.translation = (0.0, 0.0, 5.54923582)
cell20.region = -surf86

# layer8
cell21 = openmc.Cell(cell_id=21, fill=universe4)
cell21.translation = (0.0, 0.0, 6.370030747)
cell21.region = -surf87

# layer9
cell22 = openmc.Cell(cell_id=22, fill=universe4)
cell22.translation = (0.0, 0.0, 7.190825674)
cell22.region = -surf88

# layer10
cell23 = openmc.Cell(cell_id=23, fill=universe4)
cell23.translation = (0.0, 0.0, 8.011620601)
cell23.region = -surf89

# layer11
cell24 = openmc.Cell(cell_id=24, fill=universe4)
cell24.translation = (0.0, 0.0, 8.832415528)
cell24.region = -surf180

# layer12
cell25 = openmc.Cell(cell_id=25, fill=universe6)
cell25.translation = (0.0, 0.0, 9.653210455)
cell25.region = -surf181

# mod
cell26 = openmc.Cell(cell_id=26, fill=mat12)
cell26.region = -surf60

# mod
cell27 = openmc.Cell(cell_id=27, fill=mat12)
cell27.region = -surf161

# mod
cell28 = openmc.Cell(cell_id=28, fill=mat12)
cell28.region = -surf162

# mod
cell29 = openmc.Cell(cell_id=29, fill=mat12)
cell29.region = -surf163

# mod
cell30 = openmc.Cell(cell_id=30, fill=mat12)
cell30.region = -surf164

# mod
cell31 = openmc.Cell(cell_id=31, fill=mat12)
cell31.region = -surf165

# poly1
cell32 = openmc.Cell(cell_id=32, fill=mat12)
cell32.region = -surf10

# poly2
cell33 = openmc.Cell(cell_id=33, fill=mat11)
cell33.region = -surf50

# assby
cell39 = openmc.Cell(cell_id=39, fill=universe3)
cell39.region = -surf1

# assby
cell45 = openmc.Cell(cell_id=45, fill=universe2)
cell45.region = -surf1

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell39, cell45])
geometry = openmc.Geometry(root_universe)

# ==============================================================================
# Settings
# ==============================================================================

settings = openmc.Settings()
settings.particles = 10000
settings.batches = 150
settings.inactive = 10
settings.run_mode = "eigenvalue"

source = openmc.IndependentSource()
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
