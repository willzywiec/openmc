"""
U233-SOL-THERM-017-6: 0.732 kg 233U @ H/X=546.2 and N/U=2.15 (Exp't No. 244d)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Sol'n No. 32a
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 1.201500e-04)
mat1.add_nuclide("U234", 1.284200e-06)
mat1.add_nuclide("U235", 3.175500e-08)
mat1.add_nuclide("U236", 1.216100e-09)
mat1.add_nuclide("U238", 1.671400e-06)
mat1.add_nuclide("H1", 6.562500e-02)
mat1.add_element("N", 2.644300e-04)
mat1.add_nuclide("O16", 3.384600e-02)
mat1.add_element("Th", 1.546400e-06)
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
# ALP
cell2 = openmc.Cell(cell_id=2, fill=mat2)
# SOL
cell3 = openmc.Cell(cell_id=3, fill=mat1)
# AlT
cell4 = openmc.Cell(cell_id=4, fill=mat2)
# ALL
cell5 = openmc.Cell(cell_id=5, fill=mat2)
# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat3)
# TANK
cell7 = openmc.Cell(cell_id=7, fill=mat4)
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
source.space = openmc.stats.Point((0.0, 0.0, 14.948))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
