"""
LCT027-4: 14x14 array reflected by lead with no 1.5 cm water gap
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# UO2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 7.108700e-06)
mat1.add_nuclide("U235", 1.110400e-03)
mat1.add_nuclide("U236", 3.179200e-05)
mat1.add_nuclide("U238", 2.200600e-02)
mat1.add_nuclide("O16", 4.631100e-02)
mat1.add_element("Al", 4.170100e-06)
mat1.add_element("Fe", 9.514000e-06)
mat1.add_element("Si", 2.247900e-05)
mat1.add_nuclide("B10", 6.903700e-08)
mat1.add_nuclide("B11", 2.778800e-07)

# AGS clad & plugs
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.956900e-02)
mat2.add_element("Mg", 3.144200e-04)
mat2.add_element("Si", 2.489400e-04)
mat2.add_element("Zn", 7.459700e-06)
mat2.add_element("Fe", 6.405200e-05)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.670600e-02)
mat3.add_nuclide("O16", 3.335300e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Mild steel
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 8.448900e-02)
mat4.add_element("C", 2.376500e-04)
mat4.add_element("Mn", 3.463900e-04)
mat4.add_element("S", 4.450900e-05)
mat4.add_element("Si", 5.081800e-04)
mat4.add_element("P", 4.607900e-05)

# Stainless steel
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 6.001400e-02)
mat5.add_element("Cr", 1.646900e-02)
mat5.add_element("Ni", 8.106100e-03)
mat5.add_element("Mn", 8.659700e-04)
mat5.add_element("Si", 8.469600e-04)
mat5.add_element("C", 5.941400e-05)
mat5.add_element("S", 2.225600e-05)
mat5.add_element("P", 3.071900e-05)

# Lead
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Pb", 3.251500e-02)

# Air
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("N", 4.198500e-05)
mat7.add_nuclide("O16", 1.126500e-05)

# Basket bottom plate
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_nuclide("H1", 8.084800e-03)
mat8.add_nuclide("O16", 4.042400e-03)
mat8.add_element("Fe", 5.274100e-02)
mat8.add_element("Cr", 1.447300e-02)
mat8.add_element("Ni", 7.123600e-03)
mat8.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Critical height
surf1 = openmc.ZPlane(surface_id=1, z0=81.23)
# Array boundary
surf2 = openmc.model.RectangularParallelepiped(-11.2, 11.2, -11.2, 11.2, -499.95, 499.95)
# Angled corner
surf3 = openmc.model.RectangularParallelepiped(-13.2, -9.2, -11.399999999999999, -11.0, -3.1999999999999957, 103.4)
# Angled corner
surf4 = openmc.model.RectangularParallelepiped(9.2, 13.2, -11.399999999999999, -11.0, -3.1999999999999957, 103.4)
# Angled corner
surf5 = openmc.model.RectangularParallelepiped(-13.2, -9.2, 11.0, 11.399999999999999, -3.1999999999999957, 103.4)
# Angled corner
surf6 = openmc.model.RectangularParallelepiped(9.2, 13.2, 11.0, 11.399999999999999, -3.1999999999999957, 103.4)
# Angled corner
surf7 = openmc.model.RectangularParallelepiped(-11.399999999999999, -11.0, -13.2, -9.2, -3.1999999999999957, 103.4)
# Angled corner
surf8 = openmc.model.RectangularParallelepiped(11.0, 11.399999999999999, -13.2, -9.2, -3.1999999999999957, 103.4)
# Angled corner
surf9 = openmc.model.RectangularParallelepiped(-11.399999999999999, -11.0, 9.2, 13.2, -3.1999999999999957, 103.4)
# Angled corner
surf10 = openmc.model.RectangularParallelepiped(11.0, 11.399999999999999, 9.2, 13.2, -3.1999999999999957, 103.4)
# UO2
surf11 = openmc.ZCylinder(surface_id=11, r=0.3946)
# Air
surf12 = openmc.ZCylinder(surface_id=12, r=0.41)
# Clad
# surf13: Unsupported surface type "rev" with params ['3', '-1.8', '0.0', '-1.0', '0.47', '98.2', '0.47', 'tr', '0', '0', '0', '0', '0', '1', '0', '1', '0']
# Hole
surf14 = openmc.ZCylinder(surface_id=14, r=0.5)
# Basket bottom plate
surf15 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, -2.2, -1.8)
# Lower grid plate
surf16 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, 0.7000000000000001, 0.9)
# Upper grid plate
surf17 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, 96.4, 96.6)
# Top plate
surf18 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, 103.39999999999999, 103.8)
# Source support rod
surf20 = openmc.ZCylinder(surface_id=20, r=0.3)
# Hole in the mild steel pedestal support plate
surf21 = openmc.ZCylinder(surface_id=21, r=4.2215)
# Top of the pedestal support plate
surf22 = openmc.ZPlane(surface_id=22, z0=-3.2)
# Top of the pedestal support plate
surf23 = openmc.ZPlane(surface_id=23, z0=-4.2)
# Lead #1 Xo=-18.8+1.5=-17.3; Yo=-26.2-1.5=-27.7
surf25 = openmc.model.RectangularParallelepiped(-47.3, 12.7, -42.7, -12.7, -3.200000000000003, 91.8)
# Lead #2
surf26 = openmc.model.RectangularParallelepiped(-12.7, 47.3, 12.7, 42.7, -3.200000000000003, 91.8)
# Lead #3 Xo=-26.2-1.5=-27.7; Yo=18.8-1.5=17.3
surf27 = openmc.model.RectangularParallelepiped(-42.7, -12.7, -12.7, 47.3, -3.200000000000003, 91.8)
# Lead #4
surf28 = openmc.model.RectangularParallelepiped(12.7, 42.7, -47.3, 12.7, -3.200000000000003, 91.8)
# BCD
surf99 = openmc.model.RectangularParallelepiped(-59.0, 59.0, -59.0, 59.0, -22.200000000000003, 103.8, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf11_zmin = openmc.ZPlane(surface_id=1099, z0=0.0)
surf11_zmax = openmc.ZPlane(surface_id=1100, z0=89.7)
surf12_zmin = openmc.ZPlane(surface_id=1101, z0=0.0)
surf12_zmax = openmc.ZPlane(surface_id=1102, z0=96.9)
surf14_zmin = openmc.ZPlane(surface_id=1103, z0=-1.8)
surf14_zmax = openmc.ZPlane(surface_id=1104, z0=98.2)
surf20_zmin = openmc.ZPlane(surface_id=1105, z0=46.8)
surf20_zmax = openmc.ZPlane(surface_id=1106, z0=103.4)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u1_cell1 = openmc.Cell(fill=mat7)
u1_cell1.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & -surf13
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = +surf13 & (-surf14 & +surf14_zmin & -surf14_zmax) & -surf16
u1_cell4 = openmc.Cell(fill=mat7)
u1_cell4.region = +surf13 & (-surf14 & +surf14_zmin & -surf14_zmax) & -surf17
u1_cell5 = openmc.Cell(fill=mat8)
u1_cell5.region = +surf13 & -surf15
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = (+surf14 | -surf14_zmin | +surf14_zmax) & -surf16
u1_cell7 = openmc.Cell(fill=mat5)
u1_cell7.region = (+surf14 | -surf14_zmin | +surf14_zmax) & -surf17
u1_cell8 = openmc.Cell(fill=mat5)
u1_cell8.region = -surf18
u1_cell9 = openmc.Cell(fill=mat3)
u1_cell9.region = -surf1 & +surf13 & +surf15 & +surf16 & +surf17 & +surf18
u1_cell10 = openmc.Cell(fill=mat7)
u1_cell10.region = +surf1 & +surf13 & +surf15 & +surf16 & +surf17 & +surf18
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10])

# Lattice 2: 14x14 array
lattice2 = openmc.RectLattice(lattice_id=2)
lattice2.lower_left = [-11.2, -11.2]
lattice2.pitch = [1.600000, 1.600000]
lattice2.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe2 = openmc.Universe(universe_id=2)
universe2.add_cell(openmc.Cell(fill=lattice2))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.region = -surf2 & +surf3 & +surf4 & +surf5 & +surf6 & +surf7 & +surf8 & +surf9 & +surf10 & (+surf20 | -surf20_zmin | +surf20_zmax) & +surf22 & -surf99

# Angl
cell2 = openmc.Cell(cell_id=2, fill=mat5)
cell2.region = -surf2 & -surf3 & -surf2 & +surf3 & -surf7

# Angl
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = -surf2 & -surf4 & -surf2 & +surf4 & -surf8

# Angl
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = -surf2 & -surf5 & -surf2 & +surf5 & -surf9

# Angl
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = -surf2 & -surf6 & -surf2 & +surf6 & -surf10

# Sppt
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = -surf2 & (-surf20 & +surf20_zmin & -surf20_zmax)

# Air
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = +surf1 & +surf2 & +surf22 & +surf25 & +surf26 & +surf27 & +surf28 & -surf99

# H2O
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = -surf1 & +surf2 & +surf22 & +surf25 & +surf26 & +surf27 & +surf28 & -surf99

# Lead
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = +surf2 & +surf22 & -surf25 & +surf2 & +surf22 & -surf26 & +surf2 & +surf22 & -surf27 & +surf2 & +surf22 & -surf28

# H2O
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = -surf21 & -surf22 & +surf23 & -surf99

# Mild
cell11 = openmc.Cell(cell_id=11, fill=mat4)
cell11.region = +surf21 & -surf22 & +surf23 & -surf99

# H2O
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = -surf23 & -surf99

# Air
cell24 = openmc.Cell(cell_id=24, fill=mat7)
cell24.region = +surf1 & +surf13 & +surf15 & +surf16 & +surf17 & +surf18

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell24])
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
source.space = openmc.stats.Box((-1.8, -1.8, 39.615), (1.8, 1.8, 41.615))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
