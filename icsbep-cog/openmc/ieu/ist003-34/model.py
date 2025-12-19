"""
IST003-34: 30F4 solution in unreflected 16-inch diameter cylinder
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Sol'n No. 30F4
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 2.408100e-04)
mat1.add_nuclide("U234", 2.793500e-06)
mat1.add_nuclide("U236", 5.539600e-07)
mat1.add_nuclide("U238", 5.436500e-04)
mat1.add_nuclide("H1", 6.385500e-02)
mat1.add_element("F", 1.575600e-03)
mat1.add_nuclide("O16", 3.350300e-02)
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

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# r=a
surf1 = openmc.ZCylinder(surface_id=1, r=20.2833)
# r=c; Z1=-d; Z2=e+91.44
surf2 = openmc.ZCylinder(surface_id=2, r=20.4509)
# Z2=Hc=b
surf3 = openmc.ZPlane(surface_id=3, z0=21.4209)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=0.0)
surf1_zmax = openmc.ZPlane(z0=91.44)
surf2_zmin = openmc.ZPlane(z0=-1.614, boundary_type="vacuum")
surf2_zmax = openmc.ZPlane(z0=92.71, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf3

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2])
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
source.space = openmc.stats.Point((0.0, 0.0, 10.71045))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
