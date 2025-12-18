"""
MST010-3: Exp. 139R with H/X=284 and 0.04 gGd/L and 0.3 gB/L
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 3.433600e-08)
mat1.add_nuclide("Pu239", 1.989200e-04)
mat1.add_nuclide("Pu240", 1.351300e-05)
mat1.add_nuclide("Pu241", 1.068100e-06)
mat1.add_nuclide("Pu242", 1.013000e-07)
mat1.add_nuclide("U234", 2.818900e-08)
mat1.add_nuclide("U235", 3.068900e-06)
mat1.add_nuclide("U236", 5.590000e-08)
mat1.add_nuclide("U238", 4.587900e-04)
mat1.add_nuclide("Am241", 2.609900e-08)
mat1.add_nuclide("H1", 5.772100e-02)
mat1.add_element("N", 2.816600e-03)
mat1.add_nuclide("O16", 3.775700e-02)
mat1.add_nuclide("Gd152", 3.063700e-10)
mat1.add_nuclide("Gd154", 3.339400e-09)
mat1.add_nuclide("Gd155", 2.267100e-08)
mat1.add_nuclide("Gd156", 3.135700e-08)
mat1.add_nuclide("Gd157", 2.397300e-08)
mat1.add_nuclide("Gd158", 3.805100e-08)
mat1.add_nuclide("Gd160", 3.348600e-08)
mat1.add_nuclide("B10", 3.308500e-06)
mat1.add_nuclide("B11", 1.340100e-05)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Air
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("O16", 1.054400e-05)
mat2.add_element("N", 3.920600e-05)

# SS304L
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.790200e-02)
mat3.add_element("Cr", 1.738400e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Mn", 1.731900e-03)
mat3.add_element("Si", 1.693900e-03)
mat3.add_element("C", 1.188300e-04)

# Carbon steel
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 8.405800e-02)
mat4.add_element("C", 3.947900e-03)

# Water
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.668900e-08)
mat5.add_nuclide("O16", 3.334400e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical height
surf1 = openmc.ZPlane(surface_id=1, z0=19.68)
# Solution tank, inner
surf2 = openmc.ZCylinder(surface_id=2, x0=0.0, y0=106.68, r=30.515)
# Solution tank, outer
surf3 = openmc.ZCylinder(surface_id=3, x0=-0.635, y0=107.633, r=30.594)
# Reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, x0=-20.635, y0=121.095, r=49.53)
# Reflector tank, outer
surf5 = openmc.ZCylinder(surface_id=5, x0=-21.905, y0=121.095, r=51.0, boundary_type="vacuum")
# Water height
surf6 = openmc.ZPlane(surface_id=6, z0=107.633)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# Air
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# SS304L
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

# H2O
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = +surf3 & -surf4 & -surf5 & -surf6

# Air
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf3 & -surf4 & -surf5 & +surf6

# Steel
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf4 & -surf5

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6])
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
source.space = openmc.stats.Point((0.0, 0.0, 9.84))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
