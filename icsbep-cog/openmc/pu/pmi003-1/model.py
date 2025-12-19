"""
PU-MET-INTER-003 (ZPR-3/58) Benchmark (R-Z) Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Core
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu240", 9.925660e-05)
mat1.add_nuclide("Pu241", 5.808850e-06)
mat1.add_nuclide("Pu239", 2.099720e-03)
mat1.add_nuclide("Pu238", 8.806330e-09)
mat1.add_nuclide("Pu242", 3.815000e-07)
mat1.add_nuclide("Am241", 3.351790e-06)
mat1.add_element("Cr", 1.907180e-03)
mat1.add_element("Ni", 9.084190e-04)
mat1.add_element("Fe", 7.421540e-03)
mat1.add_element("Al", 2.232480e-04)
mat1.add_nuclide("O16", 8.968620e-05)
mat1.add_element("C", 5.778380e-02)
mat1.add_element("Mo", 4.400110e-06)
mat1.add_element("Mn", 1.126320e-04)
mat1.add_element("Cu", 5.785140e-06)
mat1.add_element("Ti", 4.482220e-05)
mat1.add_element("Si", 9.538230e-05)
mat1.add_element("F", 1.432630e-04)

# Axial reflector
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 8.576630e-05)
mat2.add_nuclide("U238", 3.886300e-02)
mat2.add_element("Cr", 1.453880e-03)
mat2.add_element("Ni", 6.207530e-04)
mat2.add_element("Fe", 5.843770e-03)
mat2.add_element("C", 1.236310e-05)
mat2.add_element("Mn", 7.103610e-05)
mat2.add_element("H", 3.589700e-06)
mat2.add_element("Si", 7.416340e-05)
mat2.add_element("Cl", 6.201570e-06)
mat2.add_element("F", 1.836330e-05)

# Radial reflector - half 1
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 8.643340e-05)
mat3.add_nuclide("U238", 3.873310e-02)
mat3.add_element("Cr", 1.109250e-03)
mat3.add_element("Ni", 4.537960e-04)
mat3.add_element("Fe", 4.526960e-03)
mat3.add_element("C", 8.610310e-06)
mat3.add_element("Mn", 4.368490e-05)
mat3.add_element("H", 2.491150e-06)
mat3.add_element("Si", 6.067240e-05)
mat3.add_element("Cl", 4.318960e-06)
mat3.add_element("F", 1.278960e-05)

# Radial reflector - half 2
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U235", 8.603680e-05)
mat4.add_nuclide("U238", 3.854130e-02)
mat4.add_element("Cr", 1.105100e-03)
mat4.add_element("Ni", 4.520530e-04)
mat4.add_element("Fe", 4.510180e-03)
mat4.add_element("C", 8.192480e-06)
mat4.add_element("Mn", 4.349740e-05)
mat4.add_element("H", 2.370320e-06)
mat4.add_element("Si", 6.045470e-05)
mat4.add_element("Cl", 4.109380e-06)
mat4.add_element("F", 1.216900e-05)

# Drawer gap
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 3.142420e-03)
mat5.add_element("Ni", 1.445820e-03)
mat5.add_element("Fe", 1.854680e-02)
mat5.add_element("C", 2.869950e-04)
mat5.add_element("Mn", 2.088060e-04)
mat5.add_element("Si", 1.388420e-04)

# Empty matrix
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Cr", 1.109600e-03)
mat6.add_element("Ni", 4.535540e-04)
mat6.add_element("Fe", 4.529680e-03)
mat6.add_element("Mn", 4.349570e-05)
mat6.add_element("Si", 6.077000e-05)
mat6.add_element("Mo", 8.236970e-06)
mat6.add_element("Si", 6.817470e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZPlane(surface_id=1, z0=-53.4242)
surf2 = openmc.ZPlane(surface_id=2, z0=-50.8106)
surf3 = openmc.ZPlane(surface_id=3, z0=-22.9442)
surf4 = openmc.ZPlane(surface_id=4, z0=0.0)
surf5 = openmc.ZPlane(surface_id=5, z0=28.0242)
surf6 = openmc.ZPlane(surface_id=6, z0=38.1842)
surf7 = openmc.ZPlane(surface_id=7, z0=38.8192)
surf8 = openmc.ZPlane(surface_id=8, z0=59.1392)
surf9 = openmc.ZPlane(surface_id=9, z0=60.8772)
surf11 = openmc.ZCylinder(surface_id=11, r=27.5843)
surf12 = openmc.ZCylinder(surface_id=12, r=58.3482)
surf13 = openmc.ZCylinder(surface_id=13, r=96.8226)

# Z-plane surfaces for bounded cylinders
surf13_zmin = openmc.ZPlane(surface_id=1013, z0=-85.09)
surf13_zmax = openmc.ZPlane(surface_id=1014, z0=85.09)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf3 & -surf5 & -surf11

# AxRefl
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf3 & -surf11

# AxRefl
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf5 & -surf6 & -surf11

# DwgGap
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = +surf6 & -surf7 & -surf11

# AxRefl
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf7 & -surf8 & -surf11

# Matrix
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = -surf1 & -surf11 & (-surf13 & +surf13_zmin & -surf13_zmax)

# Matrix
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = +surf8 & -surf11 & (-surf13 & +surf13_zmin & -surf13_zmax)

# RdReH2
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf2 & -surf4 & +surf11 & -surf12

# RdReH1
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = +surf4 & -surf9 & +surf11 & -surf12

# Matrix
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = -surf2 & +surf11 & -surf12 & (-surf13 & +surf13_zmin & -surf13_zmax)

# Matrix
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = +surf9 & +surf11 & -surf12 & (-surf13 & +surf13_zmin & -surf13_zmax)

# Matrix
cell12 = openmc.Cell(cell_id=12, fill=mat6)
cell12.region = +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12])
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
