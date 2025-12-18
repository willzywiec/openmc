"""
PU-SOL-THERM-020 (Case 8) 1.591 kg Pu(95.43) @ H/X = 360 in a 14" SS304L sphere + 0.030" Cd in water
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.053400e-08)
mat1.add_nuclide("Pu239", 1.661000e-04)
mat1.add_nuclide("Pu240", 8.125200e-06)
mat1.add_nuclide("Pu241", 5.392000e-07)
mat1.add_nuclide("Pu242", 1.553900e-08)
mat1.add_element("N", 2.951500e-03)
mat1.add_nuclide("H1", 5.994600e-02)
mat1.add_nuclide("O16", 3.770100e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cd", 4.633000e-02)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.665500e-02)
mat4.add_nuclide("O16", 3.332700e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

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

# CD
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = 

# H2O
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5])
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
