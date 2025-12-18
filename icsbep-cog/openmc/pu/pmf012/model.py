"""
PU-MET-FAST-012: BR-1-1 Assembly with Tu Reflector
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.367900e-05)
mat1.add_nuclide("Pu239", 2.671200e-02)
mat1.add_nuclide("Pu240", 6.264900e-04)
mat1.add_nuclide("Pu241", 5.471500e-06)
mat1.add_element("Ga", 1.661100e-03)
mat1.add_element("Cu", 2.409600e-03)
mat1.add_element("Fe", 5.368000e-03)
mat1.add_element("Cr", 1.407100e-03)
mat1.add_element("Ni", 7.609200e-04)
mat1.add_element("Mn", 9.334600e-05)
mat1.add_element("Si", 7.608100e-05)
mat1.add_element("Ti", 4.239600e-05)
mat1.add_element("C", 3.735900e-05)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 1.225900e-04)
mat2.add_nuclide("U238", 2.838600e-02)
mat2.add_element("Fe", 1.959100e-04)
mat2.add_element("C", 3.415900e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 7.773100e-05)
mat3.add_nuclide("U238", 1.799900e-02)
mat3.add_element("Cu", 2.845700e-04)
mat3.add_element("Fe", 1.471200e-02)
mat3.add_element("Cr", 3.823800e-03)
mat3.add_element("Ni", 2.067800e-03)
mat3.add_element("Mn", 2.536700e-04)
mat3.add_element("Si", 2.067500e-04)
mat3.add_element("Ti", 1.152100e-04)
mat3.add_element("C", 2.267500e-03)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U235", 1.715400e-04)
mat4.add_nuclide("U238", 3.972100e-02)
mat4.add_element("Fe", 2.741400e-04)
mat4.add_element("C", 4.780000e-03)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U235", 1.850400e-04)
mat5.add_nuclide("U238", 4.284800e-02)
mat5.add_element("Fe", 2.957200e-04)
mat5.add_element("C", 5.156300e-03)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("U235", 1.690300e-04)
mat6.add_nuclide("U238", 3.914000e-02)
mat6.add_element("Fe", 2.701300e-04)
mat6.add_element("C", 4.710100e-03)

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("U235", 1.244100e-04)
mat7.add_nuclide("U238", 2.880700e-02)
mat7.add_element("Fe", 1.988200e-04)
mat7.add_element("C", 3.466600e-03)

mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_nuclide("U235", 1.225900e-04)
mat8.add_nuclide("U238", 2.838600e-02)
mat8.add_element("Fe", 1.088200e-02)
mat8.add_element("Cr", 2.801200e-03)
mat8.add_element("Ni", 1.514800e-03)
mat8.add_element("Mn", 1.858300e-04)
mat8.add_element("Si", 1.514600e-04)
mat8.add_element("Ti", 8.440100e-05)
mat8.add_element("C", 3.490200e-03)

mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_nuclide("U235", 1.342000e-04)
mat9.add_nuclide("U238", 3.107500e-02)
mat9.add_element("Fe", 1.090100e-02)
mat9.add_element("Cr", 2.801200e-03)
mat9.add_element("Ni", 1.514800e-03)
mat9.add_element("Mn", 1.858300e-04)
mat9.add_element("Si", 1.514600e-04)
mat9.add_element("Ti", 8.440100e-05)
mat9.add_element("C", 3.813800e-03)

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
mat11.add_nuclide("U235", 2.040400e-04)
mat11.add_nuclide("U238", 4.724800e-02)
mat11.add_element("Fe", 3.260800e-04)
mat11.add_element("C", 5.685700e-03)

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
mat13.add_nuclide("U235", 1.970000e-04)
mat13.add_nuclide("U238", 4.561700e-02)
mat13.add_element("Fe", 3.148300e-04)
mat13.add_element("C", 5.489500e-03)

mat14 = openmc.Material(material_id=14)
mat14.set_density("sum")
mat14.add_element("Fe", 2.756100e-02)
mat14.add_element("Cr", 7.224500e-03)
mat14.add_element("Ni", 3.906900e-03)
mat14.add_element("Mn", 4.792700e-04)
mat14.add_element("Si", 3.906300e-04)
mat14.add_element("Ti", 2.176800e-04)
mat14.add_element("C", 1.918200e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11, mat12, mat13, mat14])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# VOID
cell1 = openmc.Cell(cell_id=1)
cell1.region = +surf4 & -surf5 & +surf20 & -surf24

# VOID
cell2 = openmc.Cell(cell_id=2)
cell2.region = +surf4 & -surf5 & +surf29 & -surf32

# VOID
cell3 = openmc.Cell(cell_id=3)
cell3.region = +surf6 & -surf7 & +surf20 & -surf24

# VOID
cell4 = openmc.Cell(cell_id=4)
cell4.region = +surf4 & -surf7 & +surf24 & -surf25

# VOID
cell5 = openmc.Cell(cell_id=5)
cell5.region = +surf8 & -surf9 & +surf20 & -surf24

# VOID
cell6 = openmc.Cell(cell_id=6)
cell6.region = +surf10 & -surf11 & +surf20 & -surf24

# VOID
cell7 = openmc.Cell(cell_id=7)
cell7.region = +surf8 & -surf11 & +surf24 & -surf27

# VOID
cell8 = openmc.Cell(cell_id=8)
cell8.region = +surf12 & -surf13 & +surf20 & -surf32

# REG01
cell9 = openmc.Cell(cell_id=9, fill=mat1)
cell9.region = +surf1 & -surf2 & +surf23 & -surf24

# REG02
cell10 = openmc.Cell(cell_id=10, fill=mat2)
cell10.region = +surf2 & -surf3 & +surf22 & -surf24

# REG03
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = +surf1 & -surf2 & +surf22 & -surf23

# REG03
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = +surf1 & -surf2 & +surf24 & -surf26

# REG04
cell13 = openmc.Cell(cell_id=13, fill=mat4)
cell13.region = +surf1 & -surf2 & +surf21 & -surf22

# REG05
cell14 = openmc.Cell(cell_id=14, fill=mat5)
cell14.region = +surf1 & -surf2 & +surf26 & -surf28

# REG05
cell15 = openmc.Cell(cell_id=15, fill=mat5)
cell15.region = +surf1 & -surf2 & +surf30 & -surf31

# REG06
cell16 = openmc.Cell(cell_id=16, fill=mat6)
cell16.region = +surf1 & -surf2 & +surf28 & -surf30

# REG07
cell17 = openmc.Cell(cell_id=17, fill=mat7)
cell17.region = +surf2 & -surf3 & +surf21 & -surf22

# REG08
cell18 = openmc.Cell(cell_id=18, fill=mat8)
cell18.region = +surf2 & -surf3 & +surf24 & -surf26

# REG08
cell19 = openmc.Cell(cell_id=19, fill=mat8)
cell19.region = +surf2 & -surf3 & +surf28 & -surf30

# REG09
cell20 = openmc.Cell(cell_id=20, fill=mat9)
cell20.region = +surf2 & -surf3 & +surf26 & -surf28

# REG09
cell21 = openmc.Cell(cell_id=21, fill=mat9)
cell21.region = +surf2 & -surf3 & +surf30 & -surf31

# REG10
cell22 = openmc.Cell(cell_id=22, fill=mat10)
cell22.region = -surf1 & +surf20 & -surf32

# REG11
cell23 = openmc.Cell(cell_id=23, fill=mat11)
cell23.region = +surf1 & -surf3 & +surf20 & -surf21

# REG11
cell24 = openmc.Cell(cell_id=24, fill=mat11)
cell24.region = +surf5 & -surf6 & +surf20 & -surf24

# REG11
cell25 = openmc.Cell(cell_id=25, fill=mat11)
cell25.region = +surf5 & -surf12 & +surf29 & -surf32

# REG11
cell26 = openmc.Cell(cell_id=26, fill=mat11)
cell26.region = +surf13 & -surf14 & +surf20 & -surf32

# REG12
cell27 = openmc.Cell(cell_id=27, fill=mat12)
cell27.region = +surf3 & -surf4 & +surf20 & -surf32

# REG12
cell28 = openmc.Cell(cell_id=28, fill=mat12)
cell28.region = +surf7 & -surf8 & +surf20 & -surf25

# REG12
cell29 = openmc.Cell(cell_id=29, fill=mat12)
cell29.region = +surf4 & -surf8 & +surf25 & -surf27

# REG12
cell30 = openmc.Cell(cell_id=30, fill=mat12)
cell30.region = +surf4 & -surf12 & +surf27 & -surf29

# REG12
cell31 = openmc.Cell(cell_id=31, fill=mat12)
cell31.region = +surf11 & -surf12 & +surf20 & -surf27

# REG13
cell32 = openmc.Cell(cell_id=32, fill=mat13)
cell32.region = +surf9 & -surf10 & +surf20 & -surf24

# REG14
cell33 = openmc.Cell(cell_id=33, fill=mat14)
cell33.region = +surf1 & -surf3 & +surf31 & -surf32

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33])
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
