"""
TEX Experiment tex5di
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_element("P", 1.514500e+01)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("P", 7.900000e+00)

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

materials = openmc.Materials([mat1, mat2, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11, mat12])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.model.RectangularParallelepiped(-15.327376, 15.327376, -15.327376, 15.327376, -0.1487805, 0.1487805)
surf2 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -0.14878049999999998, 0.1616455)
surf3 = openmc.model.RectangularParallelepiped(-15.327376, 15.327376, -15.327376, 15.327376, 0.14878049999999998, 0.1616455)
surf4 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, -0.1767205, -0.14878049999999998)
surf5 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -0.34073749999999997, -0.1767205)
surf6 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 0.18728916699999987, 2.569394167)
surf7 = openmc.model.RectangularParallelepiped(-24.445976, 24.445976, -24.445976, 24.445976, 8.389657501, 8.705379501000001)
surf8 = openmc.model.RectangularParallelepiped(-57.15, 57.15, -57.15, 57.15, 5.849657500999999, 8.389657501)
surf9 = openmc.model.RectangularParallelepiped(-24.13, 24.13, -24.13, 24.13, 5.849657500999999, 8.389657501)
surf10 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 12.2040955, 12.5172175)
surf11 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -2.722843, -0.3407374999999999)
surf12 = openmc.model.RectangularParallelepiped(-27.94, 27.94, -27.94, 27.94, -2.7228429999999997, -2.087843)
surf13 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -2.7228429999999997, -2.087843)
surf14 = openmc.model.RectangularParallelepiped(-27.939999999999998, -22.86, -27.94, -17.145, -2.7228429999999997, -2.087843)
surf15 = openmc.model.RectangularParallelepiped(-27.939999999999998, -22.86, 17.145, 27.94, -2.7228429999999997, -2.087843)
surf16 = openmc.model.RectangularParallelepiped(-22.86, -15.875, 22.86, 27.939999999999998, -2.7228429999999997, -2.087843)
surf17 = openmc.model.RectangularParallelepiped(-30.48, 30.48, -30.48, 30.48, -3.9928429999999997, -2.722843)
surf20 = openmc.model.RectangularParallelepiped(-39.37, 39.37, -39.37, 39.37, -7.802843, -3.9928429999999997)
surf40 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, -0.3407375, 0.1616455)
surf41 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 2.56939417, 3.07177717)
surf42 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 5.47952583, 5.98190883)
surf43 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 8.7053795, 9.207762500000001)
surf44 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 11.645790000000002, 12.148173)
surf50 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 12.5172175, 12.8303395)
surf51 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 12.830339500000001, 15.3728795)
surf61 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 3.097420834, 5.479525834)
surf62 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 6.007552507, 8.389657507)
surf63 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 9.263685, 11.64579)
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
surf117_cyl = openmc.ZCylinder(surface_id=117, x0=tr, y0=-1.60401, r=0.555625)
surf117_zmin = openmc.ZPlane(z0=3.0047565)
surf117_zmax = openmc.ZPlane(z0=0.0)
surf117 = (surf117_cyl, surf117_zmin, surf117_zmax)
surf118_cyl = openmc.ZCylinder(surface_id=118, x0=tr, y0=-1.60401, r=0.635)
surf118_zmin = openmc.ZPlane(z0=3.0047565)
surf118_zmax = openmc.ZPlane(z0=0.0)
surf118 = (surf118_cyl, surf118_zmin, surf118_zmax)
surf119_cyl = openmc.ZCylinder(surface_id=119, x0=tr, y0=1.60401, r=0.555625)
surf119_zmin = openmc.ZPlane(z0=3.0047565)
surf119_zmax = openmc.ZPlane(z0=0.0)
surf119 = (surf119_cyl, surf119_zmin, surf119_zmax)
surf120_cyl = openmc.ZCylinder(surface_id=120, x0=tr, y0=1.60401, r=0.635)
surf120_zmin = openmc.ZPlane(z0=3.0047565)
surf120_zmax = openmc.ZPlane(z0=0.0)
surf120 = (surf120_cyl, surf120_zmin, surf120_zmax)
surf121_cyl = openmc.ZCylinder(surface_id=121, x0=tr, y0=-1.60401, r=0.555625)
surf121_zmin = openmc.ZPlane(z0=-3.1496635)
surf121_zmax = openmc.ZPlane(z0=0.0)
surf121 = (surf121_cyl, surf121_zmin, surf121_zmax)
surf122_cyl = openmc.ZCylinder(surface_id=122, x0=tr, y0=-1.60401, r=0.635)
surf122_zmin = openmc.ZPlane(z0=-3.1496635)
surf122_zmax = openmc.ZPlane(z0=0.0)
surf122 = (surf122_cyl, surf122_zmin, surf122_zmax)
surf123_cyl = openmc.ZCylinder(surface_id=123, x0=tr, y0=1.60401, r=0.555625)
surf123_zmin = openmc.ZPlane(z0=-3.14966355)
surf123_zmax = openmc.ZPlane(z0=0.0)
surf123 = (surf123_cyl, surf123_zmin, surf123_zmax)
surf124_cyl = openmc.ZCylinder(surface_id=124, x0=tr, y0=1.60401, r=0.635)
surf124_zmin = openmc.ZPlane(z0=-3.14966355)
surf124_zmax = openmc.ZPlane(z0=0.0)
surf124 = (surf124_cyl, surf124_zmin, surf124_zmax)
surf125_cyl = openmc.YCylinder(surface_id=125, x0=tr, y0=-2.159635, r=0.079375)
surf125_zmin = openmc.ZPlane(z0=-0.0724535)
surf125_zmax = openmc.ZPlane(z0=-0.027305)
surf125 = (surf125_cyl, surf125_zmin, surf125_zmax)
surf126_cyl = openmc.YCylinder(surface_id=126, x0=tr, y0=-2.159635, r=0.079375)
surf126_zmin = openmc.ZPlane(z0=-0.0724535)
surf126_zmax = openmc.ZPlane(z0=0.027305)
surf126 = (surf126_cyl, surf126_zmin, surf126_zmax)
surf127_cyl = openmc.YCylinder(surface_id=127, x0=tr, y0=2.159635, r=0.079375)
surf127_zmin = openmc.ZPlane(z0=-0.0724535)
surf127_zmax = openmc.ZPlane(z0=-0.027305)
surf127 = (surf127_cyl, surf127_zmin, surf127_zmax)
surf128_cyl = openmc.YCylinder(surface_id=128, x0=tr, y0=2.159635, r=0.079375)
surf128_zmin = openmc.ZPlane(z0=-0.0724535)
surf128_zmax = openmc.ZPlane(z0=0.027305)
surf128 = (surf128_cyl, surf128_zmin, surf128_zmax)
surf129_cyl = openmc.ZCylinder(surface_id=129, x0=tr, y0=0, r=0.079375)
surf129_zmin = openmc.ZPlane(z0=3.5603815)
surf129_zmax = openmc.ZPlane(z0=-0.027305)
surf129 = (surf129_cyl, surf129_zmin, surf129_zmax)
surf130_cyl = openmc.ZCylinder(surface_id=130, x0=tr, y0=0, r=0.079375)
surf130_zmin = openmc.ZPlane(z0=3.5603815)
surf130_zmax = openmc.ZPlane(z0=0.027305)
surf130 = (surf130_cyl, surf130_zmin, surf130_zmax)
surf131_cyl = openmc.ZCylinder(surface_id=131, x0=tr, y0=0, r=0.079375)
surf131_zmin = openmc.ZPlane(z0=-3.7052885)
surf131_zmax = openmc.ZPlane(z0=-0.027305)
surf131 = (surf131_cyl, surf131_zmin, surf131_zmax)
surf132_cyl = openmc.ZCylinder(surface_id=132, x0=tr, y0=0, r=0.079375)
surf132_zmin = openmc.ZPlane(z0=-3.7052885)
surf132_zmax = openmc.ZPlane(z0=0.027305)
surf132 = (surf132_cyl, surf132_zmin, surf132_zmax)
# surf133: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '-1.60401', '3.0047565', '-0.027305']
# surf134: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '-1.60401', '3.0047565', '0.027305']
# surf135: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '1.60401', '3.0047565', '-0.027305']
# surf136: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '1.60401', '3.0047565', '0.027305']
# surf137: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '-1.60401', '-3.0047565', '-0.027305']
# surf138: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '-1.60401', '-3.0047565', '-0.027305']
# surf139: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '1.60401', '-3.0047565', '-0.027305']
# surf140: Unsupported surface type "torus" with params ['0.555625', '0.079375', '0.079375', 'tr', '1.60401', '-3.0047565', '0.027305']
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
surf301 = openmc.model.RectangularParallelepiped(-0.142992, 4.918445999999999, 0.07594600000000007, 7.701661, -0.1487805, 0.1487805)
surf302 = openmc.model.RectangularParallelepiped(-5.20443, -0.142992, 0.07594600000000007, 7.701661, -0.1487805, 0.1487805)
surf303 = openmc.model.RectangularParallelepiped(-10.265868, -5.20443, 0.07594600000000007, 7.701661, -0.1487805, 0.1487805)
surf304 = openmc.model.RectangularParallelepiped(-15.327306, -10.265868000000001, 0.07594600000000007, 7.701661, -0.1487805, 0.1487805)
surf305 = openmc.model.RectangularParallelepiped(4.918445999999999, 9.979884, 0.07594600000000007, 7.701661, -0.1487805, 0.1487805)
surf306 = openmc.model.RectangularParallelepiped(9.979884, 15.041322, 0.07594600000000007, 7.701661, -0.1487805, 0.1487805)
surf307 = openmc.model.RectangularParallelepiped(-0.142992, 4.918445999999999, 7.701661, 15.327376, -0.1487805, 0.1487805)
surf308 = openmc.model.RectangularParallelepiped(-5.20443, -0.142992, 7.701661, 15.327376, -0.1487805, 0.1487805)
surf309 = openmc.model.RectangularParallelepiped(-10.265868, -5.20443, 7.701661, 15.327376, -0.1487805, 0.1487805)
surf310 = openmc.model.RectangularParallelepiped(-15.327306, -10.265868000000001, 7.701661, 15.327376, -0.1487805, 0.1487805)
surf311 = openmc.model.RectangularParallelepiped(4.918445999999999, 9.979884, 7.701661, 15.327376, -0.1487805, 0.1487805)
surf312 = openmc.model.RectangularParallelepiped(9.979884, 15.041322, 7.701661, 15.327376, -0.1487805, 0.1487805)
surf313 = openmc.model.RectangularParallelepiped(-0.142992, 4.918445999999999, -7.5497689999999995, 0.07594599999999962, -0.1487805, 0.1487805)
surf314 = openmc.model.RectangularParallelepiped(-5.20443, -0.142992, -7.5497689999999995, 0.07594599999999962, -0.1487805, 0.1487805)
surf315 = openmc.model.RectangularParallelepiped(-10.265868, -5.20443, -7.5497689999999995, 0.07594599999999962, -0.1487805, 0.1487805)
surf316 = openmc.model.RectangularParallelepiped(-15.327306, -10.265868000000001, -7.5497689999999995, 0.07594599999999962, -0.1487805, 0.1487805)
surf317 = openmc.model.RectangularParallelepiped(4.918445999999999, 9.979884, -7.5497689999999995, 0.07594599999999962, -0.1487805, 0.1487805)
surf318 = openmc.model.RectangularParallelepiped(9.979884, 15.041322, -7.5497689999999995, 0.07594599999999962, -0.1487805, 0.1487805)
surf319 = openmc.model.RectangularParallelepiped(-0.142992, 4.918445999999999, -15.175483999999999, -7.5497689999999995, -0.1487805, 0.1487805)
surf320 = openmc.model.RectangularParallelepiped(-5.20443, -0.142992, -15.175483999999999, -7.5497689999999995, -0.1487805, 0.1487805)
surf321 = openmc.model.RectangularParallelepiped(-10.265868, -5.20443, -15.175483999999999, -7.5497689999999995, -0.1487805, 0.1487805)
surf322 = openmc.model.RectangularParallelepiped(-15.327306, -10.265868000000001, -15.175483999999999, -7.5497689999999995, -0.1487805, 0.1487805)
surf323 = openmc.model.RectangularParallelepiped(4.918445999999999, 9.979884, -15.175483999999999, -7.5497689999999995, -0.1487805, 0.1487805)
surf324 = openmc.model.RectangularParallelepiped(9.979884, 15.041322, -15.175483999999999, -7.5497689999999995, -0.1487805, 0.1487805)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

universe1 = openmc.Universe(universe_id=1, cells=[])

universe2 = openmc.Universe(universe_id=2, cells=[])

u3_cell0 = openmc.Cell()
u3_cell0.region = +surf1 & -surf3
u3_cell1 = openmc.Cell(fill=mat5)
u3_cell1.region = +surf1 & +surf3 & -surf2
u3_cell2 = openmc.Cell(fill=mat4)
u3_cell2.region = -surf4
u3_cell3 = openmc.Cell(fill=mat10)
u3_cell3.region = -surf5
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# poly2
cell1 = openmc.Cell(cell_id=1, fill=mat11)
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

# bott
cell5 = openmc.Cell(cell_id=5, fill=mat11)
cell5.region = -surf11

# layer1
cell6 = openmc.Cell(cell_id=6, fill=universe3)
cell6.region = -surf40

# layer2
cell7 = openmc.Cell(cell_id=7, fill=universe3)
cell7.translation = (0.0, 0.0, 2.910131667)
cell7.region = -surf41

# layer3
cell8 = openmc.Cell(cell_id=8, fill=universe3)
cell8.translation = (0.0, 0.0, 5.820263334)
cell8.region = -surf42

# imlayer2
cell9 = openmc.Cell(cell_id=9, fill=mat11)
cell9.region = -surf61

# imlayer3
cell10 = openmc.Cell(cell_id=10, fill=mat11)
cell10.region = -surf62

# pla4
cell11 = openmc.Cell(cell_id=11, fill=mat7)
cell11.region = -surf8 & +surf9

# dia
cell12 = openmc.Cell(cell_id=12, fill=mat8)
cell12.region = -surf7

# layer4
cell13 = openmc.Cell(cell_id=13, fill=universe3)
cell13.translation = (0.0, 0.0, 9.046117001)
cell13.region = -surf43

# layer5
cell14 = openmc.Cell(cell_id=14, fill=universe3)
cell14.translation = (0.0, 0.0, 11.986527501)
cell14.region = -surf44

# mod
cell15 = openmc.Cell(cell_id=15, fill=mat11)
cell15.region = -surf63

# poly1
cell16 = openmc.Cell(cell_id=16, fill=mat12)
cell16.region = -surf10

# poly2
cell17 = openmc.Cell(cell_id=17, fill=mat12)
cell17.region = -surf50

# poly3
cell18 = openmc.Cell(cell_id=18, fill=mat11)
cell18.region = -surf51

# assby
cell23 = openmc.Cell(cell_id=23, fill=universe2)
cell23.region = -surf1

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell23])
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
source.space = openmc.stats.Box((-1.0, -0.7, -1.0), (1.0, 1.3, 12.9))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
