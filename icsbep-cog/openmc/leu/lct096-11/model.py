"""
LEU-COMP-THERM-096-11: 45x45 array of 1600 fuel rods with 0.8001 cm square pitch; Hc = 42.19 cm
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(6.90)O2 fuel
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 6.553900e-06)
mat1.add_nuclide("U235", 1.601000e-03)
mat1.add_nuclide("U236", 1.463200e-05)
mat1.add_nuclide("U238", 2.129600e-02)
mat1.add_nuclide("O16", 4.583700e-02)
mat1.add_element("Ag", 9.231900e-09)
mat1.add_element("B", 2.385800e-07)
mat1.add_element("Cd", 1.238000e-08)
mat1.add_element("Co", 2.162000e-08)
mat1.add_element("Cr", 2.510000e-06)
mat1.add_element("Cu", 2.131600e-07)
mat1.add_element("Fe", 1.031100e-05)
mat1.add_element("Mn", 2.837200e-07)
mat1.add_element("Mo", 1.244300e-07)
mat1.add_element("Ni", 3.498900e-06)
mat1.add_element("V", 1.481300e-08)
mat1.add_element("W", 3.599800e-09)

# Al-3003 @ 2.73 g/cc
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.966800e-02)
mat2.add_element("Si", 1.756100e-04)
mat2.add_element("Fe", 1.030300e-04)
mat2.add_element("Cu", 3.233900e-05)
mat2.add_element("Mn", 3.740700e-04)
mat2.add_element("Zn", 1.257100e-05)

# Water @ 0.99705 g/cc
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.665900e-02)
mat3.add_nuclide("O16", 3.332900e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Al-6061 @ 2.70 g/cc
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 5.837600e-02)
mat4.add_element("Si", 4.168300e-04)
mat4.add_element("Fe", 1.805100e-04)
mat4.add_element("Cu", 7.932000e-05)
mat4.add_element("Mn", 2.663700e-05)
mat4.add_element("Mg", 6.957400e-04)
mat4.add_element("Cr", 6.254200e-05)
mat4.add_element("Zn", 2.983900e-05)
mat4.add_element("Ti", 6.791800e-06)
mat4.add_element("V", 3.191800e-06)

# SS304
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 1.252700e-02)
mat5.add_element("Cr", 3.645500e-03)
mat5.add_element("Ni", 1.572400e-03)
mat5.add_element("Mn", 1.816000e-04)
mat5.add_element("C", 3.322500e-05)
mat5.add_element("P", 7.247100e-06)
mat5.add_element("S", 4.666300e-06)
mat5.add_element("Si", 1.776100e-04)
mat5.add_element("N", 3.561300e-05)

# CH2
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 8.275500e-02)
mat6.add_element("C", 4.137700e-02)
mat6.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Hole containing fuel rod, water, or air/outer
surf1 = openmc.ZCylinder(surface_id=1, x0=-1.27, y0=68.2752, r=0.333375)
# Al-3003 lower end cap
surf2 = openmc.ZCylinder(surface_id=2, x0=-1.27, y0=0.0, r=0.317475)
# UO2 fuel
surf3 = openmc.ZCylinder(surface_id=3, x0=0.0, y0=48.780, r=0.262814)
# SS304 spring/inner
surf4 = openmc.ZCylinder(surface_id=4, r=0.17526)
# SS304 spring/outer
surf5 = openmc.ZCylinder(surface_id=5, x0=48.780, y0=50.4952, r=0.2286)
# Al-6061 spacer
surf6 = openmc.ZCylinder(surface_id=6, x0=50.4952, y0=53.0352, r=0.26289)
# CH2 spacer
surf7 = openmc.ZCylinder(surface_id=7, x0=53.0352, y0=68.2752, r=0.26289)
# Al-3003 cladding/inner
surf8 = openmc.ZCylinder(surface_id=8, r=0.284519)
# Al-3003 cladding/inner
surf9 = openmc.ZCylinder(surface_id=9, x0=0.0, y0=68.2752, r=0.317474)
# Al-6061 lower grid plate
surf11 = openmc.ZCylinder(surface_id=11, x0=-2.54, y0=0.0, r=46.8)
# Critical water height, Hc
surf13 = openmc.ZPlane(surface_id=13, z0=42.19)
# Al-6061 upper grid plate/upper
surf14 = openmc.model.RectangularParallelepiped(-20.955, 20.955, -20.955, 20.955, 50.4952, 53.0352)
# X-Y lattice boundary
surf15 = openmc.model.RectangularParallelepiped(-18.00225, 18.00225, -18.00225, 18.00225, -499.5, 499.5)
# Entire assembly/outer boundary (BCD)
surf16 = openmc.ZCylinder(surface_id=16, x0=-19.05, y0=68.2752, r=46.8376)
# Al-6061 tube/inner
surf21 = openmc.ZCylinder(surface_id=21, x0=0.635, y0=68.2752, r=2.8575)
# Al-6061 tube/outer
surf22 = openmc.ZCylinder(surface_id=22, x0=0.0, y0=68.2752, r=3.175)
# CH2/inner
surf23 = openmc.ZCylinder(surface_id=23, r=3.30581)
# CH2/outer
surf24 = openmc.ZCylinder(surface_id=24, x0=0.762, y0=30.7848, r=5.75945)
# at (-32.385, -6.4, 0)
# surf26: Error converting surface type "cylinder": could not convert string to float: 'tr'
# at (-32.385, -6.4, 0)
# surf27: Error converting surface type "cylinder": could not convert string to float: 'tr'

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat2)
u1_cell0.region = -surf1 & -surf2
u1_cell1 = openmc.Cell(fill=mat1)
u1_cell1.region = -surf1 & +surf2 & -surf3
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = -surf1 & +surf3 & +surf4 & -surf5
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf1 & +surf5 & -surf6
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = -surf1 & +surf6 & -surf7
u1_cell5 = openmc.Cell(fill=mat2)
u1_cell5.region = -surf1 & +surf2 & +surf8 & -surf9
u1_cell6 = openmc.Cell(fill=mat3)
u1_cell6.region = -surf1 & +surf2 & +surf9 & -surf13
u1_cell7 = openmc.Cell(fill=mat3)
u1_cell7.region = +surf1 & +surf11 & -surf13 & -surf16
u1_cell8 = openmc.Cell(fill=mat4)
u1_cell8.region = +surf1 & -surf11 & -surf16
u1_cell9 = openmc.Cell(fill=mat4)
u1_cell9.region = +surf1 & -surf14 & -surf16
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9])

# Lattice 2: 45x45 array
lattice2 = openmc.RectLattice(lattice_id=2)
lattice2.lower_left = [-18.00225, -18.00225]
lattice2.pitch = [0.800100, 0.800100]
lattice2.universes = [
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
]
universe2 = openmc.Universe(universe_id=2)
universe2.add_cell(openmc.Cell(fill=lattice2))

u3_cell0 = openmc.Cell(fill=mat4)
u3_cell0.region = +surf21 & -surf22
u3_cell1 = openmc.Cell(fill=mat3)
u3_cell1.region = +surf22 & -surf23 & -surf24
u3_cell2 = openmc.Cell(fill=mat6)
u3_cell2.region = +surf23 & -surf24
u3_cell3 = openmc.Cell(fill=mat3)
u3_cell3.region = -surf13 & +surf22 & +surf24 & -surf16
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3])

u4_cell0 = openmc.Cell(fill=mat3)
u4_cell0.region = +surf11 & -surf13 & -surf16
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf11 & -surf16
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf14 & -surf16
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2])

u5_cell0 = openmc.Cell(fill=mat3)
u5_cell0.region = -surf1 & -surf11 & -surf13 & -surf16
u5_cell1 = openmc.Cell(fill=mat3)
u5_cell1.region = -surf1 & +surf11 & -surf13 & -surf16
u5_cell2 = openmc.Cell(fill=mat3)
u5_cell2.region = +surf1 & +surf11 & -surf13 & -surf16
u5_cell3 = openmc.Cell(fill=mat4)
u5_cell3.region = +surf1 & -surf11 & -surf16
u5_cell4 = openmc.Cell(fill=mat4)
u5_cell4.region = +surf1 & -surf14 & -surf16
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0, u5_cell1, u5_cell2, u5_cell3, u5_cell4])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# array
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.region = -surf15 & -surf16

# dtct1
cell2 = openmc.Cell(cell_id=2, fill=universe3)
cell2.translation = (-32.385, -6.4, 0.0)
cell2.region = -surf26 & -surf16

# dtct2
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.translation = (32.385, 6.4, 0.0)
cell3.region = -surf27 & -surf16

# assy
cell4 = openmc.Cell(cell_id=4, fill=universe4)
cell4.region = +surf15 & -surf16 & +surf26 & +surf27

# Al6061
cell15 = openmc.Cell(cell_id=15, fill=mat4)
cell15.region = +surf1 & -surf14 & -surf16

# H2O
cell20 = openmc.Cell(cell_id=20, fill=mat3)
cell20.region = -surf13 & +surf22 & +surf24 & -surf16

# Al6061
cell24 = openmc.Cell(cell_id=24, fill=mat4)
cell24.region = -surf14 & -surf16

# Al6061
cell30 = openmc.Cell(cell_id=30, fill=mat4)
cell30.region = +surf1 & -surf14 & -surf16

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell15, cell20, cell24, cell30])
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
source.space = openmc.stats.Box((-1.0, -1.8, 20.095), (1.0, 1.8, 22.095))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
