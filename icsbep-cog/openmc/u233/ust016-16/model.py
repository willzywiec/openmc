"""
U233-SOL-THERM-016-16: 3.815 kg 233U @ H/X=196.1 and N/U=2.15 (Exp't No. 139)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Sol'n No. 13
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 3.272900e-04)
mat1.add_nuclide("U234", 3.498100e-06)
mat1.add_nuclide("U235", 8.649700e-08)
mat1.add_nuclide("U236", 3.312600e-09)
mat1.add_nuclide("U238", 4.552700e-06)
mat1.add_nuclide("H1", 6.419300e-02)
mat1.add_element("N", 7.202900e-04)
mat1.add_nuclide("O16", 3.491200e-02)
mat1.add_element("Th", 4.212400e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Aluminum-2S
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 5.810800e-04)

# Stainless
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 3.184800e-04)
mat3.add_element("Si", 1.702500e-03)
mat3.add_element("P", 6.946800e-05)
mat3.add_element("Cr", 1.747200e-02)
mat3.add_element("Mn", 1.740700e-03)
mat3.add_element("Fe", 5.854300e-02)
mat3.add_element("Ni", 7.739800e-03)

# Regualr
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 3.472200e-04)
mat4.add_element("Al", 1.745400e-03)
mat4.add_element("Ca", 1.520600e-03)
mat4.add_nuclide("O16", 4.605600e-02)
mat4.add_element("Si", 1.662000e-02)
mat4.add_nuclide("H1", 1.374200e-02)
mat4.add_element("Na", 1.747200e-03)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf7 & -surf8 & -surf10

# AlT
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf5 & +surf6 & +surf7 & -surf8

# ALL
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf7 & +surf8 & -surf9

# SOL
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = -surf5 & -surf6 & +surf7

# ALP
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf5 & -surf6 & +surf7

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf3 & -surf4

# CNC
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf1 & -surf2

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
source.space = openmc.stats.Point((0.0, 0.0, 7.1755))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
