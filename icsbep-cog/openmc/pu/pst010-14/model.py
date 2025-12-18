"""
PU-SOL-THERM-010 (Case 12-4) 0.759 kg Pu(97.15) @ H/X = 850 in a water reflected 12" diameter SS-347 cylinder
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 7.617200e-05)
mat1.add_nuclide("Pu240", 2.265500e-06)
mat1.add_element("N", 1.107200e-03)
mat1.add_nuclide("H1", 6.472000e-02)
mat1.add_nuclide("O16", 3.528500e-02)
mat1.add_element("Fe", 1.649800e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.038600e-02)
mat2.add_element("Cr", 1.667800e-02)
mat2.add_element("Ni", 9.850400e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.660200e-02)
mat3.add_nuclide("O16", 3.330100e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# VOID
cell1 = openmc.Cell(cell_id=1)
# SS347
cell2 = openmc.Cell(cell_id=2, fill=mat2)
# WATER
cell3 = openmc.Cell(cell_id=3, fill=mat3)
# SS347
cell4 = openmc.Cell(cell_id=4, fill=mat2)
# VOID
cell5 = openmc.Cell(cell_id=5)
# SOLN
cell6 = openmc.Cell(cell_id=6, fill=mat1)
# SS347
cell7 = openmc.Cell(cell_id=7, fill=mat2)
# WATER
cell8 = openmc.Cell(cell_id=8, fill=mat3)
root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8])
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
source.space = openmc.stats.Point((0.0, 0.0, 16.7))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
