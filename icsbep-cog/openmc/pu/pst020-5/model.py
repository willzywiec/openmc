"""
PU-SOL-THERM-020 (Case 5) 1.099 kg Pu(95.43) @ H/X = 483 in a water reflected 14" SS304L sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 7.270600e-09)
mat1.add_nuclide("Pu239", 1.146400e-04)
mat1.add_nuclide("Pu240", 5.608100e-06)
mat1.add_nuclide("Pu241", 3.721600e-07)
mat1.add_nuclide("Pu242", 1.072500e-08)
mat1.add_element("N", 4.517400e-03)
mat1.add_nuclide("H1", 5.579700e-02)
mat1.add_nuclide("O16", 3.943300e-02)
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
cell1.region = 

# SOLN
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = 

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = 

# H2O
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = 

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
