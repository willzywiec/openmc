"""
U233-SOL-THERM-017-5: 0.809 kg 233U @ H/X=272.2 and N/U=2.15 (Exp't No. 234d)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Sol'n No. 31
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 2.372700e-04)
mat1.add_nuclide("U234", 2.535900e-06)
mat1.add_nuclide("U235", 6.270600e-08)
mat1.add_nuclide("U236", 2.401500e-09)
mat1.add_nuclide("U238", 3.300500e-06)
mat1.add_nuclide("H1", 6.458400e-02)
mat1.add_element("N", 5.221700e-04)
mat1.add_nuclide("O16", 3.433300e-02)
mat1.add_element("Th", 3.053800e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Aluminum-2S
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 5.810800e-04)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.665800e-02)
mat3.add_nuclide("O16", 3.332900e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Aluminum-1100
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 5.993000e-02)
mat4.add_element("Si", 2.253200e-04)
mat4.add_element("Mn", 1.212500e-05)
mat4.add_element("Fe", 1.133100e-04)
mat4.add_element("Cu", 2.620600e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# ALP
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# SOL
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = +surf1 & +surf2 & -surf3 & -surf4 & -surf8

# AlT
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf1 & +surf2 & +surf3 & -surf4

# ALL
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf3 & +surf4 & -surf5

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf2 & +surf4 & -surf6 & -surf7 & -surf9

# TANK
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf2 & +surf6 & -surf7

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
source.space = openmc.stats.Point((0.0, 0.0, 12.724))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
