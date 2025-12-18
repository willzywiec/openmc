"""
LCT034-10: Four 18x18 arrays of U(4.738)O2 rods, 1.60 cm pitch, 0.65cm Boral, 0.3cm water gap, Hc=50.74cm
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

# Boral Al
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 5.916900e-02)

# Boral B4C+Al
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("C", 8.089400e-03)
mat6.add_element("Al", 4.187300e-02)
mat6.add_nuclide("B10", 6.444800e-03)
mat6.add_nuclide("B11", 2.594100e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# UO2
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0, y0=90.0, r=0.395)
# Gap
surf2 = openmc.ZCylinder(surface_id=2, x0=0.0, y0=96.9, r=0.41)
# AGS
surf3 = openmc.ZCylinder(surface_id=3, x0=-1.27, y0=98.2, r=0.47)
# Hole
surf4 = openmc.ZCylinder(surface_id=4, x0=-1.27, y0=98.2, r=0.5)
# Critical water height
surf5 = openmc.ZPlane(surface_id=5, z0=50.74)
# Lower grid plate
surf6 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -0.30000000000000004, -0.1)
# Upper grid plate
surf7 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, 96.60000000000001, 96.8)
# Basket, inner
surf8 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -1.8000000000000043, 103.4)
# Basket, outer
surf9 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -2.200000000000003, 103.8)
# Basket
surf10 = openmc.model.RectangularParallelepiped(-29.6, -0.7999999999999989, 0.7999999999999989, 29.6, -2.200000000000003, 103.8)
# Boral, 0.65cm x 100 cm
surf11 = openmc.model.RectangularParallelepiped(-30.25, -0.14999999999999858, 0.14999999999999858, 30.25, -2.200000000000003, 97.8)
# Basket
surf12 = openmc.model.RectangularParallelepiped(0.7999999999999989, 29.6, 0.7999999999999989, 29.6, -2.200000000000003, 103.8)
# Boral, 0.65cm x 100 cm
surf13 = openmc.model.RectangularParallelepiped(0.14999999999999858, 30.25, 0.14999999999999858, 30.25, -2.200000000000003, 97.8)
# Basket
surf14 = openmc.model.RectangularParallelepiped(-29.6, -0.7999999999999989, -29.6, -0.7999999999999989, -2.200000000000003, 103.8)
# Boral, 0.65cm x 100 cm
surf15 = openmc.model.RectangularParallelepiped(-30.25, -0.14999999999999858, -30.25, -0.14999999999999858, -2.200000000000003, 97.8)
# Basket
surf16 = openmc.model.RectangularParallelepiped(0.7999999999999989, 29.6, -29.6, -0.7999999999999989, -2.200000000000003, 103.8)
# Boral, 0.65cm x 100 cm
surf17 = openmc.model.RectangularParallelepiped(0.14999999999999858, 30.25, -30.25, -0.14999999999999858, -2.200000000000003, 97.8)
# Pedestal support plate
surf18 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -3.0, -2.2)
# Tank & BCD
surf19 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -22.200000000000003, 103.8, boundary_type="vacuum")
surf20_cyl = openmc.ZCylinder(surface_id=20, x0=tr, y0=-28.6675, r=0.7975)
surf20_zmin = openmc.ZPlane(z0=28.6675)
surf20_zmax = openmc.ZPlane(z0=0.0)
surf20 = (surf20_cyl, surf20_zmin, surf20_zmax)
# surf21: Error converting surface type "c": could not convert string to float: 'tr'
# surf22: Error converting surface type "c": could not convert string to float: 'tr'
# surf23: Error converting surface type "c": could not convert string to float: 'tr'
# surf24: Error converting surface type "c": could not convert string to float: 'tr'
surf25_cyl = openmc.ZCylinder(surface_id=25, x0=tr, y0=28.6675, r=0.7975)
surf25_zmin = openmc.ZPlane(z0=28.6675)
surf25_zmax = openmc.ZPlane(z0=0.0)
surf25 = (surf25_cyl, surf25_zmin, surf25_zmax)
# surf26: Error converting surface type "c": could not convert string to float: 'tr'
# surf27: Error converting surface type "c": could not convert string to float: 'tr'
# surf28: Error converting surface type "c": could not convert string to float: 'tr'
# surf29: Error converting surface type "c": could not convert string to float: 'tr'
# Aluminum cover
surf40 = openmc.model.RectangularParallelepiped(-15.049999999999999, 14.4, -15.049999999999999, -14.4, -2.200000000000003, 97.8)
# B4C+Al
surf41 = openmc.model.RectangularParallelepiped(-50.32, 49.669999999999995, -14.94, -14.51, -452.15, 547.75)
# Aluminum cover
surf42 = openmc.model.RectangularParallelepiped(-14.4, 15.049999999999999, 14.4, 15.049999999999999, -2.200000000000003, 97.8)
# B4C+Al
surf43 = openmc.model.RectangularParallelepiped(-49.669999999999995, 50.32, 14.51, 14.94, -452.15, 547.75)
# Aluminum cover
surf44 = openmc.model.RectangularParallelepiped(-15.049999999999999, -14.4, -14.4, 15.049999999999999, -2.200000000000003, 97.8)
# B4C+Al
surf45 = openmc.model.RectangularParallelepiped(-14.94, -14.51, -49.669999999999995, 50.32, -452.15, 547.75)
# Aluminum cover
surf46 = openmc.model.RectangularParallelepiped(14.4, 15.049999999999999, -15.049999999999999, 14.4, -2.200000000000003, 97.8)
# B4C+Al
surf47 = openmc.model.RectangularParallelepiped(14.51, 14.94, -50.32, 49.669999999999995, -452.15, 547.75)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf2
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf1 & +surf2 & -surf3
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = +surf3 & -surf4 & -surf5
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = +surf4 & -surf6
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = +surf4 & -surf7
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = +surf8 & -surf9
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = +surf4 & -surf5 & +surf6 & +surf7 & -surf8 & -surf9
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

u3_cell0 = openmc.Cell(fill=mat6)
u3_cell0.region = -surf40 & -surf41
u3_cell1 = openmc.Cell(fill=mat5)
u3_cell1.region = -surf40 & +surf41
u3_cell2 = openmc.Cell(fill=mat6)
u3_cell2.region = -surf42 & -surf43 & +surf40
u3_cell3 = openmc.Cell(fill=mat5)
u3_cell3.region = -surf42 & +surf43 & +surf40
u3_cell4 = openmc.Cell(fill=mat6)
u3_cell4.region = -surf44 & -surf45 & +surf40 & +surf42
u3_cell5 = openmc.Cell(fill=mat5)
u3_cell5.region = -surf44 & +surf45 & +surf40 & +surf42
u3_cell6 = openmc.Cell(fill=mat6)
u3_cell6.region = -surf46 & -surf47 & +surf40 & +surf42 & +surf44
u3_cell7 = openmc.Cell(fill=mat5)
u3_cell7.region = -surf46 & +surf47 & +surf40 & +surf42 & +surf44
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5, u3_cell6, u3_cell7])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Assy
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.translation = (-15.2, 15.2, 0.0)
cell1.region = +surf18 & -surf10

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = +surf18 & -surf10 & +surf20

# Boral
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.translation = (-15.2, 15.2, 0.0)
cell3.region = +surf18 & +surf10 & -surf11

# Assy
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.translation = (15.2, 15.2, 0.0)
cell4.region = +surf18 & -surf12

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf18 & -surf12 & +surf25

# Boral
cell6 = openmc.Cell(cell_id=6, fill=universe3)
cell6.translation = (15.2, 15.2, 0.0)
cell6.region = +surf18 & +surf12 & -surf13

# Assy
cell7 = openmc.Cell(cell_id=7, fill=universe2)
cell7.translation = (-15.2, -15.2, 0.0)
cell7.region = +surf18 & -surf14

# SST
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf18 & -surf14

# Boral
cell9 = openmc.Cell(cell_id=9, fill=universe3)
cell9.translation = (-15.2, -15.2, 0.0)
cell9.region = +surf18 & +surf14 & -surf15

# Assy
cell10 = openmc.Cell(cell_id=10, fill=universe2)
cell10.translation = (15.2, -15.2, 0.0)
cell10.region = +surf18 & -surf16

# SST
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = +surf18 & -surf16

# Boral
cell12 = openmc.Cell(cell_id=12, fill=universe3)
cell12.translation = (15.2, -15.2, 0.0)
cell12.region = +surf18 & +surf16 & -surf17

# SST
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = -surf18

# Water
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = -surf19 & -surf5 & +surf10 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & +surf17 & +surf18

# Water
cell22 = openmc.Cell(cell_id=22, fill=mat4)
cell22.region = +surf4 & -surf5 & +surf6 & +surf7 & -surf8 & -surf9

# Al
cell31 = openmc.Cell(cell_id=31, fill=mat5)
cell31.region = -surf46 & +surf47 & +surf40 & +surf42 & +surf44

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell22, cell31])
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
source.space = openmc.stats.Box((-29.8, -29.8, 24.37), (29.8, 29.8, 26.37))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
