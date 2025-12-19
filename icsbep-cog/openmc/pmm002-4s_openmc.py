"""
TEX Experiment tex4i
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

surf1 = openmc.model.RectangularParallelepiped(-15.327376, 15.327376, -15.327376, 15.327376, -0.1487805, 0.1487805)
surf2 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -0.14878049999999998, 0.1616455)
surf3 = openmc.model.RectangularParallelepiped(-15.327376, 15.327376, -15.327376, 15.327376, 0.14878049999999998, 0.1616455)
surf4 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, -0.1767205, -0.14878049999999998)
surf5 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -0.34073749999999997, -0.1767205)
surf6 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 0.24644360000000004, 1.1848496)
surf7 = openmc.model.RectangularParallelepiped(-24.445976, 24.445976, -24.445976, 24.445976, 4.738406800000001, 5.0541288)
surf8 = openmc.model.RectangularParallelepiped(-57.15, 57.15, -57.15, 57.15, 5.849657500999999, 8.389657501)
surf9 = openmc.model.RectangularParallelepiped(-24.13, 24.13, -24.13, 24.13, 5.849657500999999, 8.389657501)
surf10 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 9.5264607, 10.4648667)
surf11 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -2.722843, -0.3407374999999999)
surf12 = openmc.model.RectangularParallelepiped(-27.94, 27.94, -27.94, 27.94, -2.7228429999999997, -2.087843)
surf13 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, -2.7228429999999997, -2.087843)
surf14 = openmc.model.RectangularParallelepiped(-27.939999999999998, -22.86, -27.94, -17.145, -2.7228429999999997, -2.087843)
surf15 = openmc.model.RectangularParallelepiped(-27.939999999999998, -22.86, 17.145, 27.94, -2.7228429999999997, -2.087843)
surf16 = openmc.model.RectangularParallelepiped(-22.86, -15.875, 22.86, 27.939999999999998, -2.7228429999999997, -2.087843)
surf17 = openmc.model.RectangularParallelepiped(-30.48, 30.48, -30.48, 30.48, -3.9928429999999997, -2.722843)
surf20 = openmc.model.RectangularParallelepiped(-39.37, 39.37, -39.37, 39.37, -7.802843, -3.9928429999999997)
surf40 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, -0.3407375, 0.1616455)
surf41 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 1.18484956, 1.68723256)
surf42 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 2.71043661, 3.21281961)
surf43 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 4.23602367, 4.73840667)
surf44 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 5.99253477, 6.49491777)
surf45 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 7.48331207, 7.98569507)
surf46 = openmc.model.RectangularParallelepiped(-22.86, 22.86, -23.034752, 23.034752, 8.974089370000002, 9.47647237)
surf50 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 10.464867, 11.403273)
surf51 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 11.4032725, 13.7853775)
surf60 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 5.0541288, 5.9925348000000005)
surf61 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 1.772030657, 2.710436657)
surf62 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 3.2976177140000003, 4.236023714)
surf63 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 6.544906097999999, 7.483312098)
surf64 = openmc.model.RectangularParallelepiped(-17.874742, 17.874742, -17.874742, 17.874742, 8.035683396, 8.974089396)
surf99 = openmc.model.RectangularParallelepiped(-95.0, 95.0, -95.0, 95.0, -10.0, 30.0, boundary_type="vacuum")
surf101 = openmc.XPlane(surface_id=101, x0=-2.21972)
surf102 = openmc.XPlane(surface_id=102, x0=2.21972)
surf103 = openmc.YPlane(surface_id=103, y0=-3.7832775)
surf104 = openmc.YPlane(surface_id=104, y0=3.6411425)
surf105 = openmc.ZPlane(surface_id=105, z0=-0.10668)
surf106 = openmc.ZPlane(surface_id=106, z0=0.10668)
surf107 = openmc.XPlane(surface_id=107, x0=-1.58472)
surf108 = openmc.XPlane(surface_id=108, x0=1.58472)
surf109 = openmc.YPlane(surface_id=109, y0=-3.1482775)
surf110 = openmc.YPlane(surface_id=110, y0=3.0061425)
surf111 = openmc.ZCylinder(surface_id=111, x0=-1.58472, y0=3.0061425, r=0.635)
surf112 = openmc.ZCylinder(surface_id=112, x0=1.58472, y0=3.0061425, r=0.635)
surf113 = openmc.ZCylinder(surface_id=113, x0=-1.58472, y0=-3.1482775, r=0.635)
surf114 = openmc.ZCylinder(surface_id=114, x0=1.58472, y0=-3.1482775, r=0.635)
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
cell1 = openmc.Cell(cell_id=1, fill=mat13)
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
cell7.translation = (0.0, 0.0, 1.525587057)
cell7.region = -surf41

# layer3
cell8 = openmc.Cell(cell_id=8, fill=universe3)
cell8.translation = (0.0, 0.0, 3.051174114)
cell8.region = -surf42

# layer4
cell9 = openmc.Cell(cell_id=9, fill=universe3)
cell9.translation = (0.0, 0.0, 4.576761171)
cell9.region = -surf43

# imlayer2
cell10 = openmc.Cell(cell_id=10, fill=mat13)
cell10.region = -surf61

# imlayer3
cell11 = openmc.Cell(cell_id=11, fill=mat13)
cell11.region = -surf62

# pla4
cell12 = openmc.Cell(cell_id=12, fill=mat7)
cell12.region = -surf8 & +surf9

# dia
cell13 = openmc.Cell(cell_id=13, fill=mat8)
cell13.region = -surf7

# layer5
cell14 = openmc.Cell(cell_id=14, fill=universe3)
cell14.translation = (0.0, 0.0, 6.333272271)
cell14.region = -surf44

# layer6
cell15 = openmc.Cell(cell_id=15, fill=universe3)
cell15.translation = (0.0, 0.0, 7.824049569)
cell15.region = -surf45

# layer7
cell16 = openmc.Cell(cell_id=16, fill=universe3)
cell16.translation = (0.0, 0.0, 9.314826867)
cell16.region = -surf46

# mod
cell17 = openmc.Cell(cell_id=17, fill=mat13)
cell17.region = -surf60

# mod
cell18 = openmc.Cell(cell_id=18, fill=mat13)
cell18.region = -surf63

# mod
cell19 = openmc.Cell(cell_id=19, fill=mat13)
cell19.region = -surf64

# poly1
cell20 = openmc.Cell(cell_id=20, fill=mat13)
cell20.region = -surf10

# poly2
cell21 = openmc.Cell(cell_id=21, fill=mat13)
cell21.region = -surf50

# poly3
cell22 = openmc.Cell(cell_id=22, fill=mat11)
cell22.region = -surf51

# assby
cell27 = openmc.Cell(cell_id=27, fill=universe2)
cell27.region = -surf1

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell27])
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
source.space = openmc.stats.Box((-1.0, -0.7, -1.0), (1.0, 1.3, 10.22))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
