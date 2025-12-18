"""
PU-MET-FAST-015: BR-1-3 Assembly with Fe Reflector
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.354600e-05)
mat1.add_nuclide("Pu239", 2.643500e-02)
mat1.add_nuclide("Pu240", 6.204200e-04)
mat1.add_nuclide("Pu241", 5.418500e-06)
mat1.add_element("Ga", 1.645100e-03)
mat1.add_element("Cu", 2.386200e-03)
mat1.add_element("Fe", 5.316000e-03)
mat1.add_element("Cr", 1.393500e-03)
mat1.add_element("Ni", 7.535500e-04)
mat1.add_element("Mn", 9.244200e-05)
mat1.add_element("Si", 7.534400e-05)
mat1.add_element("Ti", 4.198600e-05)
mat1.add_element("C", 3.699700e-05)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 1.546700e-02)
mat2.add_element("Mn", 6.336800e-05)
mat2.add_element("Si", 6.197700e-05)
mat2.add_element("C", 1.086900e-04)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cu", 2.818100e-04)
mat3.add_element("Fe", 4.598200e-02)
mat3.add_element("Cr", 3.786800e-03)
mat3.add_element("Ni", 2.047800e-03)
mat3.add_element("Mn", 3.804100e-04)
mat3.add_element("Si", 3.311100e-04)
mat3.add_element("Ti", 1.141000e-04)
mat3.add_element("C", 3.221500e-04)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 6.950100e-02)
mat4.add_element("Mn", 2.847400e-04)
mat4.add_element("Si", 2.784900e-04)
mat4.add_element("C", 4.884000e-04)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 7.497200e-02)
mat5.add_element("Mn", 3.071500e-04)
mat5.add_element("Si", 3.004100e-04)
mat5.add_element("C", 5.268400e-04)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 6.848400e-02)
mat6.add_element("Mn", 2.805700e-04)
mat6.add_element("Si", 2.744100e-04)
mat6.add_element("C", 4.812500e-04)

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Fe", 1.569700e-02)
mat7.add_element("Mn", 6.430900e-05)
mat7.add_element("Si", 6.289700e-05)
mat7.add_element("C", 1.103100e-04)

mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Fe", 4.348100e-02)
mat8.add_element("Cr", 7.343100e-03)
mat8.add_element("Ni", 3.971000e-03)
mat8.add_element("Mn", 5.505100e-04)
mat8.add_element("Si", 4.590200e-04)
mat8.add_element("Ti", 2.212500e-04)
mat8.add_element("C", 3.036600e-04)

mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Fe", 4.494700e-02)
mat9.add_element("Cr", 7.343100e-03)
mat9.add_element("Ni", 3.971000e-03)
mat9.add_element("Mn", 5.565100e-04)
mat9.add_element("Si", 4.648900e-04)
mat9.add_element("Ti", 2.212500e-04)
mat9.add_element("C", 3.139500e-04)

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
mat11.add_element("Fe", 8.347800e-02)
mat11.add_element("Mn", 3.420000e-04)
mat11.add_element("Si", 3.345000e-04)
mat11.add_element("C", 5.866200e-04)

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
mat13.add_element("Fe", 8.059800e-02)
mat13.add_element("Mn", 3.302000e-04)
mat13.add_element("Si", 3.229500e-04)
mat13.add_element("C", 5.663700e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11, mat12, mat13])

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

# REG0l
cell9 = openmc.Cell(cell_id=9, fill=mat1)
cell9.region = 

# REG02
cell10 = openmc.Cell(cell_id=10, fill=mat2)
cell10.region = 

# REG03
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = 

# REG03
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = 

# REG04
cell13 = openmc.Cell(cell_id=13, fill=mat4)
cell13.region = 

# REG05
cell14 = openmc.Cell(cell_id=14, fill=mat5)
cell14.region = 

# REG05
cell15 = openmc.Cell(cell_id=15, fill=mat5)
cell15.region = 

# REG06
cell16 = openmc.Cell(cell_id=16, fill=mat6)
cell16.region = 

# REG07
cell17 = openmc.Cell(cell_id=17, fill=mat7)
cell17.region = 

# REG08
cell18 = openmc.Cell(cell_id=18, fill=mat8)
cell18.region = 

# REG08
cell19 = openmc.Cell(cell_id=19, fill=mat8)
cell19.region = 

# REG09
cell20 = openmc.Cell(cell_id=20, fill=mat9)
cell20.region = 

# REG09
cell21 = openmc.Cell(cell_id=21, fill=mat9)
cell21.region = 

# REG10
cell22 = openmc.Cell(cell_id=22, fill=mat10)
cell22.region = 

# REG11
cell23 = openmc.Cell(cell_id=23, fill=mat11)
cell23.region = 

# REG11
cell24 = openmc.Cell(cell_id=24, fill=mat11)
cell24.region = 

# REG11
cell25 = openmc.Cell(cell_id=25, fill=mat11)
cell25.region = 

# REG11
cell26 = openmc.Cell(cell_id=26, fill=mat11)
cell26.region = 

# REG12
cell27 = openmc.Cell(cell_id=27, fill=mat12)
cell27.region = 

# REGl2
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

# REG13
cell32 = openmc.Cell(cell_id=32, fill=mat13)
cell32.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32])
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
