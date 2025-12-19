"""
U233-SOL-THERM-016-25: 1.667 kg 233U @ H/X=347.2 and N/U=2.15 (Exp't No. 178)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Sol'n No. 21
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 1.873100e-04)
mat1.add_nuclide("U234", 2.002000e-06)
mat1.add_nuclide("U235", 4.950400e-08)
mat1.add_nuclide("U236", 1.895900e-09)
mat1.add_nuclide("U238", 2.605600e-06)
mat1.add_nuclide("H1", 6.503200e-02)
mat1.add_element("N", 4.122400e-04)
mat1.add_nuclide("O16", 3.412700e-02)
mat1.add_element("Th", 2.410800e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Aluminum-2S
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 5.810800e-04)

# Stainless
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 3.184800e-04)
mat3.add_element("Si", 1.702500e-03)
mat3.add_element("P", 6.946800e-05)
mat3.add_element("Cr", 1.747200e-02)
mat3.add_element("Mn", 1.740700e-03)
mat3.add_element("Fe", 5.854300e-02)
mat3.add_element("Ni", 7.739800e-03)

# Regualr
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 3.472200e-04)
mat4.add_element("Al", 1.745400e-03)
mat4.add_element("Ca", 1.520600e-03)
mat4.add_nuclide("O16", 4.605600e-02)
mat4.add_element("Si", 1.662000e-02)
mat4.add_nuclide("H1", 1.374200e-02)
mat4.add_element("Na", 1.747200e-03)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Concrete/Inner (w/Origin on the Tank C/L)
surf1 = openmc.model.RectangularParallelepiped(-775.7414, 138.65859999999998, -470.9414, 443.4586, -257.2005, 657.5297)
# Concrete/Outer (w/Origin on the Tank C/L)
surf2 = openmc.model.RectangularParallelepiped(-928.1414, 199.61860000000001, -623.3414, 595.8586, -409.6005, 718.4897000000001, boundary_type="vacuum")
# SST/Tank/Inner
surf3 = openmc.ZCylinder(surface_id=3, r=77.3684)
# SST/Tank/Outer
surf4 = openmc.ZCylinder(surface_id=4, r=77.6986)
# Al-2S/Fill-Pipe/Inner
surf5 = openmc.ZCylinder(surface_id=5, x0=16.17275, y0=0.0, r=2.62509)
# Al-2S/Fill-Pipe/Outer
surf6 = openmc.ZCylinder(surface_id=6, x0=16.17275, y0=0.0, r=3.01625)
# Al-2S/Soln-Tank/Inner
surf7 = openmc.ZCylinder(surface_id=7, r=19.062)
# Al-2S/Soln-Tank/Outer
surf8 = openmc.ZCylinder(surface_id=8, r=19.189)
# Al-2S/Soln-Tank/Lid
surf9 = openmc.ZCylinder(surface_id=9, r=22.225)
# Solution/Hc
surf10 = openmc.ZPlane(surface_id=10, z0=19.243)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1010, z0=-48.26)
surf3_zmax = openmc.ZPlane(surface_id=1011, z0=261.2136)
surf4_zmin = openmc.ZPlane(surface_id=1012, z0=-48.5902)
surf4_zmax = openmc.ZPlane(surface_id=1013, z0=261.2136)
surf7_zmin = openmc.ZPlane(surface_id=1014, z0=0.0)
surf7_zmax = openmc.ZPlane(surface_id=1015, z0=181.61)
surf8_zmin = openmc.ZPlane(surface_id=1016, z0=-1.27)
surf8_zmax = openmc.ZPlane(surface_id=1017, z0=181.61)
surf9_zmin = openmc.ZPlane(surface_id=1018, z0=181.61)
surf9_zmax = openmc.ZPlane(surface_id=1019, z0=181.737)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf7 & +surf7_zmin & -surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax) & -surf10

# AlT
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf5 & +surf6 & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# ALL
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax) & (-surf9 & +surf9_zmin & -surf9_zmax)

# SOL
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = -surf5 & -surf6 & (+surf7 | -surf7_zmin | +surf7_zmax)

# ALP
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf5 & -surf6 & (+surf7 | -surf7_zmin | +surf7_zmax)

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# CNC
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf1 & -surf2

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
source.space = openmc.stats.Point((0.0, 0.0, 9.6215))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
