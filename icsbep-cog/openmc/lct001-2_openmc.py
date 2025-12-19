"""
LCT001-2: Three 20x17 arrays of U(2.35)O2 fuel rods with 2.032 cm pitch separated by 11.92 cm (SSC-2.35-000-015)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(2.35)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 2.856300e-06)
mat1.add_nuclide("U235", 4.878500e-04)
mat1.add_nuclide("U236", 3.534800e-06)
mat1.add_nuclide("U238", 2.000900e-02)
mat1.add_nuclide("O16", 4.120200e-02)

# Al-1100
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.966000e-02)
mat2.add_element("Cu", 3.070500e-05)
mat2.add_element("Mn", 7.399100e-06)
mat2.add_element("Zn", 1.243300e-05)
mat2.add_element("Si", 2.330200e-04)
mat2.add_element("Fe", 1.171900e-04)

# Al-5052
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.802800e-02)
mat3.add_element("Cr", 7.788800e-05)
mat3.add_element("Cu", 1.274600e-05)
mat3.add_element("Mg", 1.666300e-03)
mat3.add_element("Mn", 1.474300e-05)
mat3.add_element("Zn", 1.238700e-05)
mat3.add_element("Si", 1.297800e-04)
mat3.add_element("Fe", 6.526500e-05)

# Al-6061
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 5.843300e-02)
mat4.add_element("Cr", 6.231000e-05)
mat4.add_element("Cu", 6.373100e-05)
mat4.add_element("Mg", 6.665100e-04)
mat4.add_element("Mn", 2.211500e-05)
mat4.add_element("Ti", 2.537500e-05)
mat4.add_element("Zn", 3.096700e-05)
mat4.add_element("Si", 3.460700e-04)
mat4.add_element("Fe", 1.015200e-04)

# Water
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.670600e-02)
mat5.add_nuclide("O16", 3.335300e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

# Acrylic
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 5.664200e-02)
mat6.add_element("C", 3.564800e-02)
mat6.add_nuclide("O16", 1.427300e-02)
mat6.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Array outer Boundary
surf1 = openmc.model.RectangularParallelepiped(-72.88, 72.88, -17.272, 17.272, -499.995, 499.995)
# Entire Problem (BCD)
surf2 = openmc.model.RectangularParallelepiped(-102.884, 102.884, -47.272, 47.272, -19.11, 106.44, boundary_type="vacuum")
surf3 = openmc.XPlane(surface_id=3, x0=-32.24)
surf4 = openmc.XPlane(surface_id=4, x0=-20.32)
surf5 = openmc.XPlane(surface_id=5, x0=20.32)
surf6 = openmc.XPlane(surface_id=6, x0=32.24)
# Al-5052 lower plug
surf11 = openmc.ZCylinder(surface_id=11, r=0.5588)
# U(2.35)O2 fuel
surf12 = openmc.ZCylinder(surface_id=12, r=0.5588)
# Al-1100 upper plug
surf13 = openmc.ZCylinder(surface_id=13, r=0.5588)
# Al-6061 clad/outer
surf14 = openmc.ZCylinder(surface_id=14, r=0.635)
# Al-1100 upper plug
surf15 = openmc.ZCylinder(surface_id=15, r=0.635)
# Acrylic bottom
surf16 = openmc.ZPlane(surface_id=16, z0=-3.81)
# Acrylic top
surf17 = openmc.ZPlane(surface_id=17, z0=-1.27)

# Z-plane surfaces for bounded cylinders
surf11_zmin = openmc.ZPlane(surface_id=1017, z0=-1.27)
surf11_zmax = openmc.ZPlane(surface_id=1018, z0=0.0)
surf12_zmin = openmc.ZPlane(surface_id=1019, z0=0.0)
surf12_zmax = openmc.ZPlane(surface_id=1020, z0=91.44)
surf13_zmin = openmc.ZPlane(surface_id=1021, z0=91.44)
surf13_zmax = openmc.ZPlane(surface_id=1022, z0=91.92)
surf14_zmin = openmc.ZPlane(surface_id=1023, z0=-1.27)
surf14_zmax = openmc.ZPlane(surface_id=1024, z0=91.92)
surf15_zmin = openmc.ZPlane(surface_id=1025, z0=91.92)
surf15_zmax = openmc.ZPlane(surface_id=1026, z0=96.52)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & +surf17
u1_cell1 = openmc.Cell(fill=mat1)
u1_cell1.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & +surf17
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & +surf17
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & +surf17
u1_cell4 = openmc.Cell(fill=mat2)
u1_cell4.region = (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax) & +surf17
u1_cell5 = openmc.Cell(fill=mat6)
u1_cell5.region = -surf2 & +surf16 & -surf17
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = -surf2 & -surf16
u1_cell7 = openmc.Cell(fill=mat5)
u1_cell7.region = -surf2 & +surf17 & (+surf14 | -surf14_zmin | +surf14_zmax) & (+surf15 | -surf15_zmin | +surf15_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = -surf2 & +surf17
u2_cell1 = openmc.Cell(fill=mat6)
u2_cell1.region = -surf2 & +surf16 & -surf17
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = -surf2 & -surf16
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

# Lattice 3: 20x17 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-20.32, -17.272]
lattice3.pitch = [2.032000, 2.032000]
lattice3.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CORE
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.translation = (-52.56, 0.0, 0.0)
cell1.region = -surf1 & -surf2 & -surf3

# PLATE
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.region = -surf1 & -surf2 & +surf3 & -surf4

# CORE
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.region = -surf1 & -surf2 & +surf4 & -surf5

# PLATE
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.region = -surf1 & -surf2 & +surf5 & -surf6

# CORE
cell5 = openmc.Cell(cell_id=5, fill=universe3)
cell5.translation = (52.56, 0.0, 0.0)
cell5.region = -surf1 & -surf2 & +surf6

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = +surf1 & -surf2

# Water
cell15 = openmc.Cell(cell_id=15, fill=mat5)
cell15.region = -surf2 & +surf17 & (+surf14 | -surf14_zmin | +surf14_zmax) & (+surf15 | -surf15_zmin | +surf15_zmax)

# Water
cell19 = openmc.Cell(cell_id=19, fill=mat5)
cell19.region = -surf2 & -surf16

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell15, cell19])
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
source.space = openmc.stats.Box((-2.016, -1.0, 44.72), (2.016, 1.0, 46.72))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
