"""
LCT037-8: 12x36 array of 432 U(4.738)O2 fuel rods with 1.60 cm square pitch with 20.0/10.0 cm concrete screens
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.738)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 7.131800e-06)
mat1.add_nuclide("U235", 1.110400e-03)
mat1.add_nuclide("U236", 3.183800e-05)
mat1.add_nuclide("U238", 2.200600e-02)
mat1.add_nuclide("O16", 4.639100e-02)
mat1.add_nuclide("B10", 5.753100e-08)
mat1.add_nuclide("B11", 2.315700e-07)

# AGS clad, plugs
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.956900e-02)
mat2.add_element("Mg", 3.144200e-04)
mat2.add_element("Si", 2.489400e-04)
mat2.add_element("Fe", 6.405200e-05)
mat2.add_element("Zn", 7.459700e-06)

# AG3M pedestal top plate, basket: grids & plates
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.678000e-02)
mat3.add_element("Mg", 2.101100e-03)
mat3.add_element("Cr", 1.227600e-04)
mat3.add_element("Zn", 4.881000e-05)
mat3.add_element("Ti", 6.666100e-05)

# Stainless steel
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 1.188300e-04)
mat4.add_element("Cr", 1.646900e-02)
mat4.add_element("Fe", 5.869400e-02)
mat4.add_element("Mn", 1.731900e-03)
mat4.add_element("Ni", 8.106100e-03)
mat4.add_element("Si", 1.693900e-03)
mat4.add_element("P", 6.143800e-05)
mat4.add_element("S", 4.450400e-05)

# Air
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("N", 4.198500e-05)
mat5.add_nuclide("O16", 1.126300e-05)

# Water, case 8
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.674400e-02)
mat6.add_nuclide("O16", 3.337200e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

# Baked
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("H1", 6.166400e-03)
mat7.add_element("Al", 3.555300e-04)
mat7.add_element("Ca", 3.490800e-03)
mat7.add_element("Si", 1.665700e-02)
mat7.add_element("Fe", 9.737200e-05)
mat7.add_element("Ti", 1.060000e-05)
mat7.add_element("K", 6.788600e-05)
mat7.add_element("Na", 2.224600e-05)
mat7.add_element("Mg", 4.746400e-05)
mat7.add_nuclide("O16", 4.103000e-02)
mat7.add_element("Mn", 3.535100e-06)
mat7.add_element("Cr", 9.462400e-07)
mat7.add_element("S", 1.319400e-04)
mat7.add_s_alpha_beta("c_H_in_H2O")

# Polyvinyl bags & paint
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_nuclide("H1", 4.046900e-02)
mat8.add_element("C", 2.698000e-02)
mat8.add_element("Cl", 1.349000e-02)
mat8.add_s_alpha_beta("c_H_in_CH2")

# XC 10F steel
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Fe", 8.448900e-02)
mat9.add_element("C", 2.376600e-04)
mat9.add_element("Mn", 3.463900e-04)
mat9.add_element("Si", 5.081800e-04)
mat9.add_element("P", 5.375900e-05)
mat9.add_element("S", 4.450400e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9])

# ==============================================================================
# Geometry
# ==============================================================================

# UO2
surf1 = openmc.ZCylinder(surface_id=1, r=0.395)
# Gap
surf2 = openmc.ZCylinder(surface_id=2, r=0.41)
# AGS
surf3 = openmc.ZCylinder(surface_id=3, r=0.47)
# Hole
surf4 = openmc.ZCylinder(surface_id=4, r=0.505)
# AG3M upper grid plate
surf5 = openmc.model.RectangularParallelepiped(-16.0, 16.0, -32.0, 32.0, 97.5, 97.75)
# AG3M lower grid plate
surf6 = openmc.model.RectangularParallelepiped(-16.0, 16.0, -32.0, 32.0, -0.25, 0.0)
# Water
surf7 = openmc.ZPlane(surface_id=7, z0=47.87)
# Dummy
surf9 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, -499.95, 499.95)
# Basket, inner
surf10 = openmc.model.RectangularParallelepiped(-32.0, 0.0, -32.0, 32.0, -1.7999999999999972, 105.2)
# Basket, outer
surf11 = openmc.model.RectangularParallelepiped(-32.0, 0.0, -32.0, 32.0, -3.0, 106.4)
# Angle bracket
surf12 = openmc.model.RectangularParallelepiped(-4.0, 0.0, 31.75, 32.0, -3.0, 106.4)
# Angle bracket
surf13 = openmc.model.RectangularParallelepiped(-4.0, 0.0, -32.0, -31.75, -3.0, 106.4)
# Angle bracket
surf14 = openmc.model.RectangularParallelepiped(-32.0, -28.0, 31.75, 32.0, -3.0, 106.4)
# Angle bracket
surf15 = openmc.model.RectangularParallelepiped(-32.0, -28.0, -32.0, -31.75, -3.0, 106.4)
# Angle bracket
surf16 = openmc.model.RectangularParallelepiped(-0.25, 0.0, 28.0, 32.0, -3.0, 106.4)
# Angle bracket
surf17 = openmc.model.RectangularParallelepiped(-0.25, 0.0, -32.0, -28.0, -3.0, 106.4)
# Angle bracket
surf18 = openmc.model.RectangularParallelepiped(-32.0, -31.75, 28.0, 32.0, -3.0, 106.4)
# Angle bracket
surf19 = openmc.model.RectangularParallelepiped(-32.0, -31.75, -32.0, -28.0, -3.0, 106.4)
# Concrete
surf20 = openmc.model.RectangularParallelepiped(0.8500000000000014, 19.25, -34.2, 34.2, -2.1500000000000057, 96.25)
# Concrete
surf21 = openmc.model.RectangularParallelepiped(0.05000000000000071, 20.05, -34.2, 34.2, 2.049999999999997, 92.05)
# Frame
surf22 = openmc.model.RectangularParallelepiped(0.05000000000000071, 20.05, -35.0, 35.0, -2.950000000000003, 97.05)
# PVC & paint
surf23 = openmc.model.RectangularParallelepiped(0.0, 20.1, -35.05, 35.05, -3.0, 97.1)
# Concrete
surf30 = openmc.model.RectangularParallelepiped(20.65, 29.65, -34.5, 34.5, -2.450000000000003, 96.55)
# Concrete
surf31 = openmc.model.RectangularParallelepiped(20.15, 30.15, -34.5, 34.5, 2.049999999999997, 92.05)
# Frame
surf32 = openmc.model.RectangularParallelepiped(20.15, 30.15, -35.0, 35.0, -2.950000000000003, 97.05)
# PVC & paint
surf33 = openmc.model.RectangularParallelepiped(20.099999999999998, 30.2, -35.05, 35.05, -3.0, 97.1)
# Tank wall
surf34 = openmc.model.RectangularParallelepiped(30.200000000000003, 30.5, -65.0, 65.0, -24.0, 116.0)
# AG3M pedestal plate
surf41 = openmc.model.RectangularParallelepiped(-155.5, 30.5, -93.0, 93.0, -4.0, -3.0)
# SST  pedestal plate
surf42 = openmc.model.RectangularParallelepiped(-155.5, 30.5, -93.0, 93.0, -6.5, -4.0)
# Entire problem
surf99 = openmc.model.RectangularParallelepiped(-49.2, 30.5, -65.05, 65.05, -24.0, 116.1, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=0.0)
surf1_zmax = openmc.ZPlane(z0=90.0)
surf2_zmin = openmc.ZPlane(z0=0.0)
surf2_zmax = openmc.ZPlane(z0=96.9)
surf3_zmin = openmc.ZPlane(z0=-1.27)
surf3_zmax = openmc.ZPlane(z0=98.2)
surf4_zmin = openmc.ZPlane(z0=-1.27)
surf4_zmax = openmc.ZPlane(z0=98.2)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell(fill=mat5)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell3 = openmc.Cell(fill=mat6)
u1_cell3.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf7
u1_cell4 = openmc.Cell(fill=mat5)
u1_cell4.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & +surf7
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & -surf9
u1_cell6 = openmc.Cell(fill=mat3)
u1_cell6.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf6 & -surf9
u1_cell7 = openmc.Cell(fill=mat5)
u1_cell7.region = (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & +surf6 & +surf7 & -surf9
u1_cell8 = openmc.Cell(fill=mat6)
u1_cell8.region = (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & +surf6 & -surf7 & -surf9
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8])

u2_cell0 = openmc.Cell(fill=mat6)
u2_cell0.region = (-surf4 & +surf4_zmin & -surf4_zmax) & -surf7
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = (-surf4 & +surf4_zmin & -surf4_zmax) & +surf7
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & -surf9
u2_cell3 = openmc.Cell(fill=mat3)
u2_cell3.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf6 & -surf9
u2_cell4 = openmc.Cell(fill=mat5)
u2_cell4.region = (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & +surf6 & +surf7 & -surf9
u2_cell5 = openmc.Cell(fill=mat6)
u2_cell5.region = (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & +surf6 & -surf7 & -surf9
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5])

# Lattice 3: 20x40 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-32.0, -32.0]
lattice3.pitch = [1.600000, 1.600000]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Lttc
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf10 & -surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & +surf17 & +surf18 & +surf19

# AG3M
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = +surf10 & -surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & +surf17 & +surf18 & +surf19

# AG3M
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf10 & -surf11 & -surf12

# AG3M
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf10 & -surf11 & +surf12 & -surf16

# AG3M
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf10 & -surf11 & -surf13

# AG3M
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf10 & -surf11 & +surf13 & -surf17

# AG3M
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf10 & -surf11 & -surf14

# AG3M
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf10 & -surf11 & +surf14 & -surf18

# AG3M
cell9 = openmc.Cell(cell_id=9, fill=mat3)
cell9.region = +surf10 & -surf11 & -surf15

# AG3M
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = +surf10 & -surf11 & +surf15 & -surf19

# Cncrt
cell11 = openmc.Cell(cell_id=11, fill=mat7)
cell11.region = -surf20

# Cncrt
cell12 = openmc.Cell(cell_id=12, fill=mat7)
cell12.region = +surf20 & -surf21

# XC10F
cell13 = openmc.Cell(cell_id=13, fill=mat9)
cell13.region = +surf20 & +surf21 & -surf22

# PVC
cell14 = openmc.Cell(cell_id=14, fill=mat8)
cell14.region = +surf20 & +surf21 & +surf22 & -surf23 & +surf11

# Cncrt
cell15 = openmc.Cell(cell_id=15, fill=mat7)
cell15.region = -surf30

# Cncrt
cell16 = openmc.Cell(cell_id=16, fill=mat7)
cell16.region = +surf30 & -surf31

# XC10F
cell17 = openmc.Cell(cell_id=17, fill=mat9)
cell17.region = +surf30 & +surf31 & -surf32

# PVC
cell18 = openmc.Cell(cell_id=18, fill=mat8)
cell18.region = +surf30 & +surf31 & +surf32 & -surf33 & +surf23

# Tank
cell19 = openmc.Cell(cell_id=19, fill=mat4)
cell19.region = +surf33 & -surf34 & -surf99

# Pdstl
cell20 = openmc.Cell(cell_id=20, fill=mat3)
cell20.region = +surf34 & -surf41 & -surf99

# Pdstl
cell21 = openmc.Cell(cell_id=21, fill=mat4)
cell21.region = +surf34 & +surf41 & -surf42 & -surf99

# Air
cell22 = openmc.Cell(cell_id=22, fill=mat5)
cell22.region = +surf7 & +surf11 & +surf23 & +surf33 & +surf34 & +surf41 & +surf42 & -surf99

# Water
cell23 = openmc.Cell(cell_id=23, fill=mat6)
cell23.region = -surf7 & +surf11 & +surf23 & +surf33 & +surf34 & +surf41 & +surf42 & -surf99

# Water
cell33 = openmc.Cell(cell_id=33, fill=mat6)
cell33.region = (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & +surf6 & -surf7 & -surf9

# Water
cell40 = openmc.Cell(cell_id=40, fill=mat6)
cell40.region = (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & +surf6 & -surf7 & -surf9

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell33, cell40])
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
source.space = openmc.stats.Box((-19.4, -1.8, 22.935), (0.19999999999999996, 1.8, 24.935))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
