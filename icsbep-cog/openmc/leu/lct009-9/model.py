"""
LEU-COMP-THERM-009-9: (15x8)-3.0035cm-(0.713cm Boral)-3.0035cm-(15x8)-3.0035cm-(0.713cm Boral)-3.0035cm-(15x8) arrays U(4.31)O2 rods in water; 2.54 cm pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.31)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 5.183500e-06)
mat1.add_nuclide("U235", 1.010200e-03)
mat1.add_nuclide("U236", 5.139500e-06)
mat1.add_nuclide("U238", 2.215700e-02)
mat1.add_nuclide("O16", 4.675300e-02)

# Al-6061
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.843300e-02)
mat2.add_element("Cr", 6.231000e-05)
mat2.add_element("Cu", 6.373100e-05)
mat2.add_element("Mg", 6.665100e-04)
mat2.add_element("Mn", 2.211500e-05)
mat2.add_element("Ti", 2.537500e-05)
mat2.add_element("Zn", 3.096700e-05)
mat2.add_element("Si", 3.460700e-04)
mat2.add_element("Fe", 1.015200e-04)

# Rubber
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 5.817800e-02)
mat3.add_element("C", 4.356200e-02)
mat3.add_element("Ca", 2.566000e-03)
mat3.add_element("S", 4.782000e-04)
mat3.add_element("Si", 9.636000e-05)
mat3.add_nuclide("O16", 1.246100e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.667500e-02)
mat4.add_nuclide("O16", 3.333800e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Acrylic
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 5.664200e-02)
mat5.add_element("C", 3.564800e-02)
mat5.add_nuclide("O16", 1.427300e-02)
mat5.add_s_alpha_beta("c_H_in_CH2")

# B4C-Al
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Al", 3.467300e-02)
mat6.add_nuclide("B10", 7.921700e-03)
mat6.add_nuclide("B11", 3.188600e-02)
mat6.add_element("C", 9.950100e-03)
mat6.add_element("Cr", 1.441900e-05)
mat6.add_element("Cu", 2.123700e-05)
mat6.add_element("Fe", 8.860600e-05)
mat6.add_element("Mg", 3.084800e-05)
mat6.add_element("Mn", 1.364700e-05)
mat6.add_element("Na", 1.304500e-05)
mat6.add_element("Ni", 5.109900e-06)
mat6.add_element("Si", 1.067800e-04)
mat6.add_element("S", 1.402700e-05)
mat6.add_element("Zn", 2.293200e-05)

# Al-1100
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Al", 5.966000e-02)
mat7.add_element("Cu", 3.070500e-05)
mat7.add_element("Mn", 7.399100e-06)
mat7.add_element("Zn", 1.243300e-05)
mat7.add_element("Si", 2.330200e-04)
mat7.add_element("Fe", 1.171900e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Array Boundary
surf1 = openmc.model.RectangularParallelepiped(-63.87, 63.87, -10.16, 10.16, -499.995, 499.995)
# Entire Problem (BCD)
surf2 = openmc.model.RectangularParallelepiped(-93.87, 93.87, -40.16, 40.16, -20.0625, 107.075, boundary_type="vacuum")
surf3 = openmc.XPlane(surface_id=3, x0=-25.77)
surf4 = openmc.XPlane(surface_id=4, x0=-19.05)
surf5 = openmc.XPlane(surface_id=5, x0=19.05)
surf6 = openmc.XPlane(surface_id=6, x0=25.77)
# Rubber
surf11 = openmc.ZCylinder(surface_id=11, r=0.6415)
# U(4.31)O2 fuel
surf12 = openmc.ZCylinder(surface_id=12, r=0.6325)
# Rubber
surf13 = openmc.ZCylinder(surface_id=13, r=0.6415)
# Clad inner
surf14 = openmc.ZCylinder(surface_id=14, r=0.6415)
# Clad outer
surf15 = openmc.ZCylinder(surface_id=15, r=0.7075)
# Acrylic base plate
surf16 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, -4.7625, -2.2225)
surf21 = openmc.model.RectangularParallelepiped(-22.7665, -22.0535, -17.8, 17.8, 0.0, 91.5)
surf22 = openmc.model.RectangularParallelepiped(-22.6645, -22.1555, -499.95, 499.95, -499.95, 499.95)
surf31 = openmc.model.RectangularParallelepiped(22.0535, 22.7665, -17.8, 17.8, 0.0, 91.5)
surf32 = openmc.model.RectangularParallelepiped(22.1555, 22.6645, -499.95, 499.95, -499.95, 499.95)

# Z-plane surfaces for bounded cylinders
surf11_zmin = openmc.ZPlane(surface_id=1032, z0=-2.2225)
surf11_zmax = openmc.ZPlane(surface_id=1033, z0=0.0)
surf12_zmin = openmc.ZPlane(surface_id=1034, z0=0.0)
surf12_zmax = openmc.ZPlane(surface_id=1035, z0=92.075)
surf13_zmin = openmc.ZPlane(surface_id=1036, z0=92.075)
surf13_zmax = openmc.ZPlane(surface_id=1037, z0=94.2975)
surf15_zmin = openmc.ZPlane(surface_id=1038, z0=-2.2225)
surf15_zmax = openmc.ZPlane(surface_id=1039, z0=94.2975)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = (-surf13 & +surf13_zmin & -surf13_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u1_cell3 = openmc.Cell(fill=mat2)
u1_cell3.region = -surf1 & (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & +surf14 & (-surf15 & +surf15_zmin & -surf15_zmax)
u1_cell4 = openmc.Cell(fill=mat5)
u1_cell4.region = -surf1 & (+surf15 | -surf15_zmin | +surf15_zmax) & -surf16
u1_cell5 = openmc.Cell(fill=mat4)
u1_cell5.region = -surf1 & (+surf15 | -surf15_zmin | +surf15_zmax) & +surf16
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = -surf1 & -surf16
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = -surf1 & +surf16
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1])

# Lattice 3: 15x8 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-19.05, -10.16]
lattice3.pitch = [2.540000, 2.540000]
lattice3.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CORE
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.translation = (-44.82, 0.0, 0.0)
cell1.region = -surf1 & -surf2 & -surf3

# PLATE
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.region = -surf1 & -surf2 & +surf3 & -surf4 & +surf21 & +surf31

# CORE
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.region = -surf1 & -surf2 & +surf4 & -surf5

# PLATE
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.region = -surf1 & -surf2 & +surf5 & -surf6 & +surf21 & +surf31

# CORE
cell5 = openmc.Cell(cell_id=5, fill=universe3)
cell5.translation = (44.82, 0.0, 0.0)
cell5.region = -surf1 & -surf2 & +surf6

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf1 & -surf2 & +surf21 & +surf31

# ABSRBR
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = -surf2 & -surf21 & -surf22

# Al1100
cell8 = openmc.Cell(cell_id=8, fill=mat7)
cell8.region = -surf2 & -surf21 & +surf22

# ABSRBR
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = -surf2 & -surf31 & -surf32

# Al1100
cell10 = openmc.Cell(cell_id=10, fill=mat7)
cell10.region = -surf2 & -surf31 & +surf32

# H2O
cell17 = openmc.Cell(cell_id=17, fill=mat4)
cell17.region = -surf1 & (+surf15 | -surf15_zmin | +surf15_zmax) & +surf16

# H2O
cell20 = openmc.Cell(cell_id=20, fill=mat4)
cell20.region = -surf1 & +surf16

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell17, cell20])
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
source.space = openmc.stats.Box((-45.82, -2.27, 45.0375), (45.82, 2.27, 47.0375))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
