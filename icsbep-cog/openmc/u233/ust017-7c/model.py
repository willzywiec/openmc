"""
U233-SOL-THERM-017-7: 0.985 kg 233U @ H/X=546.2 and N/U=2.15 (Exp't No. 249c)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Sol'n No. 32a
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 1.201500e-04)
mat1.add_nuclide("U234", 1.284200e-06)
mat1.add_nuclide("U235", 3.175500e-08)
mat1.add_nuclide("U236", 1.216100e-09)
mat1.add_nuclide("U238", 1.671400e-06)
mat1.add_nuclide("H1", 6.562500e-02)
mat1.add_element("N", 2.644300e-04)
mat1.add_nuclide("O16", 3.384600e-02)
mat1.add_element("Th", 1.546400e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Aluminum-2S
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 5.810800e-04)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.665800e-02)
mat3.add_nuclide("O16", 3.332900e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Aluminum-1100
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 5.993000e-02)
mat4.add_element("Si", 2.253200e-04)
mat4.add_element("Mn", 1.212500e-05)
mat4.add_element("Fe", 1.133100e-04)
mat4.add_element("Cu", 2.620600e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Al-2S/Fill-Pipe/Inner
surf1 = openmc.ZCylinder(surface_id=1, x0=5.08, y0=0.0, r=2.62509)
# Al-2S/Fill-Pipe/Outer
surf2 = openmc.ZCylinder(surface_id=2, x0=5.08, y0=0.0, r=3.01625)
# Al-2S/Soln-Tank/Inner
surf3 = openmc.ZCylinder(surface_id=3, x0=-11.09275, y0=0.0, r=19.062)
# Al-2S/Soln-Tank/Outer
surf4 = openmc.ZCylinder(surface_id=4, x0=-11.09275, y0=0.0, r=19.189)
# Al-2S/Soln-Tank/Lid
surf5 = openmc.ZCylinder(surface_id=5, x0=-11.09275, y0=0.0, r=22.225)
# Al-1100/Tank/Inner
surf6 = openmc.ZCylinder(surface_id=6, r=45.72)
# Al-1100/Tank/Outer
surf7 = openmc.ZCylinder(surface_id=7, r=46.0375)
# Solution/Hc
surf8 = openmc.ZPlane(surface_id=8, z0=18.085)
# Water/Hr
surf9 = openmc.ZPlane(surface_id=9, z0=38.43)

# Z-plane surfaces for bounded cylinders
surf6_zmin = openmc.ZPlane(surface_id=1009, z0=-25.47)
surf6_zmax = openmc.ZPlane(surface_id=1010, z0=101.53)
surf7_zmin = openmc.ZPlane(surface_id=1011, z0=-26.74)
surf7_zmax = openmc.ZPlane(surface_id=1012, z0=101.53)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# ALP
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# SOL
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = +surf1 & +surf2 & -surf3 & -surf4 & -surf8

# AlT
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf1 & +surf2 & +surf3 & -surf4

# ALL
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf3 & +surf4 & -surf5

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf2 & +surf4 & (-surf6 & +surf6_zmin & -surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax) & -surf9

# TANK
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf2 & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7])
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
source.space = openmc.stats.Point((0.0, 0.0, 9.0425))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
