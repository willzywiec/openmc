"""
MIX-COMP-FAST-001; ZPR-6 Assembly 7; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# IC1
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu240", 1.176240e-04)
mat1.add_nuclide("Pu241", 1.338360e-05)
mat1.add_nuclide("U235", 1.260650e-05)
mat1.add_nuclide("U238", 5.792900e-03)
mat1.add_nuclide("Pu239", 8.865280e-04)
mat1.add_nuclide("Pu238", 3.336960e-07)
mat1.add_nuclide("Pu242", 1.402890e-06)
mat1.add_nuclide("Am241", 2.959250e-06)
mat1.add_element("Cr", 2.693440e-03)
mat1.add_element("Ni", 1.197930e-03)
mat1.add_element("Fe", 1.286110e-02)
mat1.add_element("Al", 4.023850e-06)
mat1.add_element("Na", 9.277520e-03)
mat1.add_nuclide("O16", 1.375260e-02)
mat1.add_element("C", 3.664460e-05)
mat1.add_element("Mo", 2.360590e-04)
mat1.add_element("Mn", 2.256510e-04)
mat1.add_element("Cu", 2.467890e-05)
mat1.add_element("Si", 1.623740e-04)
mat1.add_element("Cl", 2.984100e-07)
mat1.add_element("Co", 8.326310e-07)

# OC1
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu240", 1.177510e-04)
mat2.add_nuclide("Pu241", 1.523770e-05)
mat2.add_nuclide("U235", 1.266000e-05)
mat2.add_nuclide("U238", 5.817010e-03)
mat2.add_nuclide("Pu239", 8.877940e-04)
mat2.add_nuclide("Pu238", 4.700560e-07)
mat2.add_nuclide("Pu242", 1.766240e-06)
mat2.add_nuclide("Am241", 2.403810e-06)
mat2.add_element("Cr", 2.689250e-03)
mat2.add_element("Ni", 1.188860e-03)
mat2.add_element("Fe", 1.324940e-02)
mat2.add_element("Al", 3.623900e-06)
mat2.add_element("Na", 9.127250e-03)
mat2.add_nuclide("O16", 1.427120e-02)
mat2.add_element("C", 3.404340e-05)
mat2.add_element("Mo", 2.390770e-04)
mat2.add_element("Mn", 2.240370e-04)
mat2.add_element("Cu", 2.483290e-05)
mat2.add_element("Si", 1.549450e-04)
mat2.add_element("Cl", 2.971560e-07)
mat2.add_element("Co", 1.691380e-07)

# IR1
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 8.293140e-05)
mat3.add_nuclide("U238", 3.711380e-02)
mat3.add_element("Cr", 1.646410e-03)
mat3.add_element("Ni", 6.893740e-04)
mat3.add_element("Fe", 6.060250e-03)
mat3.add_element("C", 3.672810e-05)
mat3.add_element("Mo", 1.062050e-05)
mat3.add_element("Mn", 1.431930e-04)
mat3.add_element("Cu", 1.974170e-05)
mat3.add_element("Si", 1.062280e-04)

# IR2
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U235", 8.652640e-05)
mat4.add_nuclide("U238", 3.874790e-02)
mat4.add_element("Cr", 1.449700e-03)
mat4.add_element("Ni", 6.075160e-04)
mat4.add_element("Fe", 5.255300e-03)
mat4.add_element("C", 2.716770e-05)
mat4.add_element("Mo", 1.004160e-05)
mat4.add_element("Mn", 1.271670e-04)
mat4.add_element("Cu", 1.906790e-05)
mat4.add_element("Si", 9.520310e-05)

# OR1
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U235", 8.276570e-05)
mat5.add_nuclide("U238", 3.704140e-02)
mat5.add_element("Cr", 1.655060e-03)
mat5.add_element("Ni", 6.928370e-04)
mat5.add_element("Fe", 6.088150e-03)
mat5.add_element("C", 3.664050e-05)
mat5.add_element("Mo", 1.067350e-05)
mat5.add_element("Mn", 1.437880e-04)
mat5.add_element("Cu", 1.981800e-05)
mat5.add_element("Si", 1.060870e-04)

# OR2
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("U235", 8.556550e-05)
mat6.add_nuclide("U238", 3.831530e-02)
mat6.add_element("Cr", 1.468210e-03)
mat6.add_element("Ni", 6.150660e-04)
mat6.add_element("Fe", 5.319660e-03)
mat6.add_element("C", 2.730420e-05)
mat6.add_element("Mo", 1.020460e-05)
mat6.add_element("Mn", 1.285230e-04)
mat6.add_element("Cu", 1.921430e-05)
mat6.add_element("Si", 9.546320e-05)

# RR1
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("U235", 8.665550e-05)
mat7.add_nuclide("U238", 3.880760e-02)
mat7.add_element("Cr", 1.178210e-03)
mat7.add_element("Ni", 4.757800e-04)
mat7.add_element("Fe", 4.239980e-03)
mat7.add_element("C", 1.857210e-05)
mat7.add_element("Mo", 8.181360e-06)
mat7.add_element("Mn", 1.049360e-04)
mat7.add_element("Cu", 1.707480e-05)
mat7.add_element("Si", 6.768480e-05)

# RR2=MAT
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Cr", 1.191830e-03)
mat8.add_element("Ni", 4.821150e-04)
mat8.add_element("Fe", 4.310230e-03)
mat8.add_element("C", 1.985010e-05)
mat8.add_element("Mo", 8.277480e-06)
mat8.add_element("Mn", 1.060580e-04)
mat8.add_element("Cu", 1.719210e-05)
mat8.add_element("Si", 6.886960e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, r=24.3435)
surf2 = openmc.ZCylinder(surface_id=2, r=80.6781)
surf3 = openmc.ZCylinder(surface_id=3, r=112.2504)
surf4 = openmc.ZCylinder(surface_id=4, r=140.2589)
surf5 = openmc.ZPlane(surface_id=5, z0=-106.6800)
surf6 = openmc.ZPlane(surface_id=6, z0=-101.7257)
surf7 = openmc.ZPlane(surface_id=7, z0=-76.2813)
surf8 = openmc.ZPlane(surface_id=8, z0=76.2813)
surf9 = openmc.ZPlane(surface_id=9, z0=101.7257)
surf10 = openmc.ZPlane(surface_id=10, z0=106.6800)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(z0=-110.5357)
surf3_zmax = openmc.ZPlane(z0=110.5357)
surf4_zmin = openmc.ZPlane(z0=-121.92, boundary_type="vacuum")
surf4_zmax = openmc.ZPlane(z0=121.92, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# IC1
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & +surf7 & -surf8

# OC1
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2 & +surf7 & -surf8

# IR1
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = -surf1 & +surf6 & -surf7

# IR1
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = -surf1 & +surf8 & -surf9

# IR2
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = -surf1 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf9

# IR2
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = -surf1 & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf6

# OR1
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = +surf1 & -surf2 & +surf6 & -surf7

# OR1
cell8 = openmc.Cell(cell_id=8, fill=mat5)
cell8.region = +surf1 & -surf2 & +surf8 & -surf9

# OR2
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf6

# OR2
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf9

# RR1
cell11 = openmc.Cell(cell_id=11, fill=mat7)
cell11.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf5 & -surf10

# RR2
cell12 = openmc.Cell(cell_id=12, fill=mat8)
cell12.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf5

# RR2
cell13 = openmc.Cell(cell_id=13, fill=mat8)
cell13.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf10

# MAT
cell14 = openmc.Cell(cell_id=14, fill=mat8)
cell14.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14])
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
