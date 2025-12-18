"""
PU-SOL-THERM-003 (Case 7) 0.647 kg Pu(96.88) @ H/X = 738 in a water reflected 13" Al-2S sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 8.781100e-05)
mat1.add_nuclide("Pu240", 2.816100e-06)
mat1.add_element("N", 9.042200e-04)
mat1.add_nuclide("H1", 6.478300e-02)
mat1.add_nuclide("O16", 3.483300e-02)
mat1.add_element("Fe", 1.229300e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 3.777000e-04)
mat2.add_element("Cu", 5.136400e-05)
mat2.add_element("Zn", 2.495800e-05)
mat2.add_element("Mn", 1.485300e-05)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.662200e-02)
mat3.add_nuclide("O16", 3.331100e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = 

# AL2S
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = 

# WATER
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3])
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
