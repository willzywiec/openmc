"""
IEU-MET-FAST-020-7: FR0 experiment T6a-D (case 6 detailed model)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Fuel and teflon
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 9.616200e-05)
mat1.add_nuclide("U235", 9.599100e-03)
mat1.add_nuclide("U238", 3.769900e-02)
mat1.add_element("C", 4.918000e-05)
mat1.add_element("F", 9.836200e-05)

# Copper blocks
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cu", 8.417400e-02)
mat2.add_element("Ag", 7.950000e-05)
mat2.add_nuclide("O16", 1.340000e-04)

# Copper plates
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cu", 8.339200e-02)
mat3.add_element("Ag", 7.876000e-05)
mat3.add_nuclide("O16", 1.327500e-04)

# SST frames & inner part end blocks
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 5.857800e-02)
mat4.add_element("Cr", 1.595100e-02)
mat4.add_element("Ni", 7.458200e-03)
mat4.add_element("Mn", 8.387000e-04)
mat4.add_element("Si", 8.202900e-04)

# SST outer part end blocks
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 4.761000e-02)
mat5.add_element("Cr", 1.296400e-02)
mat5.add_element("Ni", 6.061800e-03)
mat5.add_element("Mn", 6.816600e-04)
mat5.add_element("Si", 6.667000e-04)

# Steel (iron)
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 8.410900e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Fuel or Copper plates
surf1 = openmc.model.RectangularParallelepiped(-2.15, 2.15, -2.15, 2.15, 16.45, 46.557)
# Copper reflector block
surf2 = openmc.model.RectangularParallelepiped(-2.15, 2.15, -2.15, 2.15, -24.4, 87.407)
# Inner void
surf3 = openmc.model.RectangularParallelepiped(-2.17, 2.17, -2.17, 2.17, -25.95, 89.75)
# Frame and inner end block
surf4 = openmc.model.RectangularParallelepiped(-2.25, 2.25, -2.25, 2.25, -28.25, 91.75)
# Outer void
surf5 = openmc.model.RectangularParallelepiped(-2.285, 2.285, -2.285, 2.285, -28.25, 91.75)
# SST outside end block
surf6 = openmc.model.RectangularParallelepiped(-2.285, 2.285, -2.285, 2.285, -30.05, 93.45)
# Iron rail
surf7 = openmc.model.RectangularParallelepiped(-2.285, 2.285, -2.285, 2.285, 93.45, 96.25)
# Array boundaries
surf11 = openmc.model.RectangularParallelepiped(-20.565, 20.565, -2.285, 2.285, -999.0, 999.0)
# Array boundaries
surf12 = openmc.model.RectangularParallelepiped(-18.280, 17.56333, -6.855, 6.855, -999.0, 999.0)
surf13 = openmc.model.RectangularParallelepiped(-17.56333, 17.56333, -11.425, 11.425, -999.0, 999.0)
surf14 = openmc.model.RectangularParallelepiped(-12.99333, 12.99333, -15.995, 15.995, -999.0, 999.0)
surf15 = openmc.model.RectangularParallelepiped(-11.425, -2.285, -17.56333, 17.56333, -999.0, 999.0)
surf16 = openmc.model.RectangularParallelepiped(-2.285, 2.285, -20.565, 20.565, -999.0, 999.0)
surf17 = openmc.model.RectangularParallelepiped(2.285, 6.855, -17.56333, 15.995, -999.0, 999.0)
surf18 = openmc.model.RectangularParallelepiped(6.855, 11.425, -17.56333, 17.56333, -999.0, 999.0)
# Vertical structure, inner
surf20 = openmc.model.RectangularParallelepiped(-63.4, 63.4, -61, 59.4, -30.05, 96.25)
# Vertical structure, outer
surf21 = openmc.model.RectangularParallelepiped(-65, 65, -61, 61, -30.05, 96.25)
# Table top
surf22 = openmc.ZPlane(surface_id=22, z0=-30.05)
# BCD
surf23 = openmc.model.RectangularParallelepiped(-75, 75, -71, 71, -46.05, 96.25, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf1 & -surf2
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = +surf3 & -surf4
u1_cell3 = openmc.Cell(fill=mat5)
u1_cell3.region = +surf4 & +surf5 & -surf6
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = +surf6 & -surf7
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = -surf1
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = +surf1 & -surf2
u2_cell2 = openmc.Cell(fill=mat4)
u2_cell2.region = +surf3 & -surf4
u2_cell3 = openmc.Cell(fill=mat5)
u2_cell3.region = +surf4 & +surf5 & -surf6
u2_cell4 = openmc.Cell(fill=mat6)
u2_cell4.region = +surf6 & -surf7
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

u3_cell0 = openmc.Cell(fill=mat2)
u3_cell0.region = -surf2
u3_cell1 = openmc.Cell(fill=mat4)
u3_cell1.region = +surf3 & -surf4
u3_cell2 = openmc.Cell(fill=mat5)
u3_cell2.region = +surf4 & +surf5 & -surf6
u3_cell3 = openmc.Cell(fill=mat6)
u3_cell3.region = +surf6 & -surf7
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3])

# Lattice 4: 11x11 array
lattice4 = openmc.RectLattice(lattice_id=4)
lattice4.lower_left = [-25.135, -25.135]
lattice4.pitch = [4.570000, 4.570000]
lattice4.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe1, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3],
    [universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe1, universe1, universe1],
    [universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe3, universe1, universe3, universe3],
]
universe4 = openmc.Universe(universe_id=4)
universe4.add_cell(openmc.Cell(fill=lattice4))

# Lattice 5: 11x11 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-25.135, -25.135]
lattice5.pitch = [4.570000, 4.570000]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe2, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3],
    [universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe2, universe2, universe2],
    [universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe3, universe2, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# FuArry
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = -surf20 & -surf11

# FuArry
cell2 = openmc.Cell(cell_id=2, fill=universe4)
cell2.region = -surf20 & +surf11 & -surf12

# FuArry
cell3 = openmc.Cell(cell_id=3, fill=universe4)
cell3.region = -surf20 & +surf12 & -surf13

# FuArry
cell4 = openmc.Cell(cell_id=4, fill=universe4)
cell4.region = -surf20 & +surf13 & -surf14

# FuArry
cell5 = openmc.Cell(cell_id=5, fill=universe4)
cell5.region = -surf20 & +surf14 & -surf15

# FuArry
cell6 = openmc.Cell(cell_id=6, fill=universe4)
cell6.region = -surf20 & +surf15 & -surf16

# FuArry
cell7 = openmc.Cell(cell_id=7, fill=universe4)
cell7.region = -surf20 & +surf16 & -surf17

# FuArry
cell8 = openmc.Cell(cell_id=8, fill=universe4)
cell8.region = -surf20 & +surf17 & -surf18

# CuArry
cell9 = openmc.Cell(cell_id=9, fill=universe5)
cell9.region = -surf20 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & +surf17 & +surf18

# VrtSt
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = +surf20 & -surf21

# Table
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = +surf20 & +surf21 & -surf22 & -surf23

# FeRail
cell17 = openmc.Cell(cell_id=17, fill=mat6)
cell17.region = +surf6 & -surf7

# FeRail
cell23 = openmc.Cell(cell_id=23, fill=mat6)
cell23.region = +surf6 & -surf7

# FeRail
cell28 = openmc.Cell(cell_id=28, fill=mat6)
cell28.region = +surf6 & -surf7

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell17, cell23, cell28])
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
source.space = openmc.stats.Box((-10.14, -10.14, 30.5035), (10.14, 10.14, 32.5035))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
