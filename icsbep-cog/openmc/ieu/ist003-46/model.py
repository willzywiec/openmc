"""
IST003-46: 30F17 solution in unreflected 12-inch diameter cylinder with Cadmium screen
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Sol'n No. 30F17
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.491200e-04)
mat1.add_nuclide("U234", 1.729900e-06)
mat1.add_nuclide("U236", 3.430300e-07)
mat1.add_nuclide("U238", 3.366500e-04)
mat1.add_nuclide("H1", 6.495200e-02)
mat1.add_element("F", 9.756700e-04)
mat1.add_nuclide("O16", 3.345200e-02)
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

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# r=a
surf1 = openmc.ZCylinder(surface_id=1, r=15.2435)
# r=c; Z1=-d; Z2=e+91.44
surf2 = openmc.ZCylinder(surface_id=2, r=15.4061)
# Z2=Hc=b
surf3 = openmc.ZPlane(surface_id=3, z0=50.3429)
# SST/inner
surf4 = openmc.ZCylinder(surface_id=4, r=16.4061)
# Cd/inner
surf5 = openmc.ZCylinder(surface_id=5, r=16.5661)
# Cd/outer
surf6 = openmc.ZCylinder(surface_id=6, r=16.6561)
# SST/outer
surf7 = openmc.ZCylinder(surface_id=7, r=16.8161)
# Dummy/bcd
surf8 = openmc.ZCylinder(surface_id=8, r=19.9999, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1008, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1009, z0=91.44)
surf2_zmin = openmc.ZPlane(surface_id=1010, z0=-0.9525)
surf2_zmax = openmc.ZPlane(surface_id=1011, z0=93.345)
surf7_zmin = openmc.ZPlane(surface_id=1012, z0=0.2)
surf7_zmax = openmc.ZPlane(surface_id=1013, z0=23.7)
surf8_zmin = openmc.ZPlane(surface_id=1014, z0=-1.9999, boundary_type="vacuum")
surf8_zmax = openmc.ZPlane(surface_id=1015, z0=99.9999, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf3

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf4 & -surf5 & (-surf7 & +surf7_zmin & -surf7_zmax)

# Cd
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf5 & -surf6 & (-surf7 & +surf7_zmin & -surf7_zmax)

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf6 & (-surf7 & +surf7_zmin & -surf7_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5])
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
source.space = openmc.stats.Point((0.0, 0.0, 25.17145))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
