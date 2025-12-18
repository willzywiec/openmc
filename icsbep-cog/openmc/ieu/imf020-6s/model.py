"""
IEU-MET-FAST-020-6s: Rev. 2: FR0 T5-S; simplified homogeous cylindrical benchmark
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U20
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 8.513500e-05)
mat1.add_nuclide("U235", 8.498300e-03)
mat1.add_nuclide("U238", 3.337600e-02)
mat1.add_element("C", 4.354500e-05)
mat1.add_element("F", 8.709000e-05)
mat1.add_element("Fe", 3.967100e-03)
mat1.add_element("Cr", 1.080200e-03)
mat1.add_element("Ni", 5.051000e-04)
mat1.add_element("Mn", 5.680000e-05)
mat1.add_element("Si", 5.555300e-05)

# CU
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cu", 7.450500e-02)
mat2.add_element("Ag", 7.036700e-05)
mat2.add_nuclide("O16", 1.186000e-04)
mat2.add_element("Fe", 3.967100e-03)
mat2.add_element("Cr", 1.080200e-03)
mat2.add_element("Ni", 5.051000e-04)
mat2.add_element("Mn", 5.680000e-05)
mat2.add_element("Si", 5.555300e-05)

# IV
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 3.967100e-03)
mat3.add_element("Cr", 1.080200e-03)
mat3.add_element("Ni", 5.051000e-04)
mat3.add_element("Mn", 5.680000e-05)
mat3.add_element("Si", 5.555300e-05)

# IEB
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 5.655400e-02)
mat4.add_element("Cr", 1.540000e-02)
mat4.add_element("Ni", 7.200600e-03)
mat4.add_element("Mn", 8.097200e-04)
mat4.add_element("Si", 7.919400e-04)

# OEB
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 4.761000e-02)
mat5.add_element("Cr", 1.296400e-02)
mat5.add_element("Ni", 6.061800e-03)
mat5.add_element("Mn", 6.816600e-04)
mat5.add_element("Si", 6.667000e-04)

# FE
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 8.410900e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# (U20)
surf1 = openmc.ZCylinder(surface_id=1, x0=-15.0535, y0=15.0535, r=18.173)
# Copper (CU)
surf2 = openmc.ZCylinder(surface_id=2, x0=-55.9035, y0=55.9035, r=25.398)
# Void Region (VR)
surf3 = openmc.ZCylinder(surface_id=3, x0=-57.4535, y0=58.2465, r=25.398)
# Inside End Blocks (IEB)
surf4 = openmc.ZCylinder(surface_id=4, x0=-59.7535, y0=60.2465, r=25.398)
# Outside End Blocks (OEB)
surf5 = openmc.ZCylinder(surface_id=5, x0=-61.5535, y0=61.9465, r=25.398)
# Locking rails
surf6 = openmc.ZCylinder(surface_id=6, x0=61.9465, y0=64.7465, r=25.398)
# Iron reactor table and wall; inner
surf7 = openmc.ZCylinder(surface_id=7, x0=-61.5535, y0=64.7465, r=68.4)
# Iron reactor table and wall; outer
surf8 = openmc.ZCylinder(surface_id=8, x0=-77.5535, y0=64.7465, r=70.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U20
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Cu
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# VR
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

# IEB
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf2 & +surf3 & -surf4

# OEB
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf2 & +surf3 & +surf4 & -surf5

# FE
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf5 & -surf6 & -surf7

# FE
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = +surf2 & +surf3 & +surf4 & +surf5 & +surf6 & +surf7 & -surf8

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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
