"""
MST010-4: Exp. 140 with H/X=286 and 0.128 gGd/L and 0.2733 gB/L
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 3.418200e-08)
mat1.add_nuclide("Pu239", 1.980300e-04)
mat1.add_nuclide("Pu240", 1.345300e-05)
mat1.add_nuclide("Pu241", 1.063300e-06)
mat1.add_nuclide("Pu242", 1.008500e-07)
mat1.add_nuclide("U234", 2.811500e-08)
mat1.add_nuclide("U235", 3.060800e-06)
mat1.add_nuclide("U236", 5.575300e-08)
mat1.add_nuclide("U238", 4.575900e-04)
mat1.add_nuclide("Am241", 3.412900e-08)
mat1.add_nuclide("H1", 5.775900e-02)
mat1.add_element("N", 2.874800e-03)
mat1.add_nuclide("O16", 3.792100e-02)
mat1.add_nuclide("Gd152", 9.803900e-10)
mat1.add_nuclide("Gd154", 1.068600e-08)
mat1.add_nuclide("Gd155", 7.254900e-08)
mat1.add_nuclide("Gd156", 1.003400e-07)
mat1.add_nuclide("Gd157", 7.671500e-08)
mat1.add_nuclide("Gd158", 1.217600e-07)
mat1.add_nuclide("Gd160", 1.071600e-07)
mat1.add_nuclide("B10", 3.014000e-06)
mat1.add_nuclide("B11", 1.220800e-05)
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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Critical height
surf1 = openmc.ZPlane(surface_id=1, z0=21.13)
# Solution tank, inner
surf2 = openmc.ZCylinder(surface_id=2, r=30.515)
# Solution tank, outer
surf3 = openmc.ZCylinder(surface_id=3, r=30.594)
# Reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, r=49.53)
# Reflector tank, outer
surf5 = openmc.ZCylinder(surface_id=5, r=51.0, boundary_type="vacuum")
# Water height
surf6 = openmc.ZPlane(surface_id=6, z0=107.633)

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(surface_id=1006, z0=0.0)
surf2_zmax = openmc.ZPlane(surface_id=1007, z0=106.68)
surf3_zmin = openmc.ZPlane(surface_id=1008, z0=-0.635)
surf3_zmax = openmc.ZPlane(surface_id=1009, z0=107.633)
surf4_zmin = openmc.ZPlane(surface_id=1010, z0=-20.635)
surf4_zmax = openmc.ZPlane(surface_id=1011, z0=121.095)
surf5_zmin = openmc.ZPlane(surface_id=1012, z0=-21.905, boundary_type="vacuum")
surf5_zmax = openmc.ZPlane(surface_id=1013, z0=121.095, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & (-surf2 & +surf2_zmin & -surf2_zmax)

# Air
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & (-surf2 & +surf2_zmin & -surf2_zmax)

# SS304L
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# H2O
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & -surf6

# Air
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & +surf6

# Steel
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 10.565))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
