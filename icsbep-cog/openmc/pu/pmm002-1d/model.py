"""
TEX Experiment tex1di
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_element("P", 1.514350e+01)

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

surf1 = openmc.model.RectangularParallelepiped(-15.327376, 15.327376, -15.327376, 15.327376, -0.13608050000000002, 0.1614805)
surf2 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -0.14878049999999998, 0.1616455)
surf3 = openmc.model.RectangularParallelepiped(-15.327376, 15.327376, -15.327376, 15.327376, 0.1614805, 0.16164550000000003)
surf4 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, -0.1767205, -0.14878049999999998)
surf5 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -0.34073749999999997, -0.1767205)
surf7 = openmc.model.RectangularParallelepiped(-24.445976, 24.445976, -24.445976, 24.445976, 3.1509095, 3.4666315)
surf8 = openmc.model.RectangularParallelepiped(-57.15, 57.15, -57.15, 57.15, 0.6109095, 3.1509095)
surf9 = openmc.model.RectangularParallelepiped(-24.13, 24.13, -24.13, 24.13, 0.6109095, 3.1509095)
surf10 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 7.2705085, 7.4345254999999995)
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
surf40 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, -0.3407375, 0.1616455)
surf41 = openmc.model.RectangularParallelepiped(-15.327376, 15.327376, -15.327376, 15.327376, -0.14878049999999998, -0.1360805)
surf42 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, -0.1767205, 0.1616455)
surf50 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 7.434525500000001, 9.8166305)
surf51 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 11.4032725, 13.7853775)
surf61 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 1.113344424, 1.426466424)
surf62 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 1.996946248, 2.310068248)
surf63 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 6.544906097999999, 7.483312098)
surf64 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 8.035683396, 8.974089396)
surf81 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 0.19693750000000002, 0.5353035)
surf82 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 0.5705955, 0.9089615)
surf83 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 0.9442535, 1.2826195)
surf84 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 1.3179115, 1.6562775)
surf85 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 1.6915695, 2.0299355)
surf86 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 2.0652275, 2.4035935)
surf87 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 2.4388855, 2.7772514999999998)
surf88 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 2.8125435000000003, 3.1509095)
surf89 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 3.4666315, 3.8049975)
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
surf180 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 3.8124385000000003, 4.1508045000000005)
surf181 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 4.1582455, 4.4966115)
surf182 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 4.504052499999999, 4.8424185)
surf183 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 4.8498595, 5.188225500000001)
surf184 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 5.1956665, 5.5340325)
surf185 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 5.5414734999999995, 5.8798395)
surf186 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 5.8872805, 6.225646500000001)
surf187 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 6.2330875, 6.5714535000000005)
surf188 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 6.5788945, 6.9172605)
surf189 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 6.924701499999999, 7.2630675)
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
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf4
u4_cell3 = openmc.Cell(fill=mat6)
u4_cell3.region = -surf41
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3])

u5_cell0 = openmc.Cell(fill=mat9)
u5_cell0.region = +surf201 & -surf204 & +surf205 & -surf210 & +surf211 & -surf216
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0])

u6_cell0 = openmc.Cell()
u6_cell0.region = +surf1 & -surf3
u6_cell1 = openmc.Cell(fill=mat5)
u6_cell1.region = +surf1 & +surf3 & +surf41 & -surf2
u6_cell2 = openmc.Cell(fill=mat4)
u6_cell2.region = -surf4
u6_cell3 = openmc.Cell(fill=mat5)
u6_cell3.region = -surf5
u6_cell4 = openmc.Cell(fill=mat6)
u6_cell4.region = -surf41
universe6 = openmc.Universe(universe_id=6, cells=[u6_cell0, u6_cell1, u6_cell2, u6_cell3, u6_cell4])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# plat
cell1 = openmc.Cell(cell_id=1, fill=mat9)
cell1.region = -surf12 & +surf13 & +surf14 & +surf15 & +surf16

# plat2
cell2 = openmc.Cell(cell_id=2, fill=mat9)
cell2.region = -surf17

# plat5
cell3 = openmc.Cell(cell_id=3, fill=mat9)
cell3.region = -surf18 & +surf17

# plat6
cell4 = openmc.Cell(cell_id=4, fill=mat9)
cell4.region = -surf19 & +surf17

# plat
cell5 = openmc.Cell(cell_id=5, fill=mat9)
cell5.region = -surf20

# bott
cell6 = openmc.Cell(cell_id=6, fill=mat11)
cell6.region = -surf11

# layer1
cell7 = openmc.Cell(cell_id=7, fill=universe6)
cell7.translation = (0.0, 0.0, 0.0)
cell7.region = -surf40

# layer2
cell8 = openmc.Cell(cell_id=8, fill=universe4)
cell8.translation = (0.0, 0.0, 0.373658)
cell8.region = -surf81

# layer3
cell9 = openmc.Cell(cell_id=9, fill=universe4)
cell9.translation = (0.0, 0.0, 0.747316)
cell9.region = -surf82

# layer4
cell10 = openmc.Cell(cell_id=10, fill=universe4)
cell10.translation = (0.0, 0.0, 1.120974)
cell10.region = -surf83

# layer5
cell11 = openmc.Cell(cell_id=11, fill=universe4)
cell11.translation = (0.0, 0.0, 1.494632)
cell11.region = -surf84

# layer6
cell12 = openmc.Cell(cell_id=12, fill=universe4)
cell12.translation = (0.0, 0.0, 1.86829)
cell12.region = -surf85

# layer7
cell13 = openmc.Cell(cell_id=13, fill=universe4)
cell13.translation = (0.0, 0.0, 2.241948)
cell13.region = -surf86

# layer8
cell14 = openmc.Cell(cell_id=14, fill=universe4)
cell14.translation = (0.0, 0.0, 2.615606)
cell14.region = -surf87

# layer9
cell15 = openmc.Cell(cell_id=15, fill=universe4)
cell15.translation = (0.0, 0.0, 2.989264)
cell15.region = -surf88

# dia
cell16 = openmc.Cell(cell_id=16, fill=mat8)
cell16.region = -surf7

# pla4
cell17 = openmc.Cell(cell_id=17, fill=mat7)
cell17.region = -surf8 & +surf9

# layer10
cell18 = openmc.Cell(cell_id=18, fill=universe4)
cell18.translation = (0.0, 0.0, 3.643352)
cell18.region = -surf89

# layer11
cell19 = openmc.Cell(cell_id=19, fill=universe4)
cell19.translation = (0.0, 0.0, 3.989159)
cell19.region = -surf180

# layer12
cell20 = openmc.Cell(cell_id=20, fill=universe4)
cell20.translation = (0.0, 0.0, 4.334966)
cell20.region = -surf181

# layer13
cell21 = openmc.Cell(cell_id=21, fill=universe4)
cell21.translation = (0.0, 0.0, 4.680773)
cell21.region = -surf182

# layer14
cell22 = openmc.Cell(cell_id=22, fill=universe4)
cell22.translation = (0.0, 0.0, 5.02658)
cell22.region = -surf183

# layer15
cell23 = openmc.Cell(cell_id=23, fill=universe4)
cell23.translation = (0.0, 0.0, 5.372387)
cell23.region = -surf184

# layer16
cell24 = openmc.Cell(cell_id=24, fill=universe4)
cell24.translation = (0.0, 0.0, 5.718194)
cell24.region = -surf185

# layer17
cell25 = openmc.Cell(cell_id=25, fill=universe4)
cell25.translation = (0.0, 0.0, 6.064001)
cell25.region = -surf186

# layer18
cell26 = openmc.Cell(cell_id=26, fill=universe4)
cell26.translation = (0.0, 0.0, 6.409808)
cell26.region = -surf187

# layer19
cell27 = openmc.Cell(cell_id=27, fill=universe4)
cell27.translation = (0.0, 0.0, 6.755615)
cell27.region = -surf188

# layer20
cell28 = openmc.Cell(cell_id=28, fill=universe4)
cell28.translation = (0.0, 0.0, 7.101422)
cell28.region = -surf189

# poly1
cell29 = openmc.Cell(cell_id=29, fill=mat10)
cell29.region = -surf10

# poly2
cell30 = openmc.Cell(cell_id=30, fill=mat11)
cell30.region = -surf50

# assby
cell35 = openmc.Cell(cell_id=35, fill=universe3)
cell35.region = -surf1

# assby
cell41 = openmc.Cell(cell_id=41, fill=universe2)
cell41.region = -surf1

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell35, cell41])
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
