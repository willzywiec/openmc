"""
LEU-COMP-THERM-010-9: (13x8)-11.765cm-(13x8)-11.765cm-(13x8) array of U(4.306)O2 rods in water; 2.54 cm pitch; Steel walls; 0.0 gap
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.306)O2
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
mat3.add_s_alpha_beta("c_H_in_H2O")

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.670600e-02)
mat4.add_nuclide("O16", 3.335300e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Acrylic
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 5.664200e-02)
mat5.add_element("C", 3.564800e-02)
mat5.add_nuclide("O16", 1.427300e-02)
mat5.add_s_alpha_beta("c_H_in_CH2")

# Steel
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 8.181000e-02)
mat6.add_element("C", 7.468600e-04)
mat6.add_element("Mn", 1.100000e-03)
mat6.add_element("P", 6.097100e-06)
mat6.add_element("S", 8.833200e-06)
mat6.add_element("Si", 3.698300e-04)
mat6.add_element("Ni", 6.355200e-04)
mat6.add_element("Mo", 2.411400e-04)
mat6.add_element("Cr", 1.089600e-04)
mat6.add_element("Cu", 9.658700e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Array Boundary
surf1 = openmc.model.RectangularParallelepiped(-61.295, 61.295, -10.16, 10.16, -499.995, 499.995)
# Entire Problem (BCD)
surf2 = openmc.model.RectangularParallelepiped(-104.15, 104.15, -40.66, 40.66, -20.0625, 109.4975, boundary_type="vacuum")
surf3 = openmc.XPlane(surface_id=3, x0=-28.275)
surf4 = openmc.XPlane(surface_id=4, x0=-16.51)
surf5 = openmc.XPlane(surface_id=5, x0=16.51)
surf6 = openmc.XPlane(surface_id=6, x0=28.275)
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
# Reflecting wall
surf21 = openmc.model.RectangularParallelepiped(-73.65, 73.65, -28.01, -10.16, -20.0625, 101.8375)
# Reflecting wall
surf22 = openmc.model.RectangularParallelepiped(-73.65, 73.65, 10.16, 28.01, -20.0625, 101.8375)

# Z-plane surfaces for bounded cylinders
surf11_zmin = openmc.ZPlane(z0=-2.2225)
surf11_zmax = openmc.ZPlane(z0=0.0)
surf12_zmin = openmc.ZPlane(z0=0.0)
surf12_zmax = openmc.ZPlane(z0=92.075)
surf13_zmin = openmc.ZPlane(z0=92.075)
surf13_zmax = openmc.ZPlane(z0=94.2975)
surf15_zmin = openmc.ZPlane(z0=-2.2225)
surf15_zmax = openmc.ZPlane(z0=94.2975)

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

# Lattice 3: 13x8 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-16.51, -10.16]
lattice3.pitch = [2.540000, 2.540000]
lattice3.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CORE
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.translation = (-44.785, 0.0, 0.0)
cell1.region = -surf1 & -surf2 & -surf3 & +surf21 & +surf22

# PLATE
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.region = -surf1 & -surf2 & +surf3 & -surf4 & +surf21 & +surf22

# CORE
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.region = -surf1 & -surf2 & +surf4 & -surf5 & +surf21 & +surf22

# PLATE
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.region = -surf1 & -surf2 & +surf5 & -surf6 & +surf21 & +surf22

# CORE
cell5 = openmc.Cell(cell_id=5, fill=universe3)
cell5.translation = (44.785, 0.0, 0.0)
cell5.region = -surf1 & -surf2 & +surf6 & +surf21 & +surf22

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf1 & -surf2 & +surf21 & +surf22

# STEEL
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = +surf1 & -surf2 & -surf21

# STEEL
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = +surf1 & -surf2 & -surf22

# H2O
cell15 = openmc.Cell(cell_id=15, fill=mat4)
cell15.region = -surf1 & (+surf15 | -surf15_zmin | +surf15_zmax) & +surf16

# H2O
cell18 = openmc.Cell(cell_id=18, fill=mat4)
cell18.region = -surf1 & +surf16

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell15, cell18])
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
source.space = openmc.stats.Box((-45.785, -2.27, 45.0375), (45.785, 2.27, 47.0375))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
