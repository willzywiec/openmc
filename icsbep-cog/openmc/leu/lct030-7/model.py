"""
LCT030-7: 793 U(3.5)O2 rods, 1.27 cm trianglur pitch, Hc=72.52cm
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(3.5)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 6.158300e-06)
mat1.add_nuclide("U235", 7.948900e-04)
mat1.add_nuclide("U238", 2.163300e-02)
mat1.add_nuclide("O16", 4.486900e-02)

# Zr alloy clad, plugs and ends
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Zr", 4.279400e-02)
mat2.add_element("Nb", 4.245600e-04)
mat2.add_element("Hf", 6.629700e-06)

# 12X18H10T
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.871500e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Si", 1.355100e-03)
mat3.add_element("Mn", 9.525700e-04)
mat3.add_element("Ti", 6.955400e-04)
mat3.add_element("P", 5.375900e-05)
mat3.add_element("C", 4.753100e-04)
mat3.add_element("Cu", 2.246000e-04)
mat3.add_element("S", 2.966900e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.676200e-02)
mat4.add_nuclide("O16", 3.338100e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical water height
surf1 = openmc.ZPlane(surface_id=1, z0=72.52)
# SST lower grid plate
surf2 = openmc.ZCylinder(surface_id=2, x0=-3.8, y0=-2.3, r=50.0)
# SST upper grid plate
surf3 = openmc.ZCylinder(surface_id=3, x0=126.9, y0=127.9, r=50.0)
# Boundary condition
surf4 = openmc.ZCylinder(surface_id=4, x0=-33.8, y0=131.8, r=65.0, boundary_type="vacuum")
# UO2
surf10 = openmc.ZCylinder(surface_id=10, x0=0.0, y0=125.0, r=0.37875)
# Zr plug, inner
surf11 = openmc.ZCylinder(surface_id=11, r=0.15)
# Zr plug, outer
surf12 = openmc.ZCylinder(surface_id=12, x0=125.0, y0=125.7, r=0.385)
# SST spring, inner
surf13 = openmc.ZCylinder(surface_id=13, r=0.29)
# SST spring, outer
surf14 = openmc.ZCylinder(surface_id=14, x0=125.7, y0=128.0, r=0.32)
# Clad, inner
surf15 = openmc.ZCylinder(surface_id=15, x0=0.0, y0=128.0, r=0.3875)
# Clad, outer
surf16 = openmc.ZCylinder(surface_id=16, x0=-2.3, y0=130.3, r=0.4518)
# Clad, top and bottom portions
surf17 = openmc.ZCylinder(surface_id=17, x0=-3.8, y0=131.8, r=0.3)
# Hole
# surf20: Unsupported surface type "rev" with params ['4', '-3.9', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0', '0', '0', '0', '0', '1', '0', '1', '0']
# surf21: Unsupported surface type "rev" with params ['4', '-3.9', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-0.635', '1.09985', '0', '-0.635', '1.09985', '9', '-0.635', '9', '0']
# surf22: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0.635', '1.09985', '0', '0.635', '1.09985', '9', '0.635', '9', '0']
# surf23: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-1.270', '0', '0', '-1.270', '0', '9', '-1.270', '9', '0']
# surf24: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '1.270', '0', '0', '1.270', '0', '9', '1.270', '9', '0']
# surf25: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-0.635', '-1.09985', '0', '-0.635', '-1.09985', '9', '-0.635', '9', '0']
# surf26: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0.635', '-1.09985', '0', '0.635', '-1.09985', '9', '0.635', '9', '0']
# 1st prism with all fuel rods
# Prism 31: 6-sided polygon
surf31_0 = openmc.Plane(a=0.8660248905, b=0.5000008891, c=0, d=15.9478483580)
surf31_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=15.9478200000)
surf31_2 = openmc.Plane(a=-0.8660248905, b=0.5000008891, c=0, d=15.9478483580)
surf31_3 = openmc.Plane(a=-0.8660248905, b=-0.5000008891, c=0, d=15.9478483580)
surf31_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=15.9478200000)
surf31_5 = openmc.Plane(a=0.8660248905, b=-0.5000008891, c=0, d=15.9478483580)
# 2nd prism with all fuel rods
# Prism 32: 6-sided polygon
surf32_0 = openmc.Plane(a=0.8660248948, b=0.5000008815, c=0, d=17.0477000551)
surf32_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=17.0476700000)
surf32_2 = openmc.Plane(a=-0.8660248948, b=0.5000008815, c=0, d=17.0477000551)
surf32_3 = openmc.Plane(a=-0.8660248948, b=-0.5000008815, c=0, d=17.0477000551)
surf32_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=17.0476700000)
surf32_5 = openmc.Plane(a=0.8660248948, b=-0.5000008815, c=0, d=17.0477000551)
# 3rd prism with all fuel rods
# Prism 33: 6-sided polygon
surf33_0 = openmc.Plane(a=0.8660248987, b=0.5000008748, c=0, d=18.1475517522)
surf33_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=18.1475200000)
surf33_2 = openmc.Plane(a=-0.8660248987, b=0.5000008748, c=0, d=18.1475517522)
surf33_3 = openmc.Plane(a=-0.8660248987, b=-0.5000008748, c=0, d=18.1475517522)
surf33_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=18.1475200000)
surf33_5 = openmc.Plane(a=0.8660248987, b=-0.5000008748, c=0, d=18.1475517522)
# 4th prism with all fuel rods
# Prism 34: 6-sided polygon
surf34_0 = openmc.Plane(a=0.8660249021, b=0.5000008689, c=0, d=19.2474034493)
surf34_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=19.2473700000)
surf34_2 = openmc.Plane(a=-0.8660249021, b=0.5000008689, c=0, d=19.2474034493)
surf34_3 = openmc.Plane(a=-0.8660249021, b=-0.5000008689, c=0, d=19.2474034493)
surf34_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=19.2473700000)
surf34_5 = openmc.Plane(a=0.8660249021, b=-0.5000008689, c=0, d=19.2474034493)
# 5th prism with 3 more rows of holes
# Prism 35: 6-sided polygon
surf35_0 = openmc.Plane(a=0.8660249103, b=0.5000008547, c=0, d=22.5469585406)
surf35_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=22.5469200000)
surf35_2 = openmc.Plane(a=-0.8660249103, b=0.5000008547, c=0, d=22.5469585406)
surf35_3 = openmc.Plane(a=-0.8660249103, b=-0.5000008547, c=0, d=22.5469585406)
surf35_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=22.5469200000)
surf35_5 = openmc.Plane(a=0.8660249103, b=-0.5000008547, c=0, d=22.5469585406)
surf321 = openmc.model.RectangularParallelepiped(-8.89, 8.89, -499.5, 499.5, -499.5, 499.5)
# (14 on each short side)
surf322 = openmc.model.RectangularParallelepiped(-8.89, 8.89, -499.5, 499.5, -499.5, 499.5)
surf323 = openmc.model.RectangularParallelepiped(-8.89, 8.89, -499.5, 499.5, -499.5, 499.5)
surf331 = openmc.model.RectangularParallelepiped(-5.715, 5.715, -499.5, 499.5, -499.5, 499.5)
# (9 on each short side)
surf332 = openmc.model.RectangularParallelepiped(-5.715, 5.715, -499.5, 499.5, -499.5, 499.5)
surf333 = openmc.model.RectangularParallelepiped(-5.715, 5.715, -499.5, 499.5, -499.5, 499.5)
surf341 = openmc.model.RectangularParallelepiped(-2.54, 2.54, -499.5, 499.5, -499.5, 499.5)
# (4 on each short side)
surf342 = openmc.model.RectangularParallelepiped(-2.54, 2.54, -499.5, 499.5, -499.5, 499.5)
surf343 = openmc.model.RectangularParallelepiped(-2.54, 2.54, -499.5, 499.5, -499.5, 499.5)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = -surf2
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf3
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = -surf1 & +surf2 & +surf3 & -surf4
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf10 & -surf15
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = +surf10 & +surf11 & -surf12 & -surf15
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf12 & +surf13 & -surf14 & -surf15
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = +surf15 & -surf16
u2_cell4 = openmc.Cell(fill=mat2)
u2_cell4.region = +surf16 & -surf17
u2_cell5 = openmc.Cell(fill=mat4)
u2_cell5.region = -surf1 & -surf4 & +surf16 & +surf17
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = -surf1 & -surf4 & -surf20
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf1 & -surf4 & -surf21
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf1 & -surf4 & -surf22
u4_cell3 = openmc.Cell(fill=mat4)
u4_cell3.region = -surf1 & -surf4 & -surf23
u4_cell4 = openmc.Cell(fill=mat4)
u4_cell4.region = -surf1 & -surf4 & -surf24
u4_cell5 = openmc.Cell(fill=mat4)
u4_cell5.region = -surf1 & -surf4 & -surf25
u4_cell6 = openmc.Cell(fill=mat4)
u4_cell6.region = -surf1 & -surf4 & -surf26
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4, u4_cell5, u4_cell6])

# Lattice 5: 29x29 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-36.83, -31.89565]
lattice5.pitch = [2.540000, 2.199700]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 31x31 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-39.37, -34.09535]
lattice6.pitch = [2.540000, 2.199700]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Frods
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = -surf4 & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5)

# Frods
cell2 = openmc.Cell(cell_id=2, fill=universe5)
cell2.region = -surf4 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf321

# Frods
cell3 = openmc.Cell(cell_id=3, fill=universe5)
cell3.region = -surf4 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf322

# Frods
cell4 = openmc.Cell(cell_id=4, fill=universe5)
cell4.region = -surf4 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf323

# Holes
cell5 = openmc.Cell(cell_id=5, fill=universe6)
cell5.region = -surf4 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & +surf321 & +surf322 & +surf323

# Frods
cell6 = openmc.Cell(cell_id=6, fill=universe5)
cell6.region = -surf4 & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5) & (-surf33_0 & -surf33_1 & -surf33_2 & -surf33_3 & -surf33_4 & -surf33_5) & -surf331

# Frods
cell7 = openmc.Cell(cell_id=7, fill=universe5)
cell7.region = -surf4 & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5) & (-surf33_0 & -surf33_1 & -surf33_2 & -surf33_3 & -surf33_4 & -surf33_5) & -surf332

# Frods
cell8 = openmc.Cell(cell_id=8, fill=universe5)
cell8.region = -surf4 & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5) & (-surf33_0 & -surf33_1 & -surf33_2 & -surf33_3 & -surf33_4 & -surf33_5) & -surf333

# Holes
cell9 = openmc.Cell(cell_id=9, fill=universe6)
cell9.region = -surf4 & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5) & (-surf33_0 & -surf33_1 & -surf33_2 & -surf33_3 & -surf33_4 & -surf33_5) & +surf331 & +surf332 & +surf333

# Frods
cell10 = openmc.Cell(cell_id=10, fill=universe5)
cell10.region = -surf4 & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5) & (-surf34_0 & -surf34_1 & -surf34_2 & -surf34_3 & -surf34_4 & -surf34_5) & -surf341

# Frods
cell11 = openmc.Cell(cell_id=11, fill=universe5)
cell11.region = -surf4 & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5) & (-surf34_0 & -surf34_1 & -surf34_2 & -surf34_3 & -surf34_4 & -surf34_5) & -surf342

# Frods
cell12 = openmc.Cell(cell_id=12, fill=universe5)
cell12.region = -surf4 & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5) & (-surf34_0 & -surf34_1 & -surf34_2 & -surf34_3 & -surf34_4 & -surf34_5) & -surf343

# Holes
cell13 = openmc.Cell(cell_id=13, fill=universe6)
cell13.region = -surf4 & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5) & (-surf34_0 & -surf34_1 & -surf34_2 & -surf34_3 & -surf34_4 & -surf34_5) & +surf341 & +surf342 & +surf343

# Holes
cell14 = openmc.Cell(cell_id=14, fill=universe6)
cell14.region = -surf4 & (+surf34_0 | +surf34_1 | +surf34_2 | +surf34_3 | +surf34_4 | +surf34_5) & (-surf35_0 & -surf35_1 & -surf35_2 & -surf35_3 & -surf35_4 & -surf35_5)

# Alles
cell15 = openmc.Cell(cell_id=15, fill=universe1)
cell15.region = -surf4 & (+surf35_0 | +surf35_1 | +surf35_2 | +surf35_3 | +surf35_4 | +surf35_5)

# Mod
cell19 = openmc.Cell(cell_id=19, fill=mat4)
cell19.region = -surf1 & +surf2 & +surf3 & -surf4

# Mod
cell26 = openmc.Cell(cell_id=26, fill=mat4)
cell26.region = -surf1 & -surf4 & +surf16 & +surf17

# Alles
cell27 = openmc.Cell(cell_id=27, fill=universe1)
cell27.region = -surf4 & +surf20 & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Alles
cell35 = openmc.Cell(cell_id=35, fill=universe1)
cell35.region = -surf4 & +surf20 & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell19, cell26, cell27, cell35])
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
source.space = openmc.stats.Point((0.0, 0.0, 36.26))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
