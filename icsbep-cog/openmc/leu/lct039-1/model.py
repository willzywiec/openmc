"""
LCT039-1: Exp. No. 1663 22x22-25=459 (3-1/5) array of U(4.738)O2 rods on 1.26cm pitch
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

# Air
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("N", 4.198400e-05)
mat3.add_nuclide("O16", 1.126300e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.670600e-02)
mat4.add_nuclide("O16", 3.335300e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Stainless
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 5.941400e-05)
mat5.add_element("Cr", 1.646900e-02)
mat5.add_element("Fe", 6.001400e-02)
mat5.add_element("Mn", 8.659700e-04)
mat5.add_element("Ni", 8.106100e-03)
mat5.add_element("Si", 8.469600e-04)
mat5.add_element("S", 2.225200e-05)
mat5.add_element("P", 3.071900e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical height
surf1 = openmc.ZPlane(surface_id=1, z0=81.36)
# Array boundary
surf2 = openmc.model.RectangularParallelepiped(-13.86, 13.86, -13.86, 13.86, -499.995, 499.995)
# SST upper grid plate
surf3 = openmc.model.RectangularParallelepiped(-30.0, 30.0, -30.0, 30.0, 96.45, 96.7)
# SST lower grid plate
surf4 = openmc.model.RectangularParallelepiped(-30.0, 30.0, -30.0, 30.0, -0.3, -0.04999999999999999)
# SST support pedestal plate
surf5 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -2.6, -1.8000000000000003)
# Entire problem (BCD)
surf6 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -21.799999999999997, 98.2, boundary_type="vacuum")
# UO2
surf11 = openmc.ZCylinder(surface_id=11, x0=0.0, y0=89.7, r=0.3946)
# Air
surf12 = openmc.ZCylinder(surface_id=12, x0=0.0, y0=96.9, r=0.41)
# Clad
# surf13: Unsupported surface type "rev" with params ['3', '-1.8', '0.0', '-1.0', '0.47', '98.2', '0.47', 'tr', '0', '0', '0', '0', '0', '1', '0', '1', '0']

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat5)
u1_cell0.region = -surf3 & -surf6
u1_cell1 = openmc.Cell(fill=mat5)
u1_cell1.region = -surf4 & -surf6
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = -surf5 & -surf6
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf1 & +surf3 & +surf4 & +surf5 & -surf6
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = +surf1 & +surf3 & +surf4 & +surf5 & -surf6
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf11 & -surf12
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = +surf11 & -surf12
u2_cell2 = openmc.Cell(fill=mat2)
u2_cell2.region = +surf11 & +surf12
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

u3_cell0 = openmc.Cell(fill=mat3)
u3_cell0.region = +surf1
u3_cell1 = openmc.Cell(fill=mat4)
u3_cell1.region = -surf1
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1])

# Lattice 4: 22x22 array
lattice4 = openmc.RectLattice(lattice_id=4)
lattice4.lower_left = [-13.86, -13.86]
lattice4.pitch = [1.260000, 1.260000]
lattice4.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe3, universe2],
]
universe4 = openmc.Universe(universe_id=4)
universe4.add_cell(openmc.Cell(fill=lattice4))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = -surf2 & -surf6

# Refl
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.region = +surf2 & -surf6

# Air
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf1 & +surf3 & +surf4 & +surf5 & -surf6

# Alles
cell12 = openmc.Cell(cell_id=12, fill=universe1)
cell12.region = +surf11 & +surf12 & -surf6

# Alles
cell15 = openmc.Cell(cell_id=15, fill=universe1)
cell15.region = -surf6

root_universe = openmc.Universe(cells=[cell1, cell2, cell8, cell12, cell15])
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
source.space = openmc.stats.Box((-1.63, -1.63, 39.68), (1.63, 1.63, 41.68))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
