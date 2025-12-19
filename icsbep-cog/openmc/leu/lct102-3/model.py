"""
LEU-COMP-THERM-102-3: 45 x 45 array of 1424 fuel rods with 0.8001 cm square pitch
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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Hole containing fuel rod, water, or air/outer
surf1 = openmc.ZCylinder(surface_id=1, r=0.333375)
# Al-3003 lower end cap
surf2 = openmc.ZCylinder(surface_id=2, r=0.317474)
# UO2 fuel
surf3 = openmc.ZCylinder(surface_id=3, r=0.262814)
# SS304 spring/inner
surf4 = openmc.ZCylinder(surface_id=4, r=0.17526)
# SS304 spring/outer
surf5 = openmc.ZCylinder(surface_id=5, r=0.2286)
# Al-6061 spacer
surf6 = openmc.ZCylinder(surface_id=6, r=0.26289)
# CH2 spacer
surf7 = openmc.ZCylinder(surface_id=7, r=0.26289)
# Al-3003 cladding/inner
surf8 = openmc.ZCylinder(surface_id=8, r=0.284519)
# Al-3003 cladding/outer
surf9 = openmc.ZCylinder(surface_id=9, r=0.317474)
# Al-6061 lower grid plate
surf11 = openmc.ZCylinder(surface_id=11, r=46.355)
# Al-6061 upper grid plate/upper
surf14 = openmc.model.RectangularParallelepiped(-20.955, 20.955, -20.955, 20.955, 50.4952, 53.0352)
# X-Y lattice boundary
surf15 = openmc.model.RectangularParallelepiped(-18.00225, 18.00225, -18.00225, 18.00225, -499.5, 499.5)
# Entire assembly/outer boundary (BCD)
surf16 = openmc.ZCylinder(surface_id=16, r=46.8376)
# Al-6061 tube/inner
surf21 = openmc.ZCylinder(surface_id=21, r=2.8575)
# Al-6061 tube/outer
surf22 = openmc.ZCylinder(surface_id=22, r=3.175)
# CH2/inner
surf23 = openmc.ZCylinder(surface_id=23, r=3.30581)
# CH2/outer
surf24 = openmc.ZCylinder(surface_id=24, r=5.75945)
# Location of 1st detector
surf26 = openmc.ZCylinder(surface_id=26, x0=-6.4122, y0=28.94, r=6.0)
# Location of 2nd detector
surf27 = openmc.ZCylinder(surface_id=27, x0=6.4122, y0=-28.94, r=6.0)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1027, z0=-1.27)
surf1_zmax = openmc.ZPlane(surface_id=1028, z0=68.2752)
surf2_zmin = openmc.ZPlane(surface_id=1029, z0=-1.27)
surf2_zmax = openmc.ZPlane(surface_id=1030, z0=0.0)
surf3_zmin = openmc.ZPlane(surface_id=1031, z0=0.0)
surf3_zmax = openmc.ZPlane(surface_id=1032, z0=48.78)
surf5_zmin = openmc.ZPlane(surface_id=1033, z0=48.78)
surf5_zmax = openmc.ZPlane(surface_id=1034, z0=50.4952)
surf6_zmin = openmc.ZPlane(surface_id=1035, z0=50.4952)
surf6_zmax = openmc.ZPlane(surface_id=1036, z0=53.0352)
surf7_zmin = openmc.ZPlane(surface_id=1037, z0=53.0352)
surf7_zmax = openmc.ZPlane(surface_id=1038, z0=68.2752)
surf9_zmin = openmc.ZPlane(surface_id=1039, z0=0.0)
surf9_zmax = openmc.ZPlane(surface_id=1040, z0=68.2752)
surf11_zmin = openmc.ZPlane(surface_id=1041, z0=-2.54)
surf11_zmax = openmc.ZPlane(surface_id=1042, z0=0.0)
surf16_zmin = openmc.ZPlane(surface_id=1043, z0=-19.05)
surf16_zmax = openmc.ZPlane(surface_id=1044, z0=68.2752)
surf21_zmin = openmc.ZPlane(surface_id=1045, z0=0.635)
surf21_zmax = openmc.ZPlane(surface_id=1046, z0=68.2752)
surf22_zmin = openmc.ZPlane(surface_id=1047, z0=0.0)
surf22_zmax = openmc.ZPlane(surface_id=1048, z0=68.2752)
surf24_zmin = openmc.ZPlane(surface_id=1049, z0=0.762)
surf24_zmax = openmc.ZPlane(surface_id=1050, z0=30.7848)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat2)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell(fill=mat1)
u1_cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & +surf4 & (-surf5 & +surf5_zmin & -surf5_zmax)
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell5 = openmc.Cell(fill=mat2)
u1_cell5.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & +surf8 & (-surf9 & +surf9_zmin & -surf9_zmax)
u1_cell6 = openmc.Cell(fill=mat3)
u1_cell6.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf9 | -surf9_zmin | +surf9_zmax)
u1_cell7 = openmc.Cell(fill=mat3)
u1_cell7.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & +surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)
u1_cell8 = openmc.Cell(fill=mat4)
u1_cell8.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)
u1_cell9 = openmc.Cell(fill=mat4)
u1_cell9.region = (+surf1 | -surf1_zmin | +surf1_zmax) & -surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)
u2_cell2 = openmc.Cell(fill=mat4)
u2_cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)
u2_cell3 = openmc.Cell(fill=mat4)
u2_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & -surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = (+surf11 | -surf11_zmin | +surf11_zmax) & +surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

# Lattice 3: 45x45 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-18.00225, -18.00225]
lattice3.pitch = [0.800100, 0.800100]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2],
    [universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2],
    [universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2],
    [universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2],
    [universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2],
    [universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2],
    [universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2],
    [universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2],
    [universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2],
    [universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2],
    [universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2],
    [universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2],
    [universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2],
    [universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2],
    [universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2],
    [universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2],
    [universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = (+surf21 | -surf21_zmin | +surf21_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax)
u4_cell1 = openmc.Cell(fill=mat3)
u4_cell1.region = (+surf22 | -surf22_zmin | +surf22_zmax) & -surf23 & (-surf24 & +surf24_zmin & -surf24_zmax)
u4_cell2 = openmc.Cell(fill=mat6)
u4_cell2.region = +surf23 & (-surf24 & +surf24_zmin & -surf24_zmax)
u4_cell3 = openmc.Cell(fill=mat3)
u4_cell3.region = (+surf22 | -surf22_zmin | +surf22_zmax) & (+surf24 | -surf24_zmin | +surf24_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3])

u5_cell0 = openmc.Cell(fill=mat3)
u5_cell0.region = (+surf11 | -surf11_zmin | +surf11_zmax) & +surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)
u5_cell1 = openmc.Cell(fill=mat4)
u5_cell1.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)
u5_cell2 = openmc.Cell(fill=mat4)
u5_cell2.region = -surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0, u5_cell1, u5_cell2])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# array
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf15 & (-surf16 & +surf16_zmin & -surf16_zmax)

# dtct1
cell2 = openmc.Cell(cell_id=2, fill=universe4)
cell2.translation = (-6.4122, 28.94, 0.0)
cell2.region = -surf26 & (-surf16 & +surf16_zmin & -surf16_zmax)

# dtct2
cell3 = openmc.Cell(cell_id=3, fill=universe4)
cell3.translation = (6.4122, -28.94, 0.0)
cell3.region = -surf27 & (-surf16 & +surf16_zmin & -surf16_zmax)

# assy
cell4 = openmc.Cell(cell_id=4, fill=universe5)
cell4.region = +surf15 & (-surf16 & +surf16_zmin & -surf16_zmax) & +surf26 & +surf27

# Al6061
cell15 = openmc.Cell(cell_id=15, fill=mat4)
cell15.region = (+surf1 | -surf1_zmin | +surf1_zmax) & -surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)

# H2O
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = (+surf11 | -surf11_zmin | +surf11_zmax) & +surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)

# H2O
cell26 = openmc.Cell(cell_id=26, fill=mat3)
cell26.region = (+surf22 | -surf22_zmin | +surf22_zmax) & (+surf24 | -surf24_zmin | +surf24_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)

# Al6061
cell30 = openmc.Cell(cell_id=30, fill=mat4)
cell30.region = -surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell15, cell21, cell26, cell30])
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
source.space = openmc.stats.Box((-1.8, -1.8, 23.39), (1.8, 1.8, 25.39))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
