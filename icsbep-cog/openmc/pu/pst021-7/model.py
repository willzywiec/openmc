"""
PU-SOL-THERM-021 (Case 7) 1.213 kg Pu(95.4) @ H/X = 700 bare sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 5.919700e-09)
mat1.add_nuclide("Pu239", 9.336600e-05)
mat1.add_nuclide("Pu240", 4.568000e-06)
mat1.add_nuclide("Pu241", 2.757300e-07)
mat1.add_nuclide("Pu242", 8.732400e-09)
mat1.add_element("N", 6.338200e-04)
mat1.add_nuclide("H1", 6.551500e-02)
mat1.add_nuclide("O16", 3.453800e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

root_universe = openmc.Universe(cells=[cell1])
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
