"""
PMF037-10: Flooded 2x2x2 array of double-canned 3kg Pu parts in water; Hw=29.6; dx=dy=11.994; dz=8.255
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium (cases 1-10)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.605400e-02)
mat1.add_nuclide("Pu240", 2.926400e-03)
mat1.add_nuclide("Pu241", 1.421400e-04)
mat1.add_nuclide("Pu242", 4.861300e-06)
mat1.add_nuclide("Am241", 8.240900e-05)

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
surf6 = openmc.ZPlane(surface_id=6, z0=29.6)
# Inner tank
surf7 = openmc.ZCylinder(surface_id=7, r=34.925)
# Outer tank
surf8 = openmc.ZCylinder(surface_id=8, r=35.56)
surf11 = openmc.ZCylinder(surface_id=11, x0=0.0, y0=0.0, r=3.81)
surf12 = openmc.ZCylinder(surface_id=12, x0=11.994, y0=0.0, r=3.81)
surf13 = openmc.ZCylinder(surface_id=13, x0=0.0, y0=-11.994, r=3.81)
surf14 = openmc.ZCylinder(surface_id=14, x0=11.994, y0=-11.994, r=3.81)
surf21 = openmc.ZCylinder(surface_id=21, x0=0.0, y0=0.0, r=3.81)
surf22 = openmc.ZCylinder(surface_id=22, x0=11.994, y0=0.0, r=3.81)
surf23 = openmc.ZCylinder(surface_id=23, x0=0.0, y0=-11.994, r=3.81)
surf24 = openmc.ZCylinder(surface_id=24, x0=11.994, y0=-11.994, r=3.81)
# Lower bottom tray
surf31 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 10.08, 10.715000000000002)
# Lower middle tray
surf32 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 13.774999999999999, 14.41)
# Lower upper  tray
surf33 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 17.7, 18.334999999999997)
# Upper bottom tray
surf41 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 18.335, 18.97)
# Upper middle tray
surf42 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 22.03, 22.665)
# Upper upper  tray
surf43 = openmc.model.RectangularParallelepiped(-22.85, 22.85, -22.85, 22.85, 25.955000000000002, 26.59)
surf101 = openmc.ZCylinder(surface_id=101, x0=-11.994, y0=11.994, r=3.81)
surf102 = openmc.ZCylinder(surface_id=102, x0=0.0, y0=11.994, r=3.81)
surf103 = openmc.ZCylinder(surface_id=103, x0=11.994, y0=11.994, r=3.81)
surf104 = openmc.ZCylinder(surface_id=104, x0=-11.994, y0=0.0, r=3.81)
surf105 = openmc.ZCylinder(surface_id=105, x0=-11.994, y0=-11.994, r=3.81)

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
cell1.translation = (0.0, 0.0, 10.715)
cell1.region = -surf11 & +surf31

# CanPart
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.translation = (11.994, 0.0, 10.715)
cell2.region = +surf11 & -surf12 & +surf31

# CanPart
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (0.0, -11.994, 10.715)
cell3.region = +surf11 & +surf12 & -surf13 & +surf31

# CanPart
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (11.994, -11.994, 10.715)
cell4.region = +surf11 & +surf12 & +surf13 & -surf14 & +surf31

# CanPart
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (0.0, 0.0, 18.97)
cell5.region = -surf21 & +surf41

# CanPart
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (11.994, 0.0, 18.97)
cell6.region = +surf21 & -surf22 & +surf41

# CanPart
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.translation = (0.0, -11.994, 18.97)
cell7.region = +surf21 & +surf22 & -surf23 & +surf41

# CanPart
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.translation = (11.994, -11.994, 18.97)
cell8.region = +surf21 & +surf22 & +surf23 & -surf24 & +surf41

# Tray
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = -surf31

# Tray
cell10 = openmc.Cell(cell_id=10, fill=mat5)
cell10.region = -surf32 & +surf11 & +surf12 & +surf13 & +surf14 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105

# Tray
cell11 = openmc.Cell(cell_id=11, fill=mat5)
cell11.region = -surf33 & +surf41

# Tray
cell12 = openmc.Cell(cell_id=12, fill=mat5)
cell12.region = -surf41

# Tray
cell13 = openmc.Cell(cell_id=13, fill=mat5)
cell13.region = -surf42 & +surf21 & +surf22 & +surf23 & +surf24 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105

# Tray
cell14 = openmc.Cell(cell_id=14, fill=mat5)
cell14.region = -surf43

# Water
cell15 = openmc.Cell(cell_id=15, fill=mat6)
cell15.region = -surf32 & -surf101

# Water
cell16 = openmc.Cell(cell_id=16, fill=mat6)
cell16.region = -surf32 & -surf102

# Water
cell17 = openmc.Cell(cell_id=17, fill=mat6)
cell17.region = -surf32 & -surf103

# Water
cell18 = openmc.Cell(cell_id=18, fill=mat6)
cell18.region = -surf32 & -surf104

# Water
cell19 = openmc.Cell(cell_id=19, fill=mat6)
cell19.region = -surf32 & -surf105

# Water
cell20 = openmc.Cell(cell_id=20, fill=mat6)
cell20.region = -surf42 & -surf101

# Water
cell21 = openmc.Cell(cell_id=21, fill=mat6)
cell21.region = -surf42 & -surf102

# Water
cell22 = openmc.Cell(cell_id=22, fill=mat6)
cell22.region = -surf42 & -surf103

# Water
cell23 = openmc.Cell(cell_id=23, fill=mat6)
cell23.region = -surf42 & -surf104

# Water
cell24 = openmc.Cell(cell_id=24, fill=mat6)
cell24.region = -surf42 & -surf105

# Water
cell25 = openmc.Cell(cell_id=25, fill=mat6)
cell25.region = -surf6 & (-surf7 & +surf7_zmin & -surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax) & +surf11 & +surf12 & +surf13 & +surf14 & +surf21 & +surf22 & +surf23 & +surf24 & +surf31 & +surf32 & +surf33 & +surf41 & +surf42 & +surf43

# Tank
cell26 = openmc.Cell(cell_id=26, fill=mat5)
cell26.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# SS304L
cell32 = openmc.Cell(cell_id=32, fill=mat4)
cell32.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell32])
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
source.space = openmc.stats.Box((-1.0, -12.994, 13.0285), (12.994, 1.0, 23.2835))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
