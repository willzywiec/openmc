"""
PMF037-13: Flooded 2x2x3 array of double-canned 3kg Pu parts in water; Hw=46.0; dx=dy=11.994; dz=11.815
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium (cases 11-13)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.600700e-02)
mat1.add_nuclide("Pu240", 2.923400e-03)
mat1.add_nuclide("Pu241", 1.419900e-04)
mat1.add_nuclide("Pu242", 4.856300e-06)
mat1.add_nuclide("Am241", 8.232500e-05)

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
surf6 = openmc.ZPlane(surface_id=6, z0=46.0)
# Inner tank
surf7 = openmc.ZCylinder(surface_id=7, r=34.925)
# Outer tank
surf8 = openmc.ZCylinder(surface_id=8, r=35.56, boundary_type="vacuum")
surf11 = openmc.ZCylinder(surface_id=11, x0=0.0, y0=0.0, r=3.81)
surf12 = openmc.ZCylinder(surface_id=12, x0=11.994, y0=0.0, r=3.81)
surf13 = openmc.ZCylinder(surface_id=13, x0=0.0, y0=-11.994, r=3.81)
surf14 = openmc.ZCylinder(surface_id=14, x0=11.994, y0=-11.994, r=3.81)
surf21 = openmc.ZCylinder(surface_id=21, x0=0.0, y0=0.0, r=3.81)
surf22 = openmc.ZCylinder(surface_id=22, x0=11.994, y0=0.0, r=3.81)
surf23 = openmc.ZCylinder(surface_id=23, x0=0.0, y0=-11.994, r=3.81)
surf24 = openmc.ZCylinder(surface_id=24, x0=11.994, y0=-11.994, r=3.81)
surf31 = openmc.ZCylinder(surface_id=31, x0=0.0, y0=0.0, r=3.81)
surf32 = openmc.ZCylinder(surface_id=32, x0=11.994, y0=0.0, r=3.81)
surf33 = openmc.ZCylinder(surface_id=33, x0=0.0, y0=-11.994, r=3.81)
surf34 = openmc.ZCylinder(surface_id=34, x0=11.994, y0=-11.994, r=3.81)
# Lower  bottom tray
surf41 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 10.08, 10.715000000000002)
# Lower  middle tray
surf42 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 13.774999999999999, 14.41)
# Lower  upper  tray
surf43 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 17.7, 18.334999999999997)
# Middle bottom tray
surf51 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 21.895, 22.529999999999998)
# Middle middle tray
surf52 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 25.59, 26.224999999999998)
# Middle upper  tray
surf53 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 29.515, 30.15)
# Upper  bottom tray
surf61 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 33.71, 34.345000000000006)
# Upper  middle tray
surf62 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 37.404999999999994, 38.04)
# Upper  upper  tray
surf63 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 41.33, 41.965)
surf101 = openmc.ZCylinder(surface_id=101, x0=-11.994, y0=11.994, r=3.81)
surf102 = openmc.ZCylinder(surface_id=102, x0=0.0, y0=11.994, r=3.81)
surf103 = openmc.ZCylinder(surface_id=103, x0=11.994, y0=11.994, r=3.81)
surf104 = openmc.ZCylinder(surface_id=104, x0=-11.994, y0=0.0, r=3.81)
surf105 = openmc.ZCylinder(surface_id=105, x0=-11.994, y0=-11.994, r=3.81)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1105, z0=0.997)
surf1_zmax = openmc.ZPlane(surface_id=1106, z0=5.63)
surf2_zmin = openmc.ZPlane(surface_id=1107, z0=0.91)
surf2_zmax = openmc.ZPlane(surface_id=1108, z0=5.63)
surf3_zmin = openmc.ZPlane(surface_id=1109, z0=5.63)
surf3_zmax = openmc.ZPlane(surface_id=1110, z0=5.651)
surf4_zmin = openmc.ZPlane(surface_id=1111, z0=0.91)
surf4_zmax = openmc.ZPlane(surface_id=1112, z0=6.277)
surf5_zmin = openmc.ZPlane(surface_id=1113, z0=0.0)
surf5_zmax = openmc.ZPlane(surface_id=1114, z0=6.947)
surf7_zmin = openmc.ZPlane(surface_id=1115, z0=0.0)
surf7_zmax = openmc.ZPlane(surface_id=1116, z0=125.0)
surf8_zmin = openmc.ZPlane(surface_id=1117, z0=-0.635, boundary_type="vacuum")
surf8_zmax = openmc.ZPlane(surface_id=1118, z0=125.0, boundary_type="vacuum")

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
cell1.translation = (0.0, 0.0, 10.715)
cell1.region = -surf11 & +surf41

# CanPart
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.translation = (11.994, 0.0, 10.715)
cell2.region = +surf11 & -surf12 & +surf41

# CanPart
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (0.0, -11.994, 10.715)
cell3.region = +surf11 & +surf12 & -surf13 & +surf41

# CanPart
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (11.994, -11.994, 10.715)
cell4.region = +surf11 & +surf12 & +surf13 & -surf14 & +surf41

# CanPart
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (0.0, 0.0, 22.53)
cell5.region = -surf21 & +surf51

# CanPart
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (11.994, 0.0, 22.53)
cell6.region = +surf21 & -surf22 & +surf51

# CanPart
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.translation = (0.0, -11.994, 22.53)
cell7.region = +surf21 & +surf22 & -surf23 & +surf51

# CanPart
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.translation = (11.994, -11.994, 22.53)
cell8.region = +surf21 & +surf22 & +surf23 & -surf24 & +surf51

# CanPart
cell9 = openmc.Cell(cell_id=9, fill=universe1)
cell9.translation = (0.0, 0.0, 34.345)
cell9.region = -surf31 & +surf61

# CanPart
cell10 = openmc.Cell(cell_id=10, fill=universe1)
cell10.translation = (11.994, 0.0, 34.345)
cell10.region = +surf31 & -surf32 & +surf61

# CanPart
cell11 = openmc.Cell(cell_id=11, fill=universe1)
cell11.translation = (0.0, -11.994, 34.345)
cell11.region = +surf31 & +surf32 & -surf33 & +surf61

# CanPart
cell12 = openmc.Cell(cell_id=12, fill=universe1)
cell12.translation = (11.994, -11.994, 34.345)
cell12.region = +surf31 & +surf32 & +surf33 & -surf34 & +surf61

# Tray
cell13 = openmc.Cell(cell_id=13, fill=mat5)
cell13.region = -surf41

# Tray
cell14 = openmc.Cell(cell_id=14, fill=mat5)
cell14.region = -surf42 & +surf11 & +surf12 & +surf13 & +surf14 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105

# Tray
cell15 = openmc.Cell(cell_id=15, fill=mat5)
cell15.region = -surf43

# Tray
cell16 = openmc.Cell(cell_id=16, fill=mat5)
cell16.region = -surf51

# Tray
cell17 = openmc.Cell(cell_id=17, fill=mat5)
cell17.region = -surf52 & +surf21 & +surf22 & +surf23 & +surf24 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105

# Tray
cell18 = openmc.Cell(cell_id=18, fill=mat5)
cell18.region = -surf53

# Tray
cell19 = openmc.Cell(cell_id=19, fill=mat5)
cell19.region = -surf61

# Tray
cell20 = openmc.Cell(cell_id=20, fill=mat5)
cell20.region = -surf62 & +surf31 & +surf32 & +surf33 & +surf34 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105

# Tray
cell21 = openmc.Cell(cell_id=21, fill=mat5)
cell21.region = -surf63

# Water
cell22 = openmc.Cell(cell_id=22, fill=mat6)
cell22.region = -surf42 & -surf101

# Water
cell23 = openmc.Cell(cell_id=23, fill=mat6)
cell23.region = -surf42 & -surf102

# Water
cell24 = openmc.Cell(cell_id=24, fill=mat6)
cell24.region = -surf42 & -surf103

# Water
cell25 = openmc.Cell(cell_id=25, fill=mat6)
cell25.region = -surf42 & -surf104

# Water
cell26 = openmc.Cell(cell_id=26, fill=mat6)
cell26.region = -surf42 & -surf105

# Water
cell27 = openmc.Cell(cell_id=27, fill=mat6)
cell27.region = -surf52 & -surf101

# Water
cell28 = openmc.Cell(cell_id=28, fill=mat6)
cell28.region = -surf52 & -surf102

# Water
cell29 = openmc.Cell(cell_id=29, fill=mat6)
cell29.region = -surf52 & -surf103

# Water
cell30 = openmc.Cell(cell_id=30, fill=mat6)
cell30.region = -surf52 & -surf104

# Water
cell31 = openmc.Cell(cell_id=31, fill=mat6)
cell31.region = -surf52 & -surf105

# Water
cell32 = openmc.Cell(cell_id=32, fill=mat6)
cell32.region = -surf62 & -surf101

# Water
cell33 = openmc.Cell(cell_id=33, fill=mat6)
cell33.region = -surf62 & -surf102

# Water
cell34 = openmc.Cell(cell_id=34, fill=mat6)
cell34.region = -surf62 & -surf103

# Water
cell35 = openmc.Cell(cell_id=35, fill=mat6)
cell35.region = -surf62 & -surf104

# Water
cell36 = openmc.Cell(cell_id=36, fill=mat6)
cell36.region = -surf62 & -surf105

# Water
cell37 = openmc.Cell(cell_id=37, fill=mat6)
cell37.region = -surf6 & (-surf7 & +surf7_zmin & -surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax) & +surf11 & +surf12 & +surf13 & +surf14 & +surf21 & +surf22 & +surf23 & +surf24 & +surf31 & +surf32 & +surf33 & +surf34 & +surf41 & +surf42 & +surf43 & +surf51 & +surf52 & +surf53 & +surf61 & +surf62 & +surf63

# Tank
cell38 = openmc.Cell(cell_id=38, fill=mat5)
cell38.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# SS304L
cell44 = openmc.Cell(cell_id=44, fill=mat4)
cell44.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell44])
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
source.space = openmc.stats.Box((-1.0, -12.994, 13.0285), (12.994, 1.0, 38.6585))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
