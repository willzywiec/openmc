"""
PU-MET-FAST-036; 13.693 kg d-Pu(98) in 0.05 cm Cd plus 2.3 cm CH2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.593200e-02)
mat1.add_nuclide("Pu240", 6.568500e-04)
mat1.add_element("Ga", 2.261500e-03)
mat1.add_element("C", 2.966700e-04)
mat1.add_element("Ni", 4.223500e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu239", 3.682600e-02)
mat2.add_nuclide("Pu240", 6.732000e-04)
mat2.add_element("Ga", 2.317800e-03)
mat2.add_element("C", 3.040600e-04)
mat2.add_element("Ni", 1.572200e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Pu239", 3.657900e-02)
mat3.add_nuclide("Pu240", 6.687500e-04)
mat3.add_element("Ga", 2.315500e-03)
mat3.add_element("C", 3.020500e-04)
mat3.add_element("Ni", 1.933000e-03)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Pu239", 3.651200e-02)
mat4.add_nuclide("Pu240", 6.673900e-04)
mat4.add_element("Ga", 2.297800e-03)
mat4.add_element("C", 2.260800e-04)
mat4.add_element("Ni", 2.305600e-03)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Pu239", 3.657600e-02)
mat5.add_nuclide("Pu240", 6.687800e-04)
mat5.add_element("Ga", 2.328600e-03)
mat5.add_element("C", 3.020600e-04)
mat5.add_element("Ni", 1.863100e-03)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("Pu239", 3.647100e-02)
mat6.add_nuclide("Pu240", 6.666500e-04)
mat6.add_element("Ga", 2.282300e-03)
mat6.add_element("C", 3.011000e-04)
mat6.add_element("Ni", 1.971500e-03)

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Cd", 4.634000e-02)

mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_nuclide("H1", 7.384500e-02)
mat8.add_element("C", 3.692200e-02)
mat8.add_s_alpha_beta("c_H_in_CH2")

mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_nuclide("H1", 7.899700e-02)
mat9.add_element("C", 3.949800e-02)
mat9.add_s_alpha_beta("c_H_in_CH2")

mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("H1", 7.899600e-02)
mat10.add_element("C", 3.949800e-02)
mat10.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=1.16)
surf2 = openmc.Sphere(surface_id=2, r=1.40)
surf3 = openmc.Sphere(surface_id=3, r=3.15)
surf4 = openmc.Sphere(surface_id=4, r=4.02)
surf5 = openmc.Sphere(surface_id=5, r=4.66)
surf6 = openmc.Sphere(surface_id=6, r=5.35)
surf7 = openmc.Sphere(surface_id=7, r=6.00)
surf8 = openmc.Sphere(surface_id=8, r=6.05)
surf9 = openmc.Sphere(surface_id=9, r=6.75)
surf10 = openmc.Sphere(surface_id=10, r=7.55)
surf11 = openmc.Sphere(surface_id=11, r=8.35, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# VOID
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf1

# LAYER1
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf1 & -surf2

# LAYER2
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & -surf3

# LAYER3
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf3 & -surf4

# LAYER4
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf4 & -surf5

# LAYER5
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = +surf5 & -surf6

# LAYER6
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = +surf6 & -surf7

# CADMIUM
cell8 = openmc.Cell(cell_id=8, fill=mat7)
cell8.region = +surf7 & -surf8

# POLY1
cell9 = openmc.Cell(cell_id=9, fill=mat8)
cell9.region = +surf8 & -surf9

# POLY2
cell10 = openmc.Cell(cell_id=10, fill=mat9)
cell10.region = +surf9 & -surf10

# POLY3
cell11 = openmc.Cell(cell_id=11, fill=mat10)
cell11.region = +surf10 & -surf11

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11])
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
