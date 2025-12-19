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
surf1 = openmc.ZCylinder(surface_id=1, r=9.995)
# HEU
surf2 = openmc.ZCylinder(surface_id=2, r=9.995)
# CH2 disc
surf3 = openmc.ZCylinder(surface_id=3, r=9.995)
# Pu
surf4 = openmc.ZCylinder(surface_id=4, r=5.995)
# Steel can
surf5 = openmc.ZCylinder(surface_id=5, r=6.02)
# Steel can
surf6 = openmc.ZCylinder(surface_id=6, r=6.55)
# Void
surf7 = openmc.ZCylinder(surface_id=7, r=6.55)
# CH2 ring
surf8 = openmc.ZCylinder(surface_id=8, r=9.995)
# CH2 disc
surf9 = openmc.ZCylinder(surface_id=9, r=9.995)
# HEU
surf10 = openmc.ZCylinder(surface_id=10, r=9.995)
# CH2 disc
surf11 = openmc.ZCylinder(surface_id=11, r=9.995)
# Pu
surf12 = openmc.ZCylinder(surface_id=12, r=5.995)
# Steel can
surf13 = openmc.ZCylinder(surface_id=13, r=6.02)
# Steel can
surf14 = openmc.ZCylinder(surface_id=14, r=6.55)
# Void
surf15 = openmc.ZCylinder(surface_id=15, r=6.55)
# CH2 ring
surf16 = openmc.ZCylinder(surface_id=16, r=9.995)
# CH2 disc
surf17 = openmc.ZCylinder(surface_id=17, r=9.995)
# Hole in HEU
surf18 = openmc.ZCylinder(surface_id=18, r=1.75)
# HEU
surf19 = openmc.ZCylinder(surface_id=19, r=9.995)
# Steel
surf20 = openmc.ZCylinder(surface_id=20, r=12.0)
# Steel
surf21 = openmc.ZCylinder(surface_id=21, r=13.0)
# Steel
surf22 = openmc.ZCylinder(surface_id=22, r=13.0)
# CH2 disc
surf23 = openmc.ZCylinder(surface_id=23, r=9.995)
# Pu
surf24 = openmc.ZCylinder(surface_id=24, r=5.995)
# Steel can
surf25 = openmc.ZCylinder(surface_id=25, r=6.02)
# Steel can
surf26 = openmc.ZCylinder(surface_id=26, r=6.55)
# Void
surf27 = openmc.ZCylinder(surface_id=27, r=6.55)
# CH2 ring
surf28 = openmc.ZCylinder(surface_id=28, r=9.995)
# CH2 disc
surf29 = openmc.ZCylinder(surface_id=29, r=9.995)
# HEU
surf30 = openmc.ZCylinder(surface_id=30, r=9.995)
# CH2 disc
surf31 = openmc.ZCylinder(surface_id=31, r=9.995)
# Pu
surf32 = openmc.ZCylinder(surface_id=32, r=5.995)
# Steel can
surf33 = openmc.ZCylinder(surface_id=33, r=6.02)
# Steel can
surf34 = openmc.ZCylinder(surface_id=34, r=6.55)
# Void
surf35 = openmc.ZCylinder(surface_id=35, r=6.55)
# CH2 ring
surf36 = openmc.ZCylinder(surface_id=36, r=9.995)
# CH2 disc
surf37 = openmc.ZCylinder(surface_id=37, r=9.995)
# HEU
surf38 = openmc.ZCylinder(surface_id=38, r=9.995)
# CH2 disc
surf39 = openmc.ZCylinder(surface_id=39, r=9.995)
# Pu
surf40 = openmc.ZCylinder(surface_id=40, r=5.995)
# Steel can
surf41 = openmc.ZCylinder(surface_id=41, r=6.02)
# Steel can
surf42 = openmc.ZCylinder(surface_id=42, r=6.55)
# Void
surf43 = openmc.ZCylinder(surface_id=43, r=6.55)
# CH2 ring
surf44 = openmc.ZCylinder(surface_id=44, r=9.995)
# CH2 disc
surf45 = openmc.ZCylinder(surface_id=45, r=9.995)
# HEU
surf46 = openmc.ZCylinder(surface_id=46, r=9.995)
# CH2 disc
surf47 = openmc.ZCylinder(surface_id=47, r=9.995)
# Pu
surf48 = openmc.ZCylinder(surface_id=48, r=5.995)
# Steel can
surf49 = openmc.ZCylinder(surface_id=49, r=6.02)
# Steel can
surf50 = openmc.ZCylinder(surface_id=50, r=6.55)
# Void ring
surf51 = openmc.ZCylinder(surface_id=51, r=6.55)
# CH2 ring
surf52 = openmc.ZCylinder(surface_id=52, r=9.995)
# CH2 disc
surf53 = openmc.ZCylinder(surface_id=53, r=9.995)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=7.913)
surf1_zmax = openmc.ZPlane(z0=8.9)
surf2_zmin = openmc.ZPlane(z0=6.918)
surf2_zmax = openmc.ZPlane(z0=7.913)
surf3_zmin = openmc.ZPlane(z0=5.931)
surf3_zmax = openmc.ZPlane(z0=6.918)
surf4_zmin = openmc.ZPlane(z0=5.461)
surf4_zmax = openmc.ZPlane(z0=5.911)
surf5_zmin = openmc.ZPlane(z0=5.441)
surf5_zmax = openmc.ZPlane(z0=5.931)
surf6_zmin = openmc.ZPlane(z0=5.666)
surf6_zmax = openmc.ZPlane(z0=5.706)
surf7_zmin = openmc.ZPlane(z0=5.706)
surf7_zmax = openmc.ZPlane(z0=5.931)
surf8_zmin = openmc.ZPlane(z0=5.441)
surf8_zmax = openmc.ZPlane(z0=5.931)
surf9_zmin = openmc.ZPlane(z0=4.454)
surf9_zmax = openmc.ZPlane(z0=5.441)
surf10_zmin = openmc.ZPlane(z0=3.459)
surf10_zmax = openmc.ZPlane(z0=4.454)
surf11_zmin = openmc.ZPlane(z0=2.472)
surf11_zmax = openmc.ZPlane(z0=3.459)
surf12_zmin = openmc.ZPlane(z0=2.002)
surf12_zmax = openmc.ZPlane(z0=2.452)
surf13_zmin = openmc.ZPlane(z0=1.982)
surf13_zmax = openmc.ZPlane(z0=2.472)
surf14_zmin = openmc.ZPlane(z0=2.207)
surf14_zmax = openmc.ZPlane(z0=2.247)
surf15_zmin = openmc.ZPlane(z0=2.247)
surf15_zmax = openmc.ZPlane(z0=2.472)
surf16_zmin = openmc.ZPlane(z0=1.982)
surf16_zmax = openmc.ZPlane(z0=2.472)
surf17_zmin = openmc.ZPlane(z0=0.995)
surf17_zmax = openmc.ZPlane(z0=1.982)
surf19_zmin = openmc.ZPlane(z0=0.0)
surf19_zmax = openmc.ZPlane(z0=0.995)
surf21_zmin = openmc.ZPlane(z0=0.0)
surf21_zmax = openmc.ZPlane(z0=0.2)
surf22_zmin = openmc.ZPlane(z0=0.2)
surf22_zmax = openmc.ZPlane(z0=0.8)
surf23_zmin = openmc.ZPlane(z0=-2.107)
surf23_zmax = openmc.ZPlane(z0=-1.12)
surf24_zmin = openmc.ZPlane(z0=-2.577)
surf24_zmax = openmc.ZPlane(z0=-2.127)
surf25_zmin = openmc.ZPlane(z0=-2.597)
surf25_zmax = openmc.ZPlane(z0=-2.107)
surf26_zmin = openmc.ZPlane(z0=-2.372)
surf26_zmax = openmc.ZPlane(z0=-2.332)
surf27_zmin = openmc.ZPlane(z0=-2.332)
surf27_zmax = openmc.ZPlane(z0=-2.107)
surf28_zmin = openmc.ZPlane(z0=-2.597)
surf28_zmax = openmc.ZPlane(z0=-2.107)
surf29_zmin = openmc.ZPlane(z0=-3.584)
surf29_zmax = openmc.ZPlane(z0=-2.597)
surf30_zmin = openmc.ZPlane(z0=-4.579)
surf30_zmax = openmc.ZPlane(z0=-3.584)
surf31_zmin = openmc.ZPlane(z0=-5.566)
surf31_zmax = openmc.ZPlane(z0=-4.579)
surf32_zmin = openmc.ZPlane(z0=-6.036)
surf32_zmax = openmc.ZPlane(z0=-5.586)
surf33_zmin = openmc.ZPlane(z0=-6.056)
surf33_zmax = openmc.ZPlane(z0=-5.566)
surf34_zmin = openmc.ZPlane(z0=-5.831)
surf34_zmax = openmc.ZPlane(z0=-5.791)
surf35_zmin = openmc.ZPlane(z0=-5.791)
surf35_zmax = openmc.ZPlane(z0=-5.566)
surf36_zmin = openmc.ZPlane(z0=-6.056)
surf36_zmax = openmc.ZPlane(z0=-5.566)
surf37_zmin = openmc.ZPlane(z0=-7.043)
surf37_zmax = openmc.ZPlane(z0=-6.056)
surf38_zmin = openmc.ZPlane(z0=-8.038)
surf38_zmax = openmc.ZPlane(z0=-7.043)
surf39_zmin = openmc.ZPlane(z0=-9.025)
surf39_zmax = openmc.ZPlane(z0=-8.038)
surf40_zmin = openmc.ZPlane(z0=-9.495)
surf40_zmax = openmc.ZPlane(z0=-9.045)
surf41_zmin = openmc.ZPlane(z0=-9.515)
surf41_zmax = openmc.ZPlane(z0=-9.025)
surf42_zmin = openmc.ZPlane(z0=-9.29)
surf42_zmax = openmc.ZPlane(z0=-9.25)
surf43_zmin = openmc.ZPlane(z0=-9.25)
surf43_zmax = openmc.ZPlane(z0=-9.025)
surf44_zmin = openmc.ZPlane(z0=-9.515)
surf44_zmax = openmc.ZPlane(z0=-9.025)
surf45_zmin = openmc.ZPlane(z0=-10.502)
surf45_zmax = openmc.ZPlane(z0=-9.515)
surf46_zmin = openmc.ZPlane(z0=-11.497)
surf46_zmax = openmc.ZPlane(z0=-10.502)
surf47_zmin = openmc.ZPlane(z0=-12.484)
surf47_zmax = openmc.ZPlane(z0=-11.497)
surf48_zmin = openmc.ZPlane(z0=-12.954)
surf48_zmax = openmc.ZPlane(z0=-12.504)
surf49_zmin = openmc.ZPlane(z0=-12.974)
surf49_zmax = openmc.ZPlane(z0=-12.484)
surf50_zmin = openmc.ZPlane(z0=-12.749)
surf50_zmax = openmc.ZPlane(z0=-12.709)
surf51_zmin = openmc.ZPlane(z0=-12.709)
surf51_zmax = openmc.ZPlane(z0=-12.484)
surf52_zmin = openmc.ZPlane(z0=-12.974)
surf52_zmax = openmc.ZPlane(z0=-12.484)
surf53_zmin = openmc.ZPlane(z0=-13.961)
surf53_zmax = openmc.ZPlane(z0=-12.974)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Disc
cell1 = openmc.Cell(cell_id=1, fill=mat6)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax)

