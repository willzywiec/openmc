"""
LCT007-4: 18x17 array of 306 U(4.738)O2 fuel rods with 1.26x2 = 2.52 cm square pitch in water
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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Entire problem (BCD)
surf1 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -21.799999999999997, 98.2, boundary_type="vacuum")
# Lattice boundary
surf2 = openmc.model.RectangularParallelepiped(-22.05, 22.05, -20.79, 20.79, -499.95, 499.95)
# Hc
surf10 = openmc.ZPlane(surface_id=10, z0=79.85)
# UO2
surf11 = openmc.ZCylinder(surface_id=11, r=0.3946)
# Gap
surf12 = openmc.ZCylinder(surface_id=12, r=0.41)
# AGS
surf13 = openmc.Revolution(surface_id=13, rz=[(-1.8, 0.0), (-1.0, 0.47), (98.2, 0.47)], axis="x")
# Hole in grid plates
surf14 = openmc.ZCylinder(surface_id=14, r=0.5)
# SS pedestal plate
surf15 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -2.6, -1.8000000000000003)
# SS bottom grid plate
surf16 = openmc.ZCylinder(surface_id=16, r=999.9)
# SS upper grid plate
surf17 = openmc.ZCylinder(surface_id=17, r=999.9)

# Z-plane surfaces for bounded cylinders
surf11_zmin = openmc.ZPlane(surface_id=1017, z0=0.0)
surf11_zmax = openmc.ZPlane(surface_id=1018, z0=89.7)
surf12_zmin = openmc.ZPlane(surface_id=1019, z0=0.0)
surf12_zmax = openmc.ZPlane(surface_id=1020, z0=96.9)
surf16_zmin = openmc.ZPlane(surface_id=1021, z0=-0.3)
surf16_zmax = openmc.ZPlane(surface_id=1022, z0=-0.05)
surf17_zmin = openmc.ZPlane(surface_id=1023, z0=96.45)
surf17_zmax = openmc.ZPlane(surface_id=1024, z0=96.7)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf1 & (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = -surf1 & (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & -surf13
u1_cell3 = openmc.Cell(fill=mat5)
u1_cell3.region = -surf1 & +surf13 & -surf15
u1_cell4 = openmc.Cell(fill=mat5)
u1_cell4.region = -surf1 & +surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)
u1_cell5 = openmc.Cell(fill=mat5)
u1_cell5.region = -surf1 & +surf14 & (-surf17 & +surf17_zmin & -surf17_zmax)
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = -surf1 & -surf10 & +surf13 & -surf14 & +surf15
u1_cell7 = openmc.Cell(fill=mat4)
u1_cell7.region = -surf1 & -surf10 & +surf14 & +surf15 & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)
u1_cell8 = openmc.Cell(fill=mat3)
u1_cell8.region = -surf1 & +surf10 & +surf13 & -surf14 & +surf15
u1_cell9 = openmc.Cell(fill=mat3)
u1_cell9.region = -surf1 & +surf10 & +surf14 & +surf15 & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = -surf1 & -surf15
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = -surf1 & +surf14 & (-surf16 & +surf16_zmin & -surf16_zmax)
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = -surf1 & +surf14 & (-surf17 & +surf17_zmin & -surf17_zmax)
u2_cell3 = openmc.Cell(fill=mat4)
u2_cell3.region = -surf1 & -surf10 & -surf14 & +surf15
u2_cell4 = openmc.Cell(fill=mat4)
u2_cell4.region = -surf1 & -surf10 & +surf14 & +surf15 & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)
u2_cell5 = openmc.Cell(fill=mat3)
u2_cell5.region = -surf1 & +surf10 & -surf14 & +surf15
u2_cell6 = openmc.Cell(fill=mat3)
u2_cell6.region = -surf1 & +surf10 & +surf14 & +surf15 & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6])

# Lattice 3: 35x33 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-22.05, -20.79]
lattice3.pitch = [1.260000, 1.260000]
lattice3.universes = [
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
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
cell1.region = -surf1 & -surf2

# Refl
cell2 = openmc.Cell(cell_id=2, fill=universe4)
cell2.region = -surf1 & +surf2

# Air
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = -surf1 & +surf10 & +surf14 & +surf15 & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)

# Air
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = -surf1 & +surf10 & +surf14 & +surf15 & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)

# SS
cell25 = openmc.Cell(cell_id=25, fill=mat5)
cell25.region = -surf1 & -surf10 & -surf15

root_universe = openmc.Universe(cells=[cell1, cell2, cell13, cell21, cell25])
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
source.space = openmc.stats.Box((-2.26, -1.0, 38.925), (2.26, 1.0, 40.925))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
