"""
IEU-COMP-FAST-004-1: ZPR-3 Assembly 12: Simplified benchmark R/Z model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Core
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 4.537630e-03)
mat1.add_nuclide("U238", 1.681160e-02)
mat1.add_nuclide("U234", 4.401000e-05)
mat1.add_nuclide("U236", 2.109810e-05)
mat1.add_element("Cr", 1.442590e-03)
mat1.add_element("Ni", 6.190510e-04)
mat1.add_element("Fe", 5.787630e-03)
mat1.add_element("C", 2.678270e-02)
mat1.add_element("Mn", 7.213940e-05)
mat1.add_element("H", 9.544480e-06)
mat1.add_element("Si", 7.294400e-05)
mat1.add_element("Cl", 1.645050e-05)
mat1.add_element("F", 4.870320e-05)

# Axial Blanket
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 8.048950e-05)
mat2.add_nuclide("U238", 3.959180e-02)
mat2.add_element("Cr", 1.459150e-03)
mat2.add_element("Ni", 6.233270e-04)
mat2.add_element("Fe", 5.863830e-03)
mat2.add_element("C", 1.308470e-05)
mat2.add_element("Mn", 7.146600e-05)
mat2.add_element("H", 3.797870e-06)
mat2.add_element("Si", 7.436520e-05)
mat2.add_element("Cl", 6.563450e-06)
mat2.add_element("F", 1.943490e-05)

# Radial Blanket
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 8.120890e-05)
mat3.add_nuclide("U238", 4.000110e-02)
mat3.add_element("Cr", 1.111600e-03)
mat3.add_element("Ni", 4.551450e-04)
mat3.add_element("Fe", 4.535190e-03)
mat3.add_element("C", 8.680370e-06)
mat3.add_element("Mn", 4.398390e-05)
mat3.add_element("H", 2.511750e-06)
mat3.add_element("Si", 6.072020e-05)
mat3.add_element("Cl", 4.354110e-06)
mat3.add_element("F", 1.289370e-05)

# Drawer Gap
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 3.525430e-03)
mat4.add_element("Ni", 1.641420e-03)
mat4.add_element("Fe", 1.956210e-02)
mat4.add_element("C", 2.704670e-04)
mat4.add_element("Mo", 6.066740e-08)
mat4.add_element("Mn", 2.384850e-04)
mat4.add_element("Cu", 3.660700e-07)
mat4.add_element("Si", 1.503840e-04)

# Matrix
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 1.109600e-03)
mat5.add_element("Ni", 4.535540e-04)
mat5.add_element("Fe", 4.529680e-03)
mat5.add_element("Mn", 4.349570e-05)
mat5.add_element("Si", 6.077000e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.ZCylinder(surface_id=1, r=26.50215)
surf2 = openmc.ZCylinder(surface_id=2, r=56.99622)
surf3 = openmc.ZCylinder(surface_id=3, r=96.82257, boundary_type="vacuum")
surf10 = openmc.ZPlane(surface_id=10, z0=-54.12762)
surf11 = openmc.ZPlane(surface_id=11, z0=-53.34000)
surf12 = openmc.ZPlane(surface_id=12, z0=-38.88762)
surf13 = openmc.ZPlane(surface_id=13, z0=-38.18247)
surf14 = openmc.ZPlane(surface_id=14, z0=-22.94427)
surf15 = openmc.ZPlane(surface_id=15, z0=22.94427)
surf16 = openmc.ZPlane(surface_id=16, z0=38.18247)
surf17 = openmc.ZPlane(surface_id=17, z0=38.88762)
surf18 = openmc.ZPlane(surface_id=18, z0=53.34000)
surf19 = openmc.ZPlane(surface_id=19, z0=54.12762)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1019, z0=-85.09, boundary_type="vacuum")
surf3_zmax = openmc.ZPlane(surface_id=1020, z0=85.09, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Mtrx
cell1 = openmc.Cell(cell_id=1, fill=mat5)
cell1.region = -surf1 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf19

# AxBl
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = -surf1 & +surf17 & -surf19

# Gap
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf1 & +surf16 & -surf17

# AxBl
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = -surf1 & +surf15 & -surf16

# Core
cell5 = openmc.Cell(cell_id=5, fill=mat1)
cell5.region = -surf1 & +surf14 & -surf15

# AxBl
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = -surf1 & +surf13 & -surf14

# Gap
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = -surf1 & +surf12 & -surf13

# AxBl
cell8 = openmc.Cell(cell_id=8, fill=mat2)
cell8.region = -surf1 & +surf10 & -surf12

# Mtrx
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = -surf1 & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf10

# Mtrx
cell10 = openmc.Cell(cell_id=10, fill=mat5)
cell10.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf18

# RdBl
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = +surf1 & -surf2 & +surf11 & -surf18

# Mtrx
cell12 = openmc.Cell(cell_id=12, fill=mat5)
cell12.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf11

# Mtrx
cell13 = openmc.Cell(cell_id=13, fill=mat5)
cell13.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13])
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
