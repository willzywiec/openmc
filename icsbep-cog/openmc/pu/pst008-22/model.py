"""
PU-SOL-THERM-008 (Case 22) 5.011 kg Pu(95.43) @ H/X = 93 in 14" SS304L sphere with 0.030" Cd + 4" concrete
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 3.521400e-08)
mat1.add_nuclide("Pu239", 5.552200e-04)
mat1.add_nuclide("Pu240", 2.715200e-05)
mat1.add_nuclide("Pu241", 1.848900e-06)
mat1.add_nuclide("Pu242", 5.194700e-08)
mat1.add_element("N", 5.264000e-03)
mat1.add_nuclide("H1", 5.167200e-02)
mat1.add_nuclide("O16", 4.016500e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cd", 4.634000e-02)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 1.737600e-02)
mat4.add_nuclide("O16", 4.529400e-02)
mat4.add_element("Mg", 7.619500e-04)
mat4.add_element("Al", 3.353300e-03)
mat4.add_element("Ca", 2.609500e-03)
mat4.add_element("Fe", 1.341700e-03)
mat4.add_element("Na", 1.141600e-04)
mat4.add_element("K", 4.356900e-04)
mat4.add_element("Mn", 2.767300e-05)
mat4.add_element("Si", 1.293100e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = 

# SOLN
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = 

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = 

# CADMIUM
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = 

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = 

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = 

# CONCRETE
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7])
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
