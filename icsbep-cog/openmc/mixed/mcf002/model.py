"""
MIX-COMP-FAST-002; ZPR-6 Assembly 7; High 240Pu Core; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# IC1
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu240", 3.217800e-04)
mat1.add_nuclide("Pu241", 5.356900e-05)
mat1.add_nuclide("U235", 1.187200e-05)
mat1.add_nuclide("U238", 5.562000e-03)
mat1.add_nuclide("Pu239", 8.384400e-04)
mat1.add_nuclide("Pu238", 1.108300e-06)
mat1.add_nuclide("Pu242", 1.744700e-05)
mat1.add_nuclide("Am241", 1.468100e-05)
mat1.add_element("Cr", 2.679200e-03)
mat1.add_element("Ni", 1.190800e-03)
mat1.add_element("Fe", 1.280500e-02)
mat1.add_element("Al", 4.105700e-06)
mat1.add_element("Na", 9.167600e-03)
mat1.add_nuclide("O16", 1.368400e-02)
mat1.add_element("C", 3.662100e-05)
mat1.add_element("Mo", 2.366200e-04)
mat1.add_element("Mn", 2.244700e-04)
mat1.add_element("Cu", 2.458000e-05)
mat1.add_element("Si", 1.618200e-04)
mat1.add_element("Ca", 2.104400e-06)
mat1.add_element("Cl", 2.948400e-07)
mat1.add_element("Co", 8.288900e-07)

# OC1
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu240", 1.174900e-04)
mat2.add_nuclide("Pu241", 1.464100e-05)
mat2.add_nuclide("U235", 1.257500e-05)
mat2.add_nuclide("U238", 5.782000e-03)
mat2.add_nuclide("Pu239", 8.858300e-04)
mat2.add_nuclide("Pu238", 4.644400e-07)
mat2.add_nuclide("Pu242", 1.762000e-06)
mat2.add_nuclide("Am241", 2.964300e-06)
mat2.add_element("Cr", 2.679200e-03)
mat2.add_element("Ni", 1.188500e-03)
mat2.add_element("Fe", 1.323000e-02)
mat2.add_element("Al", 1.859300e-05)
mat2.add_element("Na", 9.071800e-03)
mat2.add_nuclide("O16", 1.419200e-02)
mat2.add_element("C", 3.360500e-05)
mat2.add_element("Mo", 2.387500e-04)
mat2.add_element("Mn", 2.239500e-04)
mat2.add_element("Cu", 2.488200e-05)
mat2.add_element("Si", 1.537700e-04)
mat2.add_element("Ca", 2.082800e-06)
mat2.add_element("Cl", 2.954600e-07)
mat2.add_element("Co", 5.409500e-08)

# IR1
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 8.135300e-05)
mat3.add_nuclide("U238", 3.793600e-02)
mat3.add_element("Cr", 1.646400e-03)
mat3.add_element("Ni", 6.893700e-04)
mat3.add_element("Fe", 6.060300e-03)
mat3.add_element("C", 3.672800e-05)
mat3.add_element("Mo", 1.062000e-05)
mat3.add_element("Mn", 1.431900e-04)
mat3.add_element("Cu", 1.974200e-05)
mat3.add_element("Si", 1.062300e-04)

# IR2
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U235", 8.586600e-05)
mat4.add_nuclide("U238", 4.005500e-02)
mat4.add_element("Cr", 1.449700e-03)
mat4.add_element("Ni", 6.075200e-04)
mat4.add_element("Fe", 5.255300e-03)
mat4.add_element("C", 2.716800e-05)
mat4.add_element("Mo", 1.004200e-05)
mat4.add_element("Mn", 1.271700e-04)
mat4.add_element("Cu", 1.906800e-05)
mat4.add_element("Si", 9.520300e-05)

# OR1
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U235", 8.104800e-05)
mat5.add_nuclide("U238", 3.779500e-02)
mat5.add_element("Cr", 1.655700e-03)
mat5.add_element("Ni", 6.931000e-04)
mat5.add_element("Fe", 6.090300e-03)
mat5.add_element("C", 3.663400e-05)
mat5.add_element("Mo", 1.067800e-05)
mat5.add_element("Mn", 1.438300e-04)
mat5.add_element("Cu", 1.982400e-05)
mat5.add_element("Si", 1.060800e-04)

# OR2
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("U235", 8.474000e-05)
mat6.add_nuclide("U238", 3.952700e-02)
mat6.add_element("Cr", 1.469600e-03)
mat6.add_element("Ni", 6.156400e-04)
mat6.add_element("Fe", 5.324500e-03)
mat6.add_element("C", 2.731500e-05)
mat6.add_element("Mo", 1.021700e-05)
mat6.add_element("Mn", 1.286300e-04)
mat6.add_element("Cu", 1.922500e-05)
mat6.add_element("Si", 9.548300e-05)

# RR1
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("U235", 8.584600e-05)
mat7.add_nuclide("U238", 4.004600e-02)
mat7.add_element("Cr", 1.178200e-03)
mat7.add_element("Ni", 4.757800e-04)
mat7.add_element("Fe", 4.240000e-03)
mat7.add_element("C", 1.857200e-05)
mat7.add_element("Mo", 8.181400e-06)
mat7.add_element("Mn", 1.049400e-04)
mat7.add_element("Cu", 1.707500e-05)
mat7.add_element("Si", 6.768500e-05)

# RR2=MAT
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Cr", 1.191000e-03)
mat8.add_element("Ni", 4.817200e-04)
mat8.add_element("Fe", 4.305600e-03)
mat8.add_element("C", 1.975200e-05)
mat8.add_element("Mo", 8.271900e-06)
mat8.add_element("Mn", 1.059900e-04)
mat8.add_element("Cu", 1.718600e-05)
mat8.add_element("Si", 6.878900e-05)

# PUAL
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_nuclide("Pu240", 5.069400e-05)
mat9.add_nuclide("Pu241", 2.843300e-06)
mat9.add_nuclide("U235", 1.215100e-05)
mat9.add_nuclide("U238", 5.704200e-03)
mat9.add_nuclide("Pu239", 1.069700e-03)
mat9.add_nuclide("Pu238", 1.624800e-09)
mat9.add_nuclide("Pu242", 1.100500e-07)
mat9.add_nuclide("Am241", 1.975800e-06)
mat9.add_element("Cr", 2.623000e-03)
mat9.add_element("Ni", 1.164800e-03)
mat9.add_element("Fe", 1.316000e-02)
mat9.add_element("Al", 1.147700e-04)
mat9.add_element("Na", 9.342000e-03)
mat9.add_nuclide("O16", 1.438600e-02)
mat9.add_element("C", 4.002100e-05)
mat9.add_element("Mo", 1.330600e-05)
mat9.add_element("Mn", 2.202000e-04)
mat9.add_element("Cu", 2.573100e-05)
mat9.add_element("Si", 1.587900e-04)
mat9.add_element("Ca", 2.145200e-06)
mat9.add_element("Cl", 3.035200e-07)
mat9.add_element("Co", 8.241200e-07)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, r=24.3435)
surf2 = openmc.ZCylinder(surface_id=2, r=78.0496)
surf3 = openmc.ZCylinder(surface_id=3, r=111.5583)
surf4 = openmc.ZCylinder(surface_id=4, r=140.2589)
surf5 = openmc.ZPlane(surface_id=5, z0=-106.6800)
surf6 = openmc.ZPlane(surface_id=6, z0=-101.7257)
surf7 = openmc.ZPlane(surface_id=7, z0=-76.2813)
surf8 = openmc.ZPlane(surface_id=8, z0=76.2813)
surf9 = openmc.ZPlane(surface_id=9, z0=101.7257)
surf10 = openmc.ZPlane(surface_id=10, z0=106.6800)
surf20 = openmc.ZCylinder(surface_id=20, r=75.0028)

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
cell2.region = +surf1 & -surf20 & +surf7 & -surf8

# PUAL
cell3 = openmc.Cell(cell_id=3, fill=mat9)
cell3.region = +surf20 & -surf2 & +surf7 & -surf8

# IR1
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = -surf1 & +surf6 & -surf7

# IR1
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = -surf1 & +surf8 & -surf9

# IR2
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = -surf1 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf9

# IR2
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = -surf1 & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf6

# OR1
cell8 = openmc.Cell(cell_id=8, fill=mat5)
cell8.region = +surf1 & -surf2 & +surf6 & -surf7

# OR1
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = +surf1 & -surf2 & +surf8 & -surf9

# OR2
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf6

# OR2
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf9

# RR1
cell12 = openmc.Cell(cell_id=12, fill=mat7)
cell12.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf5 & -surf10

# RR2
cell13 = openmc.Cell(cell_id=13, fill=mat8)
cell13.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf5

# RR2
cell14 = openmc.Cell(cell_id=14, fill=mat8)
cell14.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf10

# MAT
cell15 = openmc.Cell(cell_id=15, fill=mat8)
cell15.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15])
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
