"""
LCT064-7: Lattice of 1,021 U(2.4)O2 rods with 1.27 cm (triangular) pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(2.4)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("O16", 4.599500e-02)
mat1.add_nuclide("U234", 4.676900e-06)
mat1.add_nuclide("U235", 5.588300e-04)
mat1.add_nuclide("U238", 2.243400e-02)

# Zr-1Nb clad & plugs
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Zr", 4.279400e-02)
mat2.add_element("Nb", 4.245600e-04)
mat2.add_element("Hf", 6.629700e-06)

# SST
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

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("N", 4.248000e-05)
mat4.add_nuclide("O16", 1.128000e-05)

# Water
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.676200e-02)
mat5.add_nuclide("O16", 3.338100e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# UO2
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0, y0=125.0, r=0.37875)
# Zr-Nb plug inner
surf2 = openmc.ZCylinder(surface_id=2, r=0.15)
# Zr-Nb plug outer
surf3 = openmc.ZCylinder(surface_id=3, x0=125.0, y0=125.7, r=0.3825)
# SST ring inner
surf4 = openmc.ZCylinder(surface_id=4, r=0.29)
# SST ring outer
surf5 = openmc.ZCylinder(surface_id=5, x0=125.7, y0=128.0, r=0.32)
# Zr-Nb clad inner
surf6 = openmc.ZCylinder(surface_id=6, x0=0.0, y0=128.0, r=0.3875)
# Zr-Nb clad outer
surf7 = openmc.ZCylinder(surface_id=7, x0=-2.07, y0=130.53, r=0.451555)
# Zr-Nb clad top and bottom
surf8 = openmc.ZCylinder(surface_id=8, x0=-3.57, y0=132.03, r=0.3)
# Critical moderator height
surf10 = openmc.ZPlane(surface_id=10, z0=105.76)
# Lower grid plate - hole
surf11 = openmc.ZCylinder(surface_id=11, r=0.31)
# Lower grid plate
surf12 = openmc.ZCylinder(surface_id=12, x0=-3.57, y0=-2.07, r=50.0)
# Upper grid plate - hole
surf13 = openmc.ZCylinder(surface_id=13, x0=-999.9, y0=999.9, r=0.47)
# Upper grid plate
surf14 = openmc.ZCylinder(surface_id=14, x0=127.13, y0=128.13, r=50.0)
# water, air, and boundary condition
surf15 = openmc.ZCylinder(surface_id=15, x0=-33.57, y0=132.03, r=65.0, boundary_type="vacuum")
# surf21: Error converting surface type "c": could not convert string to float: 'tr'
# surf22: Error converting surface type "c": could not convert string to float: 'tr'
# surf23: Error converting surface type "c": could not convert string to float: 'tr'
# surf24: Error converting surface type "c": could not convert string to float: 'tr'
# Prism 31: 12-sided polygon
surf31_0 = openmc.Plane(a=0.4999997156, b=-0.8660255680, c=0, d=19.6849999363)
surf31_1 = openmc.Plane(a=0.8660253521, b=-0.5000000896, c=0, d=20.8971947450)
surf31_2 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=19.6850000000)
surf31_3 = openmc.Plane(a=0.8660253521, b=0.5000000896, c=0, d=20.8971947450)
surf31_4 = openmc.Plane(a=0.4999997156, b=0.8660255680, c=0, d=19.6849999363)
surf31_5 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=20.8971900000)
surf31_6 = openmc.Plane(a=-0.4999997156, b=0.8660255680, c=0, d=19.6849999363)
surf31_7 = openmc.Plane(a=-0.8660253521, b=0.5000000896, c=0, d=20.8971947450)
surf31_8 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=19.6850000000)
surf31_9 = openmc.Plane(a=-0.8660253521, b=-0.5000000896, c=0, d=20.8971947450)
surf31_10 = openmc.Plane(a=-0.4999997156, b=-0.8660255680, c=0, d=19.6849999363)
surf31_11 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=20.8971900000)
# Prism 32: 6-sided polygon
surf32_0 = openmc.Plane(a=0.8660254215, b=-0.4999999693, c=0, d=18.6974888508)
surf32_1 = openmc.Plane(a=0.8660254215, b=0.4999999693, c=0, d=18.6974888508)
surf32_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=18.6974900000)
surf32_3 = openmc.Plane(a=-0.8660254215, b=0.4999999693, c=0, d=18.6974888508)
surf32_4 = openmc.Plane(a=-0.8660254215, b=-0.4999999693, c=0, d=18.6974888508)
surf32_5 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=18.6974900000)
# Prism 33: 12-sided polygon
surf33_0 = openmc.Plane(a=0.5000005923, b=-0.8660250618, c=0, d=22.2250003472)
surf33_1 = openmc.Plane(a=0.8660253521, b=-0.5000000896, c=0, d=21.9970439421)
surf33_2 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=22.2250000000)
surf33_3 = openmc.Plane(a=0.8660253521, b=0.5000000896, c=0, d=21.9970439421)
surf33_4 = openmc.Plane(a=0.5000005923, b=0.8660250618, c=0, d=22.2250003472)
surf33_5 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=21.9970500000)
surf33_6 = openmc.Plane(a=-0.5000005923, b=0.8660250618, c=0, d=22.2250003472)
surf33_7 = openmc.Plane(a=-0.8660253521, b=0.5000000896, c=0, d=21.9970439421)
surf33_8 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=22.2250000000)
surf33_9 = openmc.Plane(a=-0.8660253521, b=-0.5000000896, c=0, d=21.9970439421)
surf33_10 = openmc.Plane(a=-0.5000005923, b=-0.8660250618, c=0, d=22.2250003472)
surf33_11 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=21.9970500000)
# Prism 34: 6-sided polygon
surf34_0 = openmc.Plane(a=0.8660254057, b=-0.4999999966, c=0, d=24.1967498363)
surf34_1 = openmc.Plane(a=0.8660254057, b=0.4999999966, c=0, d=24.1967498363)
surf34_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=24.1967500000)
surf34_3 = openmc.Plane(a=-0.8660254057, b=0.4999999966, c=0, d=24.1967498363)
surf34_4 = openmc.Plane(a=-0.8660254057, b=-0.4999999966, c=0, d=24.1967498363)
surf34_5 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=24.1967500000)
surf41 = openmc.YPlane(surface_id=41, y0=0.0)
surf42 = openmc.ZPlane(surface_id=42, z0=0)
surf43 = openmc.ZPlane(surface_id=43, z0=0)
# surf101: Error converting surface type "c": could not convert string to float: 'tr'
# surf102: Error converting surface type "c": could not convert string to float: 'tr'
# surf103: Error converting surface type "c": could not convert string to float: 'tr'
# surf104: Error converting surface type "c": could not convert string to float: 'tr'
# surf105: Error converting surface type "c": could not convert string to float: 'tr'
# surf106: Error converting surface type "c": could not convert string to float: 'tr'
# surf107: Error converting surface type "c": could not convert string to float: 'tr'
# surf108: Error converting surface type "c": could not convert string to float: 'tr'
# surf109: Error converting surface type "c": could not convert string to float: 'tr'
# surf110: Error converting surface type "c": could not convert string to float: 'tr'
# surf111: Error converting surface type "c": could not convert string to float: 'tr'
# surf112: Error converting surface type "c": could not convert string to float: 'tr'
# surf113: Error converting surface type "c": could not convert string to float: 'tr'
# surf114: Error converting surface type "c": could not convert string to float: 'tr'
# surf115: Error converting surface type "c": could not convert string to float: 'tr'
# surf116: Error converting surface type "c": could not convert string to float: 'tr'
# surf117: Error converting surface type "c": could not convert string to float: 'tr'
# surf118: Error converting surface type "c": could not convert string to float: 'tr'
# surf119: Error converting surface type "c": could not convert string to float: 'tr'
# surf120: Error converting surface type "c": could not convert string to float: 'tr'
# surf121: Error converting surface type "c": could not convert string to float: 'tr'
# surf122: Error converting surface type "c": could not convert string to float: 'tr'
# surf123: Error converting surface type "c": could not convert string to float: 'tr'
# surf201: Error converting surface type "c": could not convert string to float: 'tr'
# surf202: Error converting surface type "c": could not convert string to float: 'tr'
# surf203: Error converting surface type "c": could not convert string to float: 'tr'
# surf204: Error converting surface type "c": could not convert string to float: 'tr'
# surf205: Error converting surface type "c": could not convert string to float: 'tr'
# surf206: Error converting surface type "c": could not convert string to float: 'tr'
# surf207: Error converting surface type "c": could not convert string to float: 'tr'
# surf208: Error converting surface type "c": could not convert string to float: 'tr'
# surf209: Error converting surface type "c": could not convert string to float: 'tr'
# surf210: Error converting surface type "c": could not convert string to float: 'tr'
# surf211: Error converting surface type "c": could not convert string to float: 'tr'
# surf212: Error converting surface type "c": could not convert string to float: 'tr'
# surf213: Error converting surface type "c": could not convert string to float: 'tr'
# surf214: Error converting surface type "c": could not convert string to float: 'tr'
# surf215: Error converting surface type "c": could not convert string to float: 'tr'
# surf216: Error converting surface type "c": could not convert string to float: 'tr'
# surf217: Error converting surface type "c": could not convert string to float: 'tr'
# surf218: Error converting surface type "c": could not convert string to float: 'tr'
# surf219: Error converting surface type "c": could not convert string to float: 'tr'
# surf220: Error converting surface type "c": could not convert string to float: 'tr'
# surf221: Error converting surface type "c": could not convert string to float: 'tr'
# surf222: Error converting surface type "c": could not convert string to float: 'tr'
# surf223: Error converting surface type "c": could not convert string to float: 'tr'
# surf224: Error converting surface type "c": could not convert string to float: 'tr'
# surf225: Error converting surface type "c": could not convert string to float: 'tr'
# surf301: Error converting surface type "c": could not convert string to float: 'tr'
# surf302: Error converting surface type "c": could not convert string to float: 'tr'
# surf303: Error converting surface type "c": could not convert string to float: 'tr'
# surf304: Error converting surface type "c": could not convert string to float: 'tr'
# surf305: Error converting surface type "c": could not convert string to float: 'tr'
# surf306: Error converting surface type "c": could not convert string to float: 'tr'
# surf307: Error converting surface type "c": could not convert string to float: 'tr'
# surf308: Error converting surface type "c": could not convert string to float: 'tr'
# surf309: Error converting surface type "c": could not convert string to float: 'tr'
# surf310: Error converting surface type "c": could not convert string to float: 'tr'
# surf311: Error converting surface type "c": could not convert string to float: 'tr'
# surf312: Error converting surface type "c": could not convert string to float: 'tr'
# surf313: Error converting surface type "c": could not convert string to float: 'tr'
# surf314: Error converting surface type "c": could not convert string to float: 'tr'
# surf315: Error converting surface type "c": could not convert string to float: 'tr'
# surf316: Error converting surface type "c": could not convert string to float: 'tr'
# surf317: Error converting surface type "c": could not convert string to float: 'tr'
# surf318: Error converting surface type "c": could not convert string to float: 'tr'

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = +surf13 & -surf12
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = +surf13 & -surf14
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = +surf13 & -surf10 & +surf12 & -surf15
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = +surf13 & +surf10 & +surf14 & -surf15
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf1
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = +surf1 & +surf2 & -surf3
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf3 & +surf4 & -surf5
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = +surf1 & +surf5 & +surf6 & -surf7
u2_cell4 = openmc.Cell(fill=mat2)
u2_cell4.region = +surf7 & -surf8
u2_cell5 = openmc.Cell(fill=mat5)
u2_cell5.region = +surf7 & +surf8 & -surf11 & -surf12
u2_cell6 = openmc.Cell(fill=mat3)
u2_cell6.region = +surf11 & -surf12 & -surf13
u2_cell7 = openmc.Cell(fill=mat5)
u2_cell7.region = +surf7 & +surf8 & -surf10 & +surf12 & -surf13
u2_cell8 = openmc.Cell(fill=mat4)
u2_cell8.region = +surf7 & +surf8 & +surf10 & -surf13
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8])

u3_cell0 = openmc.Cell(fill=mat5)
u3_cell0.region = -surf11 & -surf12 & -surf13
u3_cell1 = openmc.Cell(fill=mat3)
u3_cell1.region = +surf11 & -surf12 & -surf13
u3_cell2 = openmc.Cell(fill=mat5)
u3_cell2.region = -surf10 & +surf12 & -surf13
u3_cell3 = openmc.Cell(fill=mat4)
u3_cell3.region = +surf10 & -surf13
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3])

universe4 = openmc.Universe(universe_id=4, cells=[])

# Lattice 5: 49x23 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-31.115, -25.2966]
lattice5.pitch = [1.270000, 2.199704]
lattice5.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

universe6 = openmc.Universe(universe_id=6, cells=[])

# Lattice 7: 49x23 array
lattice7 = openmc.RectLattice(lattice_id=7)
lattice7.lower_left = [-31.115, -25.2966]
lattice7.pitch = [1.270000, 2.199704]
lattice7.universes = [
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
]
universe7 = openmc.Universe(universe_id=7)
universe7.add_cell(openmc.Cell(fill=lattice7))

universe8 = openmc.Universe(universe_id=8, cells=[])

universe9 = openmc.Universe(universe_id=9, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# F-LATT
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = -surf15 & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5 & -surf31_6 & -surf31_7 & -surf31_8 & -surf31_9 & -surf31_10 & -surf31_11)

# F-LATT
cell2 = openmc.Cell(cell_id=2, fill=universe5)
cell2.region = -surf15 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# Misc
cell3 = openmc.Cell(cell_id=3, fill=universe9)
cell3.region = -surf15 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5) & (-surf33_0 & -surf33_1 & -surf33_2 & -surf33_3 & -surf33_4 & -surf33_5 & -surf33_6 & -surf33_7 & -surf33_8 & -surf33_9 & -surf33_10 & -surf33_11)

# E-LATT
cell4 = openmc.Cell(cell_id=4, fill=universe7)
cell4.region = -surf15 & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5 | +surf33_6 | +surf33_7 | +surf33_8 | +surf33_9 | +surf33_10 | +surf33_11) & (-surf34_0 & -surf34_1 & -surf34_2 & -surf34_3 & -surf34_4 & -surf34_5)

# Misc
cell5 = openmc.Cell(cell_id=5, fill=universe9)
cell5.region = -surf15 & (+surf34_0 | +surf34_1 | +surf34_2 | +surf34_3 | +surf34_4 | +surf34_5)

# Air
cell10 = openmc.Cell(cell_id=10, fill=mat4)
cell10.region = +surf13 & +surf10 & +surf14 & -surf15

# Air
cell20 = openmc.Cell(cell_id=20, fill=mat4)
cell20.region = +surf7 & +surf8 & +surf10 & -surf13

# Air
cell25 = openmc.Cell(cell_id=25, fill=mat4)
cell25.region = +surf10 & -surf13

# ALLES
cell26 = openmc.Cell(cell_id=26, fill=universe1)
cell26.region = +surf13 & +surf21 & +surf22 & +surf23 & +surf24 & -surf15

# ALLES
cell27 = openmc.Cell(cell_id=27, fill=universe1)
cell27.region = +surf13 & +surf21 & +surf22 & +surf23 & +surf24 & -surf15

# M-LATT
cell28 = openmc.Cell(cell_id=28, fill=universe8)
cell28.translation = (0.0, 0.0, 0.0)
cell28.region = -surf15 & +surf41 & -surf42

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell10, cell20, cell25, cell26, cell27, cell28])
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
source.space = openmc.stats.Point((0.0, 0.0, 52.88))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
