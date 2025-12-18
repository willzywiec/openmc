"""
MIX-MET-MIXED-001-1: Heterogeneous cylinder of Pu, HEU and CH2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.455200e-02)
mat1.add_nuclide("Pu240", 2.138900e-03)
mat1.add_nuclide("Pu241", 9.281000e-05)
mat1.add_element("C", 1.864000e-04)
mat1.add_element("Fe", 2.605800e-05)
mat1.add_nuclide("U238", 4.232300e-06)

# HEU
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 5.642000e-04)
mat2.add_nuclide("U235", 4.569500e-02)
mat2.add_nuclide("U238", 1.335000e-03)
mat2.add_element("C", 7.456200e-05)
mat2.add_element("Fe", 1.804100e-05)
mat2.add_element("W", 9.133500e-07)

# Steel can
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.049400e-02)
mat3.add_element("C", 3.422500e-04)
mat3.add_element("Si", 8.781900e-04)
mat3.add_element("Ti", 6.009800e-04)
mat3.add_element("Cr", 1.423100e-02)
mat3.add_element("Mn", 1.496500e-03)
mat3.add_element("Ni", 7.004100e-03)

# Steel 10
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 8.224200e-02)
mat4.add_element("C", 4.053700e-04)
mat4.add_element("Si", 4.457800e-04)
mat4.add_element("Mn", 4.220200e-04)
mat4.add_element("Cr", 6.688500e-05)

# CH2 rings
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 3.932000e-02)
mat5.add_nuclide("H1", 7.864100e-02)
mat5.add_s_alpha_beta("c_H_in_CH2")

# CH2 discs
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("C", 3.808000e-02)
mat6.add_nuclide("H1", 7.616000e-02)
mat6.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# CH2 disc
surf1 = openmc.ZCylinder(surface_id=1, x0=7.913, y0=8.900, r=9.995)
# HEU
surf2 = openmc.ZCylinder(surface_id=2, x0=6.918, y0=7.913, r=9.995)
# CH2 disc
surf3 = openmc.ZCylinder(surface_id=3, x0=5.931, y0=6.918, r=9.995)
# Pu
surf4 = openmc.ZCylinder(surface_id=4, x0=5.461, y0=5.911, r=5.995)
# Steel can
surf5 = openmc.ZCylinder(surface_id=5, x0=5.441, y0=5.931, r=6.02)
# Steel can
surf6 = openmc.ZCylinder(surface_id=6, x0=5.666, y0=5.706, r=6.55)
# Void
surf7 = openmc.ZCylinder(surface_id=7, x0=5.706, y0=5.931, r=6.55)
# CH2 ring
surf8 = openmc.ZCylinder(surface_id=8, x0=5.441, y0=5.931, r=9.995)
# CH2 disc
surf9 = openmc.ZCylinder(surface_id=9, x0=4.454, y0=5.441, r=9.995)
# HEU
surf10 = openmc.ZCylinder(surface_id=10, x0=3.459, y0=4.454, r=9.995)
# CH2 disc
surf11 = openmc.ZCylinder(surface_id=11, x0=2.472, y0=3.459, r=9.995)
# Pu
surf12 = openmc.ZCylinder(surface_id=12, x0=2.002, y0=2.452, r=5.995)
# Steel can
surf13 = openmc.ZCylinder(surface_id=13, x0=1.982, y0=2.472, r=6.02)
# Steel can
surf14 = openmc.ZCylinder(surface_id=14, x0=2.207, y0=2.247, r=6.55)
# Void
surf15 = openmc.ZCylinder(surface_id=15, x0=2.247, y0=2.472, r=6.55)
# CH2 ring
surf16 = openmc.ZCylinder(surface_id=16, x0=1.982, y0=2.472, r=9.995)
# CH2 disc
surf17 = openmc.ZCylinder(surface_id=17, x0=0.995, y0=1.982, r=9.995)
# Hole in HEU
surf18 = openmc.ZCylinder(surface_id=18, r=1.75)
# HEU
surf19 = openmc.ZCylinder(surface_id=19, x0=0.0, y0=0.995, r=9.995)
# Steel
surf20 = openmc.ZCylinder(surface_id=20, r=12.0)
# Steel
surf21 = openmc.ZCylinder(surface_id=21, x0=0.0, y0=0.2, r=13.0)
# Steel
surf22 = openmc.ZCylinder(surface_id=22, x0=0.2, y0=0.8, r=13.0)
# CH2 disc
surf23 = openmc.ZCylinder(surface_id=23, x0=-2.107, y0=-1.12, r=9.995)
# Pu
surf24 = openmc.ZCylinder(surface_id=24, x0=-2.577, y0=-2.127, r=5.995)
# Steel can
surf25 = openmc.ZCylinder(surface_id=25, x0=-2.597, y0=-2.107, r=6.02)
# Steel can
surf26 = openmc.ZCylinder(surface_id=26, x0=-2.372, y0=-2.332, r=6.55)
# Void
surf27 = openmc.ZCylinder(surface_id=27, x0=-2.332, y0=-2.107, r=6.55)
# CH2 ring
surf28 = openmc.ZCylinder(surface_id=28, x0=-2.597, y0=-2.107, r=9.995)
# CH2 disc
surf29 = openmc.ZCylinder(surface_id=29, x0=-3.584, y0=-2.597, r=9.995)
# HEU
surf30 = openmc.ZCylinder(surface_id=30, x0=-4.579, y0=-3.584, r=9.995)
# CH2 disc
surf31 = openmc.ZCylinder(surface_id=31, x0=-5.566, y0=-4.579, r=9.995)
# Pu
surf32 = openmc.ZCylinder(surface_id=32, x0=-6.036, y0=-5.586, r=5.995)
# Steel can
surf33 = openmc.ZCylinder(surface_id=33, x0=-6.056, y0=-5.566, r=6.02)
# Steel can
surf34 = openmc.ZCylinder(surface_id=34, x0=-5.831, y0=-5.791, r=6.55)
# Void
surf35 = openmc.ZCylinder(surface_id=35, x0=-5.791, y0=-5.566, r=6.55)
# CH2 ring
surf36 = openmc.ZCylinder(surface_id=36, x0=-6.056, y0=-5.566, r=9.995)
# CH2 disc
surf37 = openmc.ZCylinder(surface_id=37, x0=-7.043, y0=-6.056, r=9.995)
# HEU
surf38 = openmc.ZCylinder(surface_id=38, x0=-8.038, y0=-7.043, r=9.995)
# CH2 disc
surf39 = openmc.ZCylinder(surface_id=39, x0=-9.025, y0=-8.038, r=9.995)
# Pu
surf40 = openmc.ZCylinder(surface_id=40, x0=-9.495, y0=-9.045, r=5.995)
# Steel can
surf41 = openmc.ZCylinder(surface_id=41, x0=-9.515, y0=-9.025, r=6.02)
# Steel can
surf42 = openmc.ZCylinder(surface_id=42, x0=-9.290, y0=-9.250, r=6.55)
# Void
surf43 = openmc.ZCylinder(surface_id=43, x0=-9.250, y0=-9.025, r=6.55)
# CH2 ring
surf44 = openmc.ZCylinder(surface_id=44, x0=-9.515, y0=-9.025, r=9.995)
# CH2 disc
surf45 = openmc.ZCylinder(surface_id=45, x0=-10.502, y0=-9.515, r=9.995)
# HEU
surf46 = openmc.ZCylinder(surface_id=46, x0=-11.497, y0=-10.502, r=9.995)
# CH2 disc
surf47 = openmc.ZCylinder(surface_id=47, x0=-12.484, y0=-11.497, r=9.995)
# Pu
surf48 = openmc.ZCylinder(surface_id=48, x0=-12.954, y0=-12.504, r=5.995)
# Steel can
surf49 = openmc.ZCylinder(surface_id=49, x0=-12.974, y0=-12.484, r=6.02)
# Steel can
surf50 = openmc.ZCylinder(surface_id=50, x0=-12.749, y0=-12.709, r=6.55)
# Void ring
surf51 = openmc.ZCylinder(surface_id=51, x0=-12.709, y0=-12.484, r=6.55)
# CH2 ring
surf52 = openmc.ZCylinder(surface_id=52, x0=-12.974, y0=-12.484, r=9.995)
# CH2 disc
surf53 = openmc.ZCylinder(surface_id=53, x0=-13.961, y0=-12.974, r=9.995)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Disc
cell1 = openmc.Cell(cell_id=1, fill=mat6)
cell1.region = -surf1

# HEU
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# Disc
cell3 = openmc.Cell(cell_id=3, fill=mat6)
cell3.region = +surf2 & -surf3

# Pu
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = -surf4

# Can
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf3 & +surf4 & -surf5

# Can
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf5 & -surf6

# Ring
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = +surf3 & +surf5 & +surf6 & +surf7 & -surf8

# Disc
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = +surf8 & -surf9

# HEU
cell9 = openmc.Cell(cell_id=9, fill=mat2)
cell9.region = +surf9 & -surf10

# Disc
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = +surf10 & -surf11

# Pu
cell11 = openmc.Cell(cell_id=11, fill=mat1)
cell11.region = -surf12

# Can
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = +surf11 & +surf12 & -surf13

# Can
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = +surf13 & -surf14

# Ring
cell14 = openmc.Cell(cell_id=14, fill=mat5)
cell14.region = +surf11 & +surf13 & +surf14 & +surf15 & -surf16

# Disc
cell15 = openmc.Cell(cell_id=15, fill=mat6)
cell15.region = +surf16 & -surf17

# HEU
cell16 = openmc.Cell(cell_id=16, fill=mat2)
cell16.region = +surf17 & +surf18 & -surf19

# Stl
cell17 = openmc.Cell(cell_id=17, fill=mat4)
cell17.region = +surf19 & -surf21

# Stl
cell18 = openmc.Cell(cell_id=18, fill=mat4)
cell18.region = +surf20 & +surf21 & -surf22

# Disc
cell19 = openmc.Cell(cell_id=19, fill=mat6)
cell19.region = -surf23

# Pu
cell20 = openmc.Cell(cell_id=20, fill=mat1)
cell20.region = -surf24

# Can
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = +surf23 & +surf24 & -surf25

# Can
cell22 = openmc.Cell(cell_id=22, fill=mat3)
cell22.region = +surf25 & -surf26

# Ring
cell23 = openmc.Cell(cell_id=23, fill=mat5)
cell23.region = +surf23 & +surf25 & +surf26 & +surf27 & -surf28

# Disc
cell24 = openmc.Cell(cell_id=24, fill=mat6)
cell24.region = +surf28 & -surf29

# HEU
cell25 = openmc.Cell(cell_id=25, fill=mat2)
cell25.region = +surf29 & -surf30

# Disc
cell26 = openmc.Cell(cell_id=26, fill=mat6)
cell26.region = +surf30 & -surf31

# Pu
cell27 = openmc.Cell(cell_id=27, fill=mat1)
cell27.region = -surf32

# Can
cell28 = openmc.Cell(cell_id=28, fill=mat3)
cell28.region = +surf31 & +surf32 & -surf33

# Can
cell29 = openmc.Cell(cell_id=29, fill=mat3)
cell29.region = +surf33 & -surf34

# Ring
cell30 = openmc.Cell(cell_id=30, fill=mat5)
cell30.region = +surf31 & +surf33 & +surf34 & +surf35 & -surf36

# Disc
cell31 = openmc.Cell(cell_id=31, fill=mat6)
cell31.region = +surf36 & -surf37

# HEU
cell32 = openmc.Cell(cell_id=32, fill=mat2)
cell32.region = +surf37 & -surf38

# Disc
cell33 = openmc.Cell(cell_id=33, fill=mat6)
cell33.region = +surf38 & -surf39

# Pu
cell34 = openmc.Cell(cell_id=34, fill=mat1)
cell34.region = -surf40

# Can
cell35 = openmc.Cell(cell_id=35, fill=mat3)
cell35.region = +surf39 & +surf40 & -surf41

# Can
cell36 = openmc.Cell(cell_id=36, fill=mat3)
cell36.region = +surf41 & -surf42

# Ring
cell37 = openmc.Cell(cell_id=37, fill=mat5)
cell37.region = +surf39 & +surf41 & +surf42 & +surf43 & -surf44

# Disc
cell38 = openmc.Cell(cell_id=38, fill=mat6)
cell38.region = +surf44 & -surf45

# HEU
cell39 = openmc.Cell(cell_id=39, fill=mat2)
cell39.region = +surf45 & -surf46

# Disc
cell40 = openmc.Cell(cell_id=40, fill=mat6)
cell40.region = +surf46 & -surf47

# Pu
cell41 = openmc.Cell(cell_id=41, fill=mat1)
cell41.region = -surf48

# Can
cell42 = openmc.Cell(cell_id=42, fill=mat3)
cell42.region = +surf47 & +surf48 & -surf49

# Can
cell43 = openmc.Cell(cell_id=43, fill=mat3)
cell43.region = +surf49 & -surf50

# Ring
cell44 = openmc.Cell(cell_id=44, fill=mat5)
cell44.region = +surf47 & +surf49 & +surf50 & +surf51 & -surf52

# Disc
cell45 = openmc.Cell(cell_id=45, fill=mat6)
cell45.region = +surf49 & +surf52 & -surf53

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45])
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
source.space = openmc.stats.Box((-3.0, -3.0, -13.7), (3.0, 3.0, 8.4))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
