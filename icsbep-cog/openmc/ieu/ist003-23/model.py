"""
IST003-23: 30F15 solution in water reflected 12-inch diameter cylinder with Cadmium screen
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Sol'n No. 30F15
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.732000e-04)
mat1.add_nuclide("U234", 2.009300e-06)
mat1.add_nuclide("U236", 3.984400e-07)
mat1.add_nuclide("U238", 3.910200e-04)
mat1.add_nuclide("H1", 6.473200e-02)
mat1.add_element("F", 1.133300e-03)
mat1.add_nuclide("O16", 3.349900e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# UKAEA 70001
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 6.385500e-04)
mat2.add_element("Si", 1.536100e-03)
mat2.add_element("P", 6.190400e-05)
mat2.add_element("S", 5.979700e-05)
mat2.add_element("Ti", 8.009200e-04)
mat2.add_element("Cr", 1.613400e-02)
mat2.add_element("Mn", 8.725300e-04)
mat2.add_element("Fe", 6.185100e-02)
mat2.add_element("Ni", 6.125600e-03)

# Cadmium
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cd", 4.634000e-02)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.678500e-02)
mat4.add_nuclide("O16", 3.339300e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# r=a
surf1 = openmc.ZCylinder(surface_id=1, r=15.2435)
# r=c; Z1=-d; Z2=e+91.44
surf2 = openmc.ZCylinder(surface_id=2, r=15.4061)
# Z2=Hc=b
surf3 = openmc.ZCylinder(surface_id=3, r=38.1)
# SST/inner
surf4 = openmc.ZCylinder(surface_id=4, r=16.4061)
# Cd/inner
surf5 = openmc.ZCylinder(surface_id=5, r=16.5661)
# Cd/outer
surf6 = openmc.ZCylinder(surface_id=6, r=16.6561)
# SST/outer
surf7 = openmc.ZCylinder(surface_id=7, r=16.8161)
# Dummy/bcd
surf8 = openmc.ZCylinder(surface_id=8, r=39.9999, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1008, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1009, z0=91.44)
surf2_zmin = openmc.ZPlane(surface_id=1010, z0=-0.9525)
surf2_zmax = openmc.ZPlane(surface_id=1011, z0=93.345)
surf3_zmin = openmc.ZPlane(surface_id=1012, z0=0.0)
surf3_zmax = openmc.ZPlane(surface_id=1013, z0=32.1646)
surf7_zmin = openmc.ZPlane(surface_id=1014, z0=0.2)
surf7_zmax = openmc.ZPlane(surface_id=1015, z0=23.7)
surf8_zmin = openmc.ZPlane(surface_id=1016, z0=-1.9999, boundary_type="vacuum")
surf8_zmax = openmc.ZPlane(surface_id=1017, z0=99.9999, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax)

# H2O
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf4

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf4 & -surf5 & (-surf7 & +surf7_zmin & -surf7_zmax)

# Cd
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf5 & -surf6 & (-surf7 & +surf7_zmin & -surf7_zmax)

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf4 & (-surf7 & +surf7_zmin & -surf7_zmax)

# H2O
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = (-surf3 & +surf3_zmin & -surf3_zmax) & +surf4 & (+surf7 | -surf7_zmin | +surf7_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 16.0823))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