# HEU
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# Disc
cell3 = openmc.Cell(cell_id=3, fill=mat6)
cell3.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# Pu
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = (-surf4 & +surf4_zmin & -surf4_zmax)

# Can
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# Can
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)

# Ring
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# Disc
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = (+surf8 | -surf8_zmin | +surf8_zmax) & (-surf9 & +surf9_zmin & -surf9_zmax)

# HEU
cell9 = openmc.Cell(cell_id=9, fill=mat2)
cell9.region = (+surf9 | -surf9_zmin | +surf9_zmax) & (-surf10 & +surf10_zmin & -surf10_zmax)

# Disc
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = (+surf10 | -surf10_zmin | +surf10_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax)

# Pu
cell11 = openmc.Cell(cell_id=11, fill=mat1)
cell11.region = (-surf12 & +surf12_zmin & -surf12_zmax)

# Can
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)

# Can
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)

# Ring
cell14 = openmc.Cell(cell_id=14, fill=mat5)
cell14.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (+surf15 | -surf15_zmin | +surf15_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)

# Disc
cell15 = openmc.Cell(cell_id=15, fill=mat6)
cell15.region = (+surf16 | -surf16_zmin | +surf16_zmax) & (-surf17 & +surf17_zmin & -surf17_zmax)

# HEU
cell16 = openmc.Cell(cell_id=16, fill=mat2)
cell16.region = (+surf17 | -surf17_zmin | +surf17_zmax) & +surf18 & (-surf19 & +surf19_zmin & -surf19_zmax)

