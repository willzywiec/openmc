"""
MIX-MET-FAST-008-6: ZEBRA-8F (in IRPhE: ZEBRA-FUND-RESR-001)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# MOX
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 7.681900e-07)
mat1.add_nuclide("U235", 1.155500e-04)
mat1.add_nuclide("U238", 1.593800e-02)
mat1.add_nuclide("Pu239", 4.773100e-03)
mat1.add_nuclide("Pu240", 5.335700e-04)
mat1.add_nuclide("Pu241", 5.901700e-05)
mat1.add_nuclide("Pu242", 4.768000e-06)
mat1.add_element("C", 6.228900e-05)
mat1.add_nuclide("O16", 4.286000e-02)
mat1.add_element("Fe", 1.339700e-05)
mat1.add_element("Ni", 1.274800e-05)
mat1.add_element("Al", 2.772800e-05)
mat1.add_element("Si", 2.663800e-05)
mat1.add_nuclide("Np237", 1.957700e-07)
mat1.add_nuclide("Am241", 1.753900e-05)

# Clad - MOX
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 1.708900e-04)
mat2.add_element("Fe", 5.106700e-02)
mat2.add_element("Cr", 1.413200e-02)
mat2.add_element("Mn", 1.113400e-03)
mat2.add_element("Ni", 6.987700e-03)
mat2.add_nuclide("H1", 2.036400e-05)
mat2.add_element("Nb", 2.872000e-04)
mat2.add_element("Si", 5.992700e-04)
mat2.add_element("P", 2.650700e-05)
mat2.add_element("S", 2.560500e-05)
mat2.add_s_alpha_beta("c_H_in_H2O")

# Nat-UO2
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U234", 1.187100e-06)
mat3.add_nuclide("U235", 1.646200e-04)
mat3.add_nuclide("U238", 2.269400e-02)
mat3.add_element("C", 3.084200e-05)
mat3.add_nuclide("O16", 4.573400e-02)
mat3.add_element("Fe", 6.633600e-06)
mat3.add_nuclide("H1", 2.450200e-05)
mat3.add_element("Si", 1.319000e-05)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Clad Nat-UO2
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 1.449200e-04)
mat4.add_element("Fe", 4.323500e-02)
mat4.add_element("Cr", 1.231500e-02)
mat4.add_element("Cu", 8.127000e-04)
mat4.add_element("Mn", 9.755200e-04)
mat4.add_element("Ni", 5.988900e-03)
mat4.add_element("Ag", 1.231700e-03)
mat4.add_nuclide("H1", 1.817800e-05)
mat4.add_element("Si", 6.071000e-04)
mat4.add_element("P", 2.247900e-05)
mat4.add_element("S", 2.171400e-05)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Graphite
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 8.060300e-02)
mat5.add_nuclide("O16", 1.403900e-04)
mat5.add_element("Na", 2.915800e-06)
mat5.add_element("Fe", 6.923800e-06)
mat5.add_nuclide("B10", 1.940500e-07)
mat5.add_nuclide("B11", 5.294600e-07)
mat5.add_element("Cu", 3.057600e-07)
mat5.add_element("Mn", 2.652500e-07)
mat5.add_element("Al", 1.800300e-06)
mat5.add_nuclide("H1", 2.978300e-04)
mat5.add_element("Si", 6.883500e-06)
mat5.add_element("Ca", 1.478600e-06)
mat5.add_element("V", 1.907100e-07)
mat5.add_element("S", 1.514900e-07)
mat5.add_element("Zn", 7.427700e-08)
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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Nat-UO2
surf1 = openmc.model.RectangularParallelepiped(-2.4255, 2.4255, -2.4255, 2.4255, 0.35203, 0.9062699999999999)
# MOX
surf2 = openmc.model.RectangularParallelepiped(-2.4765, 2.4765, -2.4765, 2.4765, 1.2956400000000001, 1.84876)
# Nat-UO2
surf3 = openmc.model.RectangularParallelepiped(-2.4255, 2.4255, -2.4255, 2.4255, 2.23813, 2.79237)
# Clad-MOX
surf11 = openmc.model.RectangularParallelepiped(-2.531, 2.531, -2.531, 2.531, -49.95, 49.95)
# Graphite
surf12 = openmc.model.RectangularParallelepiped(-2.5335, 2.5335, -2.5335, 2.5335, -49.95, 49.95)
# Clad-Nat-UO2
surf13 = openmc.model.RectangularParallelepiped(-2.5345, 2.5345, -2.5345, 2.5345, -49.95, 49.95)
# Sheath, inner
surf14 = openmc.model.RectangularParallelepiped(-2.551, 2.551, -2.551, 2.551, -49.95, 49.95)
# Sheath, outer
surf15 = openmc.model.RectangularParallelepiped(-2.6272, 2.6272, -2.6272, 2.6272, -49.95, 49.95, boundary_type="reflecting")
surf20 = openmc.ZPlane(surface_id=20, z0=0.0, boundary_type="periodic")
surf21 = openmc.ZPlane(surface_id=21, z0=0.3152)
surf22 = openmc.ZPlane(surface_id=22, z0=0.9431)
surf23 = openmc.ZPlane(surface_id=23, z0=1.2583)
surf24 = openmc.ZPlane(surface_id=24, z0=1.8861)
surf25 = openmc.ZPlane(surface_id=25, z0=2.2013)
surf26 = openmc.ZPlane(surface_id=26, z0=2.8292)
surf27 = openmc.ZPlane(surface_id=27, z0=3.1444, boundary_type="periodic")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UO2
cell1 = openmc.Cell(cell_id=1, fill=mat3)
cell1.region = -surf3

# MOX
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = -surf2

# UO2
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = -surf1

# C
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = -surf12 & +surf26 & -surf27

# Clad-UO2
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf3 & -surf13 & +surf25 & -surf26

# C
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = -surf12 & +surf24 & -surf25

# Clad-MOX
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = +surf2 & -surf11 & +surf23 & -surf24

# C
cell8 = openmc.Cell(cell_id=8, fill=mat5)
cell8.region = -surf12 & +surf22 & -surf23

# Clad-UO2
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = +surf1 & -surf13 & +surf21 & -surf22

# C
cell10 = openmc.Cell(cell_id=10, fill=mat5)
cell10.region = -surf12 & +surf20 & -surf21

# Sheath
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = +surf14 & -surf15 & +surf20 & -surf27

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11])
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
source.space = openmc.stats.Point((0.0, 0.0, 1.5722))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
