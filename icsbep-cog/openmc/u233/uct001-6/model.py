"""
LCT001-6: SB-5
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 235UO2-ZrO2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 3.730200e-05)
mat1.add_nuclide("U235", 3.878300e-03)
mat1.add_nuclide("U238", 2.527300e-04)
mat1.add_nuclide("O16", 5.482100e-02)
mat1.add_element("Zr", 2.324200e-02)

# ThO2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Th", 2.164100e-02)
mat2.add_nuclide("O16", 4.328200e-02)
mat2.add_element("Gd", 9.260700e-08)

# Zircaloy
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Zr", 4.253700e-02)
mat3.add_element("Sn", 4.991800e-04)

# Polyethylene
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 7.885400e-02)
mat4.add_element("C", 3.942700e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

# Water
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.673500e-02)
mat5.add_nuclide("O16", 3.336800e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

# Borated SST
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 5.925900e-02)
mat6.add_element("Cr", 1.742800e-02)
mat6.add_element("Mn", 8.681600e-04)
mat6.add_element("Ni", 7.517100e-03)
mat6.add_nuclide("B10", 3.748800e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Fuel
surf1 = openmc.ZCylinder(surface_id=1, r=0.26797)
# Lower plug
surf2 = openmc.ZCylinder(surface_id=2, r=0.26797)
# Upper plug
surf3 = openmc.ZCylinder(surface_id=3, r=0.26797)
# Clad inner
surf4 = openmc.ZCylinder(surface_id=4, r=0.2794)
# Clad outer
surf5 = openmc.ZCylinder(surface_id=5, r=0.32385)
# CH2 outer
surf6 = openmc.ZCylinder(surface_id=6, r=0.72517)
# Water
surf7 = openmc.ZCylinder(surface_id=7, r=0.72517)
surf11 = openmc.ZCylinder(surface_id=11, x0=-0.72517, y0=1.2560313, r=0.72517)
surf12 = openmc.ZCylinder(surface_id=12, x0=0.72517, y0=1.2560313, r=0.72517)
surf13 = openmc.ZCylinder(surface_id=13, x0=-1.45034, y0=0.0, r=0.72517)
surf14 = openmc.ZCylinder(surface_id=14, x0=1.45034, y0=0.0, r=0.72517)
surf15 = openmc.ZCylinder(surface_id=15, x0=-0.72517, y0=-1.2560313, r=0.72517)
surf16 = openmc.ZCylinder(surface_id=16, x0=0.72517, y0=-1.2560313, r=0.72517)
# ThO2
surf21 = openmc.ZCylinder(surface_id=21, r=0.62103)
# Lower plug
surf22 = openmc.ZCylinder(surface_id=22, r=0.62103)
# Upper plug
surf23 = openmc.ZCylinder(surface_id=23, r=0.62103)
# Clad inner
surf24 = openmc.ZCylinder(surface_id=24, r=0.63373)
# Clad outer
surf25 = openmc.ZCylinder(surface_id=25, r=0.7239)
surf31 = openmc.ZCylinder(surface_id=31, x0=-0.72517, y0=11.304282, r=0.72517)
surf32 = openmc.ZCylinder(surface_id=32, x0=0.72517, y0=11.304282, r=0.72517)
surf33 = openmc.ZCylinder(surface_id=33, x0=0.0, y0=10.04825, r=0.72517)
# Bottom of control blade at Z=15.765
surf41 = openmc.model.RectangularParallelepiped(-3.81, 3.81, 5.42798, 5.605779999999999, 15.765, 215.765)
# Bottom of control blade at Z=15.765
surf42 = openmc.model.RectangularParallelepiped(-3.81, 3.81, 1.75006, 1.92786, 15.765, 215.765)
# Bottom of control blade at Z=15.765
surf43 = openmc.model.RectangularParallelepiped(-3.81, 3.81, -1.92786, -1.75006, 15.765, 215.765)
# Bottom of control blade at Z=15.765
surf44 = openmc.model.RectangularParallelepiped(-3.81, 3.81, -5.605779999999999, -5.42798, 15.765, 215.765)
# Uniform seed rod region
# Prism 91: 6-sided polygon
surf91_0 = openmc.Plane(a=0.8660253979, b=0.5000000102, c=0, d=10.0482502047)
surf91_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=10.0482500000)
surf91_2 = openmc.Plane(a=-0.8660253979, b=0.5000000102, c=0, d=10.0482502047)
surf91_3 = openmc.Plane(a=-0.8660253979, b=-0.5000000102, c=0, d=10.0482502047)
surf91_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=10.0482500000)
surf91_5 = openmc.Plane(a=0.8660253979, b=-0.5000000102, c=0, d=10.0482502047)
# Transition region
# Prism 92: 6-sided polygon
surf92_0 = openmc.Plane(a=0.8660253740, b=0.5000000517, c=0, d=11.3042811678)
surf92_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=11.3042800000)
surf92_2 = openmc.Plane(a=-0.8660253740, b=0.5000000517, c=0, d=11.3042811678)
surf92_3 = openmc.Plane(a=-0.8660253740, b=-0.5000000517, c=0, d=11.3042811678)
surf92_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=11.3042800000)
surf92_5 = openmc.Plane(a=0.8660253740, b=-0.5000000517, c=0, d=11.3042811678)
# Uniform blanket rod region
# Prism 93: 6-sided polygon
surf93_0 = openmc.Plane(a=0.8660254410, b=0.4999999355, c=0, d=25.1206267619)
surf93_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=25.1206300000)
surf93_2 = openmc.Plane(a=-0.8660254410, b=0.4999999355, c=0, d=25.1206267619)
surf93_3 = openmc.Plane(a=-0.8660254410, b=-0.4999999355, c=0, d=25.1206267619)
surf93_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=25.1206300000)
surf93_5 = openmc.Plane(a=0.8660254410, b=-0.4999999355, c=0, d=25.1206267619)
# Uniform blanket rod region
# Prism 94: 6-sided polygon
surf94_0 = openmc.Plane(a=0.8660254287, b=0.4999999569, c=0, d=26.3766577250)
surf94_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=26.3766600000)
surf94_2 = openmc.Plane(a=-0.8660254287, b=0.4999999569, c=0, d=26.3766577250)
surf94_3 = openmc.Plane(a=-0.8660254287, b=-0.4999999569, c=0, d=26.3766577250)
surf94_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=26.3766600000)
surf94_5 = openmc.Plane(a=0.8660254287, b=-0.4999999569, c=0, d=26.3766577250)
surf95 = openmc.Plane(surface_id=95, a=-14.5034, b=25.120262, c=99.9, d=-14.5034)
surf96 = openmc.Plane(surface_id=96, a=-14.5034, b=-25.120262, c=99.9, d=-14.5034)
surf97 = openmc.YPlane(surface_id=97, y0=0.0)
surf99 = openmc.ZCylinder(surface_id=99, r=60.28)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=-19.05)
surf1_zmax = openmc.ZPlane(z0=19.05)
surf2_zmin = openmc.ZPlane(z0=-25.8191)
surf2_zmax = openmc.ZPlane(z0=-19.05)
surf3_zmin = openmc.ZPlane(z0=19.05)
surf3_zmax = openmc.ZPlane(z0=25.8191)
surf4_zmin = openmc.ZPlane(z0=-25.8191)
surf4_zmax = openmc.ZPlane(z0=25.8191)
surf5_zmin = openmc.ZPlane(z0=-25.8191)
surf5_zmax = openmc.ZPlane(z0=25.8191)
surf6_zmin = openmc.ZPlane(z0=-0.3175)
surf6_zmax = openmc.ZPlane(z0=0.3175)
surf7_zmin = openmc.ZPlane(z0=-25.8191)
surf7_zmax = openmc.ZPlane(z0=25.8191)
surf21_zmin = openmc.ZPlane(z0=-19.05)
surf21_zmax = openmc.ZPlane(z0=19.05)
surf22_zmin = openmc.ZPlane(z0=-25.8191)
surf22_zmax = openmc.ZPlane(z0=-19.05)
surf23_zmin = openmc.ZPlane(z0=19.05)
surf23_zmax = openmc.ZPlane(z0=25.8191)
surf24_zmin = openmc.ZPlane(z0=-25.8191)
surf24_zmax = openmc.ZPlane(z0=25.8191)
surf25_zmin = openmc.ZPlane(z0=-25.8191)
surf25_zmax = openmc.ZPlane(z0=25.8191)
surf99_zmin = openmc.ZPlane(z0=-56.2991, boundary_type="vacuum")
surf99_zmax = openmc.ZPlane(z0=56.2991, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell3 = openmc.Cell()
u1_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell5 = openmc.Cell(fill=mat4)
u1_cell5.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = (-surf99 & +surf99_zmin & -surf99_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0])

# Lattice 3: 9x9 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-13.05306, -11.30428]
lattice3.pitch = [2.900680, 2.512062]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

u4_cell0 = openmc.Cell(fill=mat2)
u4_cell0.region = (-surf21 & +surf21_zmin & -surf21_zmax) & (-surf24 & +surf24_zmin & -surf24_zmax) & (-surf25 & +surf25_zmin & -surf25_zmax)
u4_cell1 = openmc.Cell(fill=mat3)
u4_cell1.region = (+surf21 | -surf21_zmin | +surf21_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax) & (-surf24 & +surf24_zmin & -surf24_zmax) & (-surf25 & +surf25_zmin & -surf25_zmax)
u4_cell2 = openmc.Cell(fill=mat3)
u4_cell2.region = (+surf21 | -surf21_zmin | +surf21_zmax) & (-surf23 & +surf23_zmin & -surf23_zmax) & (-surf24 & +surf24_zmin & -surf24_zmax) & (-surf25 & +surf25_zmin & -surf25_zmax)
u4_cell3 = openmc.Cell()
u4_cell3.region = (+surf21 | -surf21_zmin | +surf21_zmax) & (+surf22 | -surf22_zmin | +surf22_zmax) & (+surf23 | -surf23_zmin | +surf23_zmax) & (-surf24 & +surf24_zmin & -surf24_zmax) & (-surf25 & +surf25_zmin & -surf25_zmax)
u4_cell4 = openmc.Cell(fill=mat3)
u4_cell4.region = (+surf24 | -surf24_zmin | +surf24_zmax) & (-surf25 & +surf25_zmin & -surf25_zmax)
u4_cell5 = openmc.Cell(fill=mat5)
u4_cell5.region = (+surf25 | -surf25_zmin | +surf25_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4, u4_cell5])

u5_cell0 = openmc.Cell(fill=mat5)
u5_cell0.region = (-surf99 & +surf99_zmin & -surf99_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0])

# Lattice 6: 21x21 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-30.45714, -26.37666]
lattice6.pitch = [2.900680, 2.512063]
lattice6.universes = [
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

universe7 = openmc.Universe(universe_id=7, cells=[])

u8_cell0 = openmc.Cell(fill=mat5)
u8_cell0.region = (-surf99 & +surf99_zmin & -surf99_zmax) & +surf31 & +surf32 & +surf33
universe8 = openmc.Universe(universe_id=8, cells=[u8_cell0])

universe9 = openmc.Universe(universe_id=9, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Blade
cell1 = openmc.Cell(cell_id=1, fill=mat6)
cell1.region = -surf41

# Blade
cell2 = openmc.Cell(cell_id=2, fill=mat6)
cell2.region = -surf42

# Blade
cell3 = openmc.Cell(cell_id=3, fill=mat6)
cell3.region = -surf43

# Blade
cell4 = openmc.Cell(cell_id=4, fill=mat6)
cell4.region = -surf44

# Seeds
cell5 = openmc.Cell(cell_id=5, fill=universe3)
cell5.region = +surf41 & +surf42 & +surf43 & +surf44 & (-surf91_0 & -surf91_1 & -surf91_2 & -surf91_3 & -surf91_4 & -surf91_5) & (-surf99 & +surf99_zmin & -surf99_zmax)

# Mixed
cell6 = openmc.Cell(cell_id=6, fill=universe9)
cell6.region = (+surf91_0 | +surf91_1 | +surf91_2 | +surf91_3 | +surf91_4 | +surf91_5) & (-surf92_0 & -surf92_1 & -surf92_2 & -surf92_3 & -surf92_4 & -surf92_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & +surf95 & -surf96

# Mixed
cell7 = openmc.Cell(cell_id=7, fill=universe9)
cell7.translation = (0.0, 0.0, 0.0)
cell7.region = (+surf91_0 | +surf91_1 | +surf91_2 | +surf91_3 | +surf91_4 | +surf91_5) & (-surf92_0 & -surf92_1 & -surf92_2 & -surf92_3 & -surf92_4 & -surf92_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & -surf95 & +surf97

# Mixed
cell8 = openmc.Cell(cell_id=8, fill=universe9)
cell8.translation = (0.0, 0.0, 0.0)
cell8.region = (+surf91_0 | +surf91_1 | +surf91_2 | +surf91_3 | +surf91_4 | +surf91_5) & (-surf92_0 & -surf92_1 & -surf92_2 & -surf92_3 & -surf92_4 & -surf92_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & -surf96 & -surf97

# Mixed
cell9 = openmc.Cell(cell_id=9, fill=universe9)
cell9.translation = (0.0, 0.0, 0.0)
cell9.region = (+surf91_0 | +surf91_1 | +surf91_2 | +surf91_3 | +surf91_4 | +surf91_5) & (-surf92_0 & -surf92_1 & -surf92_2 & -surf92_3 & -surf92_4 & -surf92_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & -surf95 & +surf96

# Mixed
cell10 = openmc.Cell(cell_id=10, fill=universe9)
cell10.translation = (0.0, 0.0, 0.0)
cell10.region = (+surf91_0 | +surf91_1 | +surf91_2 | +surf91_3 | +surf91_4 | +surf91_5) & (-surf92_0 & -surf92_1 & -surf92_2 & -surf92_3 & -surf92_4 & -surf92_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & +surf95 & -surf97

# Mixed
cell11 = openmc.Cell(cell_id=11, fill=universe9)
cell11.translation = (0.0, 0.0, 0.0)
cell11.region = (+surf91_0 | +surf91_1 | +surf91_2 | +surf91_3 | +surf91_4 | +surf91_5) & (-surf92_0 & -surf92_1 & -surf92_2 & -surf92_3 & -surf92_4 & -surf92_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & +surf96 & +surf97

# Blnkts
cell12 = openmc.Cell(cell_id=12, fill=universe6)
cell12.region = (+surf92_0 | +surf92_1 | +surf92_2 | +surf92_3 | +surf92_4 | +surf92_5) & (-surf93_0 & -surf93_1 & -surf93_2 & -surf93_3 & -surf93_4 & -surf93_5) & (-surf99 & +surf99_zmin & -surf99_zmax)

# Blnkts
cell13 = openmc.Cell(cell_id=13, fill=universe7)
cell13.region = (+surf93_0 | +surf93_1 | +surf93_2 | +surf93_3 | +surf93_4 | +surf93_5) & (-surf94_0 & -surf94_1 & -surf94_2 & -surf94_3 & -surf94_4 & -surf94_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & +surf95 & -surf96

# Blnkts
cell14 = openmc.Cell(cell_id=14, fill=universe7)
cell14.translation = (0.0, 0.0, 0.0)
cell14.region = (+surf93_0 | +surf93_1 | +surf93_2 | +surf93_3 | +surf93_4 | +surf93_5) & (-surf94_0 & -surf94_1 & -surf94_2 & -surf94_3 & -surf94_4 & -surf94_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & -surf95 & +surf97

# Blnkts
cell15 = openmc.Cell(cell_id=15, fill=universe7)
cell15.translation = (0.0, 0.0, 0.0)
cell15.region = (+surf93_0 | +surf93_1 | +surf93_2 | +surf93_3 | +surf93_4 | +surf93_5) & (-surf94_0 & -surf94_1 & -surf94_2 & -surf94_3 & -surf94_4 & -surf94_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & -surf96 & -surf97

# Blnkts
cell16 = openmc.Cell(cell_id=16, fill=universe7)
cell16.translation = (0.0, 0.0, 0.0)
cell16.region = (+surf93_0 | +surf93_1 | +surf93_2 | +surf93_3 | +surf93_4 | +surf93_5) & (-surf94_0 & -surf94_1 & -surf94_2 & -surf94_3 & -surf94_4 & -surf94_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & -surf95 & +surf96

# Blnkts
cell17 = openmc.Cell(cell_id=17, fill=universe7)
cell17.translation = (0.0, 0.0, 0.0)
cell17.region = (+surf93_0 | +surf93_1 | +surf93_2 | +surf93_3 | +surf93_4 | +surf93_5) & (-surf94_0 & -surf94_1 & -surf94_2 & -surf94_3 & -surf94_4 & -surf94_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & +surf95 & -surf97

# Blnkts
cell18 = openmc.Cell(cell_id=18, fill=universe7)
cell18.translation = (0.0, 0.0, 0.0)
cell18.region = (+surf93_0 | +surf93_1 | +surf93_2 | +surf93_3 | +surf93_4 | +surf93_5) & (-surf94_0 & -surf94_1 & -surf94_2 & -surf94_3 & -surf94_4 & -surf94_5) & (-surf99 & +surf99_zmin & -surf99_zmax) & +surf96 & +surf97

# Water
cell19 = openmc.Cell(cell_id=19, fill=mat5)
cell19.region = (+surf94_0 | +surf94_1 | +surf94_2 | +surf94_3 | +surf94_4 | +surf94_5) & (-surf99 & +surf99_zmin & -surf99_zmax)

# Water
cell27 = openmc.Cell(cell_id=27, fill=mat5)
cell27.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)

# Water
cell29 = openmc.Cell(cell_id=29, fill=mat5)
cell29.region = (-surf99 & +surf99_zmin & -surf99_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16

# Water
cell36 = openmc.Cell(cell_id=36, fill=mat5)
cell36.region = (+surf25 | -surf25_zmin | +surf25_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)

# Water
cell38 = openmc.Cell(cell_id=38, fill=mat5)
cell38.region = (-surf99 & +surf99_zmin & -surf99_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16

# Water
cell40 = openmc.Cell(cell_id=40, fill=mat5)
cell40.region = (-surf99 & +surf99_zmin & -surf99_zmax) & +surf31 & +surf32 & +surf33

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell27, cell29, cell36, cell38, cell40])
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
