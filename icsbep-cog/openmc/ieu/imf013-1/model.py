"""
IEU-MET-FAST-013-1: ZPR-9 Assembly 1 Loading 9: Simplified benchmark R/Z model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U/Al
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 4.535590e-03)
mat1.add_nuclide("U238", 3.376140e-02)
mat1.add_nuclide("U234", 4.360790e-05)
mat1.add_nuclide("U236", 2.090580e-05)
mat1.add_element("Cr", 5.990840e-05)
mat1.add_element("Ni", 2.227090e-05)
mat1.add_element("Fe", 2.032830e-04)
mat1.add_element("Al", 5.850790e-03)
mat1.add_element("C", 5.974260e-05)
mat1.add_element("Mo", 4.003190e-07)
mat1.add_element("Mn", 1.033500e-05)
mat1.add_element("Cu", 6.170850e-06)
mat1.add_element("H", 1.690980e-05)
mat1.add_element("Ti", 2.730250e-06)
mat1.add_element("Si", 2.840080e-05)
mat1.add_element("Mg", 1.337420e-04)
mat1.add_element("Cl", 2.958300e-05)
mat1.add_element("F", 8.759070e-05)

# RR1
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cr", 5.853560e-06)
mat2.add_element("Fe", 9.421530e-06)
mat2.add_element("Al", 5.563390e-02)
mat2.add_element("Mn", 6.227400e-06)
mat2.add_element("Cu", 5.731060e-06)
mat2.add_element("Ti", 2.776530e-06)
mat2.add_element("Si", 2.750420e-05)
mat2.add_element("Mg", 1.383120e-04)

# AR1
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cr", 5.368930e-05)
mat3.add_element("Ni", 1.951190e-05)
mat3.add_element("Fe", 3.097910e-04)
mat3.add_element("Al", 5.526010e-02)
mat3.add_element("C", 6.606750e-06)
mat3.add_element("Mo", 3.507250e-07)
mat3.add_element("Mn", 1.076040e-05)
mat3.add_element("Cu", 6.475680e-06)
mat3.add_element("Ti", 2.986580e-06)
mat3.add_element("Si", 2.998300e-05)
mat3.add_element("Mg", 1.535870e-04)

# AR2
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 5.375560e-05)
mat4.add_element("Ni", 1.960900e-05)
mat4.add_element("Fe", 8.621830e-04)
mat4.add_element("Al", 5.439130e-02)
mat4.add_element("C", 5.533630e-06)
mat4.add_element("Mo", 3.513110e-07)
mat4.add_element("Mn", 1.351850e-05)
mat4.add_element("Cu", 6.527110e-06)
mat4.add_element("Ti", 2.977610e-06)
mat4.add_element("Si", 3.021280e-05)
mat4.add_element("Mg", 1.527170e-04)

# AR3
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 5.375560e-05)
mat5.add_element("Ni", 1.958070e-05)
mat5.add_element("Fe", 5.687030e-04)
mat5.add_element("Al", 6.374610e-03)
mat5.add_element("C", 3.442660e-06)
mat5.add_element("Mo", 3.513110e-07)
mat5.add_element("Mn", 1.231510e-05)
mat5.add_element("Cu", 6.500930e-06)
mat5.add_element("Ti", 2.977610e-06)
mat5.add_element("Si", 3.009990e-05)
mat5.add_element("Mg", 1.527217e-04)

# RR2
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Cr", 6.250670e-06)
mat6.add_element("Fe", 6.592960e-05)
mat6.add_element("Al", 5.599990e-02)
mat6.add_element("C", 2.556040e-06)
mat6.add_element("Mn", 7.102730e-06)
mat6.add_element("Cu", 6.000840e-06)
mat6.add_element("Ti", 2.988570e-06)
mat6.add_element("Si", 2.878750e-05)
mat6.add_element("Mg", 1.561960e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, r=31.58728)
surf2 = openmc.ZCylinder(surface_id=2, r=32.6532)
surf3 = openmc.ZCylinder(surface_id=3, r=66.64083, boundary_type="vacuum")
surf11 = openmc.ZPlane(surface_id=11, z0=-56.59882)
surf12 = openmc.ZPlane(surface_id=12, z0=-50.92573)
surf13 = openmc.ZPlane(surface_id=13, z0=-25.48346)
surf14 = openmc.ZPlane(surface_id=14, z0=25.48346)
surf15 = openmc.ZPlane(surface_id=15, z0=50.92573)
surf16 = openmc.ZPlane(surface_id=16, z0=56.59882)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1016, z0=-61.91504, boundary_type="vacuum")
surf3_zmax = openmc.ZPlane(surface_id=1017, z0=61.91504, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# AR3
cell1 = openmc.Cell(cell_id=1, fill=mat5)
cell1.region = -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf16

# AR2
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = -surf2 & +surf15 & -surf16

# AR1
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = -surf2 & +surf14 & -surf15

# U-Al
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = -surf1 & +surf13 & -surf14

# RR1
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf1 & -surf2 & +surf13 & -surf14

# AR1
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = -surf2 & +surf12 & -surf13

# AR2
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = -surf2 & +surf11 & -surf12

# AR3
cell8 = openmc.Cell(cell_id=8, fill=mat5)
cell8.region = -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf11

# RR2
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9])
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
