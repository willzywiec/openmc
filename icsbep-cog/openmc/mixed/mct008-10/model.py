"""
MIX-COMP-THERM-008-10: Central H3 absorber rod and 232 + 6 MOX pins with 2.6670 cm pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# MOX
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.030700e-04)
mat1.add_nuclide("Pu240", 9.924800e-05)
mat1.add_nuclide("Pu241", 1.695700e-05)
mat1.add_nuclide("Pu242", 2.787400e-06)
mat1.add_nuclide("Am241", 1.638900e-06)
mat1.add_nuclide("U234", 1.144800e-06)
mat1.add_nuclide("U235", 1.498700e-04)
mat1.add_nuclide("U238", 2.066400e-02)
mat1.add_nuclide("O16", 4.309000e-02)

# Zr-2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Zr", 4.262100e-02)
mat2.add_element("Ni", 3.033600e-05)
mat2.add_element("Cr", 7.609300e-05)
mat2.add_element("Fe", 9.564200e-05)
mat2.add_element("Sn", 4.832700e-04)

# Al-6061
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.843300e-02)
mat3.add_element("Si", 3.460700e-04)
mat3.add_element("Fe", 1.015200e-04)
mat3.add_element("Cu", 6.373100e-05)
mat3.add_element("Mn", 2.211500e-05)
mat3.add_element("Mg", 6.665100e-04)
mat3.add_element("Cr", 6.231000e-05)
mat3.add_element("Zn", 3.096700e-05)
mat3.add_element("Ti", 2.537500e-05)

# Lucite
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 5.678200e-02)
mat4.add_element("C", 3.548900e-02)
mat4.add_nuclide("O16", 1.419600e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

# UO2
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U234", 1.137100e-06)
mat5.add_nuclide("U235", 1.488600e-04)
mat5.add_nuclide("U238", 2.052500e-02)
mat5.add_nuclide("O16", 4.194400e-02)

# Water
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.666200e-02)
mat6.add_nuclide("O16", 3.333100e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

# H3 absorber
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Hf", 4.988300e-03)
mat7.add_nuclide("O16", 1.042800e-02)
mat7.add_element("Zr", 2.258800e-04)
mat7.add_element("Al", 4.414400e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# MOX fuel
surf1 = openmc.ZCylinder(surface_id=1, x0=3.1035, y0=94.0435, r=0.64135)
# UO2
surf2 = openmc.ZCylinder(surface_id=2, x0=2.6035, y0=3.1035, r=0.64135)
# Zr-2
surf3 = openmc.ZCylinder(surface_id=3, x0=1.9050, y0=94.8690, r=0.71775)
# surf4: Error converting surface type "c": could not convert string to float: 'tr'
# surf5: Error converting surface type "c": could not convert string to float: 'tr'
# surf6: Error converting surface type "c": could not convert string to float: 'tr'
# surf7: Error converting surface type "c": could not convert string to float: 'tr'
# Upper  Lucite plate
surf11 = openmc.model.RectangularParallelepiped(-22.6695, 22.6695, -23.0969, 23.0969, 70.1675, 72.0725)
# Middle Lucite plate
surf12 = openmc.model.RectangularParallelepiped(-22.6695, 22.6695, -23.0969, 23.0969, 24.447499999999998, 26.3525)
# Bottom Lucite plate
surf13 = openmc.model.RectangularParallelepiped(-22.6695, 22.6695, -23.0969, 23.0969, 0.0, 1.905)
# BCD
surf14 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -16.192499999999995, 115.6335, boundary_type="vacuum")
# Top of aluminum plate
surf15 = openmc.ZPlane(surface_id=15, z0=-14.9225)
# Prism 21: 6-sided polygon
surf21_0 = openmc.Plane(a=0.8660254270, b=0.4999999597, c=0, d=21.9420532322)
surf21_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=21.9420550000)
surf21_2 = openmc.Plane(a=-0.8660254270, b=0.4999999597, c=0, d=21.9420532322)
surf21_3 = openmc.Plane(a=-0.8660254270, b=-0.4999999597, c=0, d=21.9420532322)
surf21_4 = openmc.Plane(a=-0.0000000036, b=-1.0000000000, c=0, d=21.9420550450)
surf21_5 = openmc.Plane(a=0.8660254279, b=-0.4999999582, c=0, d=21.9420532547)
surf22 = openmc.model.RectangularParallelepiped(-22.6695, 22.6695, -23.0969, 23.0969, -16.192499999999995, 115.6335)
# Absorber
surf71 = openmc.ZCylinder(surface_id=71, x0=2.6035, y0=94.0435, r=0.46736)
# Zr-2
surf72 = openmc.ZCylinder(surface_id=72, x0=1.9050, y0=94.8690, r=0.53594)
# Hole
surf73 = openmc.ZCylinder(surface_id=73, x0=1.9050, y0=94.8690, r=0.71775)
# surf101: Error converting surface type "c": could not convert string to float: 'tr'
# surf102: Error converting surface type "c": could not convert string to float: 'tr'
# surf103: Error converting surface type "c": could not convert string to float: 'tr'
# surf104: Error converting surface type "c": could not convert string to float: 'tr'
# Additional fuel rod #6
# surf105: Error converting surface type "c": could not convert string to float: 'tr'
# surf106: Error converting surface type "c": could not convert string to float: 'tr'
# surf107: Error converting surface type "c": could not convert string to float: 'tr'
# surf108: Error converting surface type "c": could not convert string to float: 'tr'
# surf109: Error converting surface type "c": could not convert string to float: 'tr'
# Additional fuel rod #2
# surf110: Error converting surface type "c": could not convert string to float: 'tr'
# Additional fuel rod #4
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
# Additional fuel rod #3
# surf128: Error converting surface type "c": could not convert string to float: 'tr'
# Additional fuel rod #1
# surf129: Error converting surface type "c": could not convert string to float: 'tr'
# surf130: Error converting surface type "c": could not convert string to float: 'tr'
# surf131: Error converting surface type "c": could not convert string to float: 'tr'
# surf132: Error converting surface type "c": could not convert string to float: 'tr'
# surf133: Error converting surface type "c": could not convert string to float: 'tr'
# Additional fuel rod #5
# surf134: Error converting surface type "c": could not convert string to float: 'tr'
# surf135: Error converting surface type "c": could not convert string to float: 'tr'
# surf136: Error converting surface type "c": could not convert string to float: 'tr'
# surf137: Error converting surface type "c": could not convert string to float: 'tr'
# surf138: Error converting surface type "c": could not convert string to float: 'tr'

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & +surf2 & -surf3
u1_cell1 = openmc.Cell(fill=mat5)
u1_cell1.region = +surf1 & -surf2 & -surf3
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf1 & +surf2 & -surf3
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

u2_cell0 = openmc.Cell(fill=mat4)
u2_cell0.region = -surf11
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = -surf12
u2_cell2 = openmc.Cell(fill=mat4)
u2_cell2.region = -surf13
u2_cell3 = openmc.Cell(fill=mat6)
u2_cell3.region = +surf11 & +surf12 & +surf13 & -surf14 & +surf15
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = -surf14 & -surf15
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat6)
u4_cell0.region = -surf3
u4_cell1 = openmc.Cell(fill=mat6)
u4_cell1.region = -surf4
u4_cell2 = openmc.Cell(fill=mat6)
u4_cell2.region = -surf5
u4_cell3 = openmc.Cell(fill=mat6)
u4_cell3.region = -surf6
u4_cell4 = openmc.Cell(fill=mat6)
u4_cell4.region = -surf7
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

# Lattice 5: 27x17 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-36.0045, -39.26473]
lattice5.pitch = [2.667000, 4.619380]
lattice5.universes = [
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
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 27x17 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-36.0045, -39.26473]
lattice6.pitch = [2.667000, 4.619380]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

u7_cell0 = openmc.Cell(fill=mat7)
u7_cell0.region = -surf71
u7_cell1 = openmc.Cell(fill=mat2)
u7_cell1.region = +surf71 & -surf72 & -surf73
u7_cell2 = openmc.Cell(fill=mat6)
u7_cell2.region = +surf72 & -surf73
universe7 = openmc.Universe(universe_id=7, cells=[u7_cell0, u7_cell1, u7_cell2])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# flt5c
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & +surf101 & +surf102 & +surf103 & +surf104 & +surf106 & +surf107 & +surf108 & +surf109

# abrod
cell2 = openmc.Cell(cell_id=2, fill=universe7)
cell2.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf73

# water
cell3 = openmc.Cell(cell_id=3, fill=mat6)
cell3.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf101 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf121 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf131

# water
cell4 = openmc.Cell(cell_id=4, fill=mat6)
cell4.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf102 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf112 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf122 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf132

# water
cell5 = openmc.Cell(cell_id=5, fill=mat6)
cell5.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf103 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf113 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf123 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf133

# water
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf104 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf114 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf124

# water
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf115 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf125 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf135

# water
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf106 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf116 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf126 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf136

# water
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf107 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf117 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf127 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf137

# water
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf108 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf118 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf138

# water
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf109 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf119

# water
cell12 = openmc.Cell(cell_id=12, fill=mat6)
cell12.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf120 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf130

# elttc
cell13 = openmc.Cell(cell_id=13, fill=universe6)
cell13.region = -surf14 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & -surf22

# else
cell14 = openmc.Cell(cell_id=14, fill=universe2)
cell14.region = -surf14 & +surf22

# ZR2
cell18 = openmc.Cell(cell_id=18, fill=mat2)
cell18.region = +surf1 & +surf2 & -surf3

# Al6061
cell24 = openmc.Cell(cell_id=24, fill=mat3)
cell24.region = -surf14 & -surf15

# else
cell25 = openmc.Cell(cell_id=25, fill=universe2)
cell25.region = +surf3 & +surf4 & +surf5 & +surf6 & +surf7 & -surf14

# else
cell31 = openmc.Cell(cell_id=31, fill=universe2)
cell31.region = +surf3 & +surf4 & +surf5 & +surf6 & +surf7 & -surf14

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell18, cell24, cell25, cell31])
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
source.space = openmc.stats.Box((-3.667, -1.0, 47.5735), (3.667, 1.0, 49.5735))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
