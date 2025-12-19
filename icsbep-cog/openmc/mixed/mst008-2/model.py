"""
MIX-SOL-THERM-008-2: Raschig rings in 89.9 gPu/l with 157 gU/l and 4.1M solution (Model 3)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Am241", 4.841000e-08)
mat1.add_nuclide("Pu238", 4.321100e-08)
mat1.add_nuclide("Pu239", 2.127700e-04)
mat1.add_nuclide("Pu240", 1.267700e-05)
mat1.add_nuclide("Pu241", 7.815700e-07)
mat1.add_nuclide("Pu242", 1.364300e-07)
mat1.add_nuclide("U234", 2.423900e-08)
mat1.add_nuclide("U235", 2.675000e-06)
mat1.add_nuclide("U236", 4.806500e-08)
mat1.add_nuclide("U238", 3.944600e-04)
mat1.add_element("Gd", 8.262800e-08)
mat1.add_element("Fe", 1.609200e-05)
mat1.add_element("N", 4.217700e-03)
mat1.add_nuclide("H1", 5.393900e-02)
mat1.add_nuclide("O16", 3.918200e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Borosilicate Glass
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Si", 2.303100e-02)
mat2.add_nuclide("B10", 1.296200e-04)
mat2.add_nuclide("B11", 5.217200e-04)
mat2.add_element("Al", 6.671100e-04)
mat2.add_element("Fe", 9.465400e-06)
mat2.add_element("Na", 1.125900e-03)
mat2.add_element("K", 3.690800e-04)
mat2.add_nuclide("O16", 4.992800e-02)

# Borosilicate Glass
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Si", 4.438100e-03)
mat3.add_nuclide("B10", 2.497700e-05)
mat3.add_nuclide("B11", 1.005400e-04)
mat3.add_element("Al", 1.285500e-04)
mat3.add_element("Fe", 1.824000e-06)
mat3.add_element("Na", 2.169600e-04)
mat3.add_element("K", 7.112100e-05)
mat3.add_nuclide("O16", 9.621100e-03)

# Stainless Steel
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 5.941400e-05)
mat4.add_element("Mn", 8.659700e-04)
mat4.add_element("P", 3.455900e-05)
mat4.add_element("S", 2.225200e-05)
mat4.add_element("Si", 8.469600e-04)
mat4.add_element("Cr", 1.738400e-02)
mat4.add_element("Ni", 8.106100e-03)
mat4.add_element("Fe", 5.916000e-02)

# Water
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.673700e-02)
mat5.add_nuclide("O16", 3.336900e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Raschig ring, inner
surf1 = openmc.ZCylinder(surface_id=1, r=1.5875)
# Raschig ring, outer
surf2 = openmc.ZCylinder(surface_id=2, r=1.905)
# SST304L tank, inner
surf3 = openmc.ZCylinder(surface_id=3, r=30.495)
# SST304L tank, inner
surf4 = openmc.ZCylinder(surface_id=4, r=30.574)
# Water reflector
surf5 = openmc.ZCylinder(surface_id=5, r=49.53, boundary_type="vacuum")
# Critical height (case 2)
surf6 = openmc.ZPlane(surface_id=6, z0=63.98)
# Top of dry Raschig rings
surf7 = openmc.ZPlane(surface_id=7, z0=99.06)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1007, z0=0.0)
surf3_zmax = openmc.ZPlane(surface_id=1008, z0=106.68)
surf4_zmin = openmc.ZPlane(surface_id=1009, z0=-0.635)
surf4_zmax = openmc.ZPlane(surface_id=1010, z0=107.633)
surf5_zmin = openmc.ZPlane(surface_id=1011, z0=-20.0, boundary_type="vacuum")
surf5_zmax = openmc.ZPlane(surface_id=1012, z0=107.633, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf1 & -surf2 & (-surf5 & +surf5_zmin & -surf5_zmax)
u1_cell2 = openmc.Cell(fill=mat1)
u1_cell2.region = +surf2 & (-surf5 & +surf5_zmin & -surf5_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

# Lattice 2: 15x15 array
lattice2 = openmc.RectLattice(lattice_id=2)
lattice2.lower_left = [-31.888575, -31.888575]
lattice2.pitch = [4.251810, 4.251810]
lattice2.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe2 = openmc.Universe(universe_id=2)
universe2.add_cell(openmc.Cell(fill=lattice2))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# array
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.region = (-surf3 & +surf3_zmin & -surf3_zmax) & -surf6

# rings
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = (-surf3 & +surf3_zmin & -surf3_zmax) & +surf6 & -surf7

# void
cell3 = openmc.Cell(cell_id=3)
cell3.region = (-surf3 & +surf3_zmin & -surf3_zmax) & +surf7

# SS304L
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# water
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# Soln
cell9 = openmc.Cell(cell_id=9, fill=mat1)
cell9.region = +surf2 & (-surf5 & +surf5_zmin & -surf5_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell9])
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
source.space = openmc.stats.Point((0.0, 0.0, 31.99))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
