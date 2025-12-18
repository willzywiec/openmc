"""
LCT007-2: 16x17 array of 272 U(4.738)O2 fuel rods with 1.60 cm square pitch in water
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
# Lattice boundary
surf2 = openmc.model.RectangularParallelepiped(-12.8, 12.8, -13.6, 13.6, -499.95, 499.95)
# Hc
surf10 = openmc.ZPlane(surface_id=10, z0=73.53)
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

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf11 & -surf12
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf1 & +surf11 & -surf12
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = -surf1 & +surf11 & +surf12
u1_cell3 = openmc.Cell(fill=mat5)
u1_cell3.region = -surf1 & -surf15
u1_cell4 = openmc.Cell(fill=mat5)
u1_cell4.region = -surf1 & +surf14 & -surf16
u1_cell5 = openmc.Cell(fill=mat5)
u1_cell5.region = -surf1 & +surf14 & -surf17
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = -surf1 & -surf10 & -surf14 & +surf15
u1_cell7 = openmc.Cell(fill=mat4)
u1_cell7.region = -surf1 & -surf10 & +surf14 & +surf15 & +surf16 & +surf17
u1_cell8 = openmc.Cell(fill=mat3)
u1_cell8.region = -surf1 & +surf10 & -surf14 & +surf15
u1_cell9 = openmc.Cell(fill=mat3)
u1_cell9.region = -surf1 & +surf10 & +surf14 & +surf15 & +surf16 & +surf17
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9])

# Lattice 2: 16x17 array
lattice2 = openmc.RectLattice(lattice_id=2)
lattice2.lower_left = [-12.8, -13.6]
lattice2.pitch = [1.600000, 1.600000]
lattice2.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe2 = openmc.Universe(universe_id=2)
universe2.add_cell(openmc.Cell(fill=lattice2))

u3_cell0 = openmc.Cell(fill=mat3)
u3_cell0.region = -surf1 & +surf10
u3_cell1 = openmc.Cell(fill=mat4)
u3_cell1.region = -surf1 & -surf10 & +surf15
u3_cell2 = openmc.Cell(fill=mat5)
u3_cell2.region = -surf1 & -surf10 & -surf15
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.region = -surf1 & -surf2

# Refl
cell2 = openmc.Cell(cell_id=2, fill=universe3)
cell2.region = -surf1 & +surf2

# Air
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = -surf1 & +surf10 & +surf14 & +surf15 & +surf16 & +surf17

# SS
cell17 = openmc.Cell(cell_id=17, fill=mat5)
cell17.region = -surf1 & -surf10 & -surf15

root_universe = openmc.Universe(cells=[cell1, cell2, cell13, cell17])
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
source.space = openmc.stats.Box((-1.8, -1.0, 35.765), (1.8, 1.0, 37.765))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
