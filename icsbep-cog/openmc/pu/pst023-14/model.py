"""
PU-SOL-THERM-023 (Case 14)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Inner Sol'n
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 2.795200e-08)
mat1.add_nuclide("Pu239", 3.008100e-05)
mat1.add_nuclide("Pu240", 1.852200e-05)
mat1.add_nuclide("Pu241", 4.345200e-06)
mat1.add_nuclide("Pu242", 1.804900e-06)
mat1.add_nuclide("Am241", 2.050100e-07)
mat1.add_element("N", 2.516000e-03)
mat1.add_nuclide("H1", 6.065700e-02)
mat1.add_nuclide("O16", 3.672900e-02)
mat1.add_element("Fe", 4.507400e-07)
mat1.add_element("Cr", 1.210300e-07)
mat1.add_element("Ni", 5.957000e-08)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Driver Sol'n
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu238", 2.158800e-08)
mat2.add_nuclide("Pu239", 2.811100e-04)
mat2.add_nuclide("Pu240", 1.240300e-05)
mat2.add_nuclide("Pu241", 8.516100e-07)
mat2.add_nuclide("Pu242", 4.653300e-08)
mat2.add_nuclide("Am241", 1.753400e-07)
mat2.add_element("N", 2.417800e-03)
mat2.add_nuclide("H1", 6.073700e-02)
mat2.add_nuclide("O16", 3.701100e-02)
mat2.add_element("Fe", 4.205500e-06)
mat2.add_element("Cr", 1.129200e-06)
mat2.add_element("Ni", 5.558000e-07)
mat2.add_s_alpha_beta("c_H_in_H2O")

# SST Type
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.868600e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Mn", 1.731900e-03)
mat3.add_element("Si", 1.693900e-03)
mat3.add_element("C", 1.584400e-03)
mat3.add_element("P", 6.143900e-05)
mat3.add_element("S", 4.450400e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.670800e-02)
mat4.add_nuclide("O16", 3.335400e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# 1st Tank/Inner
surf1 = openmc.XCylinder(surface_id=1, r=7.0)
# 1st Tank/Outer
surf2 = openmc.XCylinder(surface_id=2, r=7.15)
# surf3: Unsupported surface type "revolution" with params ['3']
# 2nd Tank/Outer
surf4 = openmc.XCylinder(surface_id=4, r=18.3)
# 3rd Tank/Inner
surf5 = openmc.XCylinder(surface_id=5, r=54.6)
# 3rd Tank/Outer
surf6 = openmc.XCylinder(surface_id=6, r=55.0)
# = Hc (Table 1)
surf7 = openmc.XPlane(surface_id=7, x0=23.44)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1007, z0=3.45)
surf1_zmax = openmc.ZPlane(surface_id=1008, z0=17.45)
surf2_zmin = openmc.ZPlane(surface_id=1009, z0=3.3)
surf2_zmax = openmc.ZPlane(surface_id=1010, z0=17.6)
surf4_zmin = openmc.ZPlane(surface_id=1011, z0=-0.3)
surf4_zmax = openmc.ZPlane(surface_id=1012, z0=81.5)
surf5_zmin = openmc.ZPlane(surface_id=1013, z0=-25.9)
surf5_zmax = openmc.ZPlane(surface_id=1014, z0=50.8)
surf6_zmin = openmc.ZPlane(surface_id=1015, z0=-26.2)
surf6_zmax = openmc.ZPlane(surface_id=1016, z0=51.2)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLNI
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax)

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# SOLND
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (+surf2 | -surf2_zmin | +surf2_zmax) & -surf3 & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf7

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf3 & (-surf4 & +surf4_zmin & -surf4_zmax)

# WATER
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & -surf7

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 11.7))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
