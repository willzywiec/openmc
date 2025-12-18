"""
MIX-MET-FAST-008-3: ZEBRA-8C (in IRPhE: ZEBRA-FUND-RESR-001)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu Metal
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.609400e-02)
mat1.add_nuclide("Pu240", 1.869300e-03)
mat1.add_nuclide("Pu241", 1.117500e-04)
mat1.add_element("C", 1.043700e-04)
mat1.add_element("Fe", 2.244700e-05)
mat1.add_element("Ni", 2.136000e-05)
mat1.add_element("Al", 4.645900e-05)
mat1.add_nuclide("H1", 1.566100e-04)
mat1.add_element("Ga", 2.347000e-03)
mat1.add_element("Si", 4.463300e-05)
mat1.add_nuclide("Np237", 1.242000e-05)
mat1.add_nuclide("Am241", 3.489900e-05)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Clad
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 1.644400e-04)
mat2.add_element("Fe", 3.602100e-02)
mat2.add_element("Cr", 9.848100e-03)
mat2.add_element("Mn", 4.830000e-04)
mat2.add_element("Ni", 4.429900e-03)
mat2.add_nuclide("H1", 1.527900e-05)
mat2.add_element("Si", 3.417600e-04)
mat2.add_element("P", 1.827300e-05)
mat2.add_element("S", 1.765100e-05)
mat2.add_element("Cu", 1.616600e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

# Graphite
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 8.060300e-02)
mat3.add_nuclide("O16", 1.403900e-04)
mat3.add_element("Na", 2.915800e-06)
mat3.add_element("Fe", 6.923800e-06)
mat3.add_nuclide("B10", 1.940500e-07)
mat3.add_nuclide("B11", 5.294600e-07)
mat3.add_element("Cu", 3.057600e-07)
mat3.add_element("Mn", 2.652500e-07)
mat3.add_element("Al", 1.800300e-06)
mat3.add_nuclide("H1", 2.978300e-04)
mat3.add_element("Si", 6.883500e-06)
mat3.add_element("Ca", 1.478600e-06)
mat3.add_element("V", 1.907100e-07)
mat3.add_element("S", 1.514900e-07)
mat3.add_element("Zn", 7.427700e-08)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Nat-U Metal
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U235", 3.331700e-04)
mat4.add_nuclide("U238", 4.594900e-02)
mat4.add_element("C", 4.924100e-04)
mat4.add_element("Fe", 1.059100e-04)
mat4.add_nuclide("H1", 4.378900e-05)
mat4.add_element("Si", 2.105800e-04)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Bright Stainless
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 7.806300e-04)
mat5.add_element("Fe", 5.828600e-02)
mat5.add_element("Cr", 1.633100e-02)
mat5.add_element("Cu", 7.388500e-05)
mat5.add_element("Mo", 9.773800e-05)
mat5.add_element("Mn", 9.392200e-04)
mat5.add_element("Ni", 7.751600e-03)
mat5.add_element("Al", 1.740100e-04)
mat5.add_element("Ti", 2.939900e-04)
mat5.add_nuclide("H1", 2.326700e-05)
mat5.add_element("Si", 1.336000e-03)
mat5.add_s_alpha_beta("c_H_in_H2O")

# Dull Stainless
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("C", 7.762500e-04)
mat6.add_element("Fe", 5.790200e-02)
mat6.add_element("Cr", 1.622400e-02)
mat6.add_element("Cu", 7.332400e-05)
mat6.add_element("Mo", 9.709300e-05)
mat6.add_element("Mn", 9.329400e-04)
mat6.add_element("Ni", 7.700600e-03)
mat6.add_element("Al", 1.726900e-04)
mat6.add_element("Ti", 2.920500e-04)
mat6.add_nuclide("H1", 2.311400e-05)
mat6.add_element("Si", 1.327400e-03)
mat6.add_s_alpha_beta("c_H_in_H2O")

# Sheath
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("C", 7.781500e-04)
mat7.add_element("Fe", 5.662600e-02)
mat7.add_element("Cr", 1.610700e-02)
mat7.add_element("Cu", 7.383500e-05)
mat7.add_element("Mo", 1.463900e-04)
mat7.add_element("Mn", 1.191700e-03)
mat7.add_element("Ni", 9.004200e-03)
mat7.add_element("Al", 3.464000e-04)
mat7.add_element("Ti", 2.933100e-04)
mat7.add_nuclide("H1", 2.320500e-05)
mat7.add_element("Si", 9.998500e-04)
mat7.add_element("V", 9.210400e-05)
mat7.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.model.RectangularParallelepiped(-2.3355, 2.3355, -2.3355, 2.3355, 3.8817, 4.0976)
surf2 = openmc.model.RectangularParallelepiped(-2.5335, 2.5335, -2.5335, 2.5335, -49.95, 49.95)
surf3 = openmc.model.RectangularParallelepiped(-2.551, 2.551, -2.551, 2.551, -49.95, 49.95)
surf4 = openmc.model.RectangularParallelepiped(-2.6272, 2.6272, -2.6272, 2.6272, -49.95, 49.95, boundary_type="reflecting")
surf5 = openmc.ZPlane(surface_id=5, z0=0.0, boundary_type="periodic")
surf6 = openmc.ZPlane(surface_id=6, z0=0.9525)
surf7 = openmc.ZPlane(surface_id=7, z0=1.2697)
surf8 = openmc.ZPlane(surface_id=8, z0=1.5933)
surf9 = openmc.ZPlane(surface_id=9, z0=1.9105)
surf10 = openmc.ZPlane(surface_id=10, z0=2.2341)
surf11 = openmc.ZPlane(surface_id=11, z0=2.5513)
surf12 = openmc.ZPlane(surface_id=12, z0=2.8749)
surf13 = openmc.ZPlane(surface_id=13, z0=3.1921)
surf14 = openmc.ZPlane(surface_id=14, z0=3.5157)
surf15 = openmc.ZPlane(surface_id=15, z0=3.8309)
surf16 = openmc.ZPlane(surface_id=16, z0=4.1484)
surf17 = openmc.ZPlane(surface_id=17, z0=4.4636)
surf18 = openmc.ZPlane(surface_id=18, z0=4.7872)
surf19 = openmc.ZPlane(surface_id=19, z0=5.1044)
surf20 = openmc.ZPlane(surface_id=20, z0=5.4280)
surf21 = openmc.ZPlane(surface_id=21, z0=5.7452)
surf22 = openmc.ZPlane(surface_id=22, z0=6.0688)
surf23 = openmc.ZPlane(surface_id=23, z0=6.3860)
surf24 = openmc.ZPlane(surface_id=24, z0=6.7096)
surf25 = openmc.ZPlane(surface_id=25, z0=7.6621, boundary_type="periodic")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Nat-U
cell1 = openmc.Cell(cell_id=1, fill=mat4)
cell1.region = -surf2 & +surf24 & -surf25

# Dull
cell2 = openmc.Cell(cell_id=2, fill=mat6)
cell2.region = -surf2 & +surf23 & -surf24

# Bright
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = -surf2 & +surf22 & -surf23

# Dull
cell4 = openmc.Cell(cell_id=4, fill=mat6)
cell4.region = -surf2 & +surf21 & -surf22

# Bright
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = -surf2 & +surf20 & -surf21

# Dull
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = -surf2 & +surf19 & -surf20

# Bright
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = -surf2 & +surf18 & -surf19

# Dull
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = -surf2 & +surf17 & -surf18

# C
cell9 = openmc.Cell(cell_id=9, fill=mat3)
cell9.region = -surf2 & +surf16 & -surf17

# PU
cell10 = openmc.Cell(cell_id=10, fill=mat1)
cell10.region = -surf1

# Clad
cell11 = openmc.Cell(cell_id=11, fill=mat2)
cell11.region = +surf1 & -surf2 & +surf15 & -surf16

# C
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = -surf2 & +surf14 & -surf15

# Dull
cell13 = openmc.Cell(cell_id=13, fill=mat6)
cell13.region = -surf2 & +surf13 & -surf14

# Bright
cell14 = openmc.Cell(cell_id=14, fill=mat5)
cell14.region = -surf2 & +surf12 & -surf13

# Dull
cell15 = openmc.Cell(cell_id=15, fill=mat6)
cell15.region = -surf2 & +surf11 & -surf12

# Bright
cell16 = openmc.Cell(cell_id=16, fill=mat5)
cell16.region = -surf2 & +surf10 & -surf11

# Dull
cell17 = openmc.Cell(cell_id=17, fill=mat6)
cell17.region = -surf2 & +surf9 & -surf10

# Bright
cell18 = openmc.Cell(cell_id=18, fill=mat5)
cell18.region = -surf2 & +surf8 & -surf9

# Dull
cell19 = openmc.Cell(cell_id=19, fill=mat6)
cell19.region = -surf2 & +surf7 & -surf8

# Bright
cell20 = openmc.Cell(cell_id=20, fill=mat5)
cell20.region = -surf2 & +surf6 & -surf7

# Nat-U
cell21 = openmc.Cell(cell_id=21, fill=mat4)
cell21.region = -surf2 & +surf5 & -surf6

# Sheath
cell22 = openmc.Cell(cell_id=22, fill=mat7)
cell22.region = +surf3 & -surf4 & +surf5 & -surf25

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22])
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
source.space = openmc.stats.Point((0.0, 0.0, 3.98965))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
