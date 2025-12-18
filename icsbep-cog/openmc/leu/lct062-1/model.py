"""
LCT062-1: 18x18 array of U(2.6)O2 rods on 1.9558cm pitch with no poison plate (TCA)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(2.60)O2 pellet
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.882500e-06)
mat1.add_nuclide("U235", 6.077100e-04)
mat1.add_nuclide("U238", 2.247400e-02)
mat1.add_nuclide("O16", 4.700200e-02)

# U(2.58)O2 powder
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 4.647800e-06)
mat2.add_nuclide("U235", 5.785000e-04)
mat2.add_nuclide("U238", 2.156400e-02)
mat2.add_nuclide("O16", 4.436700e-02)

# Al-6061
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.843300e-02)
mat3.add_element("Cr", 6.231000e-05)
mat3.add_element("Cu", 6.373100e-05)
mat3.add_element("Mg", 6.665100e-04)
mat3.add_element("Mn", 2.211500e-05)
mat3.add_element("Ti", 2.537500e-05)
mat3.add_element("Zn", 3.096700e-05)
mat3.add_element("Si", 3.460700e-04)
mat3.add_element("Fe", 1.015200e-04)

# SS304L
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 1.192800e-04)
mat4.add_element("Si", 1.700300e-03)
mat4.add_element("Mn", 1.738500e-03)
mat4.add_element("P", 6.938100e-05)
mat4.add_element("S", 4.467300e-05)
mat4.add_element("Ni", 8.950900e-03)
mat4.add_element("Cr", 1.745000e-02)
mat4.add_element("Fe", 5.720200e-02)

# Water
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.673500e-02)
mat5.add_nuclide("O16", 3.336800e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical height
surf1 = openmc.ZPlane(surface_id=1, z0=80.89)
# Array boundary
surf2 = openmc.model.RectangularParallelepiped(-17.6022, 17.6022, -17.6022, 17.6022, -499.995, 499.995)
# Al6061 upper grid plate
surf3 = openmc.model.RectangularParallelepiped(-49.95, 49.95, -49.95, 49.95, 163.67, 164.27)
# Al6061 lower grid plate
surf4 = openmc.model.RectangularParallelepiped(-49.95, 49.95, -49.95, 49.95, -12.385000000000002, -11.785)
# Al6061 support plate
surf5 = openmc.model.RectangularParallelepiped(-49.95, 49.95, -49.95, 49.95, -18.1, -16.83)
# SS304L lower plate
surf6 = openmc.model.RectangularParallelepiped(-49.95, 49.95, -49.95, 49.95, -20.3, -18.099999999999998)
# Entire problem (BCD)
surf7 = openmc.model.RectangularParallelepiped(-47.6022, 47.6022, -47.6022, 47.6022, -34.10000000000001, 170.73000000000002, boundary_type="vacuum")
# Dummy
surf8 = openmc.model.RectangularParallelepiped(-49.95, 49.95, -49.95, 49.95, -499.95, 499.95)
# UO2 pellet
surf11 = openmc.ZCylinder(surface_id=11, x0=0.0, y0=144.15, r=0.625)
# Gap
surf12 = openmc.ZCylinder(surface_id=12, x0=0.0, y0=146.69, r=0.6324)
# Al6061
surf13 = openmc.ZCylinder(surface_id=13, x0=-16.83, y0=170.73, r=0.7086)
# Hole in grid plates
surf14 = openmc.ZCylinder(surface_id=14, x0=-16.84, y0=170.73, r=0.7239)
# UO2 pellet
surf21 = openmc.ZCylinder(surface_id=21, x0=0.0, y0=145.415, r=0.635)
# Al6061
surf22 = openmc.ZCylinder(surface_id=22, x0=-16.83, y0=170.73, r=0.70612)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = -surf3 & -surf8
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf4 & -surf8
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = -surf5 & -surf8
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = +surf5 & -surf6 & -surf8
u1_cell4 = openmc.Cell(fill=mat5)
u1_cell4.region = -surf1 & +surf3 & +surf4 & +surf5 & +surf6 & -surf8
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf11 & -surf12
u2_cell1 = openmc.Cell()
u2_cell1.region = +surf11 & -surf12
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf11 & +surf12 & -surf13 & -surf8
u2_cell3 = openmc.Cell(fill=mat5)
u2_cell3.region = -surf1 & +surf13 & -surf14 & -surf8
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3])

u3_cell0 = openmc.Cell(fill=mat2)
u3_cell0.region = -surf21 & -surf8
u3_cell1 = openmc.Cell(fill=mat3)
u3_cell1.region = +surf21 & -surf22 & -surf8
u3_cell2 = openmc.Cell(fill=mat5)
u3_cell2.region = -surf1 & -surf14 & +surf22 & -surf8
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2])

# Lattice 4: 18x18 array
lattice4 = openmc.RectLattice(lattice_id=4)
lattice4.lower_left = [-17.6022, -17.6022]
lattice4.pitch = [1.955800, 1.955800]
lattice4.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe4 = openmc.Universe(universe_id=4)
universe4.add_cell(openmc.Cell(fill=lattice4))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = -surf2 & -surf7

# Refl
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.region = +surf2 & -surf7

# H2O
cell8 = openmc.Cell(cell_id=8, fill=mat5)
cell8.region = -surf1 & +surf3 & +surf4 & +surf5 & +surf6 & -surf8

# Alles
cell13 = openmc.Cell(cell_id=13, fill=universe1)
cell13.region = +surf14 & -surf8

# Alles
cell17 = openmc.Cell(cell_id=17, fill=universe1)
cell17.region = +surf14 & -surf8

root_universe = openmc.Universe(cells=[cell1, cell2, cell8, cell13, cell17])
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
source.space = openmc.stats.Box((-1.98, -1.98, 39.445), (1.98, 1.98, 41.445))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
