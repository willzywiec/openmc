"""
MIX-SOL-THERM-007-6: Exp. No. 134
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Experiment
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 2.346600e-08)
mat1.add_nuclide("Pu239", 1.826400e-04)
mat1.add_nuclide("Pu240", 1.118100e-05)
mat1.add_nuclide("Pu241", 7.164400e-07)
mat1.add_nuclide("Pu242", 1.192300e-07)
mat1.add_nuclide("U234", 2.743400e-08)
mat1.add_nuclide("U235", 3.027700e-06)
mat1.add_nuclide("U236", 5.440300e-08)
mat1.add_nuclide("U238", 4.464700e-04)
mat1.add_nuclide("Am241", 4.438600e-08)
mat1.add_nuclide("H1", 5.553600e-02)
mat1.add_element("N", 3.655700e-03)
mat1.add_nuclide("O16", 3.865400e-02)
mat1.add_nuclide("Gd152", 7.069400e-09)
mat1.add_nuclide("Gd154", 7.705700e-08)
mat1.add_nuclide("Gd155", 5.231400e-07)
mat1.add_nuclide("Gd156", 7.235500e-07)
mat1.add_nuclide("Gd157", 5.531800e-07)
mat1.add_nuclide("Gd158", 8.780200e-07)
mat1.add_nuclide("Gd160", 7.726900e-07)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.790200e-02)
mat2.add_element("Cr", 1.738400e-02)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Mn", 1.731900e-03)
mat2.add_element("Si", 1.693900e-03)
mat2.add_element("C", 1.188300e-04)

# Water at 25 C
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.665800e-02)
mat3.add_nuclide("O16", 3.332900e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Carbon steel
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 8.405800e-02)
mat4.add_element("C", 3.947900e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical solution height
surf1 = openmc.ZPlane(surface_id=1, z0=53.11902)
# Solution tank, inner
surf2 = openmc.ZCylinder(surface_id=2, x0=0.0, y0=107.0, r=30.515)
# Solution tank, inner
surf3 = openmc.ZCylinder(surface_id=3, x0=-0.635, y0=107.953, r=30.594)
# Reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, x0=-20.635, y0=107.953, r=49.53)
# Reflector tank, inner
surf5 = openmc.ZCylinder(surface_id=5, x0=-21.905, y0=107.953, r=50.8, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# SS3O4L
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3 & -surf5

# Water
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf3 & -surf4 & -surf5

# CSteel
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf4 & -surf5

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
source.space = openmc.stats.Point((0.0, 0.0, 26.55951))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
