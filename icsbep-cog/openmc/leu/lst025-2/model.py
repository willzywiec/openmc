"""
LST025-2: STACY two slabs of 10% 235U uranyl nitrate with concrete (C50) isolators
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Fuel
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 5.990200e-07)
mat1.add_nuclide("U235", 7.433400e-05)
mat1.add_nuclide("U236", 7.424100e-08)
mat1.add_nuclide("U238", 6.621000e-04)
mat1.add_nuclide("H1", 5.947400e-02)
mat1.add_element("N", 1.980100e-03)
mat1.add_nuclide("O16", 3.689800e-02)
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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Zr-4 plate
surf1 = openmc.model.RectangularParallelepiped(3.9395, 4.5605, -34.5695, 34.5695, 10.0, 140.0)
# Zr-4 plate
surf2 = openmc.model.RectangularParallelepiped(-4.5605, -3.9395, -34.5695, 34.5695, 10.0, 140.0)
# SST tank, inner
surf3 = openmc.model.RectangularParallelepiped(-17.3275, 17.3275, -34.5695, 34.5695, 0.0, 149.578)
# SST tank, outer
surf4 = openmc.model.RectangularParallelepiped(-19.3105, 19.3105, -36.6005, 36.6005, -2.060999999999993, 152.183)
# Critical height
surf5 = openmc.ZPlane(surface_id=5, z0=55.38)
# Concrete
surf6 = openmc.model.RectangularParallelepiped(-2.505, 2.505, -35.7, 35.7, 0.0, 150.6)
# SST frame
surf7 = openmc.model.RectangularParallelepiped(-2.505, 2.505, -38.7, 38.7, -3.0, 153.6)
# Aluminum cover
surf8 = openmc.model.RectangularParallelepiped(-3.315, 3.315, -38.7, 38.7, -3.0, 153.6)
# BCD
surf10 = openmc.model.RectangularParallelepiped(-42.0, 42.0, -38.7, 38.7, -3.0, 153.6, boundary_type="vacuum")
# LHS SST tank
surf11 = openmc.model.RectangularParallelepiped(-42.0, -3.378999999999998, -36.6005, 36.6005, -2.060999999999993, 152.183)
# RHS SST tank
surf12 = openmc.model.RectangularParallelepiped(3.378999999999998, 42.0, -36.6005, 36.6005, -2.060999999999993, 152.183)

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

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# tank
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.translation = (-22.6895, 0.0, 0.0)
cell1.region = -surf10 & -surf11

# iso
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.translation = (0.0, 0.0, 0.0)
cell2.region = -surf10 & -surf8

# tank
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (22.6895, 0.0, 0.0)
cell3.region = -surf10 & -surf12

# air
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = -surf10 & +surf8 & +surf11 & +surf12

# SST
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = +surf3 & -surf4

# Al
cell14 = openmc.Cell(cell_id=14, fill=mat6)
cell14.region = +surf6 & +surf7 & -surf8

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell10, cell14])
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
source.space = openmc.stats.Box((-23.6895, -1.0, 26.69), (23.6895, 1.0, 28.69))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
