"""
IEU-COMP-THERM-002-1: U(17)O2 annular fuel rods with 6.8 cm pitch; no absorbers; 22.7 C
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(17)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.668300e-05)
mat1.add_nuclide("U235", 1.882700e-03)
mat1.add_nuclide("U238", 9.059400e-03)
mat1.add_nuclide("O16", 2.239600e-02)

# Stainless
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.998600e-02)
mat2.add_element("Cr", 1.572400e-02)
mat2.add_element("Ni", 8.503000e-03)
mat2.add_element("Mn", 1.043100e-03)
mat2.add_element("Si", 8.501800e-04)
mat2.add_element("Ti", 4.737600e-04)
mat2.add_element("C", 4.174800e-04)

# Aluminum
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 6.026200e-02)

# Water at 22.7 C, 0.1 MPa
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.669500e-02)
mat4.add_nuclide("O16", 3.334800e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

surf1_cyl = openmc.ZCylinder(surface_id=1, x0=tr, y0=0, r=2.35)
surf1_zmin = openmc.ZPlane(z0=34.0)
surf1_zmax = openmc.ZPlane(z0=0.0)
surf1 = (surf1_cyl, surf1_zmin, surf1_zmax)
surf2_cyl = openmc.ZCylinder(surface_id=2, x0=tr, y0=-5.88897, r=2.35)
surf2_zmin = openmc.ZPlane(z0=30.6)
surf2_zmax = openmc.ZPlane(z0=0.0)
surf2 = (surf2_cyl, surf2_zmin, surf2_zmax)
surf3_cyl = openmc.ZCylinder(surface_id=3, x0=tr, y0=5.88897, r=2.35)
surf3_zmin = openmc.ZPlane(z0=30.6)
surf3_zmax = openmc.ZPlane(z0=0.0)
surf3 = (surf3_cyl, surf3_zmin, surf3_zmax)
surf4_cyl = openmc.ZCylinder(surface_id=4, x0=tr, y0=-11.77795, r=2.35)
surf4_zmin = openmc.ZPlane(z0=27.2)
surf4_zmax = openmc.ZPlane(z0=0.0)
surf4 = (surf4_cyl, surf4_zmin, surf4_zmax)
surf5_cyl = openmc.ZCylinder(surface_id=5, x0=tr, y0=0, r=2.35)
surf5_zmin = openmc.ZPlane(z0=27.2)
surf5_zmax = openmc.ZPlane(z0=0.0)
surf5 = (surf5_cyl, surf5_zmin, surf5_zmax)
surf6_cyl = openmc.ZCylinder(surface_id=6, x0=tr, y0=11.77795, r=2.35)
surf6_zmin = openmc.ZPlane(z0=27.2)
surf6_zmax = openmc.ZPlane(z0=0.0)
surf6 = (surf6_cyl, surf6_zmin, surf6_zmax)
surf7_cyl = openmc.ZCylinder(surface_id=7, x0=tr, y0=-17.66692, r=2.35)
surf7_zmin = openmc.ZPlane(z0=23.8)
surf7_zmax = openmc.ZPlane(z0=0.0)
surf7 = (surf7_cyl, surf7_zmin, surf7_zmax)
surf8_cyl = openmc.ZCylinder(surface_id=8, x0=tr, y0=-5.88897, r=2.35)
surf8_zmin = openmc.ZPlane(z0=23.8)
surf8_zmax = openmc.ZPlane(z0=0.0)
surf8 = (surf8_cyl, surf8_zmin, surf8_zmax)
surf9_cyl = openmc.ZCylinder(surface_id=9, x0=tr, y0=5.88897, r=2.35)
surf9_zmin = openmc.ZPlane(z0=23.8)
surf9_zmax = openmc.ZPlane(z0=0.0)
surf9 = (surf9_cyl, surf9_zmin, surf9_zmax)
surf10_cyl = openmc.ZCylinder(surface_id=10, x0=tr, y0=17.66692, r=2.35)
surf10_zmin = openmc.ZPlane(z0=23.8)
surf10_zmax = openmc.ZPlane(z0=0.0)
surf10 = (surf10_cyl, surf10_zmin, surf10_zmax)
surf11_cyl = openmc.ZCylinder(surface_id=11, x0=tr, y0=-23.55589, r=2.35)
surf11_zmin = openmc.ZPlane(z0=20.4)
surf11_zmax = openmc.ZPlane(z0=0.0)
surf11 = (surf11_cyl, surf11_zmin, surf11_zmax)
surf12_cyl = openmc.ZCylinder(surface_id=12, x0=tr, y0=-11.77795, r=2.35)
surf12_zmin = openmc.ZPlane(z0=20.4)
surf12_zmax = openmc.ZPlane(z0=0.0)
surf12 = (surf12_cyl, surf12_zmin, surf12_zmax)
surf13_cyl = openmc.ZCylinder(surface_id=13, x0=tr, y0=0, r=2.35)
surf13_zmin = openmc.ZPlane(z0=20.4)
surf13_zmax = openmc.ZPlane(z0=0.0)
surf13 = (surf13_cyl, surf13_zmin, surf13_zmax)
surf14_cyl = openmc.ZCylinder(surface_id=14, x0=tr, y0=11.77795, r=2.35)
surf14_zmin = openmc.ZPlane(z0=20.4)
surf14_zmax = openmc.ZPlane(z0=0.0)
surf14 = (surf14_cyl, surf14_zmin, surf14_zmax)
surf15_cyl = openmc.ZCylinder(surface_id=15, x0=tr, y0=23.55589, r=2.35)
surf15_zmin = openmc.ZPlane(z0=20.4)
surf15_zmax = openmc.ZPlane(z0=0.0)
surf15 = (surf15_cyl, surf15_zmin, surf15_zmax)
surf16_cyl = openmc.ZCylinder(surface_id=16, x0=tr, y0=-29.44486, r=2.35)
surf16_zmin = openmc.ZPlane(z0=17.0)
surf16_zmax = openmc.ZPlane(z0=0.0)
surf16 = (surf16_cyl, surf16_zmin, surf16_zmax)
surf17_cyl = openmc.ZCylinder(surface_id=17, x0=tr, y0=-17.66692, r=2.35)
surf17_zmin = openmc.ZPlane(z0=17.0)
surf17_zmax = openmc.ZPlane(z0=0.0)
surf17 = (surf17_cyl, surf17_zmin, surf17_zmax)
surf18_cyl = openmc.ZCylinder(surface_id=18, x0=tr, y0=-5.88897, r=2.35)
surf18_zmin = openmc.ZPlane(z0=17.0)
surf18_zmax = openmc.ZPlane(z0=0.0)
surf18 = (surf18_cyl, surf18_zmin, surf18_zmax)
surf19_cyl = openmc.ZCylinder(surface_id=19, x0=tr, y0=5.88897, r=2.35)
surf19_zmin = openmc.ZPlane(z0=17.0)
surf19_zmax = openmc.ZPlane(z0=0.0)
surf19 = (surf19_cyl, surf19_zmin, surf19_zmax)
surf20_cyl = openmc.ZCylinder(surface_id=20, x0=tr, y0=17.66692, r=2.35)
surf20_zmin = openmc.ZPlane(z0=17.0)
surf20_zmax = openmc.ZPlane(z0=0.0)
surf20 = (surf20_cyl, surf20_zmin, surf20_zmax)
surf21_cyl = openmc.ZCylinder(surface_id=21, x0=tr, y0=29.44486, r=2.35)
surf21_zmin = openmc.ZPlane(z0=17.0)
surf21_zmax = openmc.ZPlane(z0=0.0)
surf21 = (surf21_cyl, surf21_zmin, surf21_zmax)
surf22_cyl = openmc.ZCylinder(surface_id=22, x0=tr, y0=-23.55589, r=2.35)
surf22_zmin = openmc.ZPlane(z0=13.6)
surf22_zmax = openmc.ZPlane(z0=0.0)
surf22 = (surf22_cyl, surf22_zmin, surf22_zmax)
surf23_cyl = openmc.ZCylinder(surface_id=23, x0=tr, y0=-11.77795, r=2.35)
surf23_zmin = openmc.ZPlane(z0=13.6)
surf23_zmax = openmc.ZPlane(z0=0.0)
surf23 = (surf23_cyl, surf23_zmin, surf23_zmax)
surf24_cyl = openmc.ZCylinder(surface_id=24, x0=tr, y0=0, r=2.35)
surf24_zmin = openmc.ZPlane(z0=13.6)
surf24_zmax = openmc.ZPlane(z0=0.0)
surf24 = (surf24_cyl, surf24_zmin, surf24_zmax)
surf25_cyl = openmc.ZCylinder(surface_id=25, x0=tr, y0=11.77795, r=2.35)
surf25_zmin = openmc.ZPlane(z0=13.6)
surf25_zmax = openmc.ZPlane(z0=0.0)
surf25 = (surf25_cyl, surf25_zmin, surf25_zmax)
surf26_cyl = openmc.ZCylinder(surface_id=26, x0=tr, y0=23.55589, r=2.35)
surf26_zmin = openmc.ZPlane(z0=13.6)
surf26_zmax = openmc.ZPlane(z0=0.0)
surf26 = (surf26_cyl, surf26_zmin, surf26_zmax)
surf27_cyl = openmc.ZCylinder(surface_id=27, x0=tr, y0=-29.44486, r=2.35)
surf27_zmin = openmc.ZPlane(z0=10.2)
surf27_zmax = openmc.ZPlane(z0=0.0)
surf27 = (surf27_cyl, surf27_zmin, surf27_zmax)
surf28_cyl = openmc.ZCylinder(surface_id=28, x0=tr, y0=-17.66692, r=2.35)
surf28_zmin = openmc.ZPlane(z0=10.2)
surf28_zmax = openmc.ZPlane(z0=0.0)
surf28 = (surf28_cyl, surf28_zmin, surf28_zmax)
surf29_cyl = openmc.ZCylinder(surface_id=29, x0=tr, y0=-5.88897, r=2.35)
surf29_zmin = openmc.ZPlane(z0=10.2)
surf29_zmax = openmc.ZPlane(z0=0.0)
surf29 = (surf29_cyl, surf29_zmin, surf29_zmax)
surf30_cyl = openmc.ZCylinder(surface_id=30, x0=tr, y0=5.88897, r=2.35)
surf30_zmin = openmc.ZPlane(z0=10.2)
surf30_zmax = openmc.ZPlane(z0=0.0)
surf30 = (surf30_cyl, surf30_zmin, surf30_zmax)
surf31_cyl = openmc.ZCylinder(surface_id=31, x0=tr, y0=17.66692, r=2.35)
surf31_zmin = openmc.ZPlane(z0=10.2)
surf31_zmax = openmc.ZPlane(z0=0.0)
surf31 = (surf31_cyl, surf31_zmin, surf31_zmax)
surf32_cyl = openmc.ZCylinder(surface_id=32, x0=tr, y0=29.44486, r=2.35)
surf32_zmin = openmc.ZPlane(z0=10.2)
surf32_zmax = openmc.ZPlane(z0=0.0)
surf32 = (surf32_cyl, surf32_zmin, surf32_zmax)
surf33_cyl = openmc.ZCylinder(surface_id=33, x0=tr, y0=-23.55589, r=2.35)
surf33_zmin = openmc.ZPlane(z0=6.8)
surf33_zmax = openmc.ZPlane(z0=0.0)
surf33 = (surf33_cyl, surf33_zmin, surf33_zmax)
surf34_cyl = openmc.ZCylinder(surface_id=34, x0=tr, y0=-11.77795, r=2.35)
surf34_zmin = openmc.ZPlane(z0=6.8)
surf34_zmax = openmc.ZPlane(z0=0.0)
surf34 = (surf34_cyl, surf34_zmin, surf34_zmax)
surf35_cyl = openmc.ZCylinder(surface_id=35, x0=tr, y0=0, r=2.35)
surf35_zmin = openmc.ZPlane(z0=6.8)
surf35_zmax = openmc.ZPlane(z0=0.0)
surf35 = (surf35_cyl, surf35_zmin, surf35_zmax)
surf36_cyl = openmc.ZCylinder(surface_id=36, x0=tr, y0=11.77795, r=2.35)
surf36_zmin = openmc.ZPlane(z0=6.8)
surf36_zmax = openmc.ZPlane(z0=0.0)
surf36 = (surf36_cyl, surf36_zmin, surf36_zmax)
surf37_cyl = openmc.ZCylinder(surface_id=37, x0=tr, y0=23.55589, r=2.35)
surf37_zmin = openmc.ZPlane(z0=6.8)
surf37_zmax = openmc.ZPlane(z0=0.0)
surf37 = (surf37_cyl, surf37_zmin, surf37_zmax)
surf38_cyl = openmc.ZCylinder(surface_id=38, x0=tr, y0=-29.44486, r=2.35)
surf38_zmin = openmc.ZPlane(z0=3.4)
surf38_zmax = openmc.ZPlane(z0=0.0)
surf38 = (surf38_cyl, surf38_zmin, surf38_zmax)
surf39_cyl = openmc.ZCylinder(surface_id=39, x0=tr, y0=-17.66692, r=2.35)
surf39_zmin = openmc.ZPlane(z0=3.4)
surf39_zmax = openmc.ZPlane(z0=0.0)
surf39 = (surf39_cyl, surf39_zmin, surf39_zmax)
surf40_cyl = openmc.ZCylinder(surface_id=40, x0=tr, y0=-5.88897, r=2.35)
surf40_zmin = openmc.ZPlane(z0=3.4)
surf40_zmax = openmc.ZPlane(z0=0.0)
surf40 = (surf40_cyl, surf40_zmin, surf40_zmax)
surf41_cyl = openmc.ZCylinder(surface_id=41, x0=tr, y0=5.88897, r=2.35)
surf41_zmin = openmc.ZPlane(z0=3.4)
surf41_zmax = openmc.ZPlane(z0=0.0)
surf41 = (surf41_cyl, surf41_zmin, surf41_zmax)
surf42_cyl = openmc.ZCylinder(surface_id=42, x0=tr, y0=17.66692, r=2.35)
surf42_zmin = openmc.ZPlane(z0=3.4)
surf42_zmax = openmc.ZPlane(z0=0.0)
surf42 = (surf42_cyl, surf42_zmin, surf42_zmax)
surf43_cyl = openmc.ZCylinder(surface_id=43, x0=tr, y0=29.44486, r=2.35)
surf43_zmin = openmc.ZPlane(z0=3.4)
surf43_zmax = openmc.ZPlane(z0=0.0)
surf43 = (surf43_cyl, surf43_zmin, surf43_zmax)
surf44_cyl = openmc.ZCylinder(surface_id=44, x0=tr, y0=-23.55589, r=2.35)
surf44_zmin = openmc.ZPlane(z0=0.0)
surf44_zmax = openmc.ZPlane(z0=0.0)
surf44 = (surf44_cyl, surf44_zmin, surf44_zmax)
surf46_cyl = openmc.ZCylinder(surface_id=46, x0=tr, y0=11.77795, r=2.35)
surf46_zmin = openmc.ZPlane(z0=0.0)
surf46_zmax = openmc.ZPlane(z0=0.0)
surf46 = (surf46_cyl, surf46_zmin, surf46_zmax)
surf91_cyl = openmc.ZCylinder(surface_id=91, x0=tr, y0=-13.74094, r=1.6)
surf91_zmin = openmc.ZPlane(z0=3.4)
surf91_zmax = openmc.ZPlane(z0=0.0)
surf91 = (surf91_cyl, surf91_zmin, surf91_zmax)
surf93_cyl = openmc.ZCylinder(surface_id=93, x0=tr, y0=3.92598, r=1.6)
surf93_zmin = openmc.ZPlane(z0=-13.6)
surf93_zmax = openmc.ZPlane(z0=0.0)
surf93 = (surf93_cyl, surf93_zmin, surf93_zmax)
# Tube 1/inner
surf101 = openmc.ZCylinder(surface_id=101, r=1.05)
# Tube 1/outer
surf102 = openmc.ZCylinder(surface_id=102, r=1.1)
# Tube 2/inner
surf103 = openmc.ZCylinder(surface_id=103, r=1.3)
# Tube 2/outer
surf104 = openmc.ZCylinder(surface_id=104, r=1.5)
# Tube 3/inner
surf105 = openmc.ZCylinder(surface_id=105, r=1.7)
# Tube 3/outer
surf106 = openmc.ZCylinder(surface_id=106, r=1.9)
# Tube 4/inner
surf107 = openmc.ZCylinder(surface_id=107, r=2.2)
# Tube 4/outer
surf108 = openmc.ZCylinder(surface_id=108, r=2.5)
# Lower lattice plate
surf111 = openmc.ZCylinder(surface_id=111, r=0.75)
# Lower support plate
surf112 = openmc.ZCylinder(surface_id=112, r=2.35)
# Upper support plate central hole; unit cell boundary
surf113 = openmc.ZCylinder(surface_id=113, r=2.53)
# Bottom of support plate
surf121 = openmc.ZPlane(surface_id=121, z0=0.0)
# Bottom of lower lattice plate
surf122 = openmc.ZPlane(surface_id=122, z0=1.5)
# Top of lower lattice plate
surf123 = openmc.ZPlane(surface_id=123, z0=3.5)
# Bottom of the 4 tubes
surf124 = openmc.ZPlane(surface_id=124, z0=4.0)
# SS1/inner
surf201 = openmc.ZCylinder(surface_id=201, r=1.17)
# UO2/inner
surf202 = openmc.ZCylinder(surface_id=202, r=1.2)
# UO2/outer
surf203 = openmc.ZCylinder(surface_id=203, r=1.43)
# SS1/outer
surf204 = openmc.ZCylinder(surface_id=204, r=1.464)
# SS2/inner
surf205 = openmc.ZCylinder(surface_id=205, r=1.7968)
# UO2/inner
surf206 = openmc.ZCylinder(surface_id=206, r=1.83)
# UO2/outer
surf207 = openmc.ZCylinder(surface_id=207, r=2.06)
# SS2/outer
surf208 = openmc.ZCylinder(surface_id=208, r=2.09)
# SS3/inner
surf209 = openmc.ZCylinder(surface_id=209, r=2.26)
# SS3/outer
surf210 = openmc.ZCylinder(surface_id=210, r=2.29)
# Plug/lower
surf211 = openmc.ZPlane(surface_id=211, z0=3.0)
# Element/lower/top
surf212 = openmc.ZPlane(surface_id=212, z0=4.3)
# Lower plug/bottom
surf213 = openmc.ZPlane(surface_id=213, z0=5.6)
# Lower plug/top
surf214 = openmc.ZPlane(surface_id=214, z0=5.9)
# Upper plug/bottom
surf215 = openmc.ZPlane(surface_id=215, z0=65.9)
# Upper plub/top
surf216 = openmc.ZPlane(surface_id=216, z0=66.2)
# Element/upper/bottom
surf217 = openmc.ZPlane(surface_id=217, z0=90.2)
# Element/upper/top
surf218 = openmc.ZPlane(surface_id=218, z0=90.5)
# SST tube/inner
surf301 = openmc.ZCylinder(surface_id=301, x0=4.3, y0=999.9, r=1.2)
# SST tube/outer
surf302 = openmc.ZCylinder(surface_id=302, x0=4.0, y0=999.9, r=1.5)
# Hole in the upper lattice plate and boundary condition
surf303 = openmc.ZCylinder(surface_id=303, r=1.6)
# SST ring/inner
surf901 = openmc.ZCylinder(surface_id=901, r=40.0)
# SST ring/outer
surf902 = openmc.ZCylinder(surface_id=902, x0=-19.0, y0=0.0, r=40.5)
# SST lower lattice and support plate w/o holes
surf903 = openmc.ZCylinder(surface_id=903, x0=0.0, y0=3.5, r=41.0)
# SST upper lattice plate w/o holes
surf904 = openmc.ZCylinder(surface_id=904, x0=66.8, y0=68.8, r=41.0)
# SST cylindrical annulus/inner
surf905 = openmc.ZCylinder(surface_id=905, r=42.0)
# SST cylindrical annulus/outer
surf906 = openmc.ZCylinder(surface_id=906, r=44.0)
# Water reflector and boundary condition
surf999 = openmc.ZCylinder(surface_id=999, x0=-19.0, y0=106.0, r=60.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell()
u1_cell0.region = -surf101 & +surf124 & -surf999
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf101 & -surf102 & +surf124 & -surf999
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = +surf102 & -surf103 & +surf124 & -surf999
u1_cell3 = openmc.Cell(fill=mat2)
u1_cell3.region = +surf103 & -surf104 & +surf124 & -surf999
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf104 & -surf105 & +surf124 & -surf999
u1_cell5 = openmc.Cell(fill=mat2)
u1_cell5.region = +surf105 & -surf106 & +surf124 & -surf999
u1_cell6 = openmc.Cell()
u1_cell6.region = +surf106 & -surf107 & +surf124 & -surf999
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = +surf107 & -surf108 & +surf124 & -surf999
u1_cell8 = openmc.Cell(fill=mat2)
u1_cell8.region = +surf111 & +surf122 & -surf123 & -surf999
u1_cell9 = openmc.Cell(fill=mat2)
u1_cell9.region = +surf112 & +surf121 & -surf122 & -surf999
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9])

u2_cell0 = openmc.Cell(fill=mat2)
u2_cell0.region = +surf111 & +surf122 & -surf123 & -surf999
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0])

u3_cell0 = openmc.Cell(fill=mat2)
u3_cell0.region = +surf111 & +surf122 & -surf123 & -surf999
u3_cell1 = openmc.Cell(fill=mat2)
u3_cell1.region = -surf111 & +surf211 & -surf124 & -surf999
u3_cell2 = openmc.Cell(fill=mat2)
u3_cell2.region = +surf124 & -surf210 & -surf212 & -surf999
u3_cell3 = openmc.Cell(fill=mat2)
u3_cell3.region = +surf201 & -surf202 & +surf212 & -surf218
u3_cell4 = openmc.Cell(fill=mat2)
u3_cell4.region = +surf202 & -surf203 & +surf213 & -surf214
u3_cell5 = openmc.Cell(fill=mat1)
u3_cell5.region = +surf202 & -surf203 & +surf214 & -surf215
u3_cell6 = openmc.Cell(fill=mat2)
u3_cell6.region = +surf202 & -surf203 & +surf215 & -surf216
u3_cell7 = openmc.Cell(fill=mat2)
u3_cell7.region = +surf203 & -surf204 & +surf213 & -surf216
u3_cell8 = openmc.Cell(fill=mat2)
u3_cell8.region = +surf205 & -surf206 & +surf212 & -surf218
u3_cell9 = openmc.Cell(fill=mat2)
u3_cell9.region = +surf206 & -surf207 & +surf213 & -surf214
u3_cell10 = openmc.Cell(fill=mat1)
u3_cell10.region = +surf206 & -surf207 & +surf214 & -surf215
u3_cell11 = openmc.Cell(fill=mat2)
u3_cell11.region = +surf206 & -surf207 & +surf215 & -surf216
u3_cell12 = openmc.Cell(fill=mat2)
u3_cell12.region = +surf207 & -surf208 & +surf213 & -surf216
u3_cell13 = openmc.Cell(fill=mat2)
u3_cell13.region = +surf209 & -surf210 & +surf212 & -surf218
u3_cell14 = openmc.Cell(fill=mat2)
u3_cell14.region = +surf202 & -surf205 & +surf217 & -surf218
u3_cell15 = openmc.Cell(fill=mat2)
u3_cell15.region = +surf206 & -surf209 & +surf217 & -surf218
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5, u3_cell6, u3_cell7, u3_cell8, u3_cell9, u3_cell10, u3_cell11, u3_cell12, u3_cell13, u3_cell14, u3_cell15])

u4_cell0 = openmc.Cell()
u4_cell0.region = -surf301 & -surf999
u4_cell1 = openmc.Cell(fill=mat2)
u4_cell1.region = +surf301 & -surf302 & -surf999
u4_cell2 = openmc.Cell(fill=mat2)
u4_cell2.region = +surf111 & +surf122 & -surf123 & -surf999
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2])

u9_cell0 = openmc.Cell(fill=mat2)
u9_cell0.region = +surf901 & -surf902 & -surf999
u9_cell1 = openmc.Cell(fill=mat2)
u9_cell1.region = +surf902 & -surf903 & -surf999
u9_cell2 = openmc.Cell(fill=mat2)
u9_cell2.region = -surf904
u9_cell3 = openmc.Cell(fill=mat2)
u9_cell3.region = +surf905 & -surf906 & -surf999
universe9 = openmc.Universe(universe_id=9, cells=[u9_cell0, u9_cell1, u9_cell2, u9_cell3])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# EMPTY
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.translation = (0.0, 34.0, 0.0)
cell1.region = -surf999 & -surf1

# EMPTY
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.translation = (-5.88897, 30.6, 0.0)
cell2.region = -surf999 & -surf2

# EMPTY
cell3 = openmc.Cell(cell_id=3, fill=universe2)
cell3.translation = (5.88897, 30.6, 0.0)
cell3.region = -surf999 & -surf3

# EMPTY
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.translation = (-11.77795, 27.2, 0.0)
cell4.region = -surf999 & -surf4

# EMPTY
cell5 = openmc.Cell(cell_id=5, fill=universe2)
cell5.translation = (0.0, 27.2, 0.0)
cell5.region = -surf999 & -surf5

# EMPTY
cell6 = openmc.Cell(cell_id=6, fill=universe2)
cell6.translation = (11.77795, 27.2, 0.0)
cell6.region = -surf999 & -surf6

# EMPTY
cell7 = openmc.Cell(cell_id=7, fill=universe2)
cell7.translation = (-17.66692, 23.8, 0.0)
cell7.region = -surf999 & -surf7

# EMPTY
cell8 = openmc.Cell(cell_id=8, fill=universe2)
cell8.translation = (-5.88897, 23.8, 0.0)
cell8.region = -surf999 & -surf8

# EMPTY
cell9 = openmc.Cell(cell_id=9, fill=universe2)
cell9.translation = (5.88897, 23.8, 0.0)
cell9.region = -surf999 & -surf9

# EMPTY
cell10 = openmc.Cell(cell_id=10, fill=universe2)
cell10.translation = (17.66692, 23.8, 0.0)
cell10.region = -surf999 & -surf10

# EMPTY
cell11 = openmc.Cell(cell_id=11, fill=universe2)
cell11.translation = (-23.55589, 20.4, 0.0)
cell11.region = -surf999 & -surf11

# EMPTY
cell12 = openmc.Cell(cell_id=12, fill=universe2)
cell12.translation = (-11.77795, 20.4, 0.0)
cell12.region = -surf999 & -surf12

# FUEL
cell13 = openmc.Cell(cell_id=13, fill=universe3)
cell13.translation = (0.0, 20.4, 0.0)
cell13.region = -surf999 & -surf13

# EMPTY
cell14 = openmc.Cell(cell_id=14, fill=universe2)
cell14.translation = (11.77795, 20.4, 0.0)
cell14.region = -surf999 & -surf14

# EMPTY
cell15 = openmc.Cell(cell_id=15, fill=universe2)
cell15.translation = (23.55589, 20.4, 0.0)
cell15.region = -surf999 & -surf15

# EMPTY
cell16 = openmc.Cell(cell_id=16, fill=universe2)
cell16.translation = (-29.44486, 17.0, 0.0)
cell16.region = -surf999 & -surf16

# EMPTY
cell17 = openmc.Cell(cell_id=17, fill=universe2)
cell17.translation = (-17.66692, 17.0, 0.0)
cell17.region = -surf999 & -surf17

# FUEL
cell18 = openmc.Cell(cell_id=18, fill=universe3)
cell18.translation = (-5.88897, 17.0, 0.0)
cell18.region = -surf999 & -surf18

# FUEL
cell19 = openmc.Cell(cell_id=19, fill=universe3)
cell19.translation = (5.88897, 17.0, 0.0)
cell19.region = -surf999 & -surf19

# EMPTY
cell20 = openmc.Cell(cell_id=20, fill=universe2)
cell20.translation = (17.66692, 17.0, 0.0)
cell20.region = -surf999 & -surf20

# EMPTY
cell21 = openmc.Cell(cell_id=21, fill=universe2)
cell21.translation = (29.44486, 17.0, 0.0)
cell21.region = -surf999 & -surf21

# EMPTY
cell22 = openmc.Cell(cell_id=22, fill=universe2)
cell22.translation = (-23.55589, 13.6, 0.0)
cell22.region = -surf999 & -surf22

# FUEL
cell23 = openmc.Cell(cell_id=23, fill=universe3)
cell23.translation = (-11.77795, 13.6, 0.0)
cell23.region = -surf999 & -surf23

# FUEL
cell24 = openmc.Cell(cell_id=24, fill=universe3)
cell24.translation = (0.0, 13.6, 0.0)
cell24.region = -surf999 & -surf24

# FUEL
cell25 = openmc.Cell(cell_id=25, fill=universe3)
cell25.translation = (11.77795, 13.6, 0.0)
cell25.region = -surf999 & -surf25

# EMPTY
cell26 = openmc.Cell(cell_id=26, fill=universe2)
cell26.translation = (23.55589, 13.6, 0.0)
cell26.region = -surf999 & -surf26

# EMPTY
cell27 = openmc.Cell(cell_id=27, fill=universe2)
cell27.translation = (-29.44486, 10.2, 0.0)
cell27.region = -surf999 & -surf27

# FUEL
cell28 = openmc.Cell(cell_id=28, fill=universe3)
cell28.translation = (-17.66692, 10.2, 0.0)
cell28.region = -surf999 & -surf28

# FUEL
cell29 = openmc.Cell(cell_id=29, fill=universe3)
cell29.translation = (-5.88897, 10.2, 0.0)
cell29.region = -surf999 & -surf29

# FUEL
cell30 = openmc.Cell(cell_id=30, fill=universe3)
cell30.translation = (5.88897, 10.2, 0.0)
cell30.region = -surf999 & -surf30

# EMPTY
cell31 = openmc.Cell(cell_id=31, fill=universe2)
cell31.translation = (17.66692, 10.2, 0.0)
cell31.region = -surf999 & -surf31

# EMPTY
cell32 = openmc.Cell(cell_id=32, fill=universe2)
cell32.translation = (29.44486, 10.2, 0.0)
cell32.region = -surf999 & -surf32

# EMPTY
cell33 = openmc.Cell(cell_id=33, fill=universe2)
cell33.translation = (-23.55589, 6.8, 0.0)
cell33.region = -surf999 & -surf33

# FUEL
cell34 = openmc.Cell(cell_id=34, fill=universe3)
cell34.translation = (-11.77795, 6.8, 0.0)
cell34.region = -surf999 & -surf34

# FUEL
cell35 = openmc.Cell(cell_id=35, fill=universe3)
cell35.translation = (0.0, 6.8, 0.0)
cell35.region = -surf999 & -surf35

# FUEL
cell36 = openmc.Cell(cell_id=36, fill=universe3)
cell36.translation = (11.77795, 6.8, 0.0)
cell36.region = -surf999 & -surf36

# EMPTY
cell37 = openmc.Cell(cell_id=37, fill=universe2)
cell37.translation = (23.55589, 6.8, 0.0)
cell37.region = -surf999 & -surf37

# EMPTY
cell38 = openmc.Cell(cell_id=38, fill=universe2)
cell38.translation = (-29.44486, 3.4, 0.0)
cell38.region = -surf999 & -surf38

# FUEL
cell39 = openmc.Cell(cell_id=39, fill=universe3)
cell39.translation = (-17.66692, 3.4, 0.0)
cell39.region = -surf999 & -surf39

# FUEL
cell40 = openmc.Cell(cell_id=40, fill=universe3)
cell40.translation = (-5.88897, 3.4, 0.0)
cell40.region = -surf999 & -surf40

# FUEL
cell41 = openmc.Cell(cell_id=41, fill=universe3)
cell41.translation = (5.88897, 3.4, 0.0)
cell41.region = -surf999 & -surf41

# FUEL
cell42 = openmc.Cell(cell_id=42, fill=universe3)
cell42.translation = (17.66692, 3.4, 0.0)
cell42.region = -surf999 & -surf42

# EMPTY
cell43 = openmc.Cell(cell_id=43, fill=universe2)
cell43.translation = (29.44486, 3.4, 0.0)
cell43.region = -surf999 & -surf43

# EMPTY
cell44 = openmc.Cell(cell_id=44, fill=universe2)
cell44.translation = (-23.55589, 0.0, 0.0)
cell44.region = -surf999 & -surf44

# FUEL
cell45 = openmc.Cell(cell_id=45, fill=universe3)
cell45.translation = (11.77795, 0.0, 0.0)
cell45.region = -surf999 & -surf46

# CHANNL
cell46 = openmc.Cell(cell_id=46, fill=universe1)
cell46.region = -surf999 & -surf113

# SFTY
cell47 = openmc.Cell(cell_id=47, fill=universe4)
cell47.translation = (-13.74094, 3.4, 0.0)
cell47.region = -surf999 & -surf91

# SFTY
cell48 = openmc.Cell(cell_id=48, fill=universe4)
cell48.translation = (3.92598, -13.6, 0.0)
cell48.region = -surf999 & -surf93

# SSTH2O
cell49 = openmc.Cell(cell_id=49, fill=universe9)
cell49.region = -surf999 & +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & +surf6 & +surf7 & +surf8 & +surf9 & +surf10 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & +surf17 & +surf18 & +surf19 & +surf20

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49])
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
source.space = openmc.stats.Box((-6.89, -7.8, 34.9), (6.89, 7.8, 36.9))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
