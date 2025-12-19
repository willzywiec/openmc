"""
LCT034-8: Four 18x18 arrays of U(4.738)O2 rods, 1.60 cm pitch, 0.155cm borated steel, 7.0cm water gap, Hc=80.66cm
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

# Stainless steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.869400e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Mn", 1.731900e-03)
mat3.add_element("Si", 1.693900e-03)
mat3.add_element("P", 6.143800e-05)
mat3.add_element("S", 4.450400e-05)
mat3.add_element("C", 1.188300e-04)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.670700e-02)
mat4.add_nuclide("O16", 3.335400e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Borated
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 5.722000e-02)
mat5.add_element("Cr", 1.720300e-02)
mat5.add_element("Ni", 1.070700e-02)
mat5.add_element("Mn", 5.987700e-04)
mat5.add_element("Si", 1.050700e-03)
mat5.add_element("P", 4.685500e-05)
mat5.add_element("S", 9.050600e-06)
mat5.add_element("C", 1.449900e-04)
mat5.add_nuclide("B10", 9.795000e-04)
mat5.add_nuclide("B11", 3.942600e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

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
surf4 = openmc.ZCylinder(surface_id=4, r=0.5)
# Critical water height
surf5 = openmc.ZPlane(surface_id=5, z0=80.66)
# Lower grid plate
surf6 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -0.30000000000000004, -0.1)
# Upper grid plate
surf7 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, 96.60000000000001, 96.8)
# Basket, inner
surf8 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -1.8000000000000043, 103.4)
# Basket, outer
surf9 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -2.200000000000003, 103.8)
# Basket
surf10 = openmc.model.RectangularParallelepiped(-32.455, -3.6549999999999994, 3.6549999999999994, 32.455, -2.200000000000003, 103.8)
# Borated steel, 0.155cm x 100 cm
surf11 = openmc.model.RectangularParallelepiped(-32.61, -3.5, 3.5, 32.61, -2.200000000000003, 97.8)
# Basket
surf12 = openmc.model.RectangularParallelepiped(3.6549999999999994, 32.455, 3.6549999999999994, 32.455, -2.200000000000003, 103.8)
# Borated steel, 0.155cm x 100 cm
surf13 = openmc.model.RectangularParallelepiped(3.5, 32.61, 3.5, 32.61, -2.200000000000003, 97.8)
# Basket
surf14 = openmc.model.RectangularParallelepiped(-32.455, -3.6549999999999994, -32.455, -3.6549999999999994, -2.200000000000003, 103.8)
# Borated steel, 0.155cm x 100 cm
surf15 = openmc.model.RectangularParallelepiped(-32.61, -3.5, -32.61, -3.5, -2.200000000000003, 97.8)
# Basket
surf16 = openmc.model.RectangularParallelepiped(3.6549999999999994, 32.455, -32.455, -3.6549999999999994, -2.200000000000003, 103.8)
# Borated steel, 0.155cm x 100 cm
surf17 = openmc.model.RectangularParallelepiped(3.5, 32.61, -32.61, -3.5, -2.200000000000003, 97.8)
# Pedestal support plate
surf18 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -3.0, -2.2)
# Tank & BCD
surf19 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -22.200000000000003, 103.8, boundary_type="vacuum")
surf20 = openmc.ZCylinder(surface_id=20, x0=-31.5225, y0=31.5225, r=0.7975)
surf21 = openmc.ZCylinder(surface_id=21, x0=-31.5225, y0=31.5225, r=0.9325)
surf22 = openmc.ZCylinder(surface_id=22, x0=-4.455, y0=31.655, r=0.5)
surf23 = openmc.ZCylinder(surface_id=23, x0=-31.655, y0=4.455, r=0.5)
surf24 = openmc.ZCylinder(surface_id=24, x0=-4.455, y0=4.455, r=0.5)
surf25 = openmc.ZCylinder(surface_id=25, x0=31.5225, y0=31.5225, r=0.7975)
surf26 = openmc.ZCylinder(surface_id=26, x0=31.5225, y0=31.5225, r=0.9325)
surf27 = openmc.ZCylinder(surface_id=27, x0=4.455, y0=31.655, r=0.5)
surf28 = openmc.ZCylinder(surface_id=28, x0=31.655, y0=4.455, r=0.5)
surf29 = openmc.ZCylinder(surface_id=29, x0=4.455, y0=4.455, r=0.5)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1029, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1030, z0=90.0)
surf2_zmin = openmc.ZPlane(surface_id=1031, z0=0.0)
surf2_zmax = openmc.ZPlane(surface_id=1032, z0=96.9)
surf3_zmin = openmc.ZPlane(surface_id=1033, z0=-1.27)
surf3_zmax = openmc.ZPlane(surface_id=1034, z0=98.2)
surf4_zmin = openmc.ZPlane(surface_id=1035, z0=-1.27)
surf4_zmax = openmc.ZPlane(surface_id=1036, z0=98.2)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf5
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf6
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf7
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = +surf8 & -surf9
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & +surf6 & +surf7 & -surf8 & -surf9
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

# Lattice 2: 18x18 array
lattice2 = openmc.RectLattice(lattice_id=2)
lattice2.lower_left = [-14.4, -14.4]
lattice2.pitch = [1.600000, 1.600000]
lattice2.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe2 = openmc.Universe(universe_id=2)
universe2.add_cell(openmc.Cell(fill=lattice2))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Assy
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.translation = (-18.055, 18.055, 0.0)
cell1.region = +surf18 & -surf10 & +surf21 & +surf22 & +surf23 & +surf24

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = +surf18 & -surf10 & +surf20 & -surf21 & -surf10 & -surf22 & -surf10 & -surf23 & -surf10 & -surf24

# Absr
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = +surf18 & +surf10 & -surf11

# Assy
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.translation = (18.055, 18.055, 0.0)
cell4.region = +surf18 & -surf12 & +surf26 & +surf27 & +surf28 & +surf29

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf18 & -surf12 & +surf25 & -surf26 & -surf12 & -surf27 & -surf12 & -surf28 & -surf12 & -surf29

# Absr
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = +surf18 & +surf12 & -surf13

# Assy
cell7 = openmc.Cell(cell_id=7, fill=universe2)
cell7.translation = (-18.055, -18.055, 0.0)
cell7.region = +surf18 & -surf14

# SST
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf18 & -surf14 & -surf14 & -surf14 & -surf14

# Absr
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = +surf18 & +surf14 & -surf15

# Assy
cell10 = openmc.Cell(cell_id=10, fill=universe2)
cell10.translation = (18.055, -18.055, 0.0)
cell10.region = +surf18 & -surf16

# SST
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = +surf18 & -surf16 & -surf16 & -surf16 & -surf16

# Absr
cell12 = openmc.Cell(cell_id=12, fill=mat5)
cell12.region = +surf18 & +surf16 & -surf17

# SST
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = -surf18

# Water
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = -surf19 & -surf5 & +surf10 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & +surf17 & +surf18

# Water
cell22 = openmc.Cell(cell_id=22, fill=mat4)
cell22.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & +surf6 & +surf7 & -surf8 & -surf9

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell22])
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
source.space = openmc.stats.Box((-32.655, -32.655, 39.33), (32.655, 32.655, 41.33))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
