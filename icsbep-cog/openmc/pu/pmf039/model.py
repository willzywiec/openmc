"""
PU-MET-FAST-039; 17.718 kg d-Pu(98) in 4.25 Duralumin
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.658100e-02)
mat1.add_nuclide("Pu240", 6.688000e-04)
mat1.add_element("Ga", 2.315200e-03)
mat1.add_element("C", 3.020700e-04)
mat1.add_element("Ni", 1.921200e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu239", 3.651200e-02)
mat2.add_nuclide("Pu240", 6.673900e-04)
mat2.add_element("Ga", 2.297800e-03)
mat2.add_element("C", 2.260800e-04)
mat2.add_element("Ni", 2.305600e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Pu239", 3.657600e-02)
mat3.add_nuclide("Pu240", 6.687800e-04)
mat3.add_element("Ga", 2.328600e-03)
mat3.add_element("C", 3.020600e-04)
mat3.add_element("Ni", 1.863100e-03)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Pu239", 3.647100e-02)
mat4.add_nuclide("Pu240", 6.666500e-04)
mat4.add_element("Ga", 2.282300e-03)
mat4.add_element("C", 3.011000e-04)
mat4.add_element("Ni", 1.971500e-03)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Pu239", 3.670700e-02)
mat5.add_nuclide("Pu240", 6.711000e-04)
mat5.add_element("Ga", 2.323600e-03)
mat5.add_element("C", 3.031100e-04)
mat5.add_element("Ni", 1.648300e-03)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Al", 5.564500e-02)
mat6.add_element("Fe", 1.018300e-03)
mat6.add_element("Cu", 1.048400e-03)

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Al", 5.349700e-02)
mat7.add_element("Fe", 9.790200e-04)
mat7.add_element("Cu", 1.007900e-03)

mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 5.155700e-02)
mat8.add_element("Fe", 9.435300e-04)
mat8.add_element("Cu", 9.713600e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# VOID
cell1 = openmc.Cell(cell_id=1)
cell1.region = 

# LAYER1
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = 

# LAYER2
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = 

# LAYER3
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = 

# LAYER4
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = 

# LAYER5
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = 

# ALUM1
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = 

# ALUM2
cell8 = openmc.Cell(cell_id=8, fill=mat7)
cell8.region = 

# ALUM3
cell9 = openmc.Cell(cell_id=9, fill=mat8)
cell9.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9])
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