# Stl
cell17 = openmc.Cell(cell_id=17, fill=mat4)
cell17.region = (+surf19 | -surf19_zmin | +surf19_zmax) & (-surf21 & +surf21_zmin & -surf21_zmax)

# Stl
cell18 = openmc.Cell(cell_id=18, fill=mat4)
cell18.region = +surf20 & (+surf21 | -surf21_zmin | +surf21_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax)

# Disc
cell19 = openmc.Cell(cell_id=19, fill=mat6)
cell19.region = (-surf23 & +surf23_zmin & -surf23_zmax)

# Pu
cell20 = openmc.Cell(cell_id=20, fill=mat1)
cell20.region = (-surf24 & +surf24_zmin & -surf24_zmax)

# Can
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = (+surf23 | -surf23_zmin | +surf23_zmax) & (+surf24 | -surf24_zmin | +surf24_zmax) & (-surf25 & +surf25_zmin & -surf25_zmax)

# Can
cell22 = openmc.Cell(cell_id=22, fill=mat3)
cell22.region = (+surf25 | -surf25_zmin | +surf25_zmax) & (-surf26 & +surf26_zmin & -surf26_zmax)

# Ring
cell23 = openmc.Cell(cell_id=23, fill=mat5)
cell23.region = (+surf23 | -surf23_zmin | +surf23_zmax) & (+surf25 | -surf25_zmin | +surf25_zmax) & (+surf26 | -surf26_zmin | +surf26_zmax) & (+surf27 | -surf27_zmin | +surf27_zmax) & (-surf28 & +surf28_zmin & -surf28_zmax)

