"""
IST003-19: 30F16 solution in a water reflected 12-inch diameter cylinder
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Sol'n No. 30F16
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.242600e-04)
mat1.add_nuclide("U234", 1.441500e-06)
mat1.add_nuclide("U236", 2.858400e-07)
mat1.add_nuclide("U238", 2.805200e-04)
mat1.add_nuclide("H1", 6.539300e-02)
mat1.add_element("F", 8.130100e-04)
mat1.add_nuclide("O16", 3.350900e-02)
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

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.678500e-02)
mat3.add_nuclide("O16", 3.339300e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# r=a
surf1 = openmc.ZCylinder(surface_id=1, r=15.2435)
# r=c; Z1=-d; Z2=e+91.44
surf2 = openmc.ZCylinder(surface_id=2, r=15.4061)
# Z2=Hc=b
surf3 = openmc.ZCylinder(surface_id=3, r=38.1)
# Arbitrary bcd
surf4 = openmc.ZCylinder(surface_id=4, r=99.9, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1004, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1005, z0=91.44)
surf2_zmin = openmc.ZPlane(surface_id=1006, z0=-0.9525)
surf2_zmax = openmc.ZPlane(surface_id=1007, z0=93.345)
surf3_zmin = openmc.ZPlane(surface_id=1008, z0=0.0)
surf3_zmax = openmc.ZPlane(surface_id=1009, z0=37.4113)
surf4_zmin = openmc.ZPlane(surface_id=1010, z0=-99.9, boundary_type="vacuum")
surf4_zmax = openmc.ZPlane(surface_id=1011, z0=99.9, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# H2O
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
source.space = openmc.stats.Point((0.0, 0.0, 18.70565))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
