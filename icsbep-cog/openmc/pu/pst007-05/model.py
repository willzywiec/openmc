"""
PU-SOL-THERM-007 (Case 5) 1.241 kg Pu(95.43) @ H/X = 267 in a water reflected 11.5" SS-304L sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.520900e-08)
mat1.add_nuclide("Pu239", 2.398300e-04)
mat1.add_nuclide("Pu240", 1.173400e-05)
mat1.add_nuclide("Pu241", 7.634800e-07)
mat1.add_nuclide("Pu242", 2.243600e-08)
mat1.add_element("N", 1.189800e-03)
mat1.add_nuclide("H1", 6.416100e-02)
mat1.add_nuclide("O16", 3.556000e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.665500e-02)
mat3.add_nuclide("O16", 3.332700e-02)
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
# SOLN
cell2 = openmc.Cell(cell_id=2, fill=mat1)
# SS347
cell3 = openmc.Cell(cell_id=3, fill=mat2)
# WATER
cell4 = openmc.Cell(cell_id=4, fill=mat3)
root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4])
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
