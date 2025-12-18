"""
MIX-MET-FAST-008-5: ZEBRA-8E (in IRPhE: ZEBRA-FUND-RESR-001)
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

# Sodium (Na)
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("O16", 1.993700e-06)
mat3.add_element("Na", 2.311900e-02)
mat3.add_element("Fe", 3.808000e-08)
mat3.add_nuclide("B10", 5.309500e-08)
mat3.add_nuclide("B11", 9.657900e-08)
mat3.add_nuclide("H1", 2.109800e-06)
mat3.add_element("K", 4.759100e-07)
mat3.add_element("Ca", 1.724400e-06)
mat3.add_nuclide("Li7", 3.788700e-07)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Clad - Na
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 2.342600e-04)
mat4.add_element("Fe", 5.851200e-02)
mat4.add_element("Cr", 1.622700e-02)
mat4.add_element("Mn", 1.169500e-03)
mat4.add_element("Ni", 7.847600e-03)
mat4.add_nuclide("H1", 2.326300e-05)
mat4.add_element("Nb", 3.281500e-04)
mat4.add_element("Si", 6.512000e-04)
mat4.add_element("P", 3.028100e-05)
mat4.add_element("S", 2.925100e-05)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Nat-U Metal
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U235", 3.331700e-04)
mat5.add_nuclide("U238", 4.594900e-02)
mat5.add_element("C", 4.924100e-04)
mat5.add_element("Fe", 1.059100e-04)
mat5.add_nuclide("H1", 4.378900e-05)
mat5.add_element("Si", 2.105800e-04)
mat5.add_s_alpha_beta("c_H_in_H2O")

# Sheath
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("C", 7.781500e-04)
mat6.add_element("Fe", 5.662600e-02)
mat6.add_element("Cr", 1.610700e-02)
mat6.add_element("Cu", 7.383500e-05)
mat6.add_element("Mo", 1.463900e-04)
mat6.add_element("Mn", 1.191700e-03)
mat6.add_element("Ni", 9.004200e-03)
mat6.add_element("Al", 3.464000e-04)
mat6.add_element("Ti", 2.933100e-04)
mat6.add_nuclide("H1", 2.320500e-05)
mat6.add_element("Si", 9.998500e-04)
mat6.add_element("V", 9.210400e-05)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Na
surf1 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 0.6718299999999999, 1.21417)
# Na
surf2 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 1.28783, 1.8301699999999999)
# Na
surf3 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 2.85633, 3.39867)
# Na
surf4 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 3.47233, 4.01467)
# Pu
surf5 = openmc.model.RectangularParallelepiped(-2.3355, 2.3355, -2.3355, 2.3355, 4.1023000000000005, 4.3182)
# Na
surf6 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 4.40583, 4.948169999999999)
# Na
surf7 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 5.0218300000000005, 5.56417)
# Na
surf8 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 6.590330000000001, 7.13267)
# Na
surf9 = openmc.model.RectangularParallelepiped(-2.4815, 2.4815, -2.4815, 2.4815, 7.20633, 7.74867)
# Na clad
surf11 = openmc.model.RectangularParallelepiped(-2.5185, 2.5185, -2.5185, 2.5185, -49.95, 49.95)
# Pu clad, C, Nat-U
surf12 = openmc.model.RectangularParallelepiped(-2.5335, 2.5335, -2.5335, 2.5335, -49.95, 49.95)
# Sheath, inner
surf13 = openmc.model.RectangularParallelepiped(-2.551, 2.551, -2.551, 2.551, -49.95, 49.95)
# Sheath, outer
surf14 = openmc.model.RectangularParallelepiped(-2.6272, 2.6272, -2.6272, 2.6272, -49.95, 49.95, boundary_type="reflecting")
surf20 = openmc.ZPlane(surface_id=20, z0=0.0, boundary_type="periodic")
surf21 = openmc.ZPlane(surface_id=21, z0=0.6350)
surf22 = openmc.ZPlane(surface_id=22, z0=1.8670)
surf23 = openmc.ZPlane(surface_id=23, z0=2.8195)
surf24 = openmc.ZPlane(surface_id=24, z0=4.0515)
surf25 = openmc.ZPlane(surface_id=25, z0=4.3690)
surf26 = openmc.ZPlane(surface_id=26, z0=5.6010)
surf27 = openmc.ZPlane(surface_id=27, z0=6.5536)
surf28 = openmc.ZPlane(surface_id=28, z0=7.7855)
surf29 = openmc.ZPlane(surface_id=29, z0=8.1030, boundary_type="periodic")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Na
cell1 = openmc.Cell(cell_id=1, fill=mat3)
cell1.region = -surf9

# Na
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = -surf8

# Na
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = -surf7

# Na
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = -surf6

# Pu
cell5 = openmc.Cell(cell_id=5, fill=mat1)
cell5.region = -surf5

# Na
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = -surf4

# Na
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = -surf3

# Na
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = -surf2

# Na
cell9 = openmc.Cell(cell_id=9, fill=mat3)
cell9.region = -surf1

# Nat-U
cell10 = openmc.Cell(cell_id=10, fill=mat5)
cell10.region = -surf12 & +surf28 & -surf29

# Clad-Na
cell11 = openmc.Cell(cell_id=11, fill=mat4)
cell11.region = +surf8 & +surf9 & -surf11 & +surf27 & -surf28

# Nat-U
cell12 = openmc.Cell(cell_id=12, fill=mat5)
cell12.region = -surf12 & +surf26 & -surf27

# Clad-Na
cell13 = openmc.Cell(cell_id=13, fill=mat4)
cell13.region = +surf6 & +surf7 & -surf11 & +surf25 & -surf26

# Clad-Pu
cell14 = openmc.Cell(cell_id=14, fill=mat2)
cell14.region = +surf5 & -surf12 & +surf24 & -surf25

# Clad-Na
cell15 = openmc.Cell(cell_id=15, fill=mat4)
cell15.region = +surf3 & +surf4 & -surf11 & +surf23 & -surf24

# Nat-U
cell16 = openmc.Cell(cell_id=16, fill=mat5)
cell16.region = -surf12 & +surf22 & -surf23

# Clad-Na
cell17 = openmc.Cell(cell_id=17, fill=mat4)
cell17.region = +surf1 & +surf2 & -surf11 & +surf21 & -surf22

# Nat-U
cell18 = openmc.Cell(cell_id=18, fill=mat5)
cell18.region = -surf12 & +surf20 & -surf21

# Sheath
cell19 = openmc.Cell(cell_id=19, fill=mat6)
cell19.region = +surf13 & -surf14 & +surf20 & -surf29

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19])
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
source.space = openmc.stats.Point((0.0, 0.0, 4.21025))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
