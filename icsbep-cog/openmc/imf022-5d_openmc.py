"""
IEU-MET-FAST-022-5: FR0 experiment 8-D (case 5 detailed model
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

# Polyethylene
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("H1", 8.120500e-02)
mat7.add_element("C", 4.060200e-02)
mat7.add_s_alpha_beta("c_H_in_CH2")

# Aluminum
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Al", 5.653800e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat9])

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
# Core region boundary
surf11 = openmc.model.RectangularParallelepiped(-2.148, 2.148, -2.150, 2.150, -19.35, 19.35)
# Axial boundaries
surf20 = openmc.ZPlane(surface_id=20, z0=-19.35)
# for the core region
surf21 = openmc.ZPlane(surface_id=21, z0=-15.05)
surf22 = openmc.ZPlane(surface_id=22, z0=-10.75)
surf23 = openmc.ZPlane(surface_id=23, z0=-6.45)
surf24 = openmc.ZPlane(surface_id=24, z0=-2.15)
surf25 = openmc.ZPlane(surface_id=25, z0=2.15)
surf26 = openmc.ZPlane(surface_id=26, z0=6.45)
surf27 = openmc.ZPlane(surface_id=27, z0=10.75)
surf28 = openmc.ZPlane(surface_id=28, z0=15.05)
surf29 = openmc.ZPlane(surface_id=29, z0=19.35)
# Core region boundary
surf30 = openmc.model.RectangularParallelepiped(-2.150, 2.150, -2.148, 2.148, -19.35, 19.35)
# Odd module
surf31 = openmc.YPlane(surface_id=31, y0=-2.0413)
# y boundaries
surf32 = openmc.YPlane(surface_id=32, y0=-1.6833)
surf33 = openmc.YPlane(surface_id=33, y0=-1.3253)
surf34 = openmc.YPlane(surface_id=34, y0=-0.9673)
surf35 = openmc.YPlane(surface_id=35, y0=-0.2513)
surf36 = openmc.YPlane(surface_id=36, y0=0.1067)
surf37 = openmc.YPlane(surface_id=37, y0=0.2667)
surf38 = openmc.YPlane(surface_id=38, y0=0.9827)
surf39 = openmc.YPlane(surface_id=39, y0=1.3407)
surf40 = openmc.YPlane(surface_id=40, y0=1.4302)
surf41 = openmc.YPlane(surface_id=41, y0=2.1462)
# Even module
surf42 = openmc.YPlane(surface_id=42, y0=-1.790)
# y boundaries
surf43 = openmc.YPlane(surface_id=43, y0=-1.432)
surf44 = openmc.YPlane(surface_id=44, y0=-0.716)
surf45 = openmc.YPlane(surface_id=45, y0=-0.358)
surf46 = openmc.YPlane(surface_id=46, y0=-0.198)
surf47 = openmc.YPlane(surface_id=47, y0=0.518)
surf48 = openmc.YPlane(surface_id=48, y0=0.876)
surf49 = openmc.YPlane(surface_id=49, y0=0.9655)
surf50 = openmc.YPlane(surface_id=50, y0=1.6815)
surf51 = openmc.YPlane(surface_id=51, y0=1.7882)
surf52 = openmc.YPlane(surface_id=52, y0=2.1462)
surf99 = openmc.YPlane(surface_id=99, y0=0.0)

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

u2_cell0 = openmc.Cell(fill=mat9)
u2_cell0.region = -surf30 & -surf31
u2_cell1 = openmc.Cell(fill=mat6)
u2_cell1.region = -surf30 & +surf31 & -surf32
u2_cell2 = openmc.Cell(fill=mat1)
u2_cell2.region = -surf30 & +surf32 & -surf33
u2_cell3 = openmc.Cell(fill=mat6)
u2_cell3.region = -surf30 & +surf33 & -surf34
u2_cell4 = openmc.Cell(fill=mat1)
u2_cell4.region = -surf30 & +surf34 & -surf35
u2_cell5 = openmc.Cell(fill=mat6)
u2_cell5.region = -surf30 & +surf35 & -surf36
u2_cell6 = openmc.Cell(fill=mat9)
u2_cell6.region = -surf30 & +surf36 & -surf37
u2_cell7 = openmc.Cell(fill=mat1)
u2_cell7.region = -surf30 & +surf37 & -surf38
u2_cell8 = openmc.Cell(fill=mat6)
u2_cell8.region = -surf30 & +surf38 & -surf39
u2_cell9 = openmc.Cell(fill=mat7)
u2_cell9.region = -surf30 & +surf39 & -surf40
u2_cell10 = openmc.Cell(fill=mat1)
u2_cell10.region = -surf30 & +surf40 & -surf41
u2_cell11 = openmc.Cell()
u2_cell11.region = -surf30 & +surf41
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8, u2_cell9, u2_cell10, u2_cell11])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = -surf30 & -surf42
u3_cell1 = openmc.Cell(fill=mat6)
u3_cell1.region = -surf30 & +surf42 & -surf43
u3_cell2 = openmc.Cell(fill=mat1)
u3_cell2.region = -surf30 & +surf43 & -surf44
u3_cell3 = openmc.Cell(fill=mat6)
u3_cell3.region = -surf30 & +surf44 & -surf45
u3_cell4 = openmc.Cell(fill=mat9)
u3_cell4.region = -surf30 & +surf45 & -surf46
u3_cell5 = openmc.Cell(fill=mat1)
u3_cell5.region = -surf30 & +surf46 & -surf47
u3_cell6 = openmc.Cell(fill=mat6)
u3_cell6.region = -surf30 & +surf47 & -surf48
u3_cell7 = openmc.Cell(fill=mat7)
u3_cell7.region = -surf30 & +surf48 & -surf49
u3_cell8 = openmc.Cell(fill=mat1)
u3_cell8.region = -surf30 & +surf49 & -surf50
u3_cell9 = openmc.Cell(fill=mat9)
u3_cell9.region = -surf30 & +surf50 & -surf51
u3_cell10 = openmc.Cell(fill=mat6)
u3_cell10.region = -surf30 & +surf51 & -surf52
u3_cell11 = openmc.Cell()
u3_cell11.region = -surf30 & +surf52
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5, u3_cell6, u3_cell7, u3_cell8, u3_cell9, u3_cell10, u3_cell11])

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
    [universe1, universe1, universe1, universe1, universe1, universe117, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe117, universe32, universe32, universe117, universe32, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe117, universe32, universe117, universe117, universe32, universe117, universe32, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe117, universe32, universe117, universe32, universe32, universe117, universe32, universe117, universe32, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe32, universe117, universe32, universe117, universe117, universe32, universe117, universe32, universe117, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe117, universe32, universe117, universe32, universe32, universe117, universe32, universe117, universe32, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe32, universe117, universe32, universe117, universe117, universe32, universe117, universe32, universe117, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe117, universe32, universe117, universe32, universe32, universe117, universe32, universe117, universe32, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe117, universe32, universe117, universe117, universe32, universe117, universe32, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe117, universe32, universe32, universe117, universe32, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe117, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe9 = openmc.Universe(universe_id=9)
universe9.add_cell(openmc.Cell(fill=lattice9))

u32_cell0 = openmc.Cell(fill=mat2)
u32_cell0.region = -surf1 & -surf20
u32_cell1 = openmc.Cell(fill=mat2)
u32_cell1.region = -surf1 & +surf29
u32_cell2 = openmc.Cell(fill=mat4)
u32_cell2.region = +surf2 & -surf3
u32_cell3 = openmc.Cell(fill=mat5)
u32_cell3.region = +surf4 & -surf5
universe32 = openmc.Universe(universe_id=32, cells=[u32_cell0, u32_cell1, u32_cell2, u32_cell3])

universe117 = openmc.Universe(universe_id=117, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# FuArry
cell1 = openmc.Cell(cell_id=1, fill=universe9)
cell1.region = -surf10

# EndBlk
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf4 & -surf5

# Void
cell18 = openmc.Cell(cell_id=18)
cell18.region = -surf30 & +surf41

# Void
cell31 = openmc.Cell(cell_id=31)
cell31.region = -surf30 & +surf52

# EndBlk
cell36 = openmc.Cell(cell_id=36, fill=mat5)
cell36.region = +surf4 & -surf5

# R+90
cell37 = openmc.Cell(cell_id=37, fill=universe32)
cell37.translation = (0.0, 0.0, 0.0)
cell37.region = -surf5

root_universe = openmc.Universe(cells=[cell1, cell5, cell18, cell31, cell36, cell37])
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