# Disc
cell24 = openmc.Cell(cell_id=24, fill=mat6)
cell24.region = (+surf28 | -surf28_zmin | +surf28_zmax) & (-surf29 & +surf29_zmin & -surf29_zmax)

# HEU
cell25 = openmc.Cell(cell_id=25, fill=mat2)
cell25.region = (+surf29 | -surf29_zmin | +surf29_zmax) & (-surf30 & +surf30_zmin & -surf30_zmax)

# Disc
cell26 = openmc.Cell(cell_id=26, fill=mat6)
cell26.region = (+surf30 | -surf30_zmin | +surf30_zmax) & (-surf31 & +surf31_zmin & -surf31_zmax)

# Pu
cell27 = openmc.Cell(cell_id=27, fill=mat1)
cell27.region = (-surf32 & +surf32_zmin & -surf32_zmax)

# Can
cell28 = openmc.Cell(cell_id=28, fill=mat3)
cell28.region = (+surf31 | -surf31_zmin | +surf31_zmax) & (+surf32 | -surf32_zmin | +surf32_zmax) & (-surf33 & +surf33_zmin & -surf33_zmax)

# Can
cell29 = openmc.Cell(cell_id=29, fill=mat3)
cell29.region = (+surf33 | -surf33_zmin | +surf33_zmax) & (-surf34 & +surf34_zmin & -surf34_zmax)

