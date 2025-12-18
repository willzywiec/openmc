"""
PU-SOL-THERM-033-63: 160.7 gPu(4.23)/L at H/X=153.2 with raschig rings (model 4)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.527500e-10)
mat1.add_nuclide("U238", 2.139500e-08)
mat1.add_nuclide("Pu238", 2.967700e-08)
mat1.add_nuclide("Pu239", 3.864400e-04)
mat1.add_nuclide("Pu240", 1.705000e-05)
mat1.add_nuclide("Pu241", 1.164100e-06)
mat1.add_nuclide("Pu242", 6.396800e-08)
mat1.add_nuclide("Am241", 1.397100e-07)
mat1.add_nuclide("H1", 5.938100e-02)
mat1.add_nuclide("O16", 3.797300e-02)
mat1.add_element("N", 2.985500e-03)
mat1.add_element("Fe", 3.235000e-06)
mat1.add_element("Cr", 1.302800e-07)
mat1.add_element("Ni", 3.429700e-07)
mat1.add_element("Mn", 1.409200e-07)
mat1.add_element("Ca", 1.931700e-06)
mat1.add_element("Cu", 1.218300e-07)
mat1.add_element("Mg", 2.389000e-07)
mat1.add_element("Zn", 4.439900e-07)
mat1.add_element("Na", 4.209500e-07)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SST
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.954600e-02)
mat2.add_element("Si", 1.646900e-03)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Mn", 8.659700e-04)
mat2.add_element("Si", 1.693900e-03)
mat2.add_element("S", 4.450400e-05)
mat2.add_element("P", 6.143900e-05)
mat2.add_element("C", 1.188300e-04)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.670600e-02)
mat3.add_nuclide("O16", 3.335300e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("N", 4.198500e-05)
mat4.add_nuclide("O16", 1.126300e-05)

# Polyethylene
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 8.310400e-02)
mat5.add_element("C", 4.155200e-02)
mat5.add_s_alpha_beta("c_H_in_CH2")

# Borated pyrex
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("B10", 1.039600e-03)
mat6.add_nuclide("B11", 4.184400e-03)
mat6.add_element("Al", 5.334600e-04)
mat6.add_element("Fe", 3.705600e-06)
mat6.add_element("Na", 1.482700e-03)
mat6.add_element("K", 3.061000e-04)
mat6.add_element("Si", 1.789200e-02)
mat6.add_nuclide("O16", 4.532300e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical solution height, Hc
surf1 = openmc.ZPlane(surface_id=1, z0=58.32)
# SST solution tank, inner
# surf2: Unsupported surface type "rev" with params ['3', '0.0', '0.0', '0.6', '17.98', '80.7', '17.98']
# SST solution  tank, outer
surf3 = openmc.ZCylinder(surface_id=3, x0=-0.3, y0=80.7, r=18.28)
# SST reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, x0=-25.9, y0=62.8, r=54.6)
# SST refelctor tank, top
surf5 = openmc.ZPlane(surface_id=5, z0=63.2)
# SST reflector tank, outer, and BCD
surf6 = openmc.ZCylinder(surface_id=6, x0=-26.3, y0=85.7, r=55.0, boundary_type="vacuum")
# SST basket, annulus
surf10 = openmc.ZCylinder(surface_id=10, x0=81.0, y0=83.0, r=13.75)
# SST basket, inner
surf11 = openmc.ZCylinder(surface_id=11, x0=1.5, y0=81.8, r=17.7)
# SST basket, outer
surf12 = openmc.ZCylinder(surface_id=12, x0=1.2, y0=82.2, r=17.732)
# Hole #1 filled with solution
surf13_cyl = openmc.ZCylinder(surface_id=13, x0=tr, y0=0, r=5.0)
surf13_zmin = openmc.ZPlane(z0=-9.5)
surf13_zmax = openmc.ZPlane(z0=0.0)
surf13 = (surf13_cyl, surf13_zmin, surf13_zmax)
# Hole #2 filled with solution
surf14_cyl = openmc.ZCylinder(surface_id=14, x0=tr, y0=-6.7175, r=5.0)
surf14_zmin = openmc.ZPlane(z0=6.7175)
surf14_zmax = openmc.ZPlane(z0=0.0)
surf14 = (surf14_cyl, surf14_zmin, surf14_zmax)
# Hole #3 filled with solution
surf15_cyl = openmc.ZCylinder(surface_id=15, x0=tr, y0=6.7175, r=5.0)
surf15_zmin = openmc.ZPlane(z0=6.7175)
surf15_zmax = openmc.ZPlane(z0=0.0)
surf15 = (surf15_cyl, surf15_zmin, surf15_zmax)
# SST bottom (thin) plate
surf16 = openmc.ZCylinder(surface_id=16, x0=1.568, y0=1.6, r=17.7)
# Raschig ring region
surf17 = openmc.ZCylinder(surface_id=17, x0=1.6, y0=41.6, r=17.7)
# CH2 plate
surf18 = openmc.ZCylinder(surface_id=18, x0=41.6, y0=41.85, r=17.7)
# Raschig ring, inner
surf20 = openmc.ZCylinder(surface_id=20, r=1.3)
# Raschig ring, outer
surf21 = openmc.ZCylinder(surface_id=21, r=1.5)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf3
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = +surf1 & -surf3
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = -surf3
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = -surf1 & +surf3 & -surf4
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf1 & +surf3 & -surf4
u1_cell5 = openmc.Cell(fill=mat2)
u1_cell5.region = +surf3 & +surf4 & -surf5 & -surf6
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = +surf3 & +surf4 & +surf5 & -surf6
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

u2_cell0 = openmc.Cell(fill=mat2)
u2_cell0.region = +surf10 & +surf11 & -surf12 & +surf13 & +surf14 & +surf15
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = -surf11 & -surf16
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = -surf11 & -surf18 & +surf13 & +surf14 & +surf15
u2_cell3 = openmc.Cell(fill=mat1)
u2_cell3.region = -surf11 & -surf18 & -surf13
u2_cell4 = openmc.Cell(fill=mat1)
u2_cell4.region = -surf11 & -surf18 & -surf14
u2_cell5 = openmc.Cell(fill=mat1)
u2_cell5.region = -surf11 & -surf18 & -surf15
u2_cell6 = openmc.Cell(fill=mat1)
u2_cell6.region = +surf11 & -surf12 & -surf13
u2_cell7 = openmc.Cell(fill=mat1)
u2_cell7.region = +surf11 & -surf12 & -surf14
u2_cell8 = openmc.Cell(fill=mat1)
u2_cell8.region = +surf11 & -surf12 & -surf15
u2_cell9 = openmc.Cell(fill=mat1)
u2_cell9.region = -surf1 & -surf11 & +surf16 & +surf18
u2_cell10 = openmc.Cell(fill=mat4)
u2_cell10.region = -surf10 & +surf11 & -surf12
u2_cell11 = openmc.Cell(fill=mat4)
u2_cell11.region = +surf1 & -surf11 & +surf16 & +surf18
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8, u2_cell9, u2_cell10, u2_cell11])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = -surf1 & -surf20 & -surf6
u3_cell1 = openmc.Cell(fill=mat4)
u3_cell1.region = +surf1 & -surf20 & -surf6
u3_cell2 = openmc.Cell(fill=mat6)
u3_cell2.region = +surf20 & -surf21 & -surf6
u3_cell3 = openmc.Cell(fill=mat1)
u3_cell3.region = -surf1 & +surf21 & -surf6
u3_cell4 = openmc.Cell(fill=mat4)
u3_cell4.region = +surf1 & +surf21 & -surf6
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4])

# Lattice 4: 13x13 array
lattice4 = openmc.RectLattice(lattice_id=4)
lattice4.lower_left = [-21.476, -21.476]
lattice4.pitch = [3.304000, 3.304000]
lattice4.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe4 = openmc.Universe(universe_id=4)
universe4.add_cell(openmc.Cell(fill=lattice4))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Array
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = -surf6 & -surf12 & -surf17

# Basket
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.region = -surf6 & -surf12 & +surf17

# Vessels
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.region = -surf6 & +surf12

# Air
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = +surf1 & +surf21 & -surf6

# Air
cell22 = openmc.Cell(cell_id=22, fill=mat4)
cell22.region = +surf1 & -surf11 & +surf16 & +surf18

# Air
cell30 = openmc.Cell(cell_id=30, fill=mat4)
cell30.region = +surf3 & +surf4 & +surf5 & -surf6

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell9, cell22, cell30])
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
source.space = openmc.stats.Point((0.0, 0.0, 29.16))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
