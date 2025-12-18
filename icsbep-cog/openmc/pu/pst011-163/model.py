"""
PU-SOL-THERM-011 (Case 16-3) 1.301 kg Pu(95.83) @ H/X = 691 in a bare 16" SS347 sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 9.205000e-05)
mat1.add_nuclide("Pu240", 3.988800e-06)
mat1.add_element("N", 1.583100e-03)
mat1.add_nuclide("H1", 6.365200e-02)
mat1.add_nuclide("O16", 3.597600e-02)
mat1.add_element("Fe", 1.337100e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.038600e-02)
mat2.add_element("Cr", 1.667800e-02)
mat2.add_element("Ni", 9.850400e-03)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
# SS347
cell2 = openmc.Cell(cell_id=2, fill=mat2)
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
