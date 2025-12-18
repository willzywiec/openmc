"""
PU-SOL-THERM-010 (Case 11-1) 0.854 kg Pu(97.15) @ H/X = 485 in a water reflected ll" diameter SS-347 cylinder
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 1.332100e-04)
mat1.add_nuclide("Pu240", 3.891500e-06)
mat1.add_element("N", 1.165500e-03)
mat1.add_nuclide("H1", 6.461000e-02)
mat1.add_nuclide("O16", 3.549300e-02)
mat1.add_element("Fe", 2.771300e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.038600e-02)
mat2.add_element("Cr", 1.667800e-02)
mat2.add_element("Ni", 9.850400e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.662300e-02)
mat3.add_nuclide("O16", 3.331200e-02)
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

# SS347
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = 

# WATER
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = 

# SS347
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = 

# VOID
cell5 = openmc.Cell(cell_id=5)
cell5.region = 

# SOLN
cell6 = openmc.Cell(cell_id=6, fill=mat1)
cell6.region = 

# SS347
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = 

# WATER
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = 

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
source.space = openmc.stats.Point((0.0, 0.0, 13.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
