"""
LCT043-1: Array of U(4.3486)O2 fuel rods with 1.5 cm square pitch in water next to 9.632 cm SST plate
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# UO2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 7.845600e-06)
mat1.add_nuclide("U235", 9.991600e-04)
mat1.add_nuclide("U238", 2.169200e-02)
mat1.add_nuclide("O16", 4.546800e-02)
mat1.add_nuclide("O17", 1.728400e-05)

# Cladding and
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.900200e-02)
mat2.add_element("Ni", 8.162500e-03)
mat2.add_element("Cr", 1.682400e-02)
mat2.add_element("Mn", 1.464500e-03)
mat2.add_element("Si", 6.793400e-04)
mat2.add_element("P", 4.004000e-05)
mat2.add_element("C", 1.123900e-04)
mat2.add_element("S", 1.561700e-05)
mat2.add_element("Co", 1.740200e-04)
mat2.add_element("Mo", 8.452000e-05)

# Alumina
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 4.474400e-02)
mat3.add_nuclide("O16", 6.709100e-02)
mat3.add_nuclide("O17", 2.550400e-05)

# Spacer
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Mn", 1.158100e-03)
mat4.add_element("Si", 1.115500e-03)
mat4.add_element("Ni", 6.570200e-03)
mat4.add_element("Cr", 1.677900e-02)
mat4.add_element("Fe", 6.189200e-02)
mat4.add_element("C", 2.407800e-04)
mat4.add_element("P", 3.112400e-05)
mat4.add_element("Co", 1.145000e-04)

# Control rod
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Ag", 4.432500e-02)
mat5.add_element("In", 7.851700e-03)
mat5.add_element("Cd", 2.589400e-03)
mat5.add_element("C", 1.505200e-03)
mat5.add_element("S", 1.879100e-04)
mat5.add_nuclide("O16", 1.769600e-03)
mat5.add_nuclide("O17", 6.727100e-07)

# Guide
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 5.694300e-02)
mat6.add_element("C", 8.896800e-05)
mat6.add_element("Cr", 1.629800e-02)
mat6.add_element("Ni", 9.103700e-03)
mat6.add_element("Mn", 1.150100e-03)
mat6.add_element("P", 4.500000e-06)
mat6.add_element("Si", 6.617000e-04)

# Gadolinia
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Gd", 6.875600e-03)
mat7.add_nuclide("O16", 1.030900e-02)
mat7.add_nuclide("O17", 3.918900e-06)

# Grid
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("C", 7.942600e-05)
mat8.add_element("Mn", 1.250300e-03)
mat8.add_element("P", 5.544000e-05)
mat8.add_element("S", 4.462000e-06)
mat8.add_element("Si", 8.661600e-04)
mat8.add_element("Ni", 7.664100e-03)
mat8.add_element("Cr", 1.670500e-02)
mat8.add_element("Mo", 2.983100e-05)
mat8.add_element("Fe", 6.003600e-02)

# SST
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("C", 1.809000e-04)
mat9.add_element("Mn", 1.039200e-03)
mat9.add_element("S", 1.081600e-05)
mat9.add_element("Si", 6.964400e-04)
mat9.add_element("Ni", 6.567000e-03)
mat9.add_element("Cr", 1.759500e-02)
mat9.add_element("Mo", 2.109100e-05)
mat9.add_element("Fe", 6.003600e-02)
mat9.add_element("Cu", 1.667900e-05)
mat9.add_element("Ti", 2.409800e-06)

# Water
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("H1", 6.673600e-02)
mat10.add_nuclide("O16", 3.335500e-02)
mat10.add_nuclide("O17", 1.268000e-05)
mat10.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10])

# ==============================================================================
# Geometry
# ==============================================================================

# Array boundary
surf1 = openmc.model.RectangularParallelepiped(-21.75, 21.75, -22.5, 22.5, -9.099999999999998, 71.2)
# Bottom grid plate
surf2 = openmc.model.RectangularParallelepiped(-29.4, 29.4, -29.4, 29.4, -11.299999999999999, -9.1)
# SST plates
surf3 = openmc.model.RectangularParallelepiped(-31.672369999999997, -22.04037, -25.4, 25.4, -4.949999999999999, 66.55)
# Boundary condition
surf4 = openmc.ZCylinder(surface_id=4, r=100.0)
# Al2O3
surf11 = openmc.ZCylinder(surface_id=11, r=0.4235)
# UO2
surf12 = openmc.ZCylinder(surface_id=12, r=0.42447)
# Al2O3
surf13 = openmc.ZCylinder(surface_id=13, r=0.4235)
# Spacer tube, inner
surf14 = openmc.ZCylinder(surface_id=14, r=0.365)
# Spacer tube, outer
surf15 = openmc.ZCylinder(surface_id=15, r=0.425)
# Clad, inner
surf16 = openmc.ZCylinder(surface_id=16, r=0.42873)
# Clad, outer
surf17 = openmc.ZCylinder(surface_id=17, r=0.49037)
# Ag-In-Cd
surf21 = openmc.ZCylinder(surface_id=21, r=0.416)
# Clad, inner
surf22 = openmc.ZCylinder(surface_id=22, r=0.42873)
# Clad, outer
surf23 = openmc.ZCylinder(surface_id=23, r=0.49037)
# Guide tube, inner
surf24 = openmc.ZCylinder(surface_id=24, r=0.565)
# Guide tube, outer
surf25 = openmc.ZCylinder(surface_id=25, r=0.6)

# Z-plane surfaces for bounded cylinders
surf4_zmin = openmc.ZPlane(z0=-41.3, boundary_type="vacuum")
surf4_zmax = openmc.ZPlane(z0=71.2, boundary_type="vacuum")
surf11_zmin = openmc.ZPlane(z0=-9.1)
surf11_zmax = openmc.ZPlane(z0=0.0)
surf12_zmin = openmc.ZPlane(z0=0.0)
surf12_zmax = openmc.ZPlane(z0=58.84)
surf13_zmin = openmc.ZPlane(z0=54.84)
surf13_zmax = openmc.ZPlane(z0=60.24)
surf15_zmin = openmc.ZPlane(z0=60.24)
surf15_zmax = openmc.ZPlane(z0=71.2)
surf17_zmin = openmc.ZPlane(z0=-9.1)
surf17_zmax = openmc.ZPlane(z0=71.2)
surf21_zmin = openmc.ZPlane(z0=54.84)
surf21_zmax = openmc.ZPlane(z0=71.2)
surf22_zmin = openmc.ZPlane(z0=54.84)
surf22_zmax = openmc.ZPlane(z0=71.2)
surf23_zmin = openmc.ZPlane(z0=53.17)
surf23_zmax = openmc.ZPlane(z0=71.2)
surf25_zmin = openmc.ZPlane(z0=-9.1)
surf25_zmax = openmc.ZPlane(z0=71.2)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax)
u1_cell1 = openmc.Cell(fill=mat1)
u1_cell1.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = (+surf13 | -surf13_zmin | +surf13_zmax) & +surf14 & (-surf15 & +surf15_zmin & -surf15_zmax)
u1_cell4 = openmc.Cell(fill=mat2)
u1_cell4.region = +surf16 & (-surf17 & +surf17_zmin & -surf17_zmax)
u1_cell5 = openmc.Cell(fill=mat10)
u1_cell5.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = (-surf21 & +surf21_zmin & -surf21_zmax)
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = (+surf21 | -surf21_zmin | +surf21_zmax) & (+surf22 | -surf22_zmin | +surf22_zmax) & (-surf23 & +surf23_zmin & -surf23_zmax)
u2_cell2 = openmc.Cell(fill=mat10)
u2_cell2.region = (+surf23 | -surf23_zmin | +surf23_zmax) & -surf24 & (-surf25 & +surf25_zmin & -surf25_zmax)
u2_cell3 = openmc.Cell(fill=mat6)
u2_cell3.region = +surf24 & (-surf25 & +surf25_zmin & -surf25_zmax)
u2_cell4 = openmc.Cell(fill=mat10)
u2_cell4.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf25 | -surf25_zmin | +surf25_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

u3_cell0 = openmc.Cell(fill=mat10)
u3_cell0.region = -surf24 & (-surf25 & +surf25_zmin & -surf25_zmax)
u3_cell1 = openmc.Cell(fill=mat6)
u3_cell1.region = +surf24 & (-surf25 & +surf25_zmin & -surf25_zmax)
u3_cell2 = openmc.Cell(fill=mat10)
u3_cell2.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf25 | -surf25_zmin | +surf25_zmax)
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2])

u4_cell0 = openmc.Cell(fill=mat7)
u4_cell0.region = -surf16 & (-surf17 & +surf17_zmin & -surf17_zmax)
u4_cell1 = openmc.Cell(fill=mat6)
u4_cell1.region = +surf16 & (-surf17 & +surf17_zmin & -surf17_zmax)
u4_cell2 = openmc.Cell(fill=mat10)
u4_cell2.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2])

u5_cell0 = openmc.Cell(fill=mat10)
u5_cell0.region = (-surf4 & +surf4_zmin & -surf4_zmax)
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0])

# Lattice 6: 29x30 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-21.75, -22.5]
lattice6.pitch = [1.500000, 1.500000]
lattice6.universes = [
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5, universe5, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5, universe5, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe5, universe5, universe5, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe4, universe1, universe1, universe4, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe1, universe1, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe1, universe1, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe4, universe1, universe1, universe4, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe5, universe5, universe5, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5, universe5, universe5],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe6)
cell1.region = -surf1

# Grid
cell2 = openmc.Cell(cell_id=2, fill=mat8)
cell2.region = -surf2

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat9)
cell3.region = +surf1 & +surf2 & -surf3

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat10)
cell4.region = +surf1 & +surf2 & +surf3 & (-surf4 & +surf4_zmin & -surf4_zmax)

# Water
cell11 = openmc.Cell(cell_id=11, fill=mat10)
cell11.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)

# Water
cell17 = openmc.Cell(cell_id=17, fill=mat10)
cell17.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf25 | -surf25_zmin | +surf25_zmax)

# Water
cell21 = openmc.Cell(cell_id=21, fill=mat10)
cell21.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf25 | -surf25_zmin | +surf25_zmax)

# Water
cell25 = openmc.Cell(cell_id=25, fill=mat10)
cell25.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)

# Water
cell27 = openmc.Cell(cell_id=27, fill=mat10)
cell27.region = (-surf4 & +surf4_zmin & -surf4_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell11, cell17, cell21, cell25, cell27])
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
source.space = openmc.stats.Box((-2.5, -1.75, 26.42), (1.0, 1.75, 28.42))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
