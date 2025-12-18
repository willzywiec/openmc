"""
LST025-7: STACY two slabs of 10% 235U uranyl nitrate with concrete (C150,C50,C100,C75,C25,C25B,C75B,C100B) isolators
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Fuel
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 6.056000e-07)
mat1.add_nuclide("U235", 7.515100e-05)
mat1.add_nuclide("U236", 7.505800e-08)
mat1.add_nuclide("U238", 6.693800e-04)
mat1.add_nuclide("H1", 5.944000e-02)
mat1.add_element("N", 1.996300e-03)
mat1.add_nuclide("O16", 3.694600e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Air
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("N", 3.901400e-05)
mat2.add_nuclide("O16", 1.041000e-05)

# SST
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 7.156700e-05)
mat3.add_element("Si", 8.416700e-04)
mat3.add_element("Mn", 7.432100e-04)
mat3.add_element("P", 4.471200e-05)
mat3.add_element("S", 5.956400e-06)
mat3.add_element("Ni", 7.424900e-03)
mat3.add_element("Cr", 1.671600e-02)
mat3.add_element("Fe", 6.094700e-02)

# SST
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 2.067500e-05)
mat4.add_element("Si", 6.631400e-04)
mat4.add_element("Mn", 1.008300e-04)
mat4.add_element("P", 4.933700e-05)
mat4.add_element("S", 1.638000e-06)
mat4.add_element("Ni", 6.688500e-03)
mat4.add_element("Cr", 1.679800e-02)
mat4.add_element("Fe", 6.143500e-02)

# Zr-4
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 7.889600e-05)
mat5.add_element("Fe", 1.398500e-04)
mat5.add_element("Zr", 4.239700e-02)
mat5.add_element("Sn", 4.970900e-04)
mat5.add_nuclide("O16", 3.698100e-04)

# Aluminum
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Al", 5.955900e-02)
mat6.add_element("Si", 8.075100e-05)
mat6.add_element("Fe", 1.711400e-04)
mat6.add_element("Cu", 1.784500e-05)

# Concrete
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("H1", 1.452800e-02)
mat7.add_nuclide("O16", 7.263900e-03)
mat7.add_nuclide("O16", 3.732600e-02)
mat7.add_element("Na", 1.053300e-03)
mat7.add_element("Mg", 1.957300e-04)
mat7.add_element("Al", 1.553300e-03)
mat7.add_element("Si", 1.474900e-02)
mat7.add_element("S", 1.090600e-04)
mat7.add_element("Cl", 9.002700e-07)
mat7.add_element("K", 1.917900e-04)
mat7.add_element("Ca", 3.933700e-03)
mat7.add_element("Fe", 2.783000e-04)
mat7.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Zr-4 plate
surf1 = openmc.model.RectangularParallelepiped(3.9395, 4.5605, -34.5695, 34.5695, 10.0, 140.0)
# Zr-4 plate
surf2 = openmc.model.RectangularParallelepiped(-4.5605, -3.9395, -34.5695, 34.5695, 10.0, 140.0)
# SST tank, inner
surf3 = openmc.model.RectangularParallelepiped(-17.3275, 17.3275, -34.5695, 34.5695, 0.0, 149.578)
# SST tank, outer
surf4 = openmc.model.RectangularParallelepiped(-19.3105, 19.3105, -36.6005, 36.6005, -2.060999999999993, 152.183)
# Critical height
surf5 = openmc.ZPlane(surface_id=5, z0=66.04)
# Concrete
surf6 = openmc.model.RectangularParallelepiped(-7.5, 7.5, -35.7, 35.7, 0.0, 150.6)
# SST frame
surf7 = openmc.model.RectangularParallelepiped(-7.5, 7.5, -38.7, 38.7, -3.0, 153.6)
# Aluminum cover
surf8 = openmc.model.RectangularParallelepiped(-8.31, 8.31, -38.7, 38.7, -3.0, 153.6)
# Concrete
surf16 = openmc.model.RectangularParallelepiped(-2.505, 2.505, -35.7, 35.7, 0.0, 150.6)
# SST frame
surf17 = openmc.model.RectangularParallelepiped(-2.505, 2.505, -38.7, 38.7, -3.0, 153.6)
# Aluminum cover
surf18 = openmc.model.RectangularParallelepiped(-3.315, 3.315, -38.7, 38.7, -3.0, 153.6)
# Concrete
surf26 = openmc.model.RectangularParallelepiped(-5.035, 5.035, -35.7, 35.7, 0.0, 150.6)
# SST frame
surf27 = openmc.model.RectangularParallelepiped(-5.035, 5.035, -38.7, 38.7, -3.0, 153.6)
# Aluminum cover
surf28 = openmc.model.RectangularParallelepiped(-5.845, 5.845, -38.7, 38.7, -3.0, 153.6)
# Concrete
surf36 = openmc.model.RectangularParallelepiped(-3.775, 3.775, -35.7, 35.7, 0.0, 150.6)
# SST frame
surf37 = openmc.model.RectangularParallelepiped(-3.775, 3.775, -38.7, 38.7, -3.0, 153.6)
# Aluminum cover
surf38 = openmc.model.RectangularParallelepiped(-4.585, 4.585, -38.7, 38.7, -3.0, 153.6)
# Concrete
surf46 = openmc.model.RectangularParallelepiped(-1.265, 1.265, -35.7, 35.7, 0.0, 150.6)
# SST frame
surf47 = openmc.model.RectangularParallelepiped(-1.265, 1.265, -38.7, 38.7, -3.0, 153.6)
# Aluminum cover
surf48 = openmc.model.RectangularParallelepiped(-2.075, 2.075, -38.7, 38.7, -3.0, 153.6)
# BCD
surf50 = openmc.model.RectangularParallelepiped(-75.985, 75.985, -38.7, 38.7, -3.0, 153.6, boundary_type="vacuum")
# LHS SST tank
surf51 = openmc.model.RectangularParallelepiped(-75.985, -37.364000000000004, -36.6005, 36.6005, -2.060999999999993, 152.183)
# C150 isolator
surf52 = openmc.model.RectangularParallelepiped(-37.202, -20.582, -38.7, 38.7, -3.0, 153.6)
# C50 isolator
surf53 = openmc.model.RectangularParallelepiped(-20.42, -13.790000000000001, -38.7, 38.7, -3.0, 153.6)
# C100 isolator
surf54 = openmc.model.RectangularParallelepiped(-13.628, -1.9380000000000006, -38.7, 38.7, -3.0, 153.6)
# C75 isolator
surf55 = openmc.model.RectangularParallelepiped(-1.7759999999999998, 7.394, -38.7, 38.7, -3.0, 153.6)
# C25 isolator
surf56 = openmc.model.RectangularParallelepiped(7.556, 11.706, -38.7, 38.7, -3.0, 153.6)
# C25B isolator
surf57 = openmc.model.RectangularParallelepiped(11.867999999999999, 16.018, -38.7, 38.7, -3.0, 153.6)
# C75B isolator
surf58 = openmc.model.RectangularParallelepiped(16.18, 25.35, -38.7, 38.7, -3.0, 153.6)
# C100B isolator
surf59 = openmc.model.RectangularParallelepiped(25.512, 37.202, -38.7, 38.7, -3.0, 153.6)
# RHS SST tank
surf60 = openmc.model.RectangularParallelepiped(37.364000000000004, 75.985, -36.6005, 36.6005, -2.060999999999993, 152.183)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat5)
u1_cell0.region = -surf1
u1_cell1 = openmc.Cell(fill=mat5)
u1_cell1.region = -surf2
u1_cell2 = openmc.Cell(fill=mat1)
u1_cell2.region = +surf1 & +surf2 & -surf3 & -surf5
u1_cell3 = openmc.Cell(fill=mat2)
u1_cell3.region = +surf1 & +surf2 & -surf3 & +surf5
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = +surf3 & -surf4
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat7)
u2_cell0.region = -surf6
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = +surf6 & -surf7
u2_cell2 = openmc.Cell(fill=mat6)
u2_cell2.region = +surf6 & +surf7 & -surf8
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

u3_cell0 = openmc.Cell(fill=mat7)
u3_cell0.region = -surf16
u3_cell1 = openmc.Cell(fill=mat4)
u3_cell1.region = +surf16 & -surf17
u3_cell2 = openmc.Cell(fill=mat6)
u3_cell2.region = +surf16 & +surf17 & -surf18
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2])

u4_cell0 = openmc.Cell(fill=mat7)
u4_cell0.region = -surf26
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = +surf26 & -surf27
u4_cell2 = openmc.Cell(fill=mat6)
u4_cell2.region = +surf26 & +surf27 & -surf28
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2])

u5_cell0 = openmc.Cell(fill=mat7)
u5_cell0.region = -surf36
u5_cell1 = openmc.Cell(fill=mat4)
u5_cell1.region = +surf36 & -surf37
u5_cell2 = openmc.Cell(fill=mat6)
u5_cell2.region = +surf36 & +surf37 & -surf38
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0, u5_cell1, u5_cell2])

u6_cell0 = openmc.Cell(fill=mat7)
u6_cell0.region = -surf46
u6_cell1 = openmc.Cell(fill=mat4)
u6_cell1.region = +surf46 & -surf47
u6_cell2 = openmc.Cell(fill=mat6)
u6_cell2.region = +surf46 & +surf47 & -surf48
universe6 = openmc.Universe(universe_id=6, cells=[u6_cell0, u6_cell1, u6_cell2])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# tank
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.translation = (-56.6745, 0.0, 0.0)
cell1.region = -surf50 & -surf51

# C150
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.translation = (-28.892, 0.0, 0.0)
cell2.region = -surf50 & -surf52

# C150
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.translation = (-17.105, 0.0, 0.0)
cell3.region = -surf50 & -surf53

# C100
cell4 = openmc.Cell(cell_id=4, fill=universe4)
cell4.translation = (-7.783, 0.0, 0.0)
cell4.region = -surf50 & -surf54

# C75
cell5 = openmc.Cell(cell_id=5, fill=universe5)
cell5.translation = (2.809, 0.0, 0.0)
cell5.region = -surf50 & -surf55

# C25
cell6 = openmc.Cell(cell_id=6, fill=universe6)
cell6.translation = (9.631, 0.0, 0.0)
cell6.region = -surf50 & -surf56

# C25B
cell7 = openmc.Cell(cell_id=7, fill=universe6)
cell7.translation = (13.943, 0.0, 0.0)
cell7.region = -surf50 & -surf57

# C75B
cell8 = openmc.Cell(cell_id=8, fill=universe5)
cell8.translation = (20.765, 0.0, 0.0)
cell8.region = -surf50 & -surf58

# C100B
cell9 = openmc.Cell(cell_id=9, fill=universe4)
cell9.translation = (31.357, 0.0, 0.0)
cell9.region = -surf50 & -surf59

# tank
cell10 = openmc.Cell(cell_id=10, fill=universe1)
cell10.translation = (56.6745, 0.0, 0.0)
cell10.region = -surf50 & -surf60

# air
cell11 = openmc.Cell(cell_id=11, fill=mat2)
cell11.region = -surf50 & +surf51 & +surf52 & +surf53 & +surf54 & +surf55 & +surf56 & +surf57 & +surf58 & +surf59 & +surf60

# SST
cell17 = openmc.Cell(cell_id=17, fill=mat3)
cell17.region = +surf3 & -surf4

# Al
cell21 = openmc.Cell(cell_id=21, fill=mat6)
cell21.region = +surf6 & +surf7 & -surf8

# Al
cell25 = openmc.Cell(cell_id=25, fill=mat6)
cell25.region = +surf16 & +surf17 & -surf18

# Al
cell29 = openmc.Cell(cell_id=29, fill=mat6)
cell29.region = +surf26 & +surf27 & -surf28

# Al
cell33 = openmc.Cell(cell_id=33, fill=mat6)
cell33.region = +surf36 & +surf37 & -surf38

# Al
cell37 = openmc.Cell(cell_id=37, fill=mat6)
cell37.region = +surf46 & +surf47 & -surf48

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell17, cell21, cell25, cell29, cell33, cell37])
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
source.space = openmc.stats.Box((-57.6745, -1.0, 32.02), (57.6745, 1.0, 34.02))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
