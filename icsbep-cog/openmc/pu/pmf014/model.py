"""
PU-MET-PAST-014: BR-1-4 Assembly with Ni Reflector
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.335700e-05)
mat1.add_nuclide("Pu239", 2.608300e-02)
mat1.add_nuclide("Pu240", 6.117500e-04)
mat1.add_nuclide("Pu241", 5.342800e-06)
mat1.add_element("Ga", 1.622100e-03)
mat1.add_element("Cu", 2.352900e-03)
mat1.add_element("Fe", 5.241800e-03)
mat1.add_element("Cr", 1.374000e-03)
mat1.add_element("Ni", 7.430200e-04)
mat1.add_element("Mn", 9.115000e-05)
mat1.add_element("Si", 7.429100e-05)
mat1.add_element("Ti", 4.139900e-05)
mat1.add_element("C", 3.648000e-05)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Ni", 4.849200e-02)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cu", 2.778700e-04)
mat3.add_element("Fe", 1.424500e-02)
mat3.add_element("Cr", 3.733900e-03)
mat3.add_element("Ni", 3.586500e-02)
mat3.add_element("Mn", 2.477100e-04)
mat3.add_element("Si", 2.018900e-04)
mat3.add_element("Ti", 1.125000e-04)
mat3.add_element("C", 9.913700e-05)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Ni", 7.496900e-02)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Ni", 8.087000e-02)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Ni", 7.387200e-02)

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Ni", 4.921200e-02)

mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Fe", 1.396200e-02)
mat8.add_element("Cr", 3.659900e-03)
mat8.add_element("Ni", 5.047100e-02)
mat8.add_element("Mn", 2.428000e-04)
mat8.add_element("Si", 1.978900e-04)
mat8.add_element("Ti", 1.102700e-04)
mat8.add_element("C", 9.717300e-05)

mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Fe", 1.396200e-02)
mat9.add_element("Cr", 3.659900e-03)
mat9.add_element("Ni", 5.506500e-02)
mat9.add_element("Mn", 2.428000e-04)
mat9.add_element("Si", 1.978900e-04)
mat9.add_element("Ti", 1.102700e-04)
mat9.add_element("C", 9.717300e-05)

mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("Fe", 6.543800e-03)
mat10.add_element("Cr", 1.715300e-03)
mat10.add_element("Ni", 9.275900e-04)
mat10.add_element("Mn", 1.137900e-04)
mat10.add_element("Si", 9.274500e-05)
mat10.add_element("Ti", 5.168200e-05)
mat10.add_element("C", 4.554200e-05)

mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_element("Ni", 9.132200e-02)

mat12 = openmc.Material(material_id=12)
mat12.set_density("sum")
mat12.add_element("Fe", 5.998600e-02)
mat12.add_element("Cr", 1.572400e-02)
mat12.add_element("Ni", 8.503000e-03)
mat12.add_element("Mn", 1.043100e-03)
mat12.add_element("Si", 8.501800e-04)
mat12.add_element("Ti", 4.737600e-04)
mat12.add_element("C", 4.174800e-04)

mat13 = openmc.Material(material_id=13)
mat13.set_density("sum")
mat13.add_element("Cu", 6.747500e-02)
mat13.add_element("Ni", 1.826400e-02)

mat14 = openmc.Material(material_id=14)
mat14.set_density("sum")
mat14.add_element("Cu", 6.514600e-02)
mat14.add_element("Ni", 1.763400e-02)

mat15 = openmc.Material(material_id=15)
mat15.set_density("sum")
mat15.add_element("Ni", 8.272300e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11, mat12, mat13, mat14, mat15])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# VOID
cell1 = openmc.Cell(cell_id=1)
cell1.region = 

# VOID
cell2 = openmc.Cell(cell_id=2)
cell2.region = 

# VOID
cell3 = openmc.Cell(cell_id=3)
cell3.region = 

# VOID
cell4 = openmc.Cell(cell_id=4)
cell4.region = 

# VOID
cell5 = openmc.Cell(cell_id=5)
cell5.region = 

# VOID
cell6 = openmc.Cell(cell_id=6)
cell6.region = 

# VOID
cell7 = openmc.Cell(cell_id=7)
cell7.region = 

# VOID
cell8 = openmc.Cell(cell_id=8)
cell8.region = 

# VOID
cell9 = openmc.Cell(cell_id=9)
cell9.region = 

# REG0l
cell10 = openmc.Cell(cell_id=10, fill=mat1)
cell10.region = 

# REG02
cell11 = openmc.Cell(cell_id=11, fill=mat2)
cell11.region = 

# REG03
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = 

# REG03
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = 

# REG04
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = 

# REG05
cell15 = openmc.Cell(cell_id=15, fill=mat5)
cell15.region = 

# REG05
cell16 = openmc.Cell(cell_id=16, fill=mat5)
cell16.region = 

# RBG06
cell17 = openmc.Cell(cell_id=17, fill=mat6)
cell17.region = 

# REG07
cell18 = openmc.Cell(cell_id=18, fill=mat7)
cell18.region = 

# REG08
cell19 = openmc.Cell(cell_id=19, fill=mat8)
cell19.region = 

# REG08
cell20 = openmc.Cell(cell_id=20, fill=mat5)
cell20.region = 

# REG09
cell21 = openmc.Cell(cell_id=21, fill=mat9)
cell21.region = 

# REG09
cell22 = openmc.Cell(cell_id=22, fill=mat9)
cell22.region = 

# REG10
cell23 = openmc.Cell(cell_id=23, fill=mat10)
cell23.region = 

# REG11
cell24 = openmc.Cell(cell_id=24, fill=mat11)
cell24.region = 

# REGll
cell25 = openmc.Cell(cell_id=25, fill=mat11)
cell25.region = 

# REG11
cell26 = openmc.Cell(cell_id=26, fill=mat11)
cell26.region = 

# REG11
cell27 = openmc.Cell(cell_id=27, fill=mat11)
cell27.region = 

# REG12
cell28 = openmc.Cell(cell_id=28, fill=mat12)
cell28.region = 

# REG12
cell29 = openmc.Cell(cell_id=29, fill=mat12)
cell29.region = 

# REG12
cell30 = openmc.Cell(cell_id=30, fill=mat12)
cell30.region = 

# REG12
cell31 = openmc.Cell(cell_id=31, fill=mat12)
cell31.region = 

# REG12
cell32 = openmc.Cell(cell_id=32, fill=mat12)
cell32.region = 

# REGl3
cell33 = openmc.Cell(cell_id=33, fill=mat13)
cell33.region = 

# REG14
cell34 = openmc.Cell(cell_id=34, fill=mat14)
cell34.region = 

# REG14
cell35 = openmc.Cell(cell_id=35, fill=mat15)
cell35.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35])
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
source.space = openmc.stats.Box((-3.0, -3.0, 34.0), (3.0, 3.0, 36.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
