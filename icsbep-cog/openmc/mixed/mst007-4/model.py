"""
MIX-SOL-THERM-007-4: Exp. No. 131
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Experiment
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 2.319300e-08)
mat1.add_nuclide("Pu239", 1.805100e-04)
mat1.add_nuclide("Pu240", 1.105100e-05)
mat1.add_nuclide("Pu241", 7.081000e-07)
mat1.add_nuclide("Pu242", 1.178500e-07)
mat1.add_nuclide("U234", 2.706400e-08)
mat1.add_nuclide("U235", 2.986800e-06)
mat1.add_nuclide("U236", 5.366800e-08)
mat1.add_nuclide("U238", 4.404400e-04)
mat1.add_nuclide("Am241", 4.386900e-08)
mat1.add_nuclide("H1", 5.598100e-02)
mat1.add_element("N", 3.546900e-03)
mat1.add_nuclide("O16", 3.859700e-02)
mat1.add_nuclide("Gd152", 4.450000e-09)
mat1.add_nuclide("Gd154", 4.850500e-08)
mat1.add_nuclide("Gd155", 3.293000e-07)
mat1.add_nuclide("Gd156", 4.554500e-07)
mat1.add_nuclide("Gd157", 3.482100e-07)
mat1.add_nuclide("Gd158", 5.526900e-07)
mat1.add_nuclide("Gd160", 4.863800e-07)
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
surf1 = openmc.ZPlane(surface_id=1, z0=33.41878)
# Solution tank, inner
surf2 = openmc.ZCylinder(surface_id=2, r=30.515)
# Solution tank, inner
surf3 = openmc.ZCylinder(surface_id=3, r=30.594)
# Reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, r=49.53)
# Reflector tank, inner
surf5 = openmc.ZCylinder(surface_id=5, r=50.8, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(surface_id=1005, z0=0.0)
surf2_zmax = openmc.ZPlane(surface_id=1006, z0=107.0)
surf3_zmin = openmc.ZPlane(surface_id=1007, z0=-0.635)
surf3_zmax = openmc.ZPlane(surface_id=1008, z0=107.953)
surf4_zmin = openmc.ZPlane(surface_id=1009, z0=-20.635)
surf4_zmax = openmc.ZPlane(surface_id=1010, z0=107.953)
surf5_zmin = openmc.ZPlane(surface_id=1011, z0=-21.905, boundary_type="vacuum")
surf5_zmax = openmc.ZPlane(surface_id=1012, z0=107.953, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & (-surf2 & +surf2_zmin & -surf2_zmax)

# SS3O4L
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# Water
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# CSteel
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 16.70939))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
