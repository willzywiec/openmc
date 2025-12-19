"""
LCT038-2: Two (18x13-2) arrays of U(4.738)O2 rods, 1.60 cm pitch, 2.5cm concrete reflector, Hc=67.0cm
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
mat1.add_nuclide("O16", 4.639200e-02)
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

# Stainless steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 1.188300e-04)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Fe", 5.869400e-02)
mat3.add_element("Mn", 1.731900e-03)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Si", 1.693900e-03)
mat3.add_element("P", 6.143800e-05)
mat3.add_element("S", 4.450400e-05)

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("N", 4.198500e-05)
mat4.add_nuclide("O16", 1.126300e-05)

# Water, cases 2, 3 & 8
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.671500e-02)
mat5.add_nuclide("O16", 3.335800e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

# Borated
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 3.333800e-02)
mat6.add_element("Al", 1.911900e-03)
mat6.add_element("Si", 1.871700e-04)
mat6.add_nuclide("B10", 2.256300e-03)
mat6.add_nuclide("B11", 9.082000e-03)
mat6.add_element("Ca", 5.495300e-03)
mat6.add_element("Fe", 5.147400e-04)
mat6.add_element("Ti", 6.257400e-05)
mat6.add_nuclide("O16", 4.324100e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

# Polyvinyl bags & paint
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("H1", 4.046900e-02)
mat7.add_element("C", 2.698000e-02)
mat7.add_element("Cl", 1.349000e-02)
mat7.add_s_alpha_beta("c_H_in_CH2")

# XC 10F steel
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Fe", 8.448900e-02)
mat8.add_element("C", 2.376600e-04)
mat8.add_element("Mn", 3.463900e-04)
mat8.add_element("Si", 5.081800e-04)
mat8.add_element("P", 5.375900e-05)
mat8.add_element("S", 4.450400e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# UO2
surf1 = openmc.ZCylinder(surface_id=1, r=0.395)
# Gap
surf2 = openmc.ZCylinder(surface_id=2, r=0.41)
# AGS
# surf3: Unsupported surface type "rev" with params ['3', '-1.8', '0.0', '-1.0', '0.470', '98.2', '0.470', 'tr', '0', '0', '0', '0', '0', '1', '0', '1', '0']
# Hole
surf4 = openmc.ZCylinder(surface_id=4, r=0.5)
# Critical water height
surf5 = openmc.ZPlane(surface_id=5, z0=67.0)
# Lower grid plate
surf6 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -0.30000000000000004, -0.1)
# Upper grid plate
surf7 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, 96.60000000000001, 96.8)
# Basket, inner
surf8 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -1.8000000000000043, 103.4)
# Basket, outer
surf9 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -2.6000000000000014, 104.19999999999999)
# Basket
surf10 = openmc.model.RectangularParallelepiped(-28.8, 0.0, 0.0, 28.8, -2.6000000000000014, 104.19999999999999)
# Basket
surf11 = openmc.model.RectangularParallelepiped(-28.8, 0.0, -28.8, 0.0, -2.6000000000000014, 104.19999999999999)
# Pedestal support plate
surf12 = openmc.model.RectangularParallelepiped(-92.4, 2.6000000000000014, -47.5, 47.5, -3.4, -2.6)
# Water & tank & BCD
surf13 = openmc.model.RectangularParallelepiped(-117.4, 2.8999999999999986, -60.0, 60.0, -22.599999999999994, 117.5, boundary_type="vacuum")
surf14 = openmc.XPlane(surface_id=14, x0=0.0)
surf15 = openmc.XPlane(surface_id=15, x0=2.6)
surf21 = openmc.ZCylinder(surface_id=21, x0=-0.8, y0=28.0, r=0.5)
surf22 = openmc.ZCylinder(surface_id=22, x0=-28.0, y0=0.8, r=0.5)
surf23 = openmc.ZCylinder(surface_id=23, x0=-28.0, y0=-0.8, r=0.5)
surf24 = openmc.ZCylinder(surface_id=24, x0=-0.8, y0=-28.0, r=0.5)
# Inner
surf31 = openmc.ZCylinder(surface_id=31, x0=-27.8675, y0=27.8675, r=0.7975)
# Outer
surf32 = openmc.ZCylinder(surface_id=32, x0=-27.8675, y0=27.8675, r=0.9325)
# Inner
surf33 = openmc.ZCylinder(surface_id=33, x0=-27.8675, y0=-27.8675, r=0.7975)
# Outer
surf34 = openmc.ZCylinder(surface_id=34, x0=-27.8675, y0=-27.8675, r=0.9325)
# Concrete
surf40 = openmc.model.RectangularParallelepiped(0.25, 2.35, -34.8, 34.8, -2.3499999999999943, 97.25)
# Concrete
surf41 = openmc.model.RectangularParallelepiped(0.050000000000000044, 2.55, -34.8, 34.8, -1.0499999999999972, 95.95)
# Frame
surf42 = openmc.model.RectangularParallelepiped(0.050000000000000044, 2.55, -35.0, 35.0, -2.549999999999997, 97.45)
# PVC & paint
surf43 = openmc.model.RectangularParallelepiped(0.0, 2.6, -35.05, 35.05, -2.5999999999999943, 97.5)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1043, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1044, z0=90.0)
surf2_zmin = openmc.ZPlane(surface_id=1045, z0=0.0)
surf2_zmax = openmc.ZPlane(surface_id=1046, z0=96.9)
surf4_zmin = openmc.ZPlane(surface_id=1047, z0=-1.8)
surf4_zmax = openmc.ZPlane(surface_id=1048, z0=98.2)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & -surf3
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = +surf3 & (-surf4 & +surf4_zmin & -surf4_zmax) & +surf5
u1_cell4 = openmc.Cell(fill=mat5)
u1_cell4.region = +surf3 & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf5
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf6
u1_cell6 = openmc.Cell(fill=mat3)
u1_cell6.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf7
u1_cell7 = openmc.Cell(fill=mat3)
u1_cell7.region = +surf8 & -surf9
u1_cell8 = openmc.Cell(fill=mat4)
u1_cell8.region = (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & +surf6 & +surf7 & -surf8 & -surf9
u1_cell9 = openmc.Cell(fill=mat5)
u1_cell9.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & +surf6 & +surf7 & -surf8 & -surf9
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9])

u2_cell0 = openmc.Cell(fill=mat4)
u2_cell0.region = (-surf4 & +surf4_zmin & -surf4_zmax) & +surf5
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = (-surf4 & +surf4_zmin & -surf4_zmax) & -surf5
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf6
u2_cell3 = openmc.Cell(fill=mat3)
u2_cell3.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf7
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = +surf8 & -surf9
u2_cell5 = openmc.Cell(fill=mat4)
u2_cell5.region = (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & +surf6 & +surf7 & -surf8 & -surf9
u2_cell6 = openmc.Cell(fill=mat5)
u2_cell6.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & +surf6 & +surf7 & -surf8 & -surf9
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6])

# Lattice 3: 18x18 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-14.4, -14.4]
lattice3.pitch = [1.600000, 1.600000]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Assy
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.translation = (-14.4, 14.4, 0.0)
cell1.region = -surf10 & +surf12 & -surf14 & +surf21 & +surf22 & +surf32

# Assy
cell2 = openmc.Cell(cell_id=2, fill=universe3)
cell2.translation = (-14.4, -14.4, 0.0)
cell2.region = +surf10 & -surf11 & +surf12 & -surf14 & +surf23 & +surf24 & +surf34

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = -surf10 & +surf12 & -surf14 & -surf21

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = -surf10 & +surf12 & -surf14 & -surf22

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf10 & -surf11 & +surf12 & -surf14 & -surf23

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf10 & -surf11 & +surf12 & -surf14 & -surf24

# Air
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = -surf10 & +surf12 & -surf14 & +surf21 & +surf22 & -surf31 & -surf32

# SST
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = -surf10 & +surf12 & -surf14 & +surf21 & +surf22 & +surf31 & -surf32

# Air
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = +surf10 & -surf11 & +surf12 & -surf14 & +surf23 & +surf24 & -surf33 & -surf34

# SST
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = +surf10 & -surf11 & +surf12 & -surf14 & +surf23 & +surf24 & +surf33 & -surf34

# Cncrt
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = -surf40

# Cncrt
cell12 = openmc.Cell(cell_id=12, fill=mat6)
cell12.region = +surf40 & -surf41

# XC10F
cell13 = openmc.Cell(cell_id=13, fill=mat8)
cell13.region = +surf40 & +surf41 & -surf42

# PVC
cell14 = openmc.Cell(cell_id=14, fill=mat7)
cell14.region = +surf40 & +surf41 & +surf42 & -surf43 & +surf14 & -surf15

# SST
cell15 = openmc.Cell(cell_id=15, fill=mat3)
cell15.region = +surf10 & +surf11 & -surf12 & -surf13 & -surf15 & +surf43

# SST
cell16 = openmc.Cell(cell_id=16, fill=mat3)
cell16.region = -surf13 & +surf15 & +surf43

# Air
cell17 = openmc.Cell(cell_id=17, fill=mat4)
cell17.region = +surf5 & +surf10 & +surf11 & +surf12 & -surf13 & -surf15 & +surf43

# Water
cell18 = openmc.Cell(cell_id=18, fill=mat5)
cell18.region = -surf5 & +surf10 & +surf11 & +surf12 & -surf13 & -surf15 & +surf43

# Water
cell29 = openmc.Cell(cell_id=29, fill=mat5)
cell29.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & +surf6 & +surf7 & -surf8 & -surf9

# Water
cell37 = openmc.Cell(cell_id=37, fill=mat5)
cell37.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & +surf6 & +surf7 & -surf8 & -surf9

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell29, cell37])
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
source.space = openmc.stats.Box((-21.0, -1.8, 32.5), (0.19999999999999996, 1.8, 34.5))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
