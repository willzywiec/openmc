"""
IEU-MET-FAST-022-6: FR0 experiment 9-D (case 6 detailed model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Fuel and teflon
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 9.628700e-05)
mat1.add_nuclide("U235", 9.611600e-03)
mat1.add_nuclide("U238", 3.774800e-02)
mat1.add_element("C", 5.178100e-05)
mat1.add_element("F", 1.035600e-04)

# Copper blocks
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cu", 8.417400e-02)
mat2.add_element("Ag", 7.950000e-05)
mat2.add_nuclide("O16", 1.340000e-04)

# Copper plates
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cu", 8.351200e-02)
mat3.add_element("Ag", 7.887400e-05)
mat3.add_nuclide("O16", 1.329400e-04)

# SST frames & inner part end blocks
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 5.834500e-02)
mat4.add_element("Cr", 1.588700e-02)
mat4.add_element("Ni", 7.428600e-03)
mat4.add_element("Mn", 8.353600e-04)
mat4.add_element("Si", 8.170300e-04)

# SST outer part end blocks
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 5.479400e-02)
mat5.add_element("Cr", 1.492000e-02)
mat5.add_element("Ni", 6.976400e-03)
mat5.add_element("Mn", 7.845100e-04)
mat5.add_element("Si", 7.672900e-04)

# Heavy water
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("H2", 6.209200e-02)
mat10.add_nuclide("O16", 3.105200e-02)
mat10.add_s_alpha_beta("c_D_in_D2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat10])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Fuel or Copper plates
surf1 = openmc.model.RectangularParallelepiped(-2.15, 2.15, -2.15, 2.15, -55.9, 55.9)
# Inner void
surf2 = openmc.model.RectangularParallelepiped(-2.17, 2.17, -2.17, 2.17, -58.05, 58.05)
# Frame and inner end block
surf3 = openmc.model.RectangularParallelepiped(-2.25, 2.25, -2.25, 2.25, -60.0, 60.0)
# Outer void
surf4 = openmc.model.RectangularParallelepiped(-2.285, 2.285, -2.285, 2.285, -60.0, 60.0)
# SST outside end block
surf5 = openmc.model.RectangularParallelepiped(-2.285, 2.285, -2.285, 2.285, -61.75, 61.75)
# Array boundary
surf10 = openmc.model.RectangularParallelepiped(-52.555, 52.555, -52.555, 52.555, -61.75, 61.75, boundary_type="vacuum")
# Axial core/reflector
surf11 = openmc.ZPlane(surface_id=11, z0=-17.20)
# boundaries
surf12 = openmc.ZPlane(surface_id=12, z0=17.20)
# Fuel/Cu plate boundary
surf13 = openmc.model.RectangularParallelepiped(-2.148, 2.148, -2.15, 2.15, -17.20, 17.20)
# Half element boundary
surf14 = openmc.XPlane(surface_id=14, x0=0.0)
# Quarter element boundary
surf15 = openmc.YPlane(surface_id=15, y0=0.0)
# Fuel/Cu plate boundary; rotated
surf19 = openmc.model.RectangularParallelepiped(-2.148, 2.148, -2.15, 2.15, -17.20, 17.20)
# D2O
surf21 = openmc.model.RectangularParallelepiped(-2.125, -1.810, -2.13, 2.13, -17.20, 17.20)
# Copper
surf22 = openmc.model.RectangularParallelepiped(-2.145, -1.790, -2.15, 2.15, -17.20, 17.20)
# Fuel
surf23 = openmc.model.RectangularParallelepiped(-1.790, -1.074, -2.15, 2.15, -17.20, 17.20)
# D2O
surf24 = openmc.model.RectangularParallelepiped(-1.051, -0.736, -2.13, 2.13, -17.20, 17.20)
# Copper
surf25 = openmc.model.RectangularParallelepiped(-1.071, -0.716, -2.15, 2.15, -17.20, 17.20)
# Fuel
surf26 = openmc.model.RectangularParallelepiped(-0.716, 0.0, -2.15, 2.15, -17.20, 17.20)
# D2O
surf27 = openmc.model.RectangularParallelepiped(0.023, 0.338, -2.13, 2.13, -17.20, 17.20)
# Copper
surf28 = openmc.model.RectangularParallelepiped(0.003, 0.358, -2.15, 2.15, -17.20, 17.20)
# Fuel
surf29 = openmc.model.RectangularParallelepiped(0.358, 1.074, -2.15, 2.15, -17.20, 17.20)
# D2O
surf30 = openmc.model.RectangularParallelepiped(1.097, 1.412, -2.13, 2.13, -17.20, 17.20)
# Copper
surf31 = openmc.model.RectangularParallelepiped(1.077, 1.432, -2.15, 2.15, -17.20, 17.20)
# Fuel
surf32 = openmc.model.RectangularParallelepiped(1.432, 2.148, -2.15, 2.15, -17.20, 17.20)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat2)
u1_cell0.region = -surf1
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = +surf2 & -surf3
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = +surf4 & -surf5
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

# Lattice 9: 23x23 array
lattice9 = openmc.RectLattice(lattice_id=9)
lattice9.lower_left = [-52.555, -52.555]
lattice9.pitch = [4.570000, 4.570000]
lattice9.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe123, universe44, universe45, universe45, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe44, universe44, universe44, universe45, universe45, universe45, universe45, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe119, universe44, universe44, universe44, universe45, universe45, universe45, universe45, universe121, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe44, universe44, universe44, universe44, universe45, universe45, universe45, universe45, universe45, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe44, universe44, universe44, universe44, universe45, universe45, universe45, universe45, universe45, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe44, universe44, universe44, universe44, universe45, universe45, universe45, universe45, universe45, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe119, universe44, universe44, universe44, universe45, universe45, universe45, universe45, universe121, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe44, universe44, universe44, universe45, universe45, universe45, universe125, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe44, universe45, universe45, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe9 = openmc.Universe(universe_id=9)
universe9.add_cell(openmc.Cell(fill=lattice9))

u44_cell0 = openmc.Cell(fill=mat2)
u44_cell0.region = -surf1 & -surf11
u44_cell1 = openmc.Cell(fill=mat10)
u44_cell1.region = -surf21 & +surf11 & -surf12
u44_cell2 = openmc.Cell(fill=mat2)
u44_cell2.region = +surf21 & -surf22 & +surf11 & -surf12
u44_cell3 = openmc.Cell(fill=mat1)
u44_cell3.region = +surf22 & -surf23 & +surf11 & -surf12
u44_cell4 = openmc.Cell(fill=mat10)
u44_cell4.region = -surf24 & +surf11 & -surf12
u44_cell5 = openmc.Cell(fill=mat2)
u44_cell5.region = +surf24 & -surf25 & +surf11 & -surf12
u44_cell6 = openmc.Cell(fill=mat1)
u44_cell6.region = +surf25 & -surf26 & +surf11 & -surf12
u44_cell7 = openmc.Cell(fill=mat10)
u44_cell7.region = -surf27 & +surf11 & -surf12
u44_cell8 = openmc.Cell(fill=mat2)
u44_cell8.region = +surf27 & -surf28 & +surf11 & -surf12
u44_cell9 = openmc.Cell(fill=mat1)
u44_cell9.region = +surf28 & -surf29 & +surf11 & -surf12
u44_cell10 = openmc.Cell(fill=mat10)
u44_cell10.region = -surf30 & +surf11 & -surf12
u44_cell11 = openmc.Cell(fill=mat2)
u44_cell11.region = +surf30 & -surf31 & +surf11 & -surf12
u44_cell12 = openmc.Cell(fill=mat1)
u44_cell12.region = +surf31 & -surf32 & +surf11 & -surf12
u44_cell13 = openmc.Cell(fill=mat2)
u44_cell13.region = -surf1 & +surf12
u44_cell14 = openmc.Cell(fill=mat4)
u44_cell14.region = +surf2 & -surf3
u44_cell15 = openmc.Cell(fill=mat5)
u44_cell15.region = +surf4 & -surf5
universe44 = openmc.Universe(universe_id=44, cells=[u44_cell0, u44_cell1, u44_cell2, u44_cell3, u44_cell4, u44_cell5, u44_cell6, u44_cell7, u44_cell8, u44_cell9, u44_cell10, u44_cell11, u44_cell12, u44_cell13, u44_cell14, u44_cell15])

universe45 = openmc.Universe(universe_id=45, cells=[])

u119_cell0 = openmc.Cell(fill=mat3)
u119_cell0.region = -surf13 & -surf14
universe119 = openmc.Universe(universe_id=119, cells=[u119_cell0])

u121_cell0 = openmc.Cell(fill=mat3)
u121_cell0.region = -surf13 & +surf14
universe121 = openmc.Universe(universe_id=121, cells=[u121_cell0])

u123_cell0 = openmc.Cell(fill=mat3)
u123_cell0.region = -surf19 & -surf15
universe123 = openmc.Universe(universe_id=123, cells=[u123_cell0])

u125_cell0 = openmc.Cell(fill=mat3)
u125_cell0.region = -surf13 & -surf14 & +surf15
u125_cell1 = openmc.Cell(fill=mat3)
u125_cell1.region = -surf13 & +surf14
universe125 = openmc.Universe(universe_id=125, cells=[u125_cell0, u125_cell1])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# FuArry
cell1 = openmc.Cell(cell_id=1, fill=universe9)
cell1.region = -surf10

# EndBlk
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf4 & -surf5

# EndBlk
cell22 = openmc.Cell(cell_id=22, fill=mat5)
cell22.region = +surf4 & -surf5

# R180
cell23 = openmc.Cell(cell_id=23, fill=universe44)
cell23.translation = (0.0, 0.0, 0.0)
cell23.region = -surf5

# Rest
cell25 = openmc.Cell(cell_id=25, fill=universe44)
cell25.region = -surf5 & +surf13

# Rest
cell27 = openmc.Cell(cell_id=27, fill=universe45)
cell27.region = -surf5 & +surf13

# Rest
cell29 = openmc.Cell(cell_id=29, fill=universe44)
cell29.region = -surf5 & +surf19

# Rest
cell32 = openmc.Cell(cell_id=32, fill=universe44)
cell32.region = -surf5 & +surf13

root_universe = openmc.Universe(cells=[cell1, cell5, cell22, cell23, cell25, cell27, cell29, cell32])
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
source.space = openmc.stats.Box((-10.14, -10.14, -1.0), (10.14, 10.14, 1.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
