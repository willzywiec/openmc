"""
IEU-MET-FAST-022-1: FR0 experiment 3X-D (case 1 detailed model)
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

# Graphite
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("C", 8.302900e-02)
mat6.add_s_alpha_beta("c_Graphite")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

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
# Fuel
surf11 = openmc.model.RectangularParallelepiped(-2.15, 2.15, -2.148, -1.432, 0.0, 4.3)
# Graphite
surf12 = openmc.model.RectangularParallelepiped(-2.15, 2.15, -1.432, -1.074, 0.0, 4.3)
# Fuel
surf13 = openmc.model.RectangularParallelepiped(-2.15, 2.15, -1.074, -0.358, 0.0, 4.3)
# Graphite
surf14 = openmc.model.RectangularParallelepiped(-2.15, 2.15, -0.358, 0.0, 0.0, 4.3)
# Fuel
surf15 = openmc.model.RectangularParallelepiped(-2.15, 2.15, 0.0, 0.716, 0.0, 4.3)
# Graphite
surf16 = openmc.model.RectangularParallelepiped(-2.15, 2.15, 0.716, 1.074, 0.0, 4.3)
# Fuel
surf17 = openmc.model.RectangularParallelepiped(-2.15, 2.15, 1.074, 1.790, 0.0, 4.3)
# Graphite
surf18 = openmc.model.RectangularParallelepiped(-2.15, 2.15, 1.790, 2.148, 0.0, 4.3)
surf20 = openmc.ZPlane(surface_id=20, z0=-19.35)
surf21 = openmc.ZPlane(surface_id=21, z0=-15.05)
surf22 = openmc.ZPlane(surface_id=22, z0=-10.75)
surf23 = openmc.ZPlane(surface_id=23, z0=-6.45)
surf24 = openmc.ZPlane(surface_id=24, z0=-2.15)
surf25 = openmc.ZPlane(surface_id=25, z0=2.15)
surf26 = openmc.ZPlane(surface_id=26, z0=6.45)
surf27 = openmc.ZPlane(surface_id=27, z0=10.75)
surf28 = openmc.ZPlane(surface_id=28, z0=15.05)
surf29 = openmc.ZPlane(surface_id=29, z0=19.35)
# Core region
surf30 = openmc.model.RectangularParallelepiped(-2.148, 2.148, -2.150, 2.150, -19.35, 19.35)
# x boundary
surf31 = openmc.XPlane(surface_id=31, x0=-1.074)
# x boundary
surf32 = openmc.XPlane(surface_id=32, x0=0.0)
# x boundary
surf33 = openmc.XPlane(surface_id=33, x0=1.074)
# Core region
surf40 = openmc.model.RectangularParallelepiped(-2.150, 2.150, -2.148, 2.148, -19.35, 19.35)
# y boundary
surf41 = openmc.YPlane(surface_id=41, y0=-1.074)
# y boundary
surf42 = openmc.YPlane(surface_id=42, y0=0.0)
# y boundary
surf43 = openmc.YPlane(surface_id=43, y0=1.074)
# y boundary
surf44 = openmc.YPlane(surface_id=44, y0=0.358)

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

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf11
u2_cell1 = openmc.Cell(fill=mat6)
u2_cell1.region = +surf11 & -surf12
u2_cell2 = openmc.Cell(fill=mat1)
u2_cell2.region = +surf12 & -surf13
u2_cell3 = openmc.Cell(fill=mat6)
u2_cell3.region = +surf13 & -surf14
u2_cell4 = openmc.Cell(fill=mat1)
u2_cell4.region = +surf14 & -surf15
u2_cell5 = openmc.Cell(fill=mat6)
u2_cell5.region = +surf15 & -surf16
u2_cell6 = openmc.Cell(fill=mat1)
u2_cell6.region = +surf16 & -surf17
u2_cell7 = openmc.Cell(fill=mat6)
u2_cell7.region = +surf17 & -surf18
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7])

# Lattice 4: 23x23 array
lattice4 = openmc.RectLattice(lattice_id=4)
lattice4.lower_left = [-52.555, -52.555]
lattice4.pitch = [4.570000, 4.570000]
lattice4.universes = [
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
    [universe1, universe1, universe1, universe1, universe1, universe128, universe116, universe32, universe116, universe127, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe134, universe116, universe32, universe32, universe32, universe116, universe146, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe140, universe116, universe32, universe116, universe32, universe117, universe32, universe116, universe142, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe144, universe32, universe116, universe32, universe32, universe116, universe32, universe116, universe32, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe32, universe116, universe32, universe116, universe32, universe117, universe32, universe116, universe32, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe144, universe32, universe116, universe32, universe32, universe116, universe32, universe32, universe116, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe136, universe116, universe32, universe116, universe32, universe117, universe32, universe116, universe138, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe130, universe116, universe32, universe116, universe32, universe116, universe132, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe126, universe116, universe32, universe116, universe125, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe4 = openmc.Universe(universe_id=4)
universe4.add_cell(openmc.Cell(fill=lattice4))

u32_cell0 = openmc.Cell(fill=mat2)
u32_cell0.region = -surf1 & -surf20
u32_cell1 = openmc.Cell(fill=mat2)
u32_cell1.region = -surf1 & +surf29
u32_cell2 = openmc.Cell(fill=mat4)
u32_cell2.region = +surf2 & -surf3
u32_cell3 = openmc.Cell(fill=mat5)
u32_cell3.region = +surf4 & -surf5
universe32 = openmc.Universe(universe_id=32, cells=[u32_cell0, u32_cell1, u32_cell2, u32_cell3])

universe116 = openmc.Universe(universe_id=116, cells=[])

universe117 = openmc.Universe(universe_id=117, cells=[])

u125_cell0 = openmc.Cell(fill=mat3)
u125_cell0.region = -surf40 & -surf32 & +surf42
u125_cell1 = openmc.Cell(fill=mat3)
u125_cell1.region = -surf40 & +surf32 & +surf41
universe125 = openmc.Universe(universe_id=125, cells=[u125_cell0, u125_cell1])

u126_cell0 = openmc.Cell(fill=mat3)
u126_cell0.region = -surf40 & -surf32 & +surf41
u126_cell1 = openmc.Cell(fill=mat3)
u126_cell1.region = -surf40 & +surf32 & +surf42
universe126 = openmc.Universe(universe_id=126, cells=[u126_cell0, u126_cell1])

u127_cell0 = openmc.Cell(fill=mat3)
u127_cell0.region = -surf40 & -surf32 & -surf42
u127_cell1 = openmc.Cell(fill=mat3)
u127_cell1.region = -surf40 & +surf32 & -surf43
universe127 = openmc.Universe(universe_id=127, cells=[u127_cell0, u127_cell1])

u128_cell0 = openmc.Cell(fill=mat3)
u128_cell0.region = -surf40 & -surf32 & -surf43
u128_cell1 = openmc.Cell(fill=mat3)
u128_cell1.region = -surf40 & +surf32 & -surf42
universe128 = openmc.Universe(universe_id=128, cells=[u128_cell0, u128_cell1])

u130_cell0 = openmc.Cell(fill=mat3)
u130_cell0.region = -surf40 & -surf32 & +surf42
universe130 = openmc.Universe(universe_id=130, cells=[u130_cell0])

u132_cell0 = openmc.Cell(fill=mat3)
u132_cell0.region = -surf30 & +surf32 & +surf42
universe132 = openmc.Universe(universe_id=132, cells=[u132_cell0])

u134_cell0 = openmc.Cell(fill=mat3)
u134_cell0.region = -surf40 & -surf32 & -surf42
universe134 = openmc.Universe(universe_id=134, cells=[u134_cell0])

u136_cell0 = openmc.Cell(fill=mat3)
u136_cell0.region = -surf40 & +surf32 & +surf43
u136_cell1 = openmc.Cell(fill=mat3)
u136_cell1.region = -surf40 & -surf32
universe136 = openmc.Universe(universe_id=136, cells=[u136_cell0, u136_cell1])

u138_cell0 = openmc.Cell(fill=mat3)
u138_cell0.region = -surf40 & -surf32 & +surf43
u138_cell1 = openmc.Cell(fill=mat3)
u138_cell1.region = -surf40 & +surf32
universe138 = openmc.Universe(universe_id=138, cells=[u138_cell0, u138_cell1])

u140_cell0 = openmc.Cell(fill=mat3)
u140_cell0.region = -surf40 & +surf32 & -surf41
u140_cell1 = openmc.Cell(fill=mat3)
u140_cell1.region = -surf40 & -surf32
universe140 = openmc.Universe(universe_id=140, cells=[u140_cell0, u140_cell1])

u142_cell0 = openmc.Cell(fill=mat3)
u142_cell0.region = -surf40 & -surf32 & -surf41
u142_cell1 = openmc.Cell(fill=mat3)
u142_cell1.region = -surf40 & +surf32
universe142 = openmc.Universe(universe_id=142, cells=[u142_cell0, u142_cell1])

u144_cell0 = openmc.Cell(fill=mat3)
u144_cell0.region = -surf30 & -surf31
universe144 = openmc.Universe(universe_id=144, cells=[u144_cell0])

u146_cell0 = openmc.Cell(fill=mat3)
u146_cell0.region = -surf40 & -surf32 & -surf44
u146_cell1 = openmc.Cell(fill=mat3)
u146_cell1.region = -surf40 & +surf32 & -surf43
universe146 = openmc.Universe(universe_id=146, cells=[u146_cell0, u146_cell1])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# FuArry
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = -surf10

# EndBlk
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf4 & -surf5

# Grpht
cell14 = openmc.Cell(cell_id=14, fill=mat6)
cell14.region = +surf17 & -surf18

root_universe = openmc.Universe(cells=[cell1, cell5, cell14])
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
