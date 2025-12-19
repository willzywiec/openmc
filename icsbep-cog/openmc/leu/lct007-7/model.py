"""
LCT007-7: 217 U(4.738)O2 fuel rods with 2.26 cm triangular pitch in water
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.738)O2
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

# AGS clad, plugs
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.959600e-02)
mat2.add_element("Mg", 3.144200e-04)
mat2.add_element("Si", 2.489400e-04)
mat2.add_element("Zn", 7.459700e-06)
mat2.add_element("Fe", 6.405200e-05)

# Air
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("N", 4.198500e-05)
mat3.add_nuclide("O16", 1.126300e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.670600e-02)
mat4.add_nuclide("O16", 3.335300e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Stainless steel
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 5.941400e-05)
mat5.add_element("Cr", 1.646900e-02)
mat5.add_element("Fe", 6.001400e-02)
mat5.add_element("Mn", 8.659700e-04)
mat5.add_element("Ni", 8.106100e-03)
mat5.add_element("Si", 8.469600e-04)
mat5.add_element("S", 2.225600e-05)
mat5.add_nuclide("P31", 3.071900e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Entire problem (BCD)
surf1 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -21.799999999999997, 98.2, boundary_type="vacuum")
# Hexagonal
# Prism 2: 6-sided polygon
surf2_0 = openmc.Plane(a=0.5000000790, b=0.8660253581, c=0, d=15.6577384753)
surf2_1 = openmc.Plane(a=-0.5000000790, b=0.8660253581, c=0, d=15.6577384753)
surf2_2 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=15.6577360000)
surf2_3 = openmc.Plane(a=-0.5000000790, b=-0.8660253581, c=0, d=15.6577384753)
surf2_4 = openmc.Plane(a=0.5000000790, b=-0.8660253581, c=0, d=15.6577384753)
surf2_5 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=15.6577360000)
# Hexagonal
# Prism 3: 6-sided polygon
surf3_0 = openmc.Plane(a=0.5000000678, b=0.8660253647, c=0, d=16.6363472550)
surf3_1 = openmc.Plane(a=-0.5000000678, b=0.8660253647, c=0, d=16.6363472550)
surf3_2 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=16.6363450000)
surf3_3 = openmc.Plane(a=-0.5000000678, b=-0.8660253647, c=0, d=16.6363472550)
surf3_4 = openmc.Plane(a=0.5000000678, b=-0.8660253647, c=0, d=16.6363472550)
surf3_5 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=16.6363450000)
# Hc
surf10 = openmc.ZPlane(surface_id=10, z0=79.50)
# UO2
surf11 = openmc.ZCylinder(surface_id=11, x0=0.0, y0=89.7, r=0.3946)
# Gap
surf12 = openmc.ZCylinder(surface_id=12, x0=0.0, y0=96.9, r=0.41)
# AGS
# surf13: Unsupported surface type "rev" with params ['3', '-1.8', '0.0', '-1.0', '0.47', '98.2', '0.47']
# Hole in grid plates
surf14 = openmc.ZCylinder(surface_id=14, r=0.5)
# SS pedestal plate
surf15 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -2.6, -1.8000000000000003)
# SS bottom grid plate
surf16 = openmc.ZCylinder(surface_id=16, x0=-0.3, y0=-0.05, r=999.9)
# SS upper grid plate
surf17 = openmc.ZCylinder(surface_id=17, x0=96.45, y0=96.7, r=999.9)
# Hole in grid plates
surf21 = openmc.ZCylinder(surface_id=21, x0=-1.957217, y0=1.13, r=0.5)
# Hole in grid plates
surf22 = openmc.ZCylinder(surface_id=22, x0=-1.957217, y0=-1.13, r=0.5)
# Hole in grid plates
surf23 = openmc.ZCylinder(surface_id=23, x0=1.957217, y0=1.13, r=0.5)
# Hole in grid plates
surf24 = openmc.ZCylinder(surface_id=24, x0=1.957217, y0=-1.13, r=0.5)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf11 & -surf12
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf1 & +surf11 & -surf12
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = -surf1 & +surf11 & +surf12
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf1 & -surf10
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = -surf1 & +surf10
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = -surf1 & -surf15
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = -surf1 & +surf14 & -surf16 & +surf21 & +surf22 & +surf23 & +surf24
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = -surf1 & +surf14 & -surf17 & +surf21 & +surf22 & +surf23 & +surf24
u2_cell3 = openmc.Cell(fill=mat4)
u2_cell3.region = -surf1 & -surf10 & +surf14 & +surf15 & +surf16 & +surf17 & +surf21 & +surf22 & +surf23 & +surf24
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = -surf1 & +surf10 & +surf14 & +surf15 & +surf16 & +surf17 & +surf21 & +surf22 & +surf23 & +surf24
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

# Lattice 3: 9x17 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-17.614953, -19.21]
lattice3.pitch = [3.914434, 2.260000]
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

u4_cell0 = openmc.Cell(fill=mat3)
u4_cell0.region = -surf1 & +surf10
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf1 & -surf10 & +surf15
u4_cell2 = openmc.Cell(fill=mat5)
u4_cell2.region = -surf1 & -surf10 & -surf15
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf1 & (-surf3_0 & -surf3_1 & -surf3_2 & -surf3_3 & -surf3_4 & -surf3_5)

# Refl
cell2 = openmc.Cell(cell_id=2, fill=universe4)
cell2.region = -surf1 & (+surf3_0 | +surf3_1 | +surf3_2 | +surf3_3 | +surf3_4 | +surf3_5)

# Air
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = -surf1 & +surf10

# Air
cell14 = openmc.Cell(cell_id=14, fill=mat3)
cell14.region = -surf1 & +surf10 & +surf14 & +surf15 & +surf16 & +surf17 & +surf21 & +surf22 & +surf23 & +surf24

# SS
cell18 = openmc.Cell(cell_id=18, fill=mat5)
cell18.region = -surf1 & -surf10 & -surf15

root_universe = openmc.Universe(cells=[cell1, cell2, cell8, cell14, cell18])
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
source.space = openmc.stats.Point((0.0, 0.0, 39.75))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