# Ring
cell30 = openmc.Cell(cell_id=30, fill=mat5)
cell30.region = (+surf31 | -surf31_zmin | +surf31_zmax) & (+surf33 | -surf33_zmin | +surf33_zmax) & (+surf34 | -surf34_zmin | +surf34_zmax) & (+surf35 | -surf35_zmin | +surf35_zmax) & (-surf36 & +surf36_zmin & -surf36_zmax)

# Disc
cell31 = openmc.Cell(cell_id=31, fill=mat6)
cell31.region = (+surf36 | -surf36_zmin | +surf36_zmax) & (-surf37 & +surf37_zmin & -surf37_zmax)

# HEU
cell32 = openmc.Cell(cell_id=32, fill=mat2)
cell32.region = (+surf37 | -surf37_zmin | +surf37_zmax) & (-surf38 & +surf38_zmin & -surf38_zmax)

# Disc
cell33 = openmc.Cell(cell_id=33, fill=mat6)
cell33.region = (+surf38 | -surf38_zmin | +surf38_zmax) & (-surf39 & +surf39_zmin & -surf39_zmax)

# Pu
cell34 = openmc.Cell(cell_id=34, fill=mat1)
cell34.region = (-surf40 & +surf40_zmin & -surf40_zmax)

# Can
cell35 = openmc.Cell(cell_id=35, fill=mat3)
cell35.region = (+surf39 | -surf39_zmin | +surf39_zmax) & (+surf40 | -surf40_zmin | +surf40_zmax) & (-surf41 & +surf41_zmin & -surf41_zmax)

# Can
cell36 = openmc.Cell(cell_id=36, fill=mat3)
cell36.region = (+surf41 | -surf41_zmin | +surf41_zmax) & (-surf42 & +surf42_zmin & -surf42_zmax)

# Ring
cell37 = openmc.Cell(cell_id=37, fill=mat5)
cell37.region = (+surf39 | -surf39_zmin | +surf39_zmax) & (+surf41 | -surf41_zmin | +surf41_zmax) & (+surf42 | -surf42_zmin | +surf42_zmax) & (+surf43 | -surf43_zmin | +surf43_zmax) & (-surf44 & +surf44_zmin & -surf44_zmax)

# Disc
cell38 = openmc.Cell(cell_id=38, fill=mat6)
cell38.region = (+surf44 | -surf44_zmin | +surf44_zmax) & (-surf45 & +surf45_zmin & -surf45_zmax)

# HEU
cell39 = openmc.Cell(cell_id=39, fill=mat2)
cell39.region = (+surf45 | -surf45_zmin | +surf45_zmax) & (-surf46 & +surf46_zmin & -surf46_zmax)

# Disc
cell40 = openmc.Cell(cell_id=40, fill=mat6)
cell40.region = (+surf46 | -surf46_zmin | +surf46_zmax) & (-surf47 & +surf47_zmin & -surf47_zmax)

# Pu
cell41 = openmc.Cell(cell_id=41, fill=mat1)
cell41.region = (-surf48 & +surf48_zmin & -surf48_zmax)

# Can
cell42 = openmc.Cell(cell_id=42, fill=mat3)
cell42.region = (+surf47 | -surf47_zmin | +surf47_zmax) & (+surf48 | -surf48_zmin | +surf48_zmax) & (-surf49 & +surf49_zmin & -surf49_zmax)

# Can
cell43 = openmc.Cell(cell_id=43, fill=mat3)
cell43.region = (+surf49 | -surf49_zmin | +surf49_zmax) & (-surf50 & +surf50_zmin & -surf50_zmax)

# Ring
cell44 = openmc.Cell(cell_id=44, fill=mat5)
cell44.region = (+surf47 | -surf47_zmin | +surf47_zmax) & (+surf49 | -surf49_zmin | +surf49_zmax) & (+surf50 | -surf50_zmin | +surf50_zmax) & (+surf51 | -surf51_zmin | +surf51_zmax) & (-surf52 & +surf52_zmin & -surf52_zmax)

# Disc
cell45 = openmc.Cell(cell_id=45, fill=mat6)
cell45.region = (+surf49 | -surf49_zmin | +surf49_zmax) & (+surf52 | -surf52_zmin | +surf52_zmax) & (-surf53 & +surf53_zmin & -surf53_zmax)

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
