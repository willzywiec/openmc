"""
PU-SOL-THERM-023 (Case 34)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Driver Sol'n
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu238", 2.158700e-08)
mat2.add_nuclide("Pu239", 2.811000e-04)
mat2.add_nuclide("Pu240", 1.240300e-05)
mat2.add_nuclide("Pu241", 8.632100e-07)
mat2.add_nuclide("Pu242", 4.653100e-08)
mat2.add_nuclide("Am241", 1.637000e-07)
mat2.add_element("N", 2.417800e-03)
mat2.add_nuclide("H1", 6.073800e-02)
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

materials = openmc.Materials([mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# surf3: Unsupported surface type "revolution" with params ['3']
# 2nd Tank/Outer
surf4 = openmc.XCylinder(surface_id=4, r=18.3)
# 3rd Tank/Inner
surf5 = openmc.XCylinder(surface_id=5, r=54.6)
# 3rd Tank/Outer
surf6 = openmc.XCylinder(surface_id=6, r=55.0)
# = Hc (Table 1)
surf7 = openmc.XPlane(surface_id=7, x0=19.08)

# Z-plane surfaces for bounded cylinders
surf4_zmin = openmc.ZPlane(z0=-0.3)
surf4_zmax = openmc.ZPlane(z0=81.5)
surf5_zmin = openmc.ZPlane(z0=-25.9)
surf5_zmax = openmc.ZPlane(z0=50.8)
surf6_zmin = openmc.ZPlane(z0=-26.2)
surf6_zmax = openmc.ZPlane(z0=51.2)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLND
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = -surf3 & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf7

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = +surf3 & (-surf4 & +surf4_zmin & -surf4_zmax)

# WATER
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & -surf7

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 9.5))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
