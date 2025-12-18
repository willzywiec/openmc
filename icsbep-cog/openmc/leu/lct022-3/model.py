"""
LCT022-3: 629 U(10)O2 rods with 1.0 cm hexagonal pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(10)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.763600e-05)
mat1.add_nuclide("U235", 2.157700e-03)
mat1.add_nuclide("U236", 1.530000e-05)
mat1.add_nuclide("U238", 1.951000e-02)
mat1.add_nuclide("O16", 4.466100e-02)

# SST
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.889400e-02)
mat2.add_element("Cr", 1.646900e-02)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Si", 1.355100e-03)
mat2.add_element("Mn", 1.299000e-03)
mat2.add_element("C", 2.376600e-04)
mat2.add_element("Ti", 4.471300e-04)

# Al-alloy
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 1.498900e-04)
mat3.add_element("Si", 2.980400e-04)
mat3.add_element("Cu", 1.146000e-03)
mat3.add_element("Al", 5.711500e-02)
mat3.add_element("Mg", 1.033200e-03)
mat3.add_element("Mn", 1.828400e-04)
mat3.add_element("Ti", 3.496500e-05)
mat3.add_element("Zn", 7.680700e-05)
mat3.add_element("Ni", 2.852500e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.673600e-02)
mat4.add_nuclide("O16", 3.336800e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Void
surf1 = openmc.ZCylinder(surface_id=1, x0=-0.8, y0=0.0, r=0.1)
# Clad - lower
surf2 = openmc.ZCylinder(surface_id=2, x0=-1.1, y0=-0.1, r=0.2)
# Clad - lower
surf3 = openmc.ZCylinder(surface_id=3, x0=-0.1, y0=0.0, r=0.255)
# Fuel
surf4 = openmc.ZCylinder(surface_id=4, x0=0.0, y0=85.6, r=0.208)
# Void
surf5 = openmc.ZCylinder(surface_id=5, x0=0.0, y0=85.9, r=0.215)
# Void
surf6 = openmc.ZCylinder(surface_id=6, x0=85.9, y0=86.7, r=0.1)
# Clad - middle
surf7 = openmc.ZCylinder(surface_id=7, x0=0.0, y0=87.3, r=0.255)
# Clad - top
surf8 = openmc.ZCylinder(surface_id=8, x0=87.3, y0=92.5, r=0.187)
# Support plate
surf10 = openmc.ZCylinder(surface_id=10, x0=-2.3, y0=-1.1, r=99.9)
# Lattice plate hole - 1
surf11 = openmc.ZCylinder(surface_id=11, r=0.26)
# Lattice plate hole - 2
surf12_cyl = openmc.ZCylinder(surface_id=12, x0=tr, y0=-0.5, r=0.26)
surf12_zmin = openmc.ZPlane(z0=0.8660254)
surf12_zmax = openmc.ZPlane(z0=0.0)
surf12 = (surf12_cyl, surf12_zmin, surf12_zmax)
# Lattice plate hole - 3
surf13_cyl = openmc.ZCylinder(surface_id=13, x0=tr, y0=-0.5, r=0.26)
surf13_zmin = openmc.ZPlane(z0=-0.8660254)
surf13_zmax = openmc.ZPlane(z0=0.0)
surf13 = (surf13_cyl, surf13_zmin, surf13_zmax)
# Lattice plate hole - 4
surf14_cyl = openmc.ZCylinder(surface_id=14, x0=tr, y0=0.5, r=0.26)
surf14_zmin = openmc.ZPlane(z0=0.8660254)
surf14_zmax = openmc.ZPlane(z0=0.0)
surf14 = (surf14_cyl, surf14_zmin, surf14_zmax)
# Lattice plate hole - 5
surf15_cyl = openmc.ZCylinder(surface_id=15, x0=tr, y0=0.5, r=0.26)
surf15_zmin = openmc.ZPlane(z0=-0.8660254)
surf15_zmax = openmc.ZPlane(z0=0.0)
surf15 = (surf15_cyl, surf15_zmin, surf15_zmax)
# Lattice plate - lower
surf16 = openmc.ZCylinder(surface_id=16, x0=0.5, y0=0.7, r=99.9)
# Lattice plate - upper
surf17 = openmc.ZCylinder(surface_id=17, x0=81.8, y0=82.1, r=99.9)
# surf21: Error converting surface type "c": could not convert string to float: 'tr'
# surf22: Error converting surface type "c": could not convert string to float: 'tr'
# surf23: Error converting surface type "c": could not convert string to float: 'tr'
# surf24: Error converting surface type "c": could not convert string to float: 'tr'
# surf25: Error converting surface type "c": could not convert string to float: 'tr'
# surf26: Error converting surface type "c": could not convert string to float: 'tr'
# surf27: Error converting surface type "c": could not convert string to float: 'tr'
# surf28: Error converting surface type "c": could not convert string to float: 'tr'
# surf29: Error converting surface type "c": could not convert string to float: 'tr'
# surf30: Error converting surface type "c": could not convert string to float: 'tr'
# surf31: Error converting surface type "c": could not convert string to float: 'tr'
# surf32: Error converting surface type "c": could not convert string to float: 'tr'
# surf33: Error converting surface type "c": could not convert string to float: 'tr'
# surf34: Error converting surface type "c": could not convert string to float: 'tr'
# surf35: Error converting surface type "c": could not convert string to float: 'tr'
# surf36: Error converting surface type "c": could not convert string to float: 'tr'
# surf37: Error converting surface type "c": could not convert string to float: 'tr'
# surf38: Error converting surface type "c": could not convert string to float: 'tr'
# surf39: Error converting surface type "c": could not convert string to float: 'tr'
# surf40: Error converting surface type "c": could not convert string to float: 'tr'
# surf41: Error converting surface type "c": could not convert string to float: 'tr'
# surf42: Error converting surface type "c": could not convert string to float: 'tr'
# surf43: Error converting surface type "c": could not convert string to float: 'tr'
# surf44: Error converting surface type "c": could not convert string to float: 'tr'
# surf45: Error converting surface type "c": could not convert string to float: 'tr'
# surf46: Error converting surface type "c": could not convert string to float: 'tr'
# surf47: Error converting surface type "c": could not convert string to float: 'tr'
# surf48: Error converting surface type "c": could not convert string to float: 'tr'
# surf49: Error converting surface type "c": could not convert string to float: 'tr'
# surf50: Error converting surface type "c": could not convert string to float: 'tr'
# surf51: Error converting surface type "c": could not convert string to float: 'tr'
# surf52: Error converting surface type "c": could not convert string to float: 'tr'
# Prism 81: 12-sided polygon
surf81_0 = openmc.Plane(a=0.4999999984, b=-0.8660254047, c=0, d=13.4999996093)
surf81_1 = openmc.Plane(a=0.8660253862, b=-0.5000000305, c=0, d=13.8564063454)
surf81_2 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=13.5000000000)
surf81_3 = openmc.Plane(a=0.8660253862, b=0.5000000305, c=0, d=13.8564063454)
surf81_4 = openmc.Plane(a=0.4999999984, b=0.8660254047, c=0, d=13.4999996093)
surf81_5 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=13.8564060000)
surf81_6 = openmc.Plane(a=-0.4999999984, b=0.8660254047, c=0, d=13.4999996093)
surf81_7 = openmc.Plane(a=-0.8660253862, b=0.5000000305, c=0, d=13.8564063454)
surf81_8 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=13.5000000000)
surf81_9 = openmc.Plane(a=-0.8660253862, b=-0.5000000305, c=0, d=13.8564063454)
surf81_10 = openmc.Plane(a=-0.4999999984, b=-0.8660254047, c=0, d=13.4999996093)
surf81_11 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=13.8564060000)
# Boundary condition
surf99 = openmc.ZCylinder(surface_id=99, x0=-20.0, y0=105.6, r=43.8, boundary_type="vacuum")
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
# surf124: Error converting surface type "c": could not convert string to float: 'tr'
# surf125: Error converting surface type "c": could not convert string to float: 'tr'
# surf126: Error converting surface type "c": could not convert string to float: 'tr'
# surf127: Error converting surface type "c": could not convert string to float: 'tr'
# surf128: Error converting surface type "c": could not convert string to float: 'tr'
# surf129: Error converting surface type "c": could not convert string to float: 'tr'
# surf130: Error converting surface type "c": could not convert string to float: 'tr'
# surf131: Error converting surface type "c": could not convert string to float: 'tr'
# surf132: Error converting surface type "c": could not convert string to float: 'tr'
# surf133: Error converting surface type "c": could not convert string to float: 'tr'
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
# surf226: Error converting surface type "c": could not convert string to float: 'tr'
# surf227: Error converting surface type "c": could not convert string to float: 'tr'
# surf228: Error converting surface type "c": could not convert string to float: 'tr'
# surf229: Error converting surface type "c": could not convert string to float: 'tr'
# surf230: Error converting surface type "c": could not convert string to float: 'tr'
# surf231: Error converting surface type "c": could not convert string to float: 'tr'
# surf232: Error converting surface type "c": could not convert string to float: 'tr'
# surf233: Error converting surface type "c": could not convert string to float: 'tr'

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell()
u1_cell0.region = -surf1 & -surf2
u1_cell1 = openmc.Cell()
u1_cell1.region = -surf1 & -surf3
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf1 & -surf2
u1_cell3 = openmc.Cell(fill=mat2)
u1_cell3.region = +surf1 & +surf2 & -surf3
u1_cell4 = openmc.Cell(fill=mat1)
u1_cell4.region = +surf1 & +surf2 & +surf3 & -surf4
u1_cell5 = openmc.Cell()
u1_cell5.region = +surf1 & +surf2 & +surf3 & +surf4 & -surf5
u1_cell6 = openmc.Cell()
u1_cell6.region = +surf5 & -surf6
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & +surf6 & -surf7
u1_cell8 = openmc.Cell(fill=mat2)
u1_cell8.region = +surf7 & -surf8
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = -surf10 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & -surf99
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & -surf16 & -surf99
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & -surf17 & -surf99
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

# Lattice 3: 27x17 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-13.5, -14.722432]
lattice3.pitch = [1.000000, 1.732051]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = (-surf81_0 & -surf81_1 & -surf81_2 & -surf81_3 & -surf81_4 & -surf81_5 & -surf81_6 & -surf81_7 & -surf81_8 & -surf81_9 & -surf81_10 & -surf81_11) & -surf99

root_universe = openmc.Universe(cells=[cell1])
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
source.space = openmc.stats.Point((0.0, 0.0, 42.8))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
