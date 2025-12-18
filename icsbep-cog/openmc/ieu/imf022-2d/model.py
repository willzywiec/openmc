"""
IEU-MET-FAST-022-2: FR0 experiment 5-D (case 2 detailed model
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

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

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
surf31 = openmc.YPlane(surface_id=31, y0=-1.790)
# y boundaries
surf32 = openmc.YPlane(surface_id=32, y0=-1.7005)
surf33 = openmc.YPlane(surface_id=33, y0=-1.3425)
surf34 = openmc.YPlane(surface_id=34, y0=-0.9845)
surf35 = openmc.YPlane(surface_id=35, y0=-0.895)
surf36 = openmc.YPlane(surface_id=36, y0=-0.1790)
surf37 = openmc.YPlane(surface_id=37, y0=0.1790)
surf38 = openmc.YPlane(surface_id=38, y0=0.2685)
surf39 = openmc.YPlane(surface_id=39, y0=0.9845)
surf40 = openmc.YPlane(surface_id=40, y0=1.3425)
surf41 = openmc.YPlane(surface_id=41, y0=1.432)
# Even module
surf42 = openmc.YPlane(surface_id=42, y0=-2.0585)
# y boundaries
surf43 = openmc.YPlane(surface_id=43, y0=-1.7005)
surf44 = openmc.YPlane(surface_id=44, y0=-1.3425)
surf45 = openmc.YPlane(surface_id=45, y0=-1.253)
surf46 = openmc.YPlane(surface_id=46, y0=-0.537)
surf47 = openmc.YPlane(surface_id=47, y0=-0.1790)
surf48 = openmc.YPlane(surface_id=48, y0=-0.0895)
surf49 = openmc.YPlane(surface_id=49, y0=0.6265)
surf50 = openmc.YPlane(surface_id=50, y0=0.9845)
surf51 = openmc.YPlane(surface_id=51, y0=1.074)
surf52 = openmc.YPlane(surface_id=52, y0=1.790)
# Odd module -
surf61 = openmc.XPlane(surface_id=61, x0=0.0)
# half-filled element
surf62 = openmc.XPlane(surface_id=62, x0=0.358)
# x boundaries
surf63 = openmc.XPlane(surface_id=63, x0=0.4475)
surf64 = openmc.XPlane(surface_id=64, x0=0.8055)
surf65 = openmc.XPlane(surface_id=65, x0=1.5215)
surf66 = openmc.XPlane(surface_id=66, x0=1.611)
surf67 = openmc.XPlane(surface_id=67, x0=1.790)
# Even module -
surf71 = openmc.XPlane(surface_id=71, x0=0.0)
# half-filled element
surf72 = openmc.XPlane(surface_id=72, x0=0.1790)
# x boundaries
surf73 = openmc.XPlane(surface_id=73, x0=0.2685)
surf74 = openmc.XPlane(surface_id=74, x0=0.6265)
surf75 = openmc.XPlane(surface_id=75, x0=0.9845)
surf76 = openmc.XPlane(surface_id=76, x0=1.3425)
surf77 = openmc.XPlane(surface_id=77, x0=1.432)
surf78 = openmc.XPlane(surface_id=78, x0=1.790)
# Even module -
surf81 = openmc.XPlane(surface_id=81, x0=0.0)
# quarter-filled element
surf82 = openmc.XPlane(surface_id=82, x0=0.358)
# x boundaries
surf83 = openmc.XPlane(surface_id=83, x0=1.074)
surf84 = openmc.XPlane(surface_id=84, x0=1.432)
# Odd module -
surf91 = openmc.XPlane(surface_id=91, x0=0.0)
# quarter-filled element
surf92 = openmc.XPlane(surface_id=92, x0=0.0895)
# x boundaries
surf93 = openmc.XPlane(surface_id=93, x0=0.8055)
surf94 = openmc.XPlane(surface_id=94, x0=0.895)
surf95 = openmc.XPlane(surface_id=95, x0=1.253)
surf96 = openmc.XPlane(surface_id=96, x0=1.3425)
surf97 = openmc.XPlane(surface_id=97, x0=1.7005)
surf98 = openmc.XPlane(surface_id=98, x0=1.790)
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

u2_cell0 = openmc.Cell(fill=mat6)
u2_cell0.region = -surf30 & -surf31
u2_cell1 = openmc.Cell(fill=mat7)
u2_cell1.region = -surf30 & +surf31 & -surf32
u2_cell2 = openmc.Cell(fill=mat1)
u2_cell2.region = -surf30 & +surf32 & -surf33
u2_cell3 = openmc.Cell(fill=mat6)
u2_cell3.region = -surf30 & +surf33 & -surf34
u2_cell4 = openmc.Cell(fill=mat7)
u2_cell4.region = -surf30 & +surf34 & -surf35
u2_cell5 = openmc.Cell(fill=mat1)
u2_cell5.region = -surf30 & +surf35 & -surf36
u2_cell6 = openmc.Cell(fill=mat6)
u2_cell6.region = -surf30 & +surf36 & -surf37
u2_cell7 = openmc.Cell(fill=mat7)
u2_cell7.region = -surf30 & +surf37 & -surf38
u2_cell8 = openmc.Cell(fill=mat1)
u2_cell8.region = -surf30 & +surf38 & -surf39
u2_cell9 = openmc.Cell(fill=mat6)
u2_cell9.region = -surf30 & +surf39 & -surf40
u2_cell10 = openmc.Cell(fill=mat7)
u2_cell10.region = -surf30 & +surf40 & -surf41
u2_cell11 = openmc.Cell(fill=mat1)
u2_cell11.region = -surf30 & +surf41
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8, u2_cell9, u2_cell10, u2_cell11])

u3_cell0 = openmc.Cell(fill=mat7)
u3_cell0.region = -surf30 & -surf42
u3_cell1 = openmc.Cell(fill=mat1)
u3_cell1.region = -surf30 & +surf42 & -surf43
u3_cell2 = openmc.Cell(fill=mat6)
u3_cell2.region = -surf30 & +surf43 & -surf44
u3_cell3 = openmc.Cell(fill=mat7)
u3_cell3.region = -surf30 & +surf44 & -surf45
u3_cell4 = openmc.Cell(fill=mat1)
u3_cell4.region = -surf30 & +surf45 & -surf46
u3_cell5 = openmc.Cell(fill=mat6)
u3_cell5.region = -surf30 & +surf46 & -surf47
u3_cell6 = openmc.Cell(fill=mat7)
u3_cell6.region = -surf30 & +surf47 & -surf48
u3_cell7 = openmc.Cell(fill=mat1)
u3_cell7.region = -surf30 & +surf48 & -surf49
u3_cell8 = openmc.Cell(fill=mat6)
u3_cell8.region = -surf30 & +surf49 & -surf50
u3_cell9 = openmc.Cell(fill=mat7)
u3_cell9.region = -surf30 & +surf50 & -surf51
u3_cell10 = openmc.Cell(fill=mat1)
u3_cell10.region = -surf30 & +surf51 & -surf52
u3_cell11 = openmc.Cell(fill=mat6)
u3_cell11.region = -surf30 & +surf52
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5, u3_cell6, u3_cell7, u3_cell8, u3_cell9, u3_cell10, u3_cell11])

u4_cell0 = openmc.Cell(fill=mat3)
u4_cell0.region = -surf11 & -surf61
u4_cell1 = openmc.Cell(fill=mat1)
u4_cell1.region = -surf11 & +surf61 & -surf62
u4_cell2 = openmc.Cell(fill=mat7)
u4_cell2.region = -surf11 & +surf62 & -surf63
u4_cell3 = openmc.Cell(fill=mat6)
u4_cell3.region = -surf11 & +surf63 & -surf64
u4_cell4 = openmc.Cell(fill=mat1)
u4_cell4.region = -surf11 & +surf64 & -surf65
u4_cell5 = openmc.Cell(fill=mat7)
u4_cell5.region = -surf11 & +surf65 & -surf66
u4_cell6 = openmc.Cell(fill=mat6)
u4_cell6.region = -surf11 & +surf66 & -surf67
u4_cell7 = openmc.Cell(fill=mat1)
u4_cell7.region = -surf11 & +surf67
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4, u4_cell5, u4_cell6, u4_cell7])

u5_cell0 = openmc.Cell(fill=mat3)
u5_cell0.region = -surf11 & -surf71
u5_cell1 = openmc.Cell(fill=mat6)
u5_cell1.region = -surf11 & +surf71 & -surf72
u5_cell2 = openmc.Cell(fill=mat7)
u5_cell2.region = -surf11 & +surf72 & -surf73
u5_cell3 = openmc.Cell(fill=mat1)
u5_cell3.region = -surf11 & +surf73 & -surf74
u5_cell4 = openmc.Cell(fill=mat6)
u5_cell4.region = -surf11 & +surf74 & -surf75
u5_cell5 = openmc.Cell(fill=mat1)
u5_cell5.region = -surf11 & +surf75 & -surf76
u5_cell6 = openmc.Cell(fill=mat7)
u5_cell6.region = -surf11 & +surf76 & -surf77
u5_cell7 = openmc.Cell(fill=mat6)
u5_cell7.region = -surf11 & +surf77 & -surf78
u5_cell8 = openmc.Cell(fill=mat1)
u5_cell8.region = -surf11 & +surf78
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0, u5_cell1, u5_cell2, u5_cell3, u5_cell4, u5_cell5, u5_cell6, u5_cell7, u5_cell8])

u7_cell0 = openmc.Cell(fill=mat3)
u7_cell0.region = -surf11 & -surf81
u7_cell1 = openmc.Cell(fill=mat6)
u7_cell1.region = -surf11 & +surf81 & -surf82
u7_cell2 = openmc.Cell(fill=mat1)
u7_cell2.region = -surf11 & +surf82 & -surf83
u7_cell3 = openmc.Cell(fill=mat6)
u7_cell3.region = -surf11 & +surf83 & -surf84
u7_cell4 = openmc.Cell(fill=mat1)
u7_cell4.region = -surf11 & +surf84
universe7 = openmc.Universe(universe_id=7, cells=[u7_cell0, u7_cell1, u7_cell2, u7_cell3, u7_cell4])

u8_cell0 = openmc.Cell(fill=mat3)
u8_cell0.region = -surf11 & -surf91
u8_cell1 = openmc.Cell(fill=mat7)
u8_cell1.region = -surf11 & +surf91 & -surf92
u8_cell2 = openmc.Cell(fill=mat1)
u8_cell2.region = -surf11 & +surf92 & -surf93
u8_cell3 = openmc.Cell(fill=mat7)
u8_cell3.region = -surf11 & +surf93 & -surf94
u8_cell4 = openmc.Cell(fill=mat6)
u8_cell4.region = -surf11 & +surf94 & -surf95
u8_cell5 = openmc.Cell(fill=mat7)
u8_cell5.region = -surf11 & +surf95 & -surf96
u8_cell6 = openmc.Cell(fill=mat1)
u8_cell6.region = -surf11 & +surf96 & -surf97
u8_cell7 = openmc.Cell(fill=mat7)
u8_cell7.region = -surf11 & +surf97 & -surf98
u8_cell8 = openmc.Cell(fill=mat6)
u8_cell8.region = -surf11 & +surf98
universe8 = openmc.Universe(universe_id=8, cells=[u8_cell0, u8_cell1, u8_cell2, u8_cell3, u8_cell4, u8_cell5, u8_cell6, u8_cell7, u8_cell8])

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
    [universe1, universe1, universe1, universe1, universe1, universe1, universe170, universe198, universe174, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe117, universe117, universe32, universe117, universe32, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe32, universe117, universe32, universe117, universe32, universe117, universe32, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe186, universe117, universe117, universe117, universe32, universe117, universe32, universe117, universe190, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe202, universe32, universe117, universe32, universe117, universe32, universe117, universe32, universe206, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe178, universe117, universe117, universe117, universe32, universe117, universe32, universe117, universe182, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe32, universe117, universe32, universe117, universe32, universe117, universe32, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe32, universe117, universe32, universe117, universe32, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe166, universe194, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
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

universe166 = openmc.Universe(universe_id=166, cells=[])

universe170 = openmc.Universe(universe_id=170, cells=[])

universe174 = openmc.Universe(universe_id=174, cells=[])

u178_cell0 = openmc.Cell(fill=mat2)
u178_cell0.region = -surf1 & -surf20
u178_cell1 = openmc.Cell(fill=mat3)
u178_cell1.region = -surf1 & +surf20 & -surf29 & -surf71
u178_cell2 = openmc.Cell(fill=mat3)
u178_cell2.region = -surf1 & +surf20 & -surf29 & +surf71 & +surf99
u178_cell3 = openmc.Cell(fill=mat2)
u178_cell3.region = -surf1 & +surf29
u178_cell4 = openmc.Cell(fill=mat4)
u178_cell4.region = +surf2 & -surf3
u178_cell5 = openmc.Cell(fill=mat5)
u178_cell5.region = +surf4 & -surf5
universe178 = openmc.Universe(universe_id=178, cells=[u178_cell0, u178_cell1, u178_cell2, u178_cell3, u178_cell4, u178_cell5])

universe182 = openmc.Universe(universe_id=182, cells=[])

u186_cell0 = openmc.Cell(fill=mat2)
u186_cell0.region = -surf1 & -surf20
u186_cell1 = openmc.Cell(fill=mat3)
u186_cell1.region = -surf1 & +surf20 & -surf29 & -surf71
u186_cell2 = openmc.Cell(fill=mat3)
u186_cell2.region = -surf1 & +surf20 & -surf29 & +surf71 & -surf99
u186_cell3 = openmc.Cell(fill=mat2)
u186_cell3.region = -surf1 & +surf29
u186_cell4 = openmc.Cell(fill=mat4)
u186_cell4.region = +surf2 & -surf3
u186_cell5 = openmc.Cell(fill=mat5)
u186_cell5.region = +surf4 & -surf5
universe186 = openmc.Universe(universe_id=186, cells=[u186_cell0, u186_cell1, u186_cell2, u186_cell3, u186_cell4, u186_cell5])

universe190 = openmc.Universe(universe_id=190, cells=[])

universe194 = openmc.Universe(universe_id=194, cells=[])

universe198 = openmc.Universe(universe_id=198, cells=[])

u202_cell0 = openmc.Cell(fill=mat2)
u202_cell0.region = -surf1 & -surf20
u202_cell1 = openmc.Cell(fill=mat2)
u202_cell1.region = -surf1 & +surf29
u202_cell2 = openmc.Cell(fill=mat4)
u202_cell2.region = +surf2 & -surf3
u202_cell3 = openmc.Cell(fill=mat5)
u202_cell3.region = +surf4 & -surf5
universe202 = openmc.Universe(universe_id=202, cells=[u202_cell0, u202_cell1, u202_cell2, u202_cell3])

universe206 = openmc.Universe(universe_id=206, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# FuArry
cell1 = openmc.Cell(cell_id=1, fill=universe9)
cell1.region = -surf10

# EndBlk
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf4 & -surf5

# Fuel
cell18 = openmc.Cell(cell_id=18, fill=mat1)
cell18.region = -surf30 & +surf41

# Grpht
cell31 = openmc.Cell(cell_id=31, fill=mat6)
cell31.region = -surf30 & +surf52

# Fuel
cell40 = openmc.Cell(cell_id=40, fill=mat1)
cell40.region = -surf11 & +surf67

# Fuel
cell50 = openmc.Cell(cell_id=50, fill=mat1)
cell50.region = -surf11 & +surf78

# Fuel
cell56 = openmc.Cell(cell_id=56, fill=mat1)
cell56.region = -surf11 & +surf84

# Grpht
cell66 = openmc.Cell(cell_id=66, fill=mat6)
cell66.region = -surf11 & +surf98

# EndBlk
cell71 = openmc.Cell(cell_id=71, fill=mat5)
cell71.region = +surf4 & -surf5

# R-90
cell72 = openmc.Cell(cell_id=72, fill=universe32)
cell72.translation = (0.0, 0.0, 0.0)
cell72.region = -surf5

# R-90
cell73 = openmc.Cell(cell_id=73, fill=universe186)
cell73.translation = (0.0, 0.0, 0.0)
cell73.region = -surf5

# R+90
cell74 = openmc.Cell(cell_id=74, fill=universe178)
cell74.translation = (0.0, 0.0, 0.0)
cell74.region = -surf5

# R+90
cell75 = openmc.Cell(cell_id=75, fill=universe186)
cell75.translation = (0.0, 0.0, 0.0)
cell75.region = -surf5

# EndBlk
cell82 = openmc.Cell(cell_id=82, fill=mat5)
cell82.region = +surf4 & -surf5

# R180
cell83 = openmc.Cell(cell_id=83, fill=universe186)
cell83.translation = (0.0, 0.0, 0.0)
cell83.region = -surf5

# EndBlk
cell90 = openmc.Cell(cell_id=90, fill=mat5)
cell90.region = +surf4 & -surf5

# R180
cell91 = openmc.Cell(cell_id=91, fill=universe178)
cell91.translation = (0.0, 0.0, 0.0)
cell91.region = -surf5

# R-90
cell92 = openmc.Cell(cell_id=92, fill=universe202)
cell92.translation = (0.0, 0.0, 0.0)
cell92.region = -surf5

# R+90
cell93 = openmc.Cell(cell_id=93, fill=universe202)
cell93.translation = (0.0, 0.0, 0.0)
cell93.region = -surf5

# EndBlk
cell98 = openmc.Cell(cell_id=98, fill=mat5)
cell98.region = +surf4 & -surf5

# R180
cell99 = openmc.Cell(cell_id=99, fill=universe202)
cell99.translation = (0.0, 0.0, 0.0)
cell99.region = -surf5

root_universe = openmc.Universe(cells=[cell1, cell5, cell18, cell31, cell40, cell50, cell56, cell66, cell71, cell72, cell73, cell74, cell75, cell82, cell83, cell90, cell91, cell92, cell93, cell98, cell99])
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
