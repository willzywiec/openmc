"""
LCT052-6: Pseudocylindrical array of 1285 U(4.738)O2 fuel rods with 2.26 cm triangular pitch in gadolinium nitrate solution
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
mat3.add_element("C", 1.188300e-04)
mat3.add_element("P", 6.143800e-05)
mat3.add_element("S", 4.450400e-05)

# Gadolinium nitrate solution
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Gd", 6.969930e-07)
mat4.add_element("N", 5.704240e-06)
mat4.add_nuclide("H1", 6.671200e-02)
mat4.add_nuclide("O16", 3.337130e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Entire problem (BCD)
surf1 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -20.0, 100.0, boundary_type="vacuum")
# Support plate
surf2 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -2.6, -1.8000000000000003)
# Lower grid plate
surf3 = openmc.model.RectangularParallelepiped(-46.25, 46.25, -46.25, 46.25, -0.3, -0.04999999999999999)
# Upper grid plate
surf4 = openmc.model.RectangularParallelepiped(-46.25, 46.25, -46.25, 46.25, 96.45, 96.7)
# Solution critica height
surf5 = openmc.ZPlane(surface_id=5, z0=87.5)
# UO2
surf11 = openmc.ZCylinder(surface_id=11, r=0.395)
# Gap
surf12 = openmc.ZCylinder(surface_id=12, r=0.41)
# AGS
surf13 = openmc.Revolution(surface_id=13, rz=[(-1.8, 0.0), (-1.0, 0.47), (98.2, 0.47)], axis="x")
# Hole
surf20 = openmc.ZCylinder(surface_id=20, r=0.5)
# Hole
surf21 = openmc.ZCylinder(surface_id=21, x0=-1.13, y0=1.957217, r=0.5)
# Hole
surf22 = openmc.ZCylinder(surface_id=22, x0=1.13, y0=1.957217, r=0.5)
# Hole
surf23 = openmc.ZCylinder(surface_id=23, x0=-2.26, y0=0.0, r=0.5)
# Hole
surf24 = openmc.ZCylinder(surface_id=24, x0=2.26, y0=0.0, r=0.5)
# Hole
surf25 = openmc.ZCylinder(surface_id=25, x0=-1.13, y0=-1.957217, r=0.5)
# Hole
surf26 = openmc.ZCylinder(surface_id=26, x0=1.13, y0=-1.957217, r=0.5)
surf31 = openmc.ZCylinder(surface_id=31, x0=-12.43, y0=41.101567, r=0.51)
surf32 = openmc.ZCylinder(surface_id=32, x0=12.43, y0=41.101567, r=0.51)
surf33 = openmc.ZCylinder(surface_id=33, x0=-29.38, y0=31.315479, r=0.51)
surf34 = openmc.ZCylinder(surface_id=34, x0=29.38, y0=31.315479, r=0.51)
surf35 = openmc.ZCylinder(surface_id=35, x0=-41.81, y0=9.786087, r=0.51)
surf36 = openmc.ZCylinder(surface_id=36, x0=41.81, y0=9.786087, r=0.51)
surf37 = openmc.ZCylinder(surface_id=37, x0=-41.81, y0=-9.786087, r=0.51)
surf38 = openmc.ZCylinder(surface_id=38, x0=41.81, y0=-9.786087, r=0.51)
surf39 = openmc.ZCylinder(surface_id=39, x0=-29.38, y0=-31.315479, r=0.51)
surf40 = openmc.ZCylinder(surface_id=40, x0=29.38, y0=-31.315479, r=0.51)
surf41 = openmc.ZCylinder(surface_id=41, x0=-12.43, y0=-41.101567, r=0.51)
surf42 = openmc.ZCylinder(surface_id=42, x0=12.43, y0=-41.101567, r=0.51)
# Lattice
# Prism 99: 12-sided polygon
surf99_0 = openmc.Plane(a=0.5000001474, b=-0.8660253187, c=0, d=42.3750203643)
surf99_1 = openmc.Plane(a=0.8685309020, b=-0.4956350192, c=0, d=42.0199362644)
surf99_2 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=42.2375000000)
surf99_3 = openmc.Plane(a=0.8685309020, b=0.4956350192, c=0, d=42.0199362644)
surf99_4 = openmc.Plane(a=0.5000001474, b=0.8660253187, c=0, d=42.3750203643)
surf99_5 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=42.0802000000)
surf99_6 = openmc.Plane(a=-0.5000001474, b=0.8660253187, c=0, d=42.3750203643)
surf99_7 = openmc.Plane(a=-0.8685309020, b=0.4956350192, c=0, d=42.0199362644)
surf99_8 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=42.2375000000)
surf99_9 = openmc.Plane(a=-0.8685309020, b=-0.4956350192, c=0, d=42.0199362644)
surf99_10 = openmc.Plane(a=-0.5000001474, b=-0.8660253187, c=0, d=42.3750203643)
surf99_11 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=42.0802000000)

# Z-plane surfaces for bounded cylinders
surf11_zmin = openmc.ZPlane(surface_id=1099, z0=0.0)
surf11_zmax = openmc.ZPlane(surface_id=1100, z0=90.0)
surf12_zmin = openmc.ZPlane(surface_id=1101, z0=0.0)
surf12_zmax = openmc.ZPlane(surface_id=1102, z0=96.9)
surf20_zmin = openmc.ZPlane(surface_id=1103, z0=-1.8)
surf20_zmax = openmc.ZPlane(surface_id=1104, z0=98.2)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

universe2 = openmc.Universe(universe_id=2, cells=[])

# Lattice 3: 21x23 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-47.46, -45.01606]
lattice3.pitch = [4.520000, 3.914440]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = -surf1 & +surf2 & +surf3 & +surf4 & -surf5
u4_cell1 = openmc.Cell(fill=mat3)
u4_cell1.region = -surf2
u4_cell2 = openmc.Cell(fill=mat3)
u4_cell2.region = -surf3
u4_cell3 = openmc.Cell(fill=mat3)
u4_cell3.region = -surf4
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & +surf31 & +surf32 & +surf33 & +surf34 & +surf35 & +surf36 & +surf37 & +surf38 & +surf39 & +surf40 & +surf41 & +surf42

# Refl
cell2 = openmc.Cell(cell_id=2, fill=universe4)
cell2.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf31 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf37

# Refl
cell3 = openmc.Cell(cell_id=3, fill=universe4)
cell3.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf32 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf38

# Refl
cell4 = openmc.Cell(cell_id=4, fill=universe4)
cell4.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf33 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf39

# Refl
cell5 = openmc.Cell(cell_id=5, fill=universe4)
cell5.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf34 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf40

# Refl
cell6 = openmc.Cell(cell_id=6, fill=universe4)
cell6.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf35 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf41

# Refl
cell7 = openmc.Cell(cell_id=7, fill=universe4)
cell7.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf36 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf42

# Refl
cell8 = openmc.Cell(cell_id=8, fill=universe4)
cell8.region = -surf1 & (+surf99_0 | +surf99_1 | +surf99_2 | +surf99_3 | +surf99_4 | +surf99_5 | +surf99_6 | +surf99_7 | +surf99_8 | +surf99_9 | +surf99_10 | +surf99_11)

# UO2
cell9 = openmc.Cell(cell_id=9, fill=mat1)
cell9.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)

# Void
cell10 = openmc.Cell(cell_id=10)
cell10.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)

# AGS
cell11 = openmc.Cell(cell_id=11, fill=mat2)
cell11.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & -surf13 & (-surf20 & +surf20_zmin & -surf20_zmax)

# Soln
cell12 = openmc.Cell(cell_id=12, fill=mat4)
cell12.region = -surf5 & +surf13 & (-surf20 & +surf20_zmin & -surf20_zmax)

# Refl
cell13 = openmc.Cell(cell_id=13, fill=universe4)
cell13.region = -surf1 & (+surf20 | -surf20_zmin | +surf20_zmax) & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Grid
cell18 = openmc.Cell(cell_id=18, fill=mat3)
cell18.region = -surf4

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell18])
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
source.space = openmc.stats.Point((0.0, 0.0, 43.75))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
