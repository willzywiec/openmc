"""
IEU-MET-FAST-001-1i: Idealized Model of Jemima Configuration #1 with Oy-Tu Disk Pairs, Fillers In
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Al-2024
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_element("Mg", 1.029500e-03)
mat1.add_element("Al", 5.786800e-02)
mat1.add_element("Mn", 1.518200e-04)
mat1.add_element("Cu", 1.155000e-03)

# SST
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cr", 1.653200e-02)
mat2.add_element("Fe", 6.327800e-02)
mat2.add_element("Ni", 6.509500e-03)

# Tu
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U234", 2.642300e-06)
mat3.add_nuclide("U235", 3.459100e-04)
mat3.add_nuclide("U238", 4.769400e-02)

# Oy
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U234", 4.915600e-04)
mat4.add_nuclide("U235", 4.482400e-02)
mat4.add_nuclide("U238", 2.639100e-03)

# Mixed U
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U234", 2.556100e-04)
mat5.add_nuclide("U235", 2.335300e-02)
mat5.add_nuclide("U238", 2.193900e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# ** inner radius of uranium disks **
surf2 = openmc.ZCylinder(surface_id=2, r=1.11125)
# ** rad. of upper Al filler support cylinder **
surf3 = openmc.ZCylinder(surface_id=3, r=1.74625)
# ** rad. of lower Al filler support cylinder **
surf7 = openmc.ZCylinder(surface_id=7, r=4.60375)
# ** inner radius of lower Al support ring **
surf8 = openmc.ZCylinder(surface_id=8, r=12.065)
# ** idlzd. Tu/Al bndry in upper supp. ring **
surf10 = openmc.ZCylinder(surface_id=10, r=12.66939)
# ** o.r. unique Tu disk; i.r. spacer platform **
surf11 = openmc.ZCylinder(surface_id=11, r=12.7)
# ** outer radius of uranium disks **
surf12 = openmc.ZCylinder(surface_id=12, r=13.335)
# ** outer rad. of idealized Al rect. spacers **
surf14 = openmc.ZCylinder(surface_id=14, r=13.67711)
# ** outer edge of idlzd. Al upper supp. ring **
surf17 = openmc.ZCylinder(surface_id=17, r=15.29416)
# ** outer rad. of idealized lower Al ring **
surf18 = openmc.ZCylinder(surface_id=18, r=15.82055)
# ** outer rad. of idealized Al platform spacer **
surf19 = openmc.ZCylinder(surface_id=19, r=17.1965)
# ** rad. of cyl. equiv. to 12"x15" Fe plate **
surf20 = openmc.ZCylinder(surface_id=20, r=19.22627)
# ** inner rad. ext. cell (idealized models) **
surf21 = openmc.ZCylinder(surface_id=21, r=21.0, boundary_type="vacuum")
# ** lower surface of bottom uranium disk **
surf101 = openmc.ZPlane(surface_id=101, z0=0.000)
surf105 = openmc.ZPlane(surface_id=105, z0=0.804)
surf106 = openmc.ZPlane(surface_id=106, z0=1.408)
surf109 = openmc.ZPlane(surface_id=109, z0=2.212)
surf110 = openmc.ZPlane(surface_id=110, z0=2.816)
surf113 = openmc.ZPlane(surface_id=113, z0=3.620)
surf114 = openmc.ZPlane(surface_id=114, z0=4.224)
surf117 = openmc.ZPlane(surface_id=117, z0=5.028)
surf118 = openmc.ZPlane(surface_id=118, z0=5.632)
surf121 = openmc.ZPlane(surface_id=121, z0=6.436)
surf122 = openmc.ZPlane(surface_id=122, z0=7.040)
surf125 = openmc.ZPlane(surface_id=125, z0=7.844)
surf126 = openmc.ZPlane(surface_id=126, z0=8.448)
# ** parting plane **
surf129 = openmc.ZPlane(surface_id=129, z0=9.252)
surf131 = openmc.ZPlane(surface_id=131, z0=9.856)
surf134 = openmc.ZPlane(surface_id=134, z0=10.660)
surf136 = openmc.ZPlane(surface_id=136, z0=11.264)
surf138 = openmc.ZPlane(surface_id=138, z0=12.068)
surf140 = openmc.ZPlane(surface_id=140, z0=12.672)
surf142 = openmc.ZPlane(surface_id=142, z0=13.476)
surf144 = openmc.ZPlane(surface_id=144, z0=14.080)
surf146 = openmc.ZPlane(surface_id=146, z0=14.884)
surf161 = openmc.ZPlane(surface_id=161, z0=14.9631)
surf201 = openmc.ZPlane(surface_id=201, z0=-0.3175)
surf202 = openmc.ZPlane(surface_id=202, z0=-0.9525)
surf203 = openmc.ZPlane(surface_id=203, z0=-3.1750)
surf204 = openmc.ZPlane(surface_id=204, z0=-4.7625)
surf205 = openmc.ZPlane(surface_id=205, z0=-6.0325)
surf206 = openmc.ZPlane(surface_id=206, z0=-8.5725)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Mx
cell1 = openmc.Cell(cell_id=1, fill=mat5)
cell1.region = +surf101 & -surf129 & -surf2

# Oy
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = +surf101 & -surf105 & +surf2 & -surf12

# Tu
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf105 & -surf106 & +surf2 & -surf12

# Oy
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf106 & -surf109 & +surf2 & -surf12

# Tu
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf109 & -surf110 & +surf2 & -surf12

# Oy
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf110 & -surf113 & +surf2 & -surf12

# Tu
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf113 & -surf114 & +surf2 & -surf12

# Oy
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = +surf114 & -surf117 & +surf2 & -surf12

# Tu
cell9 = openmc.Cell(cell_id=9, fill=mat3)
cell9.region = +surf117 & -surf118 & +surf2 & -surf12

# Oy
cell10 = openmc.Cell(cell_id=10, fill=mat4)
cell10.region = +surf118 & -surf121 & +surf2 & -surf12

# Tu
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = +surf121 & -surf122 & +surf2 & -surf12

# Oy
cell12 = openmc.Cell(cell_id=12, fill=mat4)
cell12.region = +surf122 & -surf125 & +surf2 & -surf12

# Tu
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = +surf125 & -surf126 & +surf2 & -surf12

# Oy
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = +surf126 & -surf129 & +surf2 & -surf12

# Tu
cell15 = openmc.Cell(cell_id=15, fill=mat3)
cell15.region = +surf129 & -surf131 & -surf10

# Oy
cell16 = openmc.Cell(cell_id=16, fill=mat4)
cell16.region = +surf131 & -surf134 & -surf12

# Tu
cell17 = openmc.Cell(cell_id=17, fill=mat3)
cell17.region = +surf134 & -surf136 & -surf12

# Oy
cell18 = openmc.Cell(cell_id=18, fill=mat4)
cell18.region = +surf136 & -surf138 & -surf12

# Tu
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = +surf138 & -surf140 & -surf12

# Oy
cell20 = openmc.Cell(cell_id=20, fill=mat4)
cell20.region = +surf140 & -surf142 & -surf12

# Tu
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = +surf142 & -surf144 & -surf12

# Oy
cell22 = openmc.Cell(cell_id=22, fill=mat4)
cell22.region = +surf144 & -surf146 & -surf12

# Tu
cell23 = openmc.Cell(cell_id=23, fill=mat3)
cell23.region = +surf146 & -surf161 & -surf12

# Al
cell24 = openmc.Cell(cell_id=24, fill=mat1)
cell24.region = +surf129 & -surf131 & +surf10 & -surf17

# Al
cell25 = openmc.Cell(cell_id=25, fill=mat1)
cell25.region = +surf202 & -surf101 & +surf8 & -surf18

# Al
cell26 = openmc.Cell(cell_id=26, fill=mat1)
cell26.region = +surf203 & -surf201 & -surf3

# Al
cell27 = openmc.Cell(cell_id=27, fill=mat1)
cell27.region = +surf205 & -surf203 & -surf7

# Al
cell28 = openmc.Cell(cell_id=28, fill=mat1)
cell28.region = +surf204 & -surf202 & +surf12 & -surf14

# Al
cell29 = openmc.Cell(cell_id=29, fill=mat1)
cell29.region = +surf205 & -surf204 & +surf11 & -surf19

# SS
cell30 = openmc.Cell(cell_id=30, fill=mat2)
cell30.region = +surf206 & -surf205 & -surf20

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30])
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
source.space = openmc.stats.Box((-9.0, -9.0, -0.598), (9.0, 9.0, 15.482))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
