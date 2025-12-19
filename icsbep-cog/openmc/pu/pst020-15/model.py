"""
PU-SOL-THERM-020 (Case 15) 1.572 kg Pu(95.43) @ H/X = 358 in a 14" SS304L sphere + 0.030" Cd in water
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.047300e-08)
mat1.add_nuclide("Pu239", 1.651400e-04)
mat1.add_nuclide("Pu240", 8.078400e-06)
mat1.add_nuclide("Pu241", 5.360900e-07)
mat1.add_nuclide("Pu242", 1.545000e-08)
mat1.add_element("N", 3.043700e-03)
mat1.add_nuclide("H1", 5.928800e-02)
mat1.add_nuclide("O16", 3.760100e-02)
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

# SST/Inner/Table 5
surf1 = openmc.Sphere(surface_id=1, r=17.5872)
# SST/Outer/Table 5
surf2 = openmc.Sphere(surface_id=2, r=17.6990)
# Cd/Outer/Table 5
surf3 = openmc.Sphere(surface_id=3, r=17.7752)
# H2O/Outer/Table 5
surf4 = openmc.Sphere(surface_id=4, r=47.7752, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# CD
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

# H2O
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf3 & -surf4

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
