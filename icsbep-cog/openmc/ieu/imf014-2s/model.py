"""
IEU-MET-FAST-014: ZPR-9/3; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 4.478430e-03)
mat1.add_nuclide("U238", 1.704550e-02)
mat1.add_nuclide("U234", 4.338240e-05)
mat1.add_nuclide("U236", 2.079810e-05)
mat1.add_element("Cr", 4.721560e-05)
mat1.add_element("Ni", 1.703350e-05)
mat1.add_element("Fe", 1.577270e-04)
mat1.add_element("Al", 5.883590e-03)
mat1.add_element("C", 3.414770e-05)
mat1.add_element("Mo", 3.061760e-07)
mat1.add_element("Mn", 9.305290e-06)
mat1.add_element("Cu", 6.106580e-06)
mat1.add_element("H", 9.752030e-06)
mat1.add_element("Ti", 2.745290e-06)
mat1.add_element("Si", 2.838540e-05)
mat1.add_element("Mg", 1.336840e-04)
mat1.add_element("Cl", 1.682840e-05)
mat1.add_element("F", 4.985480e-05)
mat1.add_element("W", 2.132870e-02)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cr", 4.596920e-05)
mat2.add_element("Ni", 1.621680e-05)
mat2.add_element("Fe", 3.695510e-04)
mat2.add_element("Al", 5.450570e-02)
mat2.add_element("C", 1.051850e-05)
mat2.add_element("Mo", 2.914940e-07)
mat2.add_element("Mn", 1.093780e-05)
mat2.add_element("Cu", 6.561100e-06)
mat2.add_element("Ti", 3.153470e-06)
mat2.add_element("Si", 3.053380e-05)
mat2.add_element("Mg", 1.700310e-04)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cr", 4.579210e-05)
mat3.add_element("Ni", 1.630080e-05)
mat3.add_element("Fe", 5.624010e-04)
mat3.add_element("Al", 5.483640e-02)
mat3.add_element("C", 3.487890e-06)
mat3.add_element("Mo", 2.923120e-07)
mat3.add_element("Mn", 1.181020e-05)
mat3.add_element("Cu", 6.440020e-06)
mat3.add_element("Ti", 2.986250e-06)
mat3.add_element("Si", 2.998380e-05)
mat3.add_element("Mg", 1.535700e-04)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 6.250680e-06)
mat4.add_element("Fe", 6.592950e-05)
mat4.add_element("Al", 5.600540e-02)
mat4.add_element("C", 2.556050e-06)
mat4.add_element("Mn", 7.102730e-06)
mat4.add_element("Cu", 6.000840e-06)
mat4.add_element("Ti", 2.988580e-06)
mat4.add_element("Si", 2.878750e-05)
mat4.add_element("Mg", 1.561960e-04)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 4.394950e-06)
mat5.add_element("Fe", 7.164270e-06)
mat5.add_element("Al", 4.122060e-03)
mat5.add_element("Mn", 1.662710e-06)
mat5.add_element("Cu", 5.033610e-06)
mat5.add_element("Ti", 1.907020e-06)
mat5.add_element("Si", 2.442030e-05)
mat5.add_element("Mg", 4.702990e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CORE
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = 

# AR1
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = 

# AR2
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = 

# RR
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = 

# MTX
cell5 = openmc.Cell(cell_id=5, fill=mat5)
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0001))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
