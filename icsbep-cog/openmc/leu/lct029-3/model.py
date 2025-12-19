"""
LCT029-3: 22x22 array of 484 U(4.738)O2 fuel rods with 1.60 cm square pitch with two, 0.2934cm thick, Hf plates
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
mat2.add_element("Al", 5.956900e-02)
mat2.add_element("Mg", 3.144200e-04)
mat2.add_element("Si", 2.489400e-04)
mat2.add_element("Fe", 6.405200e-05)
mat2.add_element("Zn", 7.459700e-06)

# Stainless steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 6.001400e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Mn", 8.659700e-04)
mat3.add_element("Si", 8.469600e-04)
mat3.add_element("C", 5.941400e-05)
mat3.add_element("S", 2.225200e-05)
mat3.add_element("P", 3.071900e-05)

# Hafnium
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Zr", 2.807500e-03)
mat4.add_nuclide("Hf174", 7.031600e-05)
mat4.add_nuclide("Hf176", 2.259700e-03)
mat4.add_nuclide("Hf177", 8.075900e-03)
mat4.add_nuclide("Hf178", 1.184800e-02)
mat4.add_nuclide("Hf179", 5.915700e-03)
mat4.add_nuclide("Hf180", 1.523500e-02)

# Air
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("N", 4.198500e-05)
mat5.add_nuclide("O16", 1.126300e-05)

# Water, cases 2-6
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.675000e-02)
mat6.add_nuclide("O16", 3.337500e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Entire problem (BCD)
surf1 = openmc.model.RectangularParallelepiped(-45.0, 45.0, -45.0, 45.0, -22.6, 98.4, boundary_type="vacuum")
# Support plate
surf2 = openmc.model.RectangularParallelepiped(-49.95, 49.95, -49.95, 49.95, -2.6, -1.8000000000000003)
# Lower grid plate
surf3 = openmc.model.RectangularParallelepiped(-30.0, 30.0, -30.0, 30.0, -0.25, 0.0)
# Upper grid plate
surf4 = openmc.model.RectangularParallelepiped(-30.0, 30.0, -30.0, 30.0, 95.0, 95.25)
# Water critical height
surf5 = openmc.ZPlane(surface_id=5, z0=37.73)
# Lattice core boundary
surf6 = openmc.model.RectangularParallelepiped(-17.6, 17.6, -17.6, 17.6, -499.95, 499.95)
# Hafnium plate
surf7 = openmc.model.RectangularParallelepiped(-24.75, 24.75, 17.6, 17.8934, 0.0, 50.0)
# Hafnium plate
surf8 = openmc.model.RectangularParallelepiped(-24.75, 24.75, -17.8934, -17.6, 0.0, 50.0)
# UO2
surf11 = openmc.ZCylinder(surface_id=11, r=0.3946)
# Gap
surf12 = openmc.ZCylinder(surface_id=12, r=0.41)
# AGS
# surf13: Unsupported surface type "rev" with params ['3', '-1.8', '0.0', '-1.0', '0.47', '98.2', '0.47']
# Hole
surf14 = openmc.ZCylinder(surface_id=14, r=0.505)

# Z-plane surfaces for bounded cylinders
surf11_zmin = openmc.ZPlane(surface_id=1014, z0=0.0)
surf11_zmax = openmc.ZPlane(surface_id=1015, z0=89.7)
surf12_zmin = openmc.ZPlane(surface_id=1016, z0=0.0)
surf12_zmax = openmc.ZPlane(surface_id=1017, z0=96.9)
surf14_zmin = openmc.ZPlane(surface_id=1018, z0=-1.8)
surf14_zmax = openmc.ZPlane(surface_id=1019, z0=98.2)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat6)
u1_cell0.region = -surf1 & +surf2 & +surf3 & +surf4 & -surf5
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf1 & -surf2
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = -surf3
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = -surf4
u1_cell4 = openmc.Cell(fill=mat1)
u1_cell4.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u1_cell5 = openmc.Cell()
u1_cell5.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u1_cell6 = openmc.Cell(fill=mat2)
u1_cell6.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & -surf13 & (-surf14 & +surf14_zmin & -surf14_zmax)
u1_cell7 = openmc.Cell(fill=mat6)
u1_cell7.region = -surf5 & +surf13 & (-surf14 & +surf14_zmin & -surf14_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

# Lattice 3: 22x22 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-17.6, -17.6]
lattice3.pitch = [1.600000, 1.600000]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf1 & -surf6

# Hf
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = -surf1 & +surf6 & -surf7

# Hf
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf1 & +surf6 & -surf8

# Refl
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.region = -surf1 & +surf6 & +surf7 & +surf8

# Refl
cell13 = openmc.Cell(cell_id=13, fill=universe1)
cell13.region = -surf1 & (+surf14 | -surf14_zmin | +surf14_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell13])
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
source.space = openmc.stats.Box((-1.8, -1.8, 17.865), (1.8, 1.8, 19.865))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
