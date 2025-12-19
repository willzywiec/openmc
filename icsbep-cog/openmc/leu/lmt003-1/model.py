"""
LMT003-1: ZED-2 with 22.86 cm triangular pitch and Hc = 167.520 cm
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Uranium metal fuel
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 2.620100e-06)
mat1.add_nuclide("U235", 3.429900e-04)
mat1.add_nuclide("U238", 4.729200e-02)

# Heavy water (case 1)
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 4.039200e-04)
mat2.add_nuclide("H2", 6.605900e-02)
mat2.add_nuclide("O16", 3.311200e-02)
mat2.add_nuclide("O17", 1.993900e-05)
mat2.add_nuclide("O16", 9.969500e-05)
mat2.add_s_alpha_beta("c_H_in_H2O")
mat2.add_s_alpha_beta("c_D_in_D2O")

# Graphite
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Li", 2.418900e-08)
mat3.add_element("B", 2.740600e-09)
mat3.add_element("C", 8.222300e-02)
mat3.add_element("V", 5.816200e-07)
mat3.add_element("Gd", 1.256100e-10)

# Fuel
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Li", 1.756900e-06)
mat4.add_element("B", 1.052800e-06)
mat4.add_element("Al", 5.960100e-02)
mat4.add_element("Mn", 1.479800e-05)
mat4.add_element("Fe", 1.281000e-04)
mat4.add_element("Cu", 3.582200e-05)
mat4.add_element("Cd", 1.012500e-07)
mat4.add_element("Gd", 1.034000e-09)

# CR sheath, beams, hangers
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 1.767000e-02)
mat5.add_element("Mn", 1.173600e-03)
mat5.add_element("Fe", 6.024900e-02)
mat5.add_element("Ni", 7.621500e-03)

# Calandria, dump lines, SAR sheath, rod top enclosures
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Mg", 1.672500e-03)
mat6.add_element("Al", 5.822300e-02)
mat6.add_element("Cr", 7.817800e-05)
mat6.add_element("Mn", 1.973100e-05)
mat6.add_element("Fe", 7.763900e-05)

# Borated polyethylene
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("H1", 6.600000e-02)
mat7.add_element("B", 2.600000e-03)
mat7.add_element("C", 3.975300e-02)
mat7.add_s_alpha_beta("c_H_in_CH2")

# Concrete
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_nuclide("H1", 2.891900e-03)
mat8.add_element("C", 6.518000e-03)
mat8.add_nuclide("O16", 4.324800e-02)
mat8.add_element("Mg", 1.204200e-04)
mat8.add_element("Al", 2.656000e-04)
mat8.add_element("Si", 9.391600e-03)
mat8.add_element("S", 3.605400e-05)
mat8.add_element("Ca", 8.730100e-03)
mat8.add_element("Fe", 7.828600e-05)
mat8.add_s_alpha_beta("c_H_in_H2O")

# Heavy
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_nuclide("H1", 4.779900e-03)
mat9.add_element("C", 9.526300e-04)
mat9.add_nuclide("O16", 4.482900e-02)
mat9.add_element("Mg", 1.313200e-03)
mat9.add_element("Al", 1.674000e-03)
mat9.add_element("Si", 2.615900e-03)
mat9.add_element("Ca", 1.697900e-03)
mat9.add_element("Ti", 6.452300e-03)
mat9.add_element("Fe", 1.498900e-02)
mat9.add_s_alpha_beta("c_H_in_H2O")

# Air
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("H1", 4.958700e-07)
mat10.add_element("C", 9.421600e-09)
mat10.add_element("N", 3.871800e-05)
mat10.add_nuclide("O16", 1.065500e-05)
mat10.add_element("Ar", 2.315700e-07)
mat10.add_s_alpha_beta("c_H_in_H2O")

# Boron glue / masonite shielding
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_nuclide("H1", 3.682600e-02)
mat11.add_element("B", 1.638500e-03)
mat11.add_element("C", 1.922600e-02)
mat11.add_nuclide("O16", 2.166200e-02)
mat11.add_s_alpha_beta("c_H_in_H2O")

# Reactor well boron shielding
mat12 = openmc.Material(material_id=12)
mat12.set_density("sum")
mat12.add_element("B", 8.188400e-03)

# Cadmium SARS, control ring
mat13 = openmc.Material(material_id=13)
mat13.set_density("sum")
mat13.add_element("Cd", 4.634000e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11, mat12, mat13])

# ==============================================================================
# Geometry
# ==============================================================================

# Uranium
surf1 = openmc.ZCylinder(surface_id=1, x0=15.0, y0=304.741, r=1.62645)
# Gap
surf2 = openmc.ZCylinder(surface_id=2, x0=15.0, y0=306.053, r=1.6549)
# Sheath
surf3 = openmc.ZCylinder(surface_id=3, x0=14.53, y0=306.053, r=1.7549)
# Sheath
surf4 = openmc.ZCylinder(surface_id=4, x0=305.953, y0=306.053, r=2.115)
# D2O (Chime)
surf5 = openmc.ZCylinder(surface_id=5, x0=14.53, y0=14.85, r=1.5049)
# Boundary and rod top enclosure (top & sides)
surf6 = openmc.ZCylinder(surface_id=6, x0=14.53, y0=307.958, r=2.54)
# Rod top enclosure (bottom)
surf7 = openmc.ZPlane(surface_id=7, z0=304.048)
# D2O (Hc)
surf8 = openmc.ZPlane(surface_id=8, z0=167.520)
# Sheath, inner
surf11 = openmc.ZCylinder(surface_id=11, r=1.429)
# Cadmium, inner
surf12 = openmc.ZCylinder(surface_id=12, r=1.7085)
# Cadmium, outer
surf13 = openmc.ZCylinder(surface_id=13, r=1.746)
# Sheath, outer
surf14 = openmc.ZCylinder(surface_id=14, x0=279.14, y0=324.86, r=1.905)
# Steel beam offset -4 cm in y-direction
surf16 = openmc.model.RectangularParallelepiped(-200.422, 200.422, -6.54, -1.46, 366.42499999999995, 395.0)
# Steel hangers centered on rods
surf17 = openmc.ZCylinder(surface_id=17, x0=355.63, y0=402.38, r=1.425)
# Arbitrary volume enclosing the beams & hangers
surf18 = openmc.model.RectangularParallelepiped(-300.0, 300.0, -300.0, 300.0, 350.0, 410.0)
# D2O (lowest level)
surf20 = openmc.ZPlane(surface_id=20, z0=-207.0)
# Calendria, inner
surf21 = openmc.ZCylinder(surface_id=21, x0=0.0, y0=333.0, r=168.0)
# Calandria, outer
surf22 = openmc.ZCylinder(surface_id=22, x0=-2.69, y0=333.0, r=168.635)
# Lattice boundary
surf23 = openmc.model.RectangularParallelepiped(-120.015, 120.015, -108.88537, 108.88537, -499.95, 499.95)
# Dump line inner - 1st
surf24 = openmc.ZCylinder(surface_id=24, x0=129.54, y0=0.0, r=22.066)
# Dump line outer - 1st
surf25 = openmc.ZCylinder(surface_id=25, x0=129.54, y0=0.0, r=22.86)
# Dump line inner - 2nd
surf26 = openmc.ZCylinder(surface_id=26, x0=-64.77, y0=122.18, r=22.066)
# Dump line outer - 2nd
surf27 = openmc.ZCylinder(surface_id=27, x0=-64.77, y0=122.18, r=22.86)
# Dump line inner - 3rd
surf28 = openmc.ZCylinder(surface_id=28, x0=-64.77, y0=-122.18, r=22.066)
# Dump line outer - 3rd
surf29 = openmc.ZCylinder(surface_id=29, x0=-64.77, y0=-122.18, r=22.86)
# Casing, inner
surf31 = openmc.ZCylinder(surface_id=31, r=169.88)
# Cadmium, inner
surf32 = openmc.ZCylinder(surface_id=32, r=170.2)
# Cadmium, outer
surf33 = openmc.ZCylinder(surface_id=33, x0=308.6, y0=320.6, r=170.24)
# Casing, outer
surf34 = openmc.ZCylinder(surface_id=34, x0=307.6, y0=321.6, r=170.56)
# Graphite, inner
surf40 = openmc.ZCylinder(surface_id=40, x0=-2.69, y0=315.45, r=171.806)
# Graphite, inner
surf41 = openmc.ZCylinder(surface_id=41, x0=-92.69, y0=315.45, r=231.806)
# Dump line outer - 1st
surf42 = openmc.ZCylinder(surface_id=42, x0=129.54, y0=0.0, r=23.1775)
# Dump line outer - 2nd
surf43 = openmc.ZCylinder(surface_id=43, x0=-64.77, y0=122.18, r=23.1775)
# Dump line outer - 3rd
surf44 = openmc.ZCylinder(surface_id=44, x0=-64.77, y0=-122.18, r=23.1775)
# Detector hole - 1st
surf45 = openmc.ZCylinder(surface_id=45, x0=91.44, y0=0.0, r=7.1438)
# Detector hole - 2nd
surf46 = openmc.ZCylinder(surface_id=46, x0=0.0, y0=91.44, r=7.1438)
# Detector hole - 3rd
surf47 = openmc.ZCylinder(surface_id=47, x0=-91.44, y0=0.0, r=7.1438)
# Detector hole - 4th
surf48 = openmc.ZCylinder(surface_id=48, x0=0.0, y0=-91.44, r=7.1438)
# Detector hole - 5th
surf49 = openmc.ZCylinder(surface_id=49, x0=64.66, y0=-64.66, r=7.1438)
surf51 = openmc.model.RectangularParallelepiped(-200.422, 200.422, 132.04138, 137.12138, 366.42499999999995, 395.0)
surf52 = openmc.model.RectangularParallelepiped(-200.422, 200.422, 112.24404, 117.32404000000001, 366.42499999999995, 395.0)
surf53 = openmc.model.RectangularParallelepiped(-200.422, 200.422, 92.44669999999999, 97.5267, 366.42499999999995, 395.0)
surf54 = openmc.model.RectangularParallelepiped(-200.422, 200.422, 72.64935999999999, 77.72936, 366.42499999999995, 395.0)
surf55 = openmc.model.RectangularParallelepiped(-200.422, 200.422, 52.85202, 57.93202, 366.42499999999995, 395.0)
surf56 = openmc.model.RectangularParallelepiped(-200.422, 200.422, 33.05468, 38.134679999999996, 366.42499999999995, 395.0)
surf57 = openmc.model.RectangularParallelepiped(-200.422, 200.422, 13.25734, 18.33734, 366.42499999999995, 395.0)
surf58 = openmc.model.RectangularParallelepiped(-200.422, 200.422, -26.337339999999998, -21.25734, 366.42499999999995, 395.0)
surf59 = openmc.model.RectangularParallelepiped(-200.422, 200.422, -46.134679999999996, -41.05468, 366.42499999999995, 395.0)
surf60 = openmc.model.RectangularParallelepiped(-200.422, 200.422, -65.93202000000001, -60.85202, 366.42499999999995, 395.0)
surf61 = openmc.model.RectangularParallelepiped(-200.422, 200.422, -85.72936, -80.64935999999999, 366.42499999999995, 395.0)
surf62 = openmc.model.RectangularParallelepiped(-200.422, 200.422, -105.5267, -100.44669999999999, 366.42499999999995, 395.0)
surf63 = openmc.model.RectangularParallelepiped(-200.422, 200.422, -125.32404000000001, -120.24404, 366.42499999999995, 395.0)
# Interface between heavy & normal concrete
surf70 = openmc.ZPlane(surface_id=70, z0=-92.65)
# Concrete, inner
surf71 = openmc.model.RectangularParallelepiped(-320.04, 320.04, -320.04, 320.04, -332.69, 466.58)
# Concrete, outer
surf72 = openmc.model.RectangularParallelepiped(-365.76, 365.76, -365.76, 365.76, -363.17, 513.57)
# Large square hole in heavy concrete (on top)
surf73 = openmc.model.RectangularParallelepiped(-180.0225, 180.0225, -180.0225, 180.0225, 450.0, 520.0)
# Heavy concrete & borated concrete (on top)
surf74 = openmc.model.RectangularParallelepiped(-220.98, 220.98, -220.98, 220.98, -4999.95, 4999.95)
# Interface between heavy concrete & borated concrete
surf75 = openmc.ZPlane(surface_id=75, z0=551.57)
# Boron glue/masonite, upper
surf76 = openmc.model.RectangularParallelepiped(-327.66, 327.66, -327.66, 327.66, 451.34, 466.58)
# Boron glue/masonite, innermost
surf77 = openmc.model.RectangularParallelepiped(-304.8, 304.8, -304.8, 304.8, -4999.95, 4999.95)
surf78 = openmc.ZPlane(surface_id=78, z0=330.69)
# Boudnary condition
surf99 = openmc.model.RectangularParallelepiped(-365.76, 365.76, -365.76, 365.76, -363.17, 576.57, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf2
u1_cell1 = openmc.Cell()
u1_cell1.region = +surf1 & -surf2
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = +surf2 & -surf3 & +surf5
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = +surf3 & -surf4
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = +surf3 & +surf4 & -surf6 & +surf7
u1_cell5 = openmc.Cell(fill=mat10)
u1_cell5.region = +surf3 & +surf4 & -surf6 & -surf7 & +surf8
u1_cell6 = openmc.Cell(fill=mat2)
u1_cell6.region = +surf3 & +surf4 & -surf6 & -surf7 & -surf8
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = +surf2 & -surf3 & -surf5 & -surf8
u1_cell8 = openmc.Cell(fill=mat2)
u1_cell8.region = +surf6 & -surf8 & -surf99
u1_cell9 = openmc.Cell(fill=mat10)
u1_cell9.region = +surf6 & +surf8 & +surf16 & +surf17 & -surf99
u1_cell10 = openmc.Cell(fill=mat5)
u1_cell10.region = -surf16
u1_cell11 = openmc.Cell(fill=mat5)
u1_cell11.region = +surf16 & -surf17
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11])

u2_cell0 = openmc.Cell(fill=mat2)
u2_cell0.region = -surf8 & -surf11 & -surf14
u2_cell1 = openmc.Cell(fill=mat10)
u2_cell1.region = +surf8 & -surf11 & -surf14
u2_cell2 = openmc.Cell(fill=mat6)
u2_cell2.region = +surf11 & -surf12 & -surf14
u2_cell3 = openmc.Cell(fill=mat13)
u2_cell3.region = +surf12 & -surf13 & -surf14
u2_cell4 = openmc.Cell(fill=mat6)
u2_cell4.region = +surf13 & -surf14
u2_cell5 = openmc.Cell(fill=mat2)
u2_cell5.region = -surf8 & +surf14 & -surf99
u2_cell6 = openmc.Cell(fill=mat10)
u2_cell6.region = +surf8 & +surf14 & +surf16 & +surf17 & -surf99
u2_cell7 = openmc.Cell(fill=mat5)
u2_cell7.region = -surf16
u2_cell8 = openmc.Cell(fill=mat5)
u2_cell8.region = +surf16 & -surf17
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8])

u3_cell0 = openmc.Cell(fill=mat2)
u3_cell0.region = -surf8 & -surf99
u3_cell1 = openmc.Cell(fill=mat10)
u3_cell1.region = +surf8 & +surf16 & -surf99
u3_cell2 = openmc.Cell(fill=mat5)
u3_cell2.region = -surf16
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2])

# Lattice 4: 21x11 array
lattice4 = openmc.RectLattice(lattice_id=4)
lattice4.lower_left = [-120.015, -108.88537]
lattice4.pitch = [11.430000, 19.797340]
lattice4.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe1, universe2, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe2, universe1, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe1, universe2, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe2, universe1, universe3, universe3, universe3],
    [universe3, universe3, universe1, universe2, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe2, universe1, universe3, universe3],
    [universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3],
    [universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1],
    [universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3],
    [universe3, universe3, universe1, universe2, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe2, universe1, universe3, universe3],
    [universe3, universe3, universe3, universe1, universe2, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe2, universe1, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe1, universe2, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe2, universe1, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe1, universe3, universe3, universe3, universe3, universe3],
]
universe4 = openmc.Universe(universe_id=4)
universe4.add_cell(openmc.Cell(fill=lattice4))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Array
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = -surf21 & -surf22 & -surf23

# D2O
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = -surf8 & -surf21 & -surf22 & +surf23

# Air
cell3 = openmc.Cell(cell_id=3, fill=mat10)
cell3.region = +surf8 & -surf21 & -surf22 & +surf23

# D2O
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf21 & -surf22 & -surf24

# D2O
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf21 & -surf22 & -surf26

# D2O
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf21 & -surf22 & -surf28

# Calandria
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = +surf21 & -surf22 & +surf24 & +surf26 & +surf28

# Dumpline
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = +surf22 & +surf24 & -surf25

# Dumpline
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = +surf22 & +surf26 & -surf27

# Dumpline
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = +surf22 & +surf28 & -surf29

# D2O
cell11 = openmc.Cell(cell_id=11, fill=mat2)
cell11.region = +surf20 & +surf22 & -surf24 & -surf25

# D2O
cell12 = openmc.Cell(cell_id=12, fill=mat2)
cell12.region = +surf20 & +surf22 & -surf26 & -surf27

# D2O
cell13 = openmc.Cell(cell_id=13, fill=mat2)
cell13.region = +surf20 & +surf22 & -surf28 & -surf29

# Air
cell14 = openmc.Cell(cell_id=14, fill=mat10)
cell14.region = -surf20 & -surf24 & -surf25

# Air
cell15 = openmc.Cell(cell_id=15, fill=mat10)
cell15.region = -surf20 & -surf26 & -surf27

# Air
cell16 = openmc.Cell(cell_id=16, fill=mat10)
cell16.region = -surf20 & -surf28 & -surf29

# Sheath
cell17 = openmc.Cell(cell_id=17, fill=mat5)
cell17.region = +surf31 & -surf32 & -surf33

# Cd
cell18 = openmc.Cell(cell_id=18, fill=mat13)
cell18.region = +surf32 & -surf33

# Sheath
cell19 = openmc.Cell(cell_id=19, fill=mat5)
cell19.region = +surf31 & +surf33 & -surf34

# Graphite
cell20 = openmc.Cell(cell_id=20, fill=mat3)
cell20.region = +surf22 & +surf40 & -surf41 & +surf42 & +surf43 & +surf44 & +surf45 & +surf46 & +surf47 & +surf48 & +surf49

# Array
cell21 = openmc.Cell(cell_id=21, fill=universe4)
cell21.region = -surf18 & -surf23

# Steel
cell22 = openmc.Cell(cell_id=22, fill=mat5)
cell22.region = -surf18 & +surf23 & -surf51

# Steel
cell23 = openmc.Cell(cell_id=23, fill=mat5)
cell23.region = -surf18 & +surf23 & -surf52

# Steel
cell24 = openmc.Cell(cell_id=24, fill=mat5)
cell24.region = -surf18 & +surf23 & -surf53

# Steel
cell25 = openmc.Cell(cell_id=25, fill=mat5)
cell25.region = -surf18 & +surf23 & -surf54

# Steel
cell26 = openmc.Cell(cell_id=26, fill=mat5)
cell26.region = -surf18 & +surf23 & -surf55

# Steel
cell27 = openmc.Cell(cell_id=27, fill=mat5)
cell27.region = -surf18 & +surf23 & -surf56

# Steel
cell28 = openmc.Cell(cell_id=28, fill=mat5)
cell28.region = -surf18 & +surf23 & -surf57

# Steel
cell29 = openmc.Cell(cell_id=29, fill=mat5)
cell29.region = -surf18 & +surf23 & -surf16

# Steel
cell30 = openmc.Cell(cell_id=30, fill=mat5)
cell30.region = -surf18 & +surf23 & -surf58

# Steel
cell31 = openmc.Cell(cell_id=31, fill=mat5)
cell31.region = -surf18 & +surf23 & -surf59

# Steel
cell32 = openmc.Cell(cell_id=32, fill=mat5)
cell32.region = -surf18 & +surf23 & -surf60

# Steel
cell33 = openmc.Cell(cell_id=33, fill=mat5)
cell33.region = -surf18 & +surf23 & -surf61

# Steel
cell34 = openmc.Cell(cell_id=34, fill=mat5)
cell34.region = -surf18 & +surf23 & -surf62

# Steel
cell35 = openmc.Cell(cell_id=35, fill=mat5)
cell35.region = -surf18 & +surf23 & -surf63

# Normal
cell36 = openmc.Cell(cell_id=36, fill=mat8)
cell36.region = -surf99 & -surf70 & +surf71 & -surf72 & +surf42 & +surf43 & +surf44

# Heavy
cell37 = openmc.Cell(cell_id=37, fill=mat9)
cell37.region = -surf99 & +surf70 & +surf71 & -surf72 & +surf73 & +surf76 & +surf42 & +surf43 & +surf44

# B+CH2
cell38 = openmc.Cell(cell_id=38, fill=mat7)
cell38.region = -surf99 & +surf72 & -surf74 & -surf75

# Heavy
cell39 = openmc.Cell(cell_id=39, fill=mat9)
cell39.region = -surf99 & +surf72 & -surf74 & +surf75

# B+GLUE
cell40 = openmc.Cell(cell_id=40, fill=mat11)
cell40.region = +surf73 & -surf76

# B+GLUE
cell41 = openmc.Cell(cell_id=41, fill=mat11)
cell41.region = -surf71 & +surf76 & +surf77 & +surf78

# Hanger
cell54 = openmc.Cell(cell_id=54, fill=mat5)
cell54.region = +surf16 & -surf17

# Hanger
cell64 = openmc.Cell(cell_id=64, fill=mat5)
cell64.region = +surf16 & -surf17

# Beam
cell68 = openmc.Cell(cell_id=68, fill=mat5)
cell68.region = -surf16

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell54, cell64, cell68])
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
source.space = openmc.stats.Point((0.0, 0.0, 91.26))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
