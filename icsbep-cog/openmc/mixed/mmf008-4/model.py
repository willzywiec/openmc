"""
MIX-MET-FAST-008-4: ZEBRA-8D (in IRPhE: ZEBRA-FUND-RESR-001)
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

# Clad - Pu
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

# Sodium (Na)
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("O16", 1.993700e-06)
mat5.add_element("Na", 2.311900e-02)
mat5.add_element("Fe", 3.808000e-08)
mat5.add_nuclide("B10", 5.309500e-08)
mat5.add_nuclide("B11", 9.657900e-08)
mat5.add_nuclide("H1", 2.109800e-06)
mat5.add_element("K", 4.759100e-07)
mat5.add_element("Ca", 1.724400e-06)
mat5.add_nuclide("Li7", 3.788700e-07)
mat5.add_s_alpha_beta("c_H_in_H2O")

# Clad - Na
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("C", 2.342600e-04)
mat6.add_element("Fe", 5.851200e-02)
mat6.add_element("Cr", 1.622700e-02)
mat6.add_element("Mn", 1.169500e-03)
mat6.add_element("Ni", 7.847600e-03)
mat6.add_nuclide("H1", 2.326300e-05)
mat6.add_element("Nb", 3.281500e-04)
mat6.add_element("Si", 6.512000e-04)
mat6.add_element("P", 3.028100e-05)
mat6.add_element("S", 2.925100e-05)
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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Na
surf1 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 1.3068300000000002, 1.84917)
# Na
surf2 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 2.5532299999999997, 3.09557)
# Pu
surf3 = openmc.model.RectangularParallelepiped(-2.3355, 2.3355, -2.3355, 2.3355, 3.1832, 3.3991000000000002)
# Na
surf4 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 3.4867299999999997, 4.02907)
# Na
surf5 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 4.73313, 5.275469999999999)
# Na clad
surf6 = openmc.model.RectangularParallelepiped(-2.5185, 2.5185, -2.5185, 2.5185, -49.95, 49.95)
# Pu clad, C, Nat-U
surf7 = openmc.model.RectangularParallelepiped(-2.5335, 2.5335, -2.5335, 2.5335, -49.95, 49.95)
# Sheath, inner
surf8 = openmc.model.RectangularParallelepiped(-2.551, 2.551, -2.551, 2.551, -49.95, 49.95)
# Sheath, outer
surf9 = openmc.model.RectangularParallelepiped(-2.6272, 2.6272, -2.6272, 2.6272, -49.95, 49.95, boundary_type="reflecting")
surf10 = openmc.ZPlane(surface_id=10, z0=0.0, boundary_type="periodic")
surf11 = openmc.ZPlane(surface_id=11, z0=1.2700)
surf12 = openmc.ZPlane(surface_id=12, z0=1.8860)
surf13 = openmc.ZPlane(surface_id=13, z0=2.5164)
surf14 = openmc.ZPlane(surface_id=14, z0=3.1324)
surf15 = openmc.ZPlane(surface_id=15, z0=3.4499)
surf16 = openmc.ZPlane(surface_id=16, z0=4.0659)
surf17 = openmc.ZPlane(surface_id=17, z0=4.6963)
surf18 = openmc.ZPlane(surface_id=18, z0=5.3123)
surf19 = openmc.ZPlane(surface_id=19, z0=6.8998, boundary_type="periodic")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Na
cell1 = openmc.Cell(cell_id=1, fill=mat5)
cell1.region = -surf5

# Na
cell2 = openmc.Cell(cell_id=2, fill=mat5)
cell2.region = -surf4

# PU
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = -surf3

# Na
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = -surf2

# Na
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = -surf1

# Nat-U
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = -surf7 & +surf18 & -surf19

# Clad-Na
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = +surf5 & -surf6 & +surf17 & -surf18

# C
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = -surf7 & +surf16 & -surf17

# Clad-Na
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = +surf4 & -surf6 & +surf15 & -surf16

# Clad-Pu
cell10 = openmc.Cell(cell_id=10, fill=mat2)
cell10.region = +surf3 & -surf7 & +surf14 & -surf15

# Clad-Na
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = +surf2 & -surf6 & +surf13 & -surf14

# C
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = -surf7 & +surf12 & -surf13

# Clad-Na
cell13 = openmc.Cell(cell_id=13, fill=mat6)
cell13.region = +surf1 & -surf6 & +surf11 & -surf12

# Nat-U
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = -surf7 & +surf10 & -surf11

# Sheath
cell15 = openmc.Cell(cell_id=15, fill=mat7)
cell15.region = +surf8 & -surf9 & +surf10 & -surf19

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15])
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
source.space = openmc.stats.Point((0.0, 0.0, 3.29115))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
