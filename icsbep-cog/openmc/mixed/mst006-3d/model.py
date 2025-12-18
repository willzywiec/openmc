"""
MST006-3: 3-D Model of Exp't No. 2242 with H/X=300 and 0.361 gGd/L
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 5.251000e-07)
mat1.add_nuclide("Pu239", 1.737500e-04)
mat1.add_nuclide("Pu240", 4.688200e-05)
mat1.add_nuclide("Pu241", 6.661400e-06)
mat1.add_nuclide("Pu242", 2.464100e-06)
mat1.add_nuclide("Am241", 1.436200e-06)
mat1.add_nuclide("U234", 6.525400e-08)
mat1.add_nuclide("U235", 2.675400e-06)
mat1.add_nuclide("U236", 2.555800e-07)
mat1.add_nuclide("U238", 5.407900e-04)
mat1.add_element("N", 3.810500e-03)
mat1.add_nuclide("O16", 3.915500e-02)
mat1.add_nuclide("H1", 5.497900e-02)
mat1.add_element("Fe", 1.833100e-05)
mat1.add_element("Cr", 5.211800e-06)
mat1.add_element("Ni", 2.565200e-06)
mat1.add_element("Ca", 1.051800e-06)
mat1.add_element("Co", 8.685800e-07)
mat1.add_element("Cu", 3.316900e-07)
mat1.add_element("Mn", 3.836600e-07)
mat1.add_element("Zn", 3.683800e-07)
mat1.add_element("Cd", 2.678600e-08)
mat1.add_element("Mg", 6.194300e-07)
mat1.add_element("B", 5.570300e-07)
mat1.add_element("Gd", 1.380200e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Air
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("O16", 1.126300e-05)
mat2.add_element("N", 4.198500e-05)

# Stainless
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.869400e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Mn", 1.731900e-03)
mat3.add_element("Si", 1.693900e-03)
mat3.add_element("C", 1.188200e-04)
mat3.add_element("P", 6.143900e-05)
mat3.add_element("S", 4.464000e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.673000e-02)
mat4.add_nuclide("O16", 3.336500e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Tank, inner
# surf1: Unsupported surface type "rev" with params ['3', '0.0', '0.0', '1.2', '35.03', '103.8', '35.03', 'tr', '0', '0', '0', '0', '0', '1', '0', '1', '0']
# Tank, outer
surf2 = openmc.ZCylinder(surface_id=2, x0=-0.5, y0=105.0, r=35.33)
# Reflector, outer
surf3 = openmc.ZCylinder(surface_id=3, x0=-30.5, y0=105.0, r=65.33, boundary_type="vacuum")
# Critical height
surf4 = openmc.ZPlane(surface_id=4, z0=41.14)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf4

# Air
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf4

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = -surf2

# H2O
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf2 & -surf3 & -surf4

# Air
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf2 & -surf3 & +surf4

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
source.space = openmc.stats.Point((0.0, 0.0, 20.57))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
