"""
PU-MET-FAST-021-1. Pu cylinder with axial Be refelection.
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu per
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.442200e-02)
mat1.add_nuclide("Pu240", 2.132600e-03)
mat1.add_nuclide("Pu241", 9.253800e-05)
mat1.add_element("C", 1.951500e-04)
mat1.add_element("Fe", 8.194300e-05)

# Steel per
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.128000e-02)
mat2.add_element("C", 3.475700e-04)
mat2.add_element("Si", 8.918500e-04)
mat2.add_element("Ti", 6.103400e-04)
mat2.add_element("Cr", 1.445200e-02)
mat2.add_element("Mn", 1.519800e-03)
mat2.add_element("Ni", 7.113100e-03)

# Section 3.3
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Be", 1.838460e+00)

# Duralumin @ 1.8155 g/cc
mat41 = openmc.Material(material_id=41)
mat41.set_density("sum")
mat41.add_element("P", 1.815500e+00)
mat41.add_element("Al", 9.360000e+01)
mat41.add_element("Mg", 1.500000e+00)
mat41.add_element("Mn", 6.000000e-01)
mat41.add_element("Cu", 4.300000e+00)

# Duralumin @ 2.78 g/cc
mat42 = openmc.Material(material_id=42)
mat42.set_density("sum")
mat42.add_element("P", 2.780000e+00)
mat42.add_element("Al", 9.360000e+01)
mat42.add_element("Mg", 1.500000e+00)
mat42.add_element("Mn", 6.000000e-01)
mat42.add_element("Cu", 4.300000e+00)

# Duralumin @ 0.417 g/cc
mat43 = openmc.Material(material_id=43)
mat43.set_density("sum")
mat43.add_element("P", 4.170000e-01)
mat43.add_element("Al", 9.360000e+01)
mat43.add_element("Mg", 1.500000e+00)
mat43.add_element("Mn", 6.000000e-01)
mat43.add_element("Cu", 4.300000e+00)

materials = openmc.Materials([mat1, mat2, mat3, mat41, mat42, mat43])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Pu
surf1 = openmc.ZCylinder(surface_id=1, r=5.995)
# Pu
surf2 = openmc.ZCylinder(surface_id=2, r=5.995)
# Pu
surf3 = openmc.ZCylinder(surface_id=3, r=5.995)
# Pu
surf4 = openmc.ZCylinder(surface_id=4, r=5.995)
# Pu
surf5 = openmc.ZCylinder(surface_id=5, r=5.995)
# Steel Cover
surf6 = openmc.ZCylinder(surface_id=6, r=6.063)
# BeO/Lower
surf7 = openmc.ZCylinder(surface_id=7, r=9.995)
# A1 Centric Rings
surf8 = openmc.ZCylinder(surface_id=8, r=6.263)
# Al Bottom Align. Ring
surf9 = openmc.ZCylinder(surface_id=9, r=9.995)
# Pu
surf11 = openmc.ZCylinder(surface_id=11, r=5.995)
# Pu
surf12 = openmc.ZCylinder(surface_id=12, r=5.995)
# Pu
surf13 = openmc.ZCylinder(surface_id=13, r=5.995)
# Pu
surf14 = openmc.ZCylinder(surface_id=14, r=5.995)
# Pu
surf15 = openmc.ZCylinder(surface_id=15, r=5.995)
# Steel Cover
surf16 = openmc.ZCylinder(surface_id=16, r=6.063)
# Be/Upper
surf17 = openmc.ZCylinder(surface_id=17, r=9.995)
# Al Basket
surf18 = openmc.ZCylinder(surface_id=18, r=6.263)
# Al Ring/Outer
surf19 = openmc.ZCylinder(surface_id=19, r=9.995)
# Al Ring/Inner
surf20 = openmc.ZCylinder(surface_id=20, r=6.063)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1020, z0=-2.43)
surf1_zmax = openmc.ZPlane(surface_id=1021, z0=-1.98)
surf2_zmin = openmc.ZPlane(surface_id=1022, z0=-1.94)
surf2_zmax = openmc.ZPlane(surface_id=1023, z0=-1.49)
surf3_zmin = openmc.ZPlane(surface_id=1024, z0=-1.45)
surf3_zmax = openmc.ZPlane(surface_id=1025, z0=-1.0)
surf4_zmin = openmc.ZPlane(surface_id=1026, z0=-0.96)
surf4_zmax = openmc.ZPlane(surface_id=1027, z0=-0.51)
surf5_zmin = openmc.ZPlane(surface_id=1028, z0=-0.47)
surf5_zmax = openmc.ZPlane(surface_id=1029, z0=-0.02)
surf6_zmin = openmc.ZPlane(surface_id=1030, z0=-2.45)
surf6_zmax = openmc.ZPlane(surface_id=1031, z0=-0.0)
surf7_zmin = openmc.ZPlane(surface_id=1032, z0=-17.345)
surf7_zmax = openmc.ZPlane(surface_id=1033, z0=-2.45)
surf8_zmin = openmc.ZPlane(surface_id=1034, z0=-2.45)
surf8_zmax = openmc.ZPlane(surface_id=1035, z0=-0.0)
surf9_zmin = openmc.ZPlane(surface_id=1036, z0=-2.45)
surf9_zmax = openmc.ZPlane(surface_id=1037, z0=-2.25)
surf11_zmin = openmc.ZPlane(surface_id=1038, z0=1.99)
surf11_zmax = openmc.ZPlane(surface_id=1039, z0=2.44)
surf12_zmin = openmc.ZPlane(surface_id=1040, z0=1.5)
surf12_zmax = openmc.ZPlane(surface_id=1041, z0=1.95)
surf13_zmin = openmc.ZPlane(surface_id=1042, z0=1.01)
surf13_zmax = openmc.ZPlane(surface_id=1043, z0=1.46)
surf14_zmin = openmc.ZPlane(surface_id=1044, z0=0.52)
surf14_zmax = openmc.ZPlane(surface_id=1045, z0=0.97)
surf15_zmin = openmc.ZPlane(surface_id=1046, z0=0.03)
surf15_zmax = openmc.ZPlane(surface_id=1047, z0=0.48)
surf16_zmin = openmc.ZPlane(surface_id=1048, z0=0.01)
surf16_zmax = openmc.ZPlane(surface_id=1049, z0=2.46)
surf17_zmin = openmc.ZPlane(surface_id=1050, z0=2.48)
surf17_zmax = openmc.ZPlane(surface_id=1051, z0=17.375)
surf18_zmin = openmc.ZPlane(surface_id=1052, z0=0.01)
surf18_zmax = openmc.ZPlane(surface_id=1053, z0=2.48)
surf19_zmin = openmc.ZPlane(surface_id=1054, z0=2.28)
surf19_zmax = openmc.ZPlane(surface_id=1055, z0=2.48)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Pu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax)

# Pu
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = (-surf2 & +surf2_zmin & -surf2_zmax)

# Pu
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = (-surf3 & +surf3_zmin & -surf3_zmax)

# Pu
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = (-surf4 & +surf4_zmin & -surf4_zmax)

# Pu
cell5 = openmc.Cell(cell_id=5, fill=mat1)
cell5.region = (-surf5 & +surf5_zmin & -surf5_zmax)

# STL
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = (-surf6 & +surf6_zmin & -surf6_zmax) & (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax)

# Be
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)

# A1
cell8 = openmc.Cell(cell_id=8, fill=mat41)
cell8.region = (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# Al
cell9 = openmc.Cell(cell_id=9, fill=mat42)
cell9.region = (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax) & (-surf9 & +surf9_zmin & -surf9_zmax)

# Pu
cell10 = openmc.Cell(cell_id=10, fill=mat1)
cell10.region = (-surf11 & +surf11_zmin & -surf11_zmax)

# Pu
cell11 = openmc.Cell(cell_id=11, fill=mat1)
cell11.region = (-surf12 & +surf12_zmin & -surf12_zmax)

# Pu
cell12 = openmc.Cell(cell_id=12, fill=mat1)
cell12.region = (-surf13 & +surf13_zmin & -surf13_zmax)

# Pu
cell13 = openmc.Cell(cell_id=13, fill=mat1)
cell13.region = (-surf14 & +surf14_zmin & -surf14_zmax)

# Pu
cell14 = openmc.Cell(cell_id=14, fill=mat1)
cell14.region = (-surf15 & +surf15_zmin & -surf15_zmax)

# STL
cell15 = openmc.Cell(cell_id=15, fill=mat2)
cell15.region = (-surf16 & +surf16_zmin & -surf16_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (+surf15 | -surf15_zmin | +surf15_zmax)

# Be
cell16 = openmc.Cell(cell_id=16, fill=mat3)
cell16.region = (+surf16 | -surf16_zmin | +surf16_zmax) & (-surf17 & +surf17_zmin & -surf17_zmax)

# A1
cell17 = openmc.Cell(cell_id=17, fill=mat43)
cell17.region = (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax) & (-surf18 & +surf18_zmin & -surf18_zmax)

# Al
cell18 = openmc.Cell(cell_id=18, fill=mat42)
cell18.region = (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax) & (+surf18 | -surf18_zmin | +surf18_zmax) & (-surf19 & +surf19_zmin & -surf19_zmax) & +surf20

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18])
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
source.space = openmc.stats.Box((-1.0, -1.0, -1.3), (1.0, 1.0, 1.3))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
