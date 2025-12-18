"""
PU-COMP-MIXED-002 (Case 28) 14.322 kg Pu @ H/X = 61.9 with 18.50 wt-% Pu-240 and H/SQRT(A) = 0.579
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 2.159500e-06)
mat1.add_nuclide("Pu239", 6.996300e-04)
mat1.add_nuclide("Pu240", 1.669800e-04)
mat1.add_nuclide("Pu241", 3.936500e-05)
mat1.add_nuclide("Pu242", 1.044500e-05)
mat1.add_nuclide("Am241", 7.271700e-06)
mat1.add_element("C", 4.502400e-02)
mat1.add_nuclide("H1", 4.573600e-02)
mat1.add_nuclide("O16", 2.094800e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 5.664200e-02)
mat2.add_element("C", 3.564800e-02)
mat2.add_nuclide("O16", 1.427300e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# FUEL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# PLEX
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

root_universe = openmc.Universe(cells=[cell1, cell2])
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
