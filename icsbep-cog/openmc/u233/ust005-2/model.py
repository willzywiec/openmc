"""
U233-SOL-THERM-005 (Case 2) 233U(98.7)O2(NO3)2 @ H/U233=515; N/U=2.652
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# H/U-233 = 515
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 1.270700e-04)
mat1.add_nuclide("U234", 5.899400e-07)
mat1.add_nuclide("U238", 1.109600e-06)
mat1.add_nuclide("H1", 6.540300e-02)
mat1.add_nuclide("O16", 3.394200e-02)
mat1.add_element("N", 3.415200e-04)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Al-2S per Table 12
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 5.810800e-04)

# Water per Table 13
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.673500e-02)
mat3.add_nuclide("O16", 3.336800e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, r=12.7287)
surf2 = openmc.ZCylinder(surface_id=2, r=12.8578)
surf3 = openmc.ZCylinder(surface_id=3, r=28.0978, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1003, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1004, z0=25.6482)
surf2_zmin = openmc.ZPlane(surface_id=1005, z0=-0.1291)
surf2_zmax = openmc.ZPlane(surface_id=1006, z0=25.7773)
surf3_zmin = openmc.ZPlane(surface_id=1007, z0=-15.3691, boundary_type="vacuum")
surf3_zmax = openmc.ZPlane(surface_id=1008, z0=41.0173, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax)

# Al2S
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# Water
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3])
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
source.space = openmc.stats.Point((0.0, 0.0, 12.8))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
