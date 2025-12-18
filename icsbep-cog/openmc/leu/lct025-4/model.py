"""
LCT025-4: Lattice of 661 U(7.5)O2 rods with 1.22 cm (triangular) pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(7.5)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 9.156100e-06)
mat1.add_nuclide("U235", 1.501300e-03)
mat1.add_nuclide("U236", 9.078300e-06)
mat1.add_nuclide("U238", 1.850400e-02)
mat1.add_nuclide("O16", 4.004600e-02)

# SST clad
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.889400e-02)
mat2.add_element("Cr", 1.646900e-02)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Si", 1.355100e-03)
mat2.add_element("Mn", 1.299000e-03)
mat2.add_element("C", 2.376600e-04)
mat2.add_element("Ti", 4.471300e-04)

# D16 aluminum
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

# UO2
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0, y0=85.6, r=0.208)
# void, lower
surf2 = openmc.ZCylinder(surface_id=2, x0=-0.8, y0=0.0, r=0.1)
# void, gap
surf3 = openmc.ZCylinder(surface_id=3, x0=0.0, y0=85.9, r=0.215)
# void, upper
surf4 = openmc.ZCylinder(surface_id=4, x0=85.9, y0=86.7, r=0.1)
# SST,  lower
surf5 = openmc.ZCylinder(surface_id=5, x0=-1.0, y0=-0.1, r=0.2)
# SST,  main
surf6 = openmc.ZCylinder(surface_id=6, x0=-0.1, y0=87.4, r=0.255)
# SST,  upper
surf7 = openmc.ZCylinder(surface_id=7, x0=87.4, y0=92.6, r=0.187)
# H2O,  hole
surf8 = openmc.ZCylinder(surface_id=8, x0=-1.0, y0=999.9, r=0.26)
# Support plate
surf11 = openmc.ZCylinder(surface_id=11, x0=-2.2, y0=-1.0, r=99.9)
# Lower grid plate - w/o holes
surf12 = openmc.ZCylinder(surface_id=12, x0=0.5, y0=0.8, r=99.9)
# Upper grid plate - w/o holes
surf13 = openmc.ZCylinder(surface_id=13, x0=81.9, y0=82.2, r=99.9)
# Water and boundary condition
surf14 = openmc.ZCylinder(surface_id=14, x0=-19.9, y0=105.6, r=46.5, boundary_type="vacuum")
# surf21: Error converting surface type "c": could not convert string to float: 'tr'
# surf22: Error converting surface type "c": could not convert string to float: 'tr'
# surf23: Error converting surface type "c": could not convert string to float: 'tr'
# surf24: Error converting surface type "c": could not convert string to float: 'tr'
# Prism 31: 12-sided polygon
surf31_0 = openmc.Plane(a=0.8662983840, b=0.4995268860, c=0, d=16.3743722252)
surf31_1 = openmc.Plane(a=0.5000000026, b=0.8660254023, c=0, d=16.1650000847)
surf31_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=16.3765405000)
surf31_3 = openmc.Plane(a=-0.5000000026, b=0.8660254023, c=0, d=16.1650000847)
surf31_4 = openmc.Plane(a=-0.8662983840, b=0.4995268860, c=0, d=16.3743722252)
surf31_5 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=16.1600000000)
surf31_6 = openmc.Plane(a=-0.8662983840, b=-0.4995268860, c=0, d=16.3743722252)
surf31_7 = openmc.Plane(a=-0.5000000026, b=-0.8660254023, c=0, d=16.1650000847)
surf31_8 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=16.3765405000)
surf31_9 = openmc.Plane(a=0.5000000026, b=-0.8660254023, c=0, d=16.1650000847)
surf31_10 = openmc.Plane(a=0.8662983840, b=-0.4995268860, c=0, d=16.3743722252)
surf31_11 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=16.1600000000)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = -surf11 & -surf14
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf12 & -surf14
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = -surf13 & -surf14
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = +surf11 & +surf12 & +surf13 & -surf14
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf1
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = +surf1 & +surf2 & +surf3 & +surf4 & -surf5 & -surf8
u2_cell2 = openmc.Cell(fill=mat2)
u2_cell2.region = +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & -surf6 & -surf8
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & +surf6 & -surf7 & -surf8
u2_cell4 = openmc.Cell(fill=mat4)
u2_cell4.region = +surf5 & +surf6 & +surf7 & -surf8
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

universe3 = openmc.Universe(universe_id=3, cells=[])

# Lattice 4: 27x17 array
lattice4 = openmc.RectLattice(lattice_id=4)
lattice4.lower_left = [-16.47, -17.961367]
lattice4.pitch = [1.220000, 2.113102]
lattice4.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe4 = openmc.Universe(universe_id=4)
universe4.add_cell(openmc.Cell(fill=lattice4))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# array
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = -surf14 & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5 & -surf31_6 & -surf31_7 & -surf31_8 & -surf31_9 & -surf31_10 & -surf31_11)

# D16
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = -surf11 & -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11)

# water
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = +surf11 & -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11)

# H2O
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = +surf11 & +surf12 & +surf13 & -surf14

# Water
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = +surf5 & +surf6 & +surf7 & -surf8

# ALLES
cell15 = openmc.Cell(cell_id=15, fill=universe1)
cell15.region = +surf8 & -surf14

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell8, cell14, cell15])
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
