"""
MIX-MET-FAST-008-1: ZEBRA-8A (in IRPhE: ZEBRA-FUND-RESR-001)
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

# Sheath
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 7.781500e-04)
mat5.add_element("Fe", 5.662600e-02)
mat5.add_element("Cr", 1.610700e-02)
mat5.add_element("Cu", 7.383500e-05)
mat5.add_element("Mo", 1.463900e-04)
mat5.add_element("Mn", 1.191700e-03)
mat5.add_element("Ni", 9.004200e-03)
mat5.add_element("Al", 3.464000e-04)
mat5.add_element("Ti", 2.933100e-04)
mat5.add_nuclide("H1", 2.320500e-05)
mat5.add_element("Si", 9.998500e-04)
mat5.add_element("V", 9.210400e-05)
mat5.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.model.RectangularParallelepiped(-2.3355, 2.3355, -2.3355, 2.3355, 3.5248999999999997, 3.7408)
surf2 = openmc.model.RectangularParallelepiped(-2.5335, 2.5335, -2.5335, 2.5335, -49.95, 49.95)
surf3 = openmc.model.RectangularParallelepiped(-2.551, 2.551, -2.551, 2.551, -49.95, 49.95)
surf4 = openmc.model.RectangularParallelepiped(-2.6272, 2.6272, -2.6272, 2.6272, -49.95, 49.95, boundary_type="reflecting")
surf5 = openmc.ZPlane(surface_id=5, z0=0.0, boundary_type="periodic")
surf6 = openmc.ZPlane(surface_id=6, z0=0.9525)
surf7 = openmc.ZPlane(surface_id=7, z0=3.4741)
surf8 = openmc.ZPlane(surface_id=8, z0=3.7916)
surf9 = openmc.ZPlane(surface_id=9, z0=5.9980)
surf10 = openmc.ZPlane(surface_id=10, z0=7.5855, boundary_type="periodic")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Nat-U
cell1 = openmc.Cell(cell_id=1, fill=mat4)
cell1.region = -surf2 & +surf9 & -surf10

# C
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = -surf2 & +surf8 & -surf9

# PU
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = -surf1

# Clad
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf1 & -surf2 & +surf7 & -surf8

# C
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = -surf2 & +surf6 & -surf7

# Nat-U
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = -surf2 & +surf5 & -surf6

# Sheath
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = +surf3 & -surf4 & +surf5 & -surf10

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7])
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
source.space = openmc.stats.Point((0.0, 0.0, 3.63285))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
