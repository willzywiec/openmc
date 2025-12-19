"""
PU-SOL-THERM-033-61: 140.8 gPu(4.23)/L at H/X=176.9 with raschig rings (model 4)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.338700e-10)
mat1.add_nuclide("U238", 1.875000e-08)
mat1.add_nuclide("Pu238", 2.600200e-08)
mat1.add_nuclide("Pu239", 3.385800e-04)
mat1.add_nuclide("Pu240", 1.493900e-05)
mat1.add_nuclide("Pu241", 1.019900e-06)
mat1.add_nuclide("Pu242", 5.604700e-08)
mat1.add_nuclide("Am241", 1.224100e-07)
mat1.add_nuclide("H1", 6.006800e-02)
mat1.add_nuclide("O16", 3.757300e-02)
mat1.add_element("N", 2.728700e-03)
mat1.add_element("Fe", 2.857500e-06)
mat1.add_element("Cr", 1.141500e-07)
mat1.add_element("Ni", 3.005000e-07)
mat1.add_element("Mn", 1.234700e-07)
mat1.add_element("Ca", 1.692500e-06)
mat1.add_element("Cu", 1.067500e-07)
mat1.add_element("Mg", 2.093200e-07)
mat1.add_element("Zn", 3.890100e-07)
mat1.add_element("Na", 3.688200e-07)
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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Critical solution height, Hc
surf1 = openmc.ZPlane(surface_id=1, z0=58.50)
# SST solution tank, inner
# surf2: Unsupported surface type "rev" with params ['3', '0.0', '0.0', '0.6', '17.98', '80.7', '17.98']
# SST solution  tank, outer
surf3 = openmc.ZCylinder(surface_id=3, r=18.28)
# SST reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, r=54.6)
# SST refelctor tank, top
surf5 = openmc.ZPlane(surface_id=5, z0=63.2)
# SST reflector tank, outer, and BCD
surf6 = openmc.ZCylinder(surface_id=6, r=55.0, boundary_type="vacuum")
# SST basket, annulus
surf10 = openmc.ZCylinder(surface_id=10, r=13.75)
# SST basket, inner
surf11 = openmc.ZCylinder(surface_id=11, r=17.7)
# SST basket, outer
surf12 = openmc.ZCylinder(surface_id=12, r=17.732)
# Hole #1 filled with solution
surf13 = openmc.ZCylinder(surface_id=13, x0=0.0, y0=-9.5, r=5.0)
# Hole #2 filled with solution
surf14 = openmc.ZCylinder(surface_id=14, x0=-6.7175, y0=6.7175, r=5.0)
# Hole #3 filled with solution
surf15 = openmc.ZCylinder(surface_id=15, x0=6.7175, y0=6.7175, r=5.0)
# SST bottom (thin) plate
surf16 = openmc.ZCylinder(surface_id=16, r=17.7)
# Raschig ring region
surf17 = openmc.ZCylinder(surface_id=17, r=17.7)
# CH2 plate
surf18 = openmc.ZCylinder(surface_id=18, r=17.7)
# Raschig ring, inner
surf20 = openmc.ZCylinder(surface_id=20, r=1.3)
# Raschig ring, outer
surf21 = openmc.ZCylinder(surface_id=21, r=1.5)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1021, z0=-0.3)
surf3_zmax = openmc.ZPlane(surface_id=1022, z0=80.7)
surf4_zmin = openmc.ZPlane(surface_id=1023, z0=-25.9)
surf4_zmax = openmc.ZPlane(surface_id=1024, z0=62.8)
surf6_zmin = openmc.ZPlane(surface_id=1025, z0=-26.3, boundary_type="vacuum")
surf6_zmax = openmc.ZPlane(surface_id=1026, z0=85.7, boundary_type="vacuum")
surf10_zmin = openmc.ZPlane(surface_id=1027, z0=81.0)
surf10_zmax = openmc.ZPlane(surface_id=1028, z0=83.0)
surf11_zmin = openmc.ZPlane(surface_id=1029, z0=1.5)
surf11_zmax = openmc.ZPlane(surface_id=1030, z0=81.8)
surf12_zmin = openmc.ZPlane(surface_id=1031, z0=1.2)
surf12_zmax = openmc.ZPlane(surface_id=1032, z0=82.2)
surf16_zmin = openmc.ZPlane(surface_id=1033, z0=1.568)
surf16_zmax = openmc.ZPlane(surface_id=1034, z0=1.6)
surf17_zmin = openmc.ZPlane(surface_id=1035, z0=1.6)
surf17_zmax = openmc.ZPlane(surface_id=1036, z0=41.6)
surf18_zmin = openmc.ZPlane(surface_id=1037, z0=41.6)
surf18_zmax = openmc.ZPlane(surface_id=1038, z0=41.85)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = -surf1 & +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf1 & +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell5 = openmc.Cell(fill=mat2)
u1_cell5.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

u2_cell0 = openmc.Cell(fill=mat2)
u2_cell0.region = (+surf10 | -surf10_zmin | +surf10_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & +surf13 & +surf14 & +surf15
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf18 & +surf18_zmin & -surf18_zmax) & +surf13 & +surf14 & +surf15
u2_cell3 = openmc.Cell(fill=mat1)
u2_cell3.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf18 & +surf18_zmin & -surf18_zmax) & -surf13
u2_cell4 = openmc.Cell(fill=mat1)
u2_cell4.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf18 & +surf18_zmin & -surf18_zmax) & -surf14
u2_cell5 = openmc.Cell(fill=mat1)
u2_cell5.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf18 & +surf18_zmin & -surf18_zmax) & -surf15
u2_cell6 = openmc.Cell(fill=mat1)
u2_cell6.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & -surf13
u2_cell7 = openmc.Cell(fill=mat1)
u2_cell7.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & -surf14
u2_cell8 = openmc.Cell(fill=mat1)
u2_cell8.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & -surf15
u2_cell9 = openmc.Cell(fill=mat1)
u2_cell9.region = -surf1 & (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf18 | -surf18_zmin | +surf18_zmax)
u2_cell10 = openmc.Cell(fill=mat4)
u2_cell10.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u2_cell11 = openmc.Cell(fill=mat4)
u2_cell11.region = +surf1 & (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf18 | -surf18_zmin | +surf18_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8, u2_cell9, u2_cell10, u2_cell11])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = -surf1 & -surf20 & (-surf6 & +surf6_zmin & -surf6_zmax)
u3_cell1 = openmc.Cell(fill=mat4)
u3_cell1.region = +surf1 & -surf20 & (-surf6 & +surf6_zmin & -surf6_zmax)
u3_cell2 = openmc.Cell(fill=mat6)
u3_cell2.region = +surf20 & -surf21 & (-surf6 & +surf6_zmin & -surf6_zmax)
u3_cell3 = openmc.Cell(fill=mat1)
u3_cell3.region = -surf1 & +surf21 & (-surf6 & +surf6_zmin & -surf6_zmax)
u3_cell4 = openmc.Cell(fill=mat4)
u3_cell4.region = +surf1 & +surf21 & (-surf6 & +surf6_zmin & -surf6_zmax)
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
cell1.region = (-surf6 & +surf6_zmin & -surf6_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf17 & +surf17_zmin & -surf17_zmax)

# Basket
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.region = (-surf6 & +surf6_zmin & -surf6_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)

# Vessels
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.region = (-surf6 & +surf6_zmin & -surf6_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax)

# Air
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = +surf1 & +surf21 & (-surf6 & +surf6_zmin & -surf6_zmax)

# Air
cell22 = openmc.Cell(cell_id=22, fill=mat4)
cell22.region = +surf1 & (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf18 | -surf18_zmin | +surf18_zmax)

# Air
cell30 = openmc.Cell(cell_id=30, fill=mat4)
cell30.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 29.25))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
