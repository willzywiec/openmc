"""
PU-MET-FAST-045: LAMPRE Assembly IV (Simplified Model)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.290000e-02)
mat1.add_element("Ni", 7.770000e-03)
mat1.add_element("Ta", 4.580000e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Ni", 8.885900e-02)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Ta", 4.869000e-02)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 2.008700e-02)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 8.464800e-02)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.676600e-02)
mat6.add_nuclide("O16", 3.338300e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("H1", 7.899600e-02)
mat7.add_element("C", 3.949800e-02)
mat7.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf3

# Ta
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = +surf3 & -surf4

# Al
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = +surf4 & -surf5

# Gap
cell4 = openmc.Cell(cell_id=4)
cell4.region = +surf5 & -surf6

# Ni
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf5 & +surf6 & -surf7

# Al
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf5 & +surf6 & +surf7 & -surf8

# CH2
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = +surf5 & +surf6 & +surf8 & -surf9

# Gap
cell8 = openmc.Cell(cell_id=8)
cell8.region = +surf7 & +surf8 & +surf9 & -surf10 & -surf12

# Fe
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = +surf10 & -surf11 & -surf12

# H2O
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = +surf11 & -surf12

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10])
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
source.space = openmc.stats.Point((0.0, 0.0, 4.49))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
