"""
PU-MET-FAST-021-2. Pu cylinder with axial BeO reflection.
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu per
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.442200e-02)
mat1.add_nuclide("Pu240", 2.132600e-03)
mat1.add_nuclide("Pu241", 9.253800e-05)
mat1.add_element("C", 1.951500e-04)
mat1.add_element("Fe", 8.194300e-05)

# Steel per
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.128000e-02)
mat2.add_element("C", 3.475700e-04)
mat2.add_element("Si", 8.918500e-04)
mat2.add_element("Ti", 6.103400e-04)
mat2.add_element("Cr", 1.445200e-02)
mat2.add_element("Mn", 1.519800e-03)
mat2.add_element("Ni", 7.113100e-03)

# Section 3.3
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("O16", 1.079255e-01)

# Duralumin @ 1.8155 g/cc
mat41 = openmc.Material(material_id=41)
mat41.set_density("sum")
mat41.add_element("P", 1.815500e+00)
mat41.add_element("Al", 9.360000e+01)
mat41.add_element("Mg", 1.500000e+00)
mat41.add_element("Mn", 6.000000e-01)
mat41.add_element("Cu", 4.300000e+00)

# Duralumin @ 2.78 g/cc
mat42 = openmc.Material(material_id=42)
mat42.set_density("sum")
mat42.add_element("P", 2.780000e+00)
mat42.add_element("Al", 9.360000e+01)
mat42.add_element("Mg", 1.500000e+00)
mat42.add_element("Mn", 6.000000e-01)
mat42.add_element("Cu", 4.300000e+00)

# Duralumin @ 0.417 g/cc
mat43 = openmc.Material(material_id=43)
mat43.set_density("sum")
mat43.add_element("P", 4.170000e-01)
mat43.add_element("Al", 9.360000e+01)
mat43.add_element("Mg", 1.500000e+00)
mat43.add_element("Mn", 6.000000e-01)
mat43.add_element("Cu", 4.300000e+00)

materials = openmc.Materials([mat1, mat2, mat3, mat41, mat42, mat43])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Pu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Pu
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = -surf2

# Pu
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = -surf3

# Pu
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = -surf4

# Pu
cell5 = openmc.Cell(cell_id=5, fill=mat1)
cell5.region = -surf5

# STL
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = -surf6 & +surf1 & +surf2 & +surf3 & +surf4 & +surf5

# BeO
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf6 & -surf7

# Al
cell8 = openmc.Cell(cell_id=8, fill=mat41)
cell8.region = +surf6 & +surf7 & -surf8

# Al
cell9 = openmc.Cell(cell_id=9, fill=mat42)
cell9.region = +surf6 & +surf7 & +surf8 & -surf9

# Pu
cell10 = openmc.Cell(cell_id=10, fill=mat1)
cell10.region = -surf11

# Pu
cell11 = openmc.Cell(cell_id=11, fill=mat1)
cell11.region = -surf12

# Pu
cell12 = openmc.Cell(cell_id=12, fill=mat1)
cell12.region = -surf13

# Pu
cell13 = openmc.Cell(cell_id=13, fill=mat1)
cell13.region = -surf14

# Pu
cell14 = openmc.Cell(cell_id=14, fill=mat1)
cell14.region = -surf15

# STL
cell15 = openmc.Cell(cell_id=15, fill=mat2)
cell15.region = -surf16 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15

# BeO
cell16 = openmc.Cell(cell_id=16, fill=mat3)
cell16.region = +surf16 & -surf17

# Al
cell17 = openmc.Cell(cell_id=17, fill=mat43)
cell17.region = +surf16 & +surf17 & -surf18

# Al
cell18 = openmc.Cell(cell_id=18, fill=mat42)
cell18.region = +surf16 & +surf17 & +surf18 & -surf19 & +surf20

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18])
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
source.space = openmc.stats.Box((-1.0, -1.0, -1.3), (1.0, 1.0, 1.3))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
