"""
IEU-MET-FAST-014: ZPR-9/2; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 4.499850e-03)
mat1.add_nuclide("U238", 2.415980e-02)
mat1.add_nuclide("U234", 4.344660e-05)
mat1.add_nuclide("U236", 2.082870e-05)
mat1.add_element("Cr", 5.171910e-05)
mat1.add_element("Ni", 1.889220e-05)
mat1.add_element("Fe", 1.738920e-04)
mat1.add_element("Al", 5.871340e-03)
mat1.add_element("C", 4.522890e-05)
mat1.add_element("Mo", 3.395870e-07)
mat1.add_element("Mn", 9.674670e-06)
mat1.add_element("Cu", 6.126960e-06)
mat1.add_element("H", 1.292910e-05)
mat1.add_element("Ti", 2.739690e-06)
mat1.add_element("Si", 2.837880e-05)
mat1.add_element("Mg", 1.337750e-04)
mat1.add_element("Cl", 2.235380e-05)
mat1.add_element("F", 6.621900e-05)
mat1.add_element("W", 1.222990e-02)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cr", 6.631720e-05)
mat2.add_element("Ni", 2.470270e-05)
mat2.add_element("Fe", 3.856220e-04)
mat2.add_element("Al", 5.377290e-02)
mat2.add_element("C", 8.169550e-06)
mat2.add_element("Mo", 6.435160e-07)
mat2.add_element("Mn", 1.196030e-05)
mat2.add_element("Cu", 6.655590e-06)
mat2.add_element("Ti", 3.050890e-06)
mat2.add_element("Si", 3.079960e-05)
mat2.add_element("Mg", 1.599240e-04)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cr", 7.785250e-05)
mat3.add_element("Ni", 2.952370e-05)
mat3.add_element("Fe", 2.627000e-04)
mat3.add_element("Al", 5.372260e-02)
mat3.add_element("C", 7.962820e-07)
mat3.add_element("Mo", 8.639680e-07)
mat3.add_element("Mn", 1.248100e-05)
mat3.add_element("Cu", 6.700240e-06)
mat3.add_element("Ti", 2.982710e-06)
mat3.add_element("Si", 3.094030e-05)
mat3.add_element("Mg", 1.532210e-04)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 6.179140e-06)
mat4.add_element("Fe", 9.922260e-06)
mat4.add_element("Al", 5.655960e-02)
mat4.add_element("Mn", 7.074820e-06)
mat4.add_element("Cu", 5.919340e-06)
mat4.add_element("Ti", 2.957480e-06)
mat4.add_element("Si", 2.839170e-05)
mat4.add_element("Mg", 1.554160e-04)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 6.318820e-06)
mat5.add_element("Fe", 1.205250e-04)
mat5.add_element("Al", 5.546210e-02)
mat5.add_element("C", 5.047790e-06)
mat5.add_element("Mn", 7.125450e-06)
mat5.add_element("Cu", 6.079450e-06)
mat5.add_element("Ti", 3.017980e-06)
mat5.add_element("Si", 2.916940e-05)
mat5.add_element("Mg", 1.568650e-04)

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

# RR1
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = 

# RR2
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
