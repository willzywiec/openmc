"""
PMF037-14: Flooded 2x2x4 array of double-canned 3kg Pu parts in water; Hw=68.4; dx=dy=10.029; dz=15.365
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium (cases 14-16)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.603100e-02)
mat1.add_nuclide("Pu240", 2.924900e-03)
mat1.add_nuclide("Pu241", 1.420700e-04)
mat1.add_nuclide("Pu242", 4.858800e-06)
mat1.add_nuclide("Am241", 8.236700e-05)

# Al-3004
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.831100e-02)
mat2.add_element("Cu", 6.444200e-05)
mat2.add_element("Fe", 2.053100e-04)
mat2.add_element("Mg", 7.076400e-04)
mat2.add_element("Mn", 3.727000e-04)
mat2.add_element("Si", 1.749700e-04)
mat2.add_element("Zn", 6.262500e-05)

# Mild steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 3.154700e-04)
mat3.add_element("Fe", 8.413100e-02)
mat3.add_element("Mn", 3.189900e-04)
mat3.add_element("P", 2.293700e-05)
mat3.add_element("S", 3.692200e-05)
mat3.add_element("Si", 1.686400e-05)
mat3.add_element("Sn", 1.197000e-04)

# SS-304L
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 1.183300e-04)
mat4.add_element("Cr", 1.738400e-02)
mat4.add_element("Fe", 5.790200e-02)
mat4.add_element("Mn", 1.731900e-03)
mat4.add_element("Ni", 8.106100e-03)
mat4.add_element("Si", 1.693900e-03)

# Al-6061
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 5.818300e-02)
mat5.add_element("Cr", 6.254200e-05)
mat5.add_element("Cu", 6.396800e-05)
mat5.add_element("Fe", 2.038000e-04)
mat5.add_element("Mg", 6.689800e-04)
mat5.add_element("Mn", 4.439500e-05)
mat5.add_element("Si", 3.473600e-04)
mat5.add_element("Ti", 5.093900e-05)
mat5.add_element("Zn", 6.216400e-05)

# Water
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.673500e-02)
mat6.add_nuclide("O16", 3.336800e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Pu
surf1 = openmc.ZCylinder(surface_id=1, r=3.2625)
# Al-3004
surf2 = openmc.ZCylinder(surface_id=2, r=3.2995)
# Mild steel
surf3 = openmc.ZCylinder(surface_id=3, r=3.2995)
# Gap
surf4 = openmc.ZCylinder(surface_id=4, r=3.47)
# SS-304L
surf5 = openmc.ZCylinder(surface_id=5, r=3.81)
# Water height
surf6 = openmc.ZPlane(surface_id=6, z0=68.4)
# Inner tank
surf7 = openmc.ZCylinder(surface_id=7, r=34.925)
# Outer tank
surf8 = openmc.ZCylinder(surface_id=8, r=35.56)
surf11 = openmc.ZCylinder(surface_id=11, x0=-5.0145, y0=-5.0145, r=3.81)
surf12 = openmc.ZCylinder(surface_id=12, x0=-5.0145, y0=5.0145, r=3.81)
surf13 = openmc.ZCylinder(surface_id=13, x0=5.0145, y0=-5.0145, r=3.81)
surf14 = openmc.ZCylinder(surface_id=14, x0=5.0145, y0=5.0145, r=3.81)
surf21 = openmc.ZCylinder(surface_id=21, x0=-5.0145, y0=-5.0145, r=3.81)
surf22 = openmc.ZCylinder(surface_id=22, x0=-5.0145, y0=5.0145, r=3.81)
surf23 = openmc.ZCylinder(surface_id=23, x0=5.0145, y0=-5.0145, r=3.81)
surf24 = openmc.ZCylinder(surface_id=24, x0=5.0145, y0=5.0145, r=3.81)
surf31 = openmc.ZCylinder(surface_id=31, x0=-5.0145, y0=-5.0145, r=3.81)
surf32 = openmc.ZCylinder(surface_id=32, x0=-5.0145, y0=5.0145, r=3.81)
surf33 = openmc.ZCylinder(surface_id=33, x0=5.0145, y0=-5.0145, r=3.81)
surf34 = openmc.ZCylinder(surface_id=34, x0=5.0145, y0=5.0145, r=3.81)
surf41 = openmc.ZCylinder(surface_id=41, x0=-5.0145, y0=-5.0145, r=3.81)
surf42 = openmc.ZCylinder(surface_id=42, x0=-5.0145, y0=5.0145, r=3.81)
surf43 = openmc.ZCylinder(surface_id=43, x0=5.0145, y0=-5.0145, r=3.81)
surf44 = openmc.ZCylinder(surface_id=44, x0=5.0145, y0=5.0145, r=3.81)
# 1st bottom tray
surf51 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 10.08, 10.715000000000002)
# 1st middle tray
surf52 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 13.774999999999999, 14.41)
# 1st upper  tray
surf53 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 17.7, 18.334999999999997)
# 2nd bottom tray
surf61 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 25.445, 26.08)
# 2nd middle tray
surf62 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 29.14, 29.775)
# 2nd upper  tray
surf63 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 33.065, 33.7)
# 3rd bottom tray
surf71 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 40.809999999999995, 41.445)
# 3rd middle tray
surf72 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 44.504999999999995, 45.14)
# 3rd upper  tray
surf73 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 48.43, 49.065000000000005)
# 4th bottom tray
surf81 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 56.175, 56.81)
# 4th middle tray
surf82 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 59.87, 60.505)
# 4th upper  tray
surf83 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 63.794999999999995, 64.42999999999999)
surf101 = openmc.ZCylinder(surface_id=101, x0=-15.0435, y0=15.0435, r=3.81)
surf102 = openmc.ZCylinder(surface_id=102, x0=-5.0145, y0=15.0435, r=3.81)
surf103 = openmc.ZCylinder(surface_id=103, x0=5.0145, y0=15.0435, r=3.81)
surf104 = openmc.ZCylinder(surface_id=104, x0=15.0435, y0=15.0435, r=3.81)
surf105 = openmc.ZCylinder(surface_id=105, x0=-15.0435, y0=5.0145, r=3.81)
surf106 = openmc.ZCylinder(surface_id=106, x0=15.0435, y0=5.0145, r=3.81)
surf107 = openmc.ZCylinder(surface_id=107, x0=-15.0435, y0=-5.0145, r=3.81)
surf108 = openmc.ZCylinder(surface_id=108, x0=15.0435, y0=-5.0145, r=3.81)
surf109 = openmc.ZCylinder(surface_id=109, x0=-15.0435, y0=-15.0435, r=3.81)
surf110 = openmc.ZCylinder(surface_id=110, x0=-5.0145, y0=-15.0435, r=3.81)
surf111 = openmc.ZCylinder(surface_id=111, x0=5.0145, y0=-15.0435, r=3.81)
surf112 = openmc.ZCylinder(surface_id=112, x0=15.0435, y0=-15.0435, r=3.81)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=0.997)
surf1_zmax = openmc.ZPlane(z0=5.63)
surf2_zmin = openmc.ZPlane(z0=0.91)
surf2_zmax = openmc.ZPlane(z0=5.63)
surf3_zmin = openmc.ZPlane(z0=5.63)
surf3_zmax = openmc.ZPlane(z0=5.651)
surf4_zmin = openmc.ZPlane(z0=0.91)
surf4_zmax = openmc.ZPlane(z0=6.277)
surf5_zmin = openmc.ZPlane(z0=0.0)
surf5_zmax = openmc.ZPlane(z0=6.947)
surf7_zmin = openmc.ZPlane(z0=0.0)
surf7_zmax = openmc.ZPlane(z0=125.0)
surf8_zmin = openmc.ZPlane(z0=-0.635, boundary_type="vacuum")
surf8_zmax = openmc.ZPlane(z0=125.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell3 = openmc.Cell()
u1_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CanPart
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.translation = (-5.0145, -5.0145, 10.715)
cell1.region = -surf11 & +surf51

# CanPart
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.translation = (-5.0145, 5.0145, 10.715)
cell2.region = +surf11 & -surf12 & +surf51

# CanPart
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (5.0145, -5.0145, 10.715)
cell3.region = +surf11 & +surf12 & -surf13 & +surf51

# CanPart
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (5.0145, 5.0145, 10.715)
cell4.region = +surf11 & +surf12 & +surf13 & -surf14 & +surf51

# CanPart
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (-5.0145, -5.0145, 26.08)
cell5.region = -surf21 & +surf61

# CanPart
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (-5.0145, 5.0145, 26.08)
cell6.region = +surf21 & -surf22 & +surf61

# CanPart
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.translation = (5.0145, -5.0145, 26.08)
cell7.region = +surf21 & +surf22 & -surf23 & +surf61

# CanPart
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.translation = (5.0145, 5.0145, 26.08)
cell8.region = +surf21 & +surf22 & +surf23 & -surf24 & +surf61

# CanPart
cell9 = openmc.Cell(cell_id=9, fill=universe1)
cell9.translation = (-5.0145, -5.0145, 41.445)
cell9.region = -surf31 & +surf71

# CanPart
cell10 = openmc.Cell(cell_id=10, fill=universe1)
cell10.translation = (-5.0145, 5.0145, 41.445)
cell10.region = +surf31 & -surf32 & +surf71

# CanPart
cell11 = openmc.Cell(cell_id=11, fill=universe1)
cell11.translation = (5.0145, -5.0145, 41.445)
cell11.region = +surf31 & +surf32 & -surf33 & +surf71

# CanPart
cell12 = openmc.Cell(cell_id=12, fill=universe1)
cell12.translation = (5.0145, 5.0145, 41.445)
cell12.region = +surf31 & +surf32 & +surf33 & -surf34 & +surf71

# CanPart
cell13 = openmc.Cell(cell_id=13, fill=universe1)
cell13.translation = (-5.0145, -5.0145, 56.81)
cell13.region = -surf41 & +surf81

# CanPart
cell14 = openmc.Cell(cell_id=14, fill=universe1)
cell14.translation = (-5.0145, 5.0145, 56.81)
cell14.region = +surf41 & -surf42 & +surf81

# CanPart
cell15 = openmc.Cell(cell_id=15, fill=universe1)
cell15.translation = (5.0145, -5.0145, 56.81)
cell15.region = +surf41 & +surf42 & -surf43 & +surf81

# CanPart
cell16 = openmc.Cell(cell_id=16, fill=universe1)
cell16.translation = (5.0145, 5.0145, 56.81)
cell16.region = +surf41 & +surf42 & +surf43 & -surf44 & +surf81

# Tray
cell17 = openmc.Cell(cell_id=17, fill=mat5)
cell17.region = -surf51

# Tray
cell18 = openmc.Cell(cell_id=18, fill=mat5)
cell18.region = -surf52 & +surf11 & +surf12 & +surf13 & +surf14 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf111 & +surf112

# Tray
cell19 = openmc.Cell(cell_id=19, fill=mat5)
cell19.region = -surf53

# Tray
cell20 = openmc.Cell(cell_id=20, fill=mat5)
cell20.region = -surf61

# Tray
cell21 = openmc.Cell(cell_id=21, fill=mat5)
cell21.region = -surf62 & +surf21 & +surf22 & +surf23 & +surf24 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf111 & +surf112

# Tray
cell22 = openmc.Cell(cell_id=22, fill=mat5)
cell22.region = -surf63

# Tray
cell23 = openmc.Cell(cell_id=23, fill=mat5)
cell23.region = -surf71

# Tray
cell24 = openmc.Cell(cell_id=24, fill=mat5)
cell24.region = -surf72 & +surf31 & +surf32 & +surf33 & +surf34 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf111 & +surf112

# Tray
cell25 = openmc.Cell(cell_id=25, fill=mat5)
cell25.region = -surf73

# Tray
cell26 = openmc.Cell(cell_id=26, fill=mat5)
cell26.region = -surf81

# Tray
cell27 = openmc.Cell(cell_id=27, fill=mat5)
cell27.region = -surf82 & +surf41 & +surf42 & +surf43 & +surf44 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf111 & +surf112

# Tray
cell28 = openmc.Cell(cell_id=28, fill=mat5)
cell28.region = -surf83

# Water
cell29 = openmc.Cell(cell_id=29, fill=mat6)
cell29.region = -surf52 & -surf101

# Water
cell30 = openmc.Cell(cell_id=30, fill=mat6)
cell30.region = -surf52 & -surf102

# Water
cell31 = openmc.Cell(cell_id=31, fill=mat6)
cell31.region = -surf52 & -surf103

# Water
cell32 = openmc.Cell(cell_id=32, fill=mat6)
cell32.region = -surf52 & -surf104

# Water
cell33 = openmc.Cell(cell_id=33, fill=mat6)
cell33.region = -surf52 & -surf105

# Water
cell34 = openmc.Cell(cell_id=34, fill=mat6)
cell34.region = -surf52 & -surf106

# Water
cell35 = openmc.Cell(cell_id=35, fill=mat6)
cell35.region = -surf52 & -surf107

# Water
cell36 = openmc.Cell(cell_id=36, fill=mat6)
cell36.region = -surf52 & -surf108

# Water
cell37 = openmc.Cell(cell_id=37, fill=mat6)
cell37.region = -surf52 & -surf109

# Water
cell38 = openmc.Cell(cell_id=38, fill=mat6)
cell38.region = -surf52 & -surf110

# Water
cell39 = openmc.Cell(cell_id=39, fill=mat6)
cell39.region = -surf52 & -surf111

# Water
cell40 = openmc.Cell(cell_id=40, fill=mat6)
cell40.region = -surf52 & -surf112

# Water
cell41 = openmc.Cell(cell_id=41, fill=mat6)
cell41.region = -surf62 & -surf101

# Water
cell42 = openmc.Cell(cell_id=42, fill=mat6)
cell42.region = -surf62 & -surf102

# Water
cell43 = openmc.Cell(cell_id=43, fill=mat6)
cell43.region = -surf62 & -surf103

# Water
cell44 = openmc.Cell(cell_id=44, fill=mat6)
cell44.region = -surf62 & -surf104

# Water
cell45 = openmc.Cell(cell_id=45, fill=mat6)
cell45.region = -surf62 & -surf105

# Water
cell46 = openmc.Cell(cell_id=46, fill=mat6)
cell46.region = -surf62 & -surf106

# Water
cell47 = openmc.Cell(cell_id=47, fill=mat6)
cell47.region = -surf62 & -surf107

# Water
cell48 = openmc.Cell(cell_id=48, fill=mat6)
cell48.region = -surf62 & -surf108

# Water
cell49 = openmc.Cell(cell_id=49, fill=mat6)
cell49.region = -surf62 & -surf109

# Water
cell50 = openmc.Cell(cell_id=50, fill=mat6)
cell50.region = -surf62 & -surf110

# Water
cell51 = openmc.Cell(cell_id=51, fill=mat6)
cell51.region = -surf62 & -surf111

# Water
cell52 = openmc.Cell(cell_id=52, fill=mat6)
cell52.region = -surf62 & -surf112

# Water
cell53 = openmc.Cell(cell_id=53, fill=mat6)
cell53.region = -surf72 & -surf101

# Water
cell54 = openmc.Cell(cell_id=54, fill=mat6)
cell54.region = -surf72 & -surf102

# Water
cell55 = openmc.Cell(cell_id=55, fill=mat6)
cell55.region = -surf72 & -surf103

# Water
cell56 = openmc.Cell(cell_id=56, fill=mat6)
cell56.region = -surf72 & -surf104

# Water
cell57 = openmc.Cell(cell_id=57, fill=mat6)
cell57.region = -surf72 & -surf105

# Water
cell58 = openmc.Cell(cell_id=58, fill=mat6)
cell58.region = -surf72 & -surf106

# Water
cell59 = openmc.Cell(cell_id=59, fill=mat6)
cell59.region = -surf72 & -surf107

# Water
cell60 = openmc.Cell(cell_id=60, fill=mat6)
cell60.region = -surf72 & -surf108

# Water
cell61 = openmc.Cell(cell_id=61, fill=mat6)
cell61.region = -surf72 & -surf109

# Water
cell62 = openmc.Cell(cell_id=62, fill=mat6)
cell62.region = -surf72 & -surf110

# Water
cell63 = openmc.Cell(cell_id=63, fill=mat6)
cell63.region = -surf72 & -surf111

# Water
cell64 = openmc.Cell(cell_id=64, fill=mat6)
cell64.region = -surf72 & -surf112

# Water
cell65 = openmc.Cell(cell_id=65, fill=mat6)
cell65.region = -surf82 & -surf101

# Water
cell66 = openmc.Cell(cell_id=66, fill=mat6)
cell66.region = -surf82 & -surf102

# Water
cell67 = openmc.Cell(cell_id=67, fill=mat6)
cell67.region = -surf82 & -surf103

# Water
cell68 = openmc.Cell(cell_id=68, fill=mat6)
cell68.region = -surf82 & -surf104

# Water
cell69 = openmc.Cell(cell_id=69, fill=mat6)
cell69.region = -surf82 & -surf105

# Water
cell70 = openmc.Cell(cell_id=70, fill=mat6)
cell70.region = -surf82 & -surf106

# Water
cell71 = openmc.Cell(cell_id=71, fill=mat6)
cell71.region = -surf82 & -surf107

# Water
cell72 = openmc.Cell(cell_id=72, fill=mat6)
cell72.region = -surf82 & -surf108

# Water
cell73 = openmc.Cell(cell_id=73, fill=mat6)
cell73.region = -surf82 & -surf109

# Water
cell74 = openmc.Cell(cell_id=74, fill=mat6)
cell74.region = -surf82 & -surf110

# Water
cell75 = openmc.Cell(cell_id=75, fill=mat6)
cell75.region = -surf82 & -surf111

# Water
cell76 = openmc.Cell(cell_id=76, fill=mat6)
cell76.region = -surf82 & -surf112

# Water
cell77 = openmc.Cell(cell_id=77, fill=mat6)
cell77.region = -surf6 & (-surf7 & +surf7_zmin & -surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax) & +surf11 & +surf12 & +surf13 & +surf14 & +surf21 & +surf22 & +surf23 & +surf24 & +surf31 & +surf32 & +surf33 & +surf34 & +surf41 & +surf42 & +surf43 & +surf44 & +surf51 & +surf52 & +surf53 & +surf61 & +surf62 & +surf63 & +surf71 & +surf72 & +surf73 & +surf81 & +surf82 & +surf83

# Tank
cell78 = openmc.Cell(cell_id=78, fill=mat5)
cell78.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# SS304L
cell84 = openmc.Cell(cell_id=84, fill=mat4)
cell84.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell55, cell56, cell57, cell58, cell59, cell60, cell61, cell62, cell63, cell64, cell65, cell66, cell67, cell68, cell69, cell70, cell71, cell72, cell73, cell74, cell75, cell76, cell77, cell78, cell84])
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
source.space = openmc.stats.Box((-6.0145, -6.0145, 13.0285), (6.0145, 6.0145, 61.1235))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
