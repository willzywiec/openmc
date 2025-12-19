"""
LCT035-3: 21x19 array of U(2.6)O2 rods on 1.956cm pitch in soluble gadolinium (TCA Core C1)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(2.60)O2 fuel
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.887200e-06)
mat1.add_nuclide("U235", 6.083000e-04)
mat1.add_nuclide("U238", 2.253100e-02)
mat1.add_nuclide("O16", 4.721400e-02)

# Al+Air (homogenized) clad
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.513700e-02)

# Al end plug, grid & support plates
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 6.022400e-02)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.669400e-02)
mat4.add_element("N", 7.393500e-07)
mat4.add_nuclide("O16", 3.334900e-02)
mat4.add_nuclide("Gd152", 4.929000e-10)
mat4.add_nuclide("Gd154", 5.372600e-09)
mat4.add_nuclide("Gd155", 3.647500e-08)
mat4.add_nuclide("Gd156", 5.048800e-08)
mat4.add_nuclide("Gd157", 3.856900e-08)
mat4.add_nuclide("Gd158", 6.121800e-08)
mat4.add_nuclide("Gd160", 5.387400e-08)
mat4.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 1.192800e-04)
mat5.add_element("Si", 1.700300e-03)
mat5.add_element("Mn", 1.738500e-03)
mat5.add_element("P", 6.938100e-05)
mat5.add_element("S", 4.467300e-05)
mat5.add_element("Ni", 8.950600e-03)
mat5.add_element("Cr", 1.745000e-02)
mat5.add_element("Fe", 5.720200e-02)

# Ordinary
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 1.374200e-02)
mat6.add_nuclide("O16", 4.591900e-02)
mat6.add_element("C", 1.153200e-04)
mat6.add_element("Na", 9.639500e-04)
mat6.add_element("Mg", 1.238800e-04)
mat6.add_element("Al", 1.740900e-03)
mat6.add_element("Si", 1.661700e-02)
mat6.add_element("K", 4.605200e-04)
mat6.add_element("Ca", 1.502500e-03)
mat6.add_element("Fe", 3.449200e-04)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical height
surf1 = openmc.ZPlane(surface_id=1, z0=82.81)
# Array boundary
surf2 = openmc.model.RectangularParallelepiped(-20.538, 20.538, -18.582, 18.582, -499.995, 499.995)
# Al lower grid
surf3 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, -12.385000000000002, -11.785)
# Al support plate
surf4 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, -18.1, -16.83)
# SS304L lower plate
surf5 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, -20.3, -18.099999999999998)
# Entire problem (BCD)
surf6 = openmc.model.RectangularParallelepiped(-50.538, 50.538, -50.538, 50.538, -71.6, 144.15)
# Top of concrete
surf7 = openmc.ZPlane(surface_id=7, z0=-34.6)
# Dummy
surf8 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, -499.95, 499.95, boundary_type="vacuum")
# UO2 pellet
surf11 = openmc.ZCylinder(surface_id=11, r=0.625)
# Al+Air homogenized clad and gap
surf12 = openmc.ZCylinder(surface_id=12, r=0.7085)
# Al end plug
surf13 = openmc.ZCylinder(surface_id=13, r=0.7085)

# Z-plane surfaces for bounded cylinders
surf11_zmin = openmc.ZPlane(surface_id=1013, z0=0.0)
surf11_zmax = openmc.ZPlane(surface_id=1014, z0=144.15)
surf12_zmin = openmc.ZPlane(surface_id=1015, z0=0.0)
surf12_zmax = openmc.ZPlane(surface_id=1016, z0=144.15)
surf13_zmin = openmc.ZPlane(surface_id=1017, z0=-16.83)
surf13_zmax = openmc.ZPlane(surface_id=1018, z0=0.0)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = -surf3 & -surf8
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf4 & -surf8
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = +surf4 & -surf5 & -surf8
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf1 & +surf3 & +surf4 & +surf5 & +surf7 & -surf8
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = -surf1 & +surf3 & +surf4 & +surf5 & -surf7 & -surf8
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax)
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax)
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

# Lattice 3: 21x19 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-20.538, -18.582]
lattice3.pitch = [1.956000, 1.956000]
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
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf2 & -surf8

# Refl
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.region = +surf2 & -surf8

# Cncrt
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = -surf1 & +surf3 & +surf4 & +surf5 & -surf7 & -surf8

# Alles
cell12 = openmc.Cell(cell_id=12, fill=universe1)
cell12.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & -surf8

root_universe = openmc.Universe(cells=[cell1, cell2, cell8, cell12])
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
source.space = openmc.stats.Point((0.0, 0.0, 41.405))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
