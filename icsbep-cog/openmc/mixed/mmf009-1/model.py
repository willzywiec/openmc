"""
MixMF009-1: 13.710 kg d-Pu and 6.952 kg (0.75 cm) HEU
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu - 1st layer
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.523400e-02)
mat1.add_nuclide("Pu240", 6.441000e-04)
mat1.add_element("Ga", 2.217600e-03)
mat1.add_element("C", 2.909200e-04)
mat1.add_element("Ni", 4.141500e-03)

# Pu - 2nd layer
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu239", 3.682600e-02)
mat2.add_nuclide("Pu240", 6.732000e-04)
mat2.add_element("Ga", 2.317800e-03)
mat2.add_element("C", 3.040600e-04)
mat2.add_element("Ni", 1.572200e-03)

# Pu - 3rd layer
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Pu239", 3.657900e-02)
mat3.add_nuclide("Pu240", 6.687500e-04)
mat3.add_element("Ga", 2.315500e-03)
mat3.add_element("C", 3.020500e-04)
mat3.add_element("Ni", 1.933000e-03)

# Pu - 4th layer
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Pu239", 3.651200e-02)
mat4.add_nuclide("Pu240", 6.673900e-04)
mat4.add_element("Ga", 2.297800e-03)
mat4.add_element("C", 2.260800e-04)
mat4.add_element("Ni", 2.305600e-03)

# Pu - 5th layer
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Pu239", 3.657600e-02)
mat5.add_nuclide("Pu240", 6.687800e-04)
mat5.add_element("Ga", 2.328600e-03)
mat5.add_element("C", 3.020600e-04)
mat5.add_element("Ni", 1.863100e-03)

# Pu - 6th layer
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("Pu239", 3.647100e-02)
mat6.add_nuclide("Pu240", 6.666500e-04)
mat6.add_element("Ga", 2.282300e-03)
mat6.add_element("C", 3.011000e-04)
mat6.add_element("Ni", 1.971500e-03)

# HEU - 7th layer
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("U234", 5.050400e-04)
mat7.add_nuclide("U235", 4.130600e-02)
mat7.add_nuclide("U238", 4.213700e-03)
mat7.add_element("Cu", 8.043200e-04)
mat7.add_element("C", 3.611400e-04)
mat7.add_element("Ni", 5.557200e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Cavity
# surf1: Unsupported surface type "s" with params ['1.084']
# Pu -- 1st layer
# surf2: Unsupported surface type "s" with params ['1.400']
# Pu -- 2nd layer
# surf3: Unsupported surface type "s" with params ['3.150']
# Pu -- 3rd layer
# surf4: Unsupported surface type "s" with params ['4.020']
# Pu -- 4th layer
# surf5: Unsupported surface type "s" with params ['4.660']
# Pu -- 5th layer
# surf6: Unsupported surface type "s" with params ['5.350']
# Pu -- 6th layer
# surf7: Unsupported surface type "s" with params ['6.000']
# HEU - 7th layer
# surf8: Unsupported surface type "s" with params ['6.750']

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = 

# Pu1
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = 

# Pu2
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = 

# Pu3
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = 

# Pu4
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = 

# Pu5
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = 

# Pu6
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = 

# HEU7
cell8 = openmc.Cell(cell_id=8, fill=mat7)
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
source.space = openmc.stats.Box((-2.3, -2.3, -2.3), (2.3, 2.3, 2.3))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
