"""
LCT063-2: DIMPLE S06C/1
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(3)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.531200e-06)
mat1.add_nuclide("U235", 7.065400e-04)
mat1.add_nuclide("U236", 9.650000e-06)
mat1.add_nuclide("U238", 2.250100e-02)
mat1.add_element("Al", 6.628200e-05)
mat1.add_element("Fe", 8.988900e-06)
mat1.add_nuclide("O16", 4.664100e-02)
mat1.add_element("Si", 2.591700e-05)

# Wrapper/
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 1.641800e-02)
mat2.add_element("C", 5.553100e-03)
mat2.add_element("Cl", 7.372000e-07)
mat2.add_element("Cr", 2.513300e-07)
mat2.add_element("Cu", 1.233900e-06)
mat2.add_element("Fe", 2.807900e-05)
mat2.add_element("H", 1.104700e-02)
mat2.add_element("Mg", 3.226000e-07)
mat2.add_element("Mn", 5.708800e-07)
mat2.add_element("Ni", 1.781300e-07)
mat2.add_element("Si", 4.652900e-06)
mat2.add_element("Sn", 3.963000e-07)
mat2.add_element("Sr", 5.965700e-09)

# Clad
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 4.285900e-04)
mat3.add_element("Co", 8.136100e-05)
mat3.add_element("Cr", 1.627300e-02)
mat3.add_element("Cu", 1.124400e-04)
mat3.add_element("Fe", 5.686100e-02)
mat3.add_element("Mn", 1.420400e-03)
mat3.add_element("Mo", 1.665900e-04)
mat3.add_element("Ni", 8.954800e-03)
mat3.add_element("Ti", 6.538800e-04)
mat3.add_element("V", 4.614000e-05)
mat3.add_element("Zn", 3.738300e-05)

# Upper
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 3.506400e-02)
mat4.add_element("Cu", 7.126500e-07)
mat4.add_element("Fe", 4.691100e-05)
mat4.add_element("Mg", 4.769900e-04)
mat4.add_element("Mn", 3.039400e-05)
mat4.add_element("Ni", 9.193700e-07)
mat4.add_element("Si", 5.026000e-05)
mat4.add_element("Ti", 1.147100e-06)

# Lower
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 3.577600e-02)
mat5.add_element("Cu", 1.121700e-06)
mat5.add_element("Fe", 3.900100e-05)
mat5.add_element("Mg", 7.495000e-04)
mat5.add_element("Mn", 4.775500e-05)
mat5.add_element("Ni", 1.433900e-06)
mat5.add_element("Si", 5.287600e-05)
mat5.add_element("Ti", 1.798900e-06)

# Dowel
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Co", 7.755900e-05)
mat6.add_element("Cr", 1.185000e-02)
mat6.add_element("Cu", 1.611200e-04)
mat6.add_element("Fe", 4.617000e-02)
mat6.add_element("Mn", 7.787400e-04)
mat6.add_element("Mo", 1.619800e-04)
mat6.add_element("Ni", 6.012300e-03)
mat6.add_element("S", 7.981400e-05)
mat6.add_element("Si", 5.533300e-04)
mat6.add_element("Ti", 3.360300e-04)
mat6.add_element("Zn", 2.796000e-05)

# Upper lattice
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Al", 5.732900e-02)
mat7.add_element("Cu", 2.509400e-06)
mat7.add_element("Fe", 9.993900e-05)
mat7.add_element("Mg", 1.364700e-03)
mat7.add_element("Mn", 9.869000e-05)
mat7.add_element("Si", 1.135600e-04)
mat7.add_element("Ti", 3.330500e-06)
mat7.add_element("Zn", 2.438700e-06)

# Lower lattice
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 6.003500e-02)
mat8.add_element("Cu", 7.878000e-06)
mat8.add_element("Fe", 8.964100e-05)
mat8.add_element("Mg", 1.455500e-03)
mat8.add_element("Mn", 1.093500e-04)
mat8.add_element("Si", 7.129900e-05)

# Fuel
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Al", 5.222500e-02)
mat9.add_element("C", 1.644000e-05)
mat9.add_element("Cr", 1.795900e-03)
mat9.add_element("Cu", 4.661100e-06)
mat9.add_element("Fe", 6.544100e-03)
mat9.add_element("Mg", 1.217000e-03)
mat9.add_element("Mn", 2.368700e-04)
mat9.add_element("Nb", 2.231700e-05)
mat9.add_element("Ni", 9.541800e-04)
mat9.add_element("P", 3.825100e-06)
mat9.add_element("S", 1.847200e-06)
mat9.add_element("Si", 1.511600e-04)
mat9.add_element("Ti", 2.020800e-05)
mat9.add_element("Zn", 2.113900e-06)

# Fuel
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("Al", 5.548100e-02)
mat10.add_element("C", 1.425900e-06)
mat10.add_element("Co", 8.718400e-07)
mat10.add_element("Cr", 4.515900e-04)
mat10.add_element("Cu", 4.312300e-06)
mat10.add_element("Fe", 1.686700e-03)
mat10.add_element("Mg", 3.579700e-04)
mat10.add_element("Mn", 4.863300e-05)
mat10.add_element("Mo", 1.071100e-06)
mat10.add_element("Nb", 3.318200e-06)
mat10.add_element("Ni", 2.258700e-04)
mat10.add_element("P", 5.529500e-07)
mat10.add_element("S", 5.340500e-07)
mat10.add_element("Si", 2.482500e-03)
mat10.add_element("Sn", 6.059500e-06)
mat10.add_element("Ti", 4.507100e-05)
mat10.add_element("Zn", 2.619200e-07)

# Baffle
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_element("Al", 8.718500e-05)
mat11.add_element("C", 1.566800e-04)
mat11.add_element("Co", 1.037800e-04)
mat11.add_element("Cr", 1.566300e-02)
mat11.add_element("Cu", 1.110600e-04)
mat11.add_element("Fe", 5.928200e-02)
mat11.add_element("Mn", 1.301700e-03)
mat11.add_element("Mo", 9.317300e-05)
mat11.add_element("Ni", 7.439100e-03)
mat11.add_element("P", 6.075800e-05)
mat11.add_element("S", 1.467000e-05)
mat11.add_element("Si", 6.868100e-04)
mat11.add_element("Ti", 1.585300e-04)
mat11.add_element("V", 8.312100e-05)
mat11.add_element("Zn", 7.194900e-06)

# Water
mat12 = openmc.Material(material_id=12)
mat12.set_density("sum")
mat12.add_nuclide("H1", 6.673600e-02)
mat12.add_nuclide("O16", 3.336800e-02)
mat12.add_s_alpha_beta("c_H_in_H2O")

# Borosilicate
mat13 = openmc.Material(material_id=13)
mat13.set_density("sum")
mat13.add_element("Al", 5.296900e-04)
mat13.add_nuclide("B10", 9.915900e-04)
mat13.add_nuclide("B11", 3.991500e-03)
mat13.add_element("Ba", 4.876800e-07)
mat13.add_element("Fe", 9.353800e-06)
mat13.add_element("K", 3.514900e-04)
mat13.add_element("Mg", 5.511000e-06)
mat13.add_element("Na", 1.345900e-03)
mat13.add_nuclide("O16", 4.522700e-02)
mat13.add_element("Si", 1.787500e-02)
mat13.add_element("Ti", 3.077200e-06)
mat13.add_element("Zn", 1.433900e-06)

# Poison-rod
mat14 = openmc.Material(material_id=14)
mat14.set_density("sum")
mat14.add_element("Al", 6.460600e-05)
mat14.add_element("Co", 2.875700e-05)
mat14.add_element("Cr", 1.620400e-02)
mat14.add_element("Cu", 5.562500e-05)
mat14.add_element("Fe", 5.976100e-02)
mat14.add_element("Mn", 1.542400e-03)
mat14.add_element("Mo", 2.018800e-05)
mat14.add_element("Ni", 9.075300e-03)
mat14.add_element("P", 3.439200e-05)
mat14.add_element("S", 7.549300e-06)
mat14.add_element("Si", 3.275700e-04)
mat14.add_element("Ti", 4.652000e-04)
mat14.add_element("V", 5.988300e-05)

# Poison-rod
mat15 = openmc.Material(material_id=15)
mat15.set_density("sum")
mat15.add_element("Al", 1.316200e-05)
mat15.add_element("Co", 9.038800e-05)
mat15.add_element("Cr", 1.536700e-02)
mat15.add_element("Cu", 1.816200e-04)
mat15.add_element("Fe", 5.562100e-02)
mat15.add_element("Mn", 1.131200e-03)
mat15.add_element("Mo", 1.064200e-04)
mat15.add_element("Ni", 7.185400e-03)
mat15.add_element("P", 4.299500e-05)
mat15.add_element("S", 8.305000e-06)
mat15.add_element("Si", 6.322200e-04)
mat15.add_element("V", 6.099800e-05)

# Poison-rod
mat16 = openmc.Material(material_id=16)
mat16.set_density("sum")
mat16.add_element("Al", 4.820000e-02)
mat16.add_element("Cr", 2.072300e-06)
mat16.add_element("Cu", 3.370400e-06)
mat16.add_element("Fe", 3.813600e-05)
mat16.add_element("Mg", 9.191800e-04)
mat16.add_element("Mn", 6.450700e-05)
mat16.add_element("Ni", 1.836000e-06)
mat16.add_element("Si", 3.571400e-05)
mat16.add_element("Ti", 2.250500e-06)
mat16.add_element("Zn", 3.275400e-06)

# Poison-rod
mat17 = openmc.Material(material_id=17)
mat17.set_density("sum")
mat17.add_element("Al", 3.549300e-02)
mat17.add_element("Cu", 1.112900e-06)
mat17.add_element("Fe", 3.869200e-05)
mat17.add_element("Mg", 7.435700e-04)
mat17.add_element("Mn", 4.737800e-05)
mat17.add_element("Ni", 1.422500e-06)
mat17.add_element("Si", 5.245800e-05)
mat17.add_element("Ti", 1.784700e-06)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11, mat12, mat13, mat14, mat15, mat16, mat17])

# ==============================================================================
# Geometry
# ==============================================================================

# BCD
surf1 = openmc.ZCylinder(surface_id=1, x0=-32.348, y0=71.720, r=129.55, boundary_type="vacuum")
# Hc
surf2 = openmc.ZPlane(surface_id=2, z0=51.54)
# Upper lattice plate
surf3 = openmc.model.RectangularParallelepiped(-47.48125, 47.48125, -60.96055, 60.96055, 70.108, 70.748)
# Lower lattice plate
surf4 = openmc.model.RectangularParallelepiped(-47.48125, 47.48125, -55.88055, 55.88055, -2.348, -1.078)
# Fuel support plate
surf5 = openmc.model.RectangularParallelepiped(-4.5085, -2.4930, -64.0, 64.0, -4.126, -2.348)
# Fuel support plate
surf6 = openmc.model.RectangularParallelepiped(2.4930, 4.5085, -64.0, 64.0, -4.126, -2.348)
# Fuel beam base
surf7 = openmc.model.RectangularParallelepiped(-4.5085, -2.9639, -64.0, 64.0, -16.826, -4.126)
# Fuel beam base
surf8 = openmc.model.RectangularParallelepiped(2.9639, 4.5085, -64.0, 64.0, -16.826, -4.126)
# FSA beam 2
surf12 = openmc.model.RectangularParallelepiped(-4.5085, 4.5085, -64.0, 64.0, -16.826, -2.348)
# FSA beam 3
surf13 = openmc.model.RectangularParallelepiped(-4.5085, 4.5085, -64.0, 64.0, -16.826, -2.348)
# FSA beam 4
surf14 = openmc.model.RectangularParallelepiped(-4.5085, 4.5085, -64.0, 64.0, -16.826, -2.348)
# FSA beam 5
surf15 = openmc.model.RectangularParallelepiped(-4.5085, 4.5085, -64.0, 64.0, -16.826, -2.348)
# FSA beam 6
surf16 = openmc.model.RectangularParallelepiped(-4.5085, 4.5085, -64.0, 64.0, -16.826, -2.348)
# FSA beam 7
surf17 = openmc.model.RectangularParallelepiped(-4.5085, 4.5085, -64.0, 64.0, -16.826, -2.348)
# FSA beam 8
surf18 = openmc.model.RectangularParallelepiped(-4.5085, 4.5085, -64.0, 64.0, -16.826, -2.348)
# FSA beam 9
surf19 = openmc.model.RectangularParallelepiped(-4.5085, 4.5085, -64.0, 64.0, -16.826, -2.348)
# U(3)O2 fuel
surf21 = openmc.ZCylinder(surface_id=21, x0=0.0, y0=69.285, r=0.5065)
# Wrapper/gap
surf22 = openmc.ZCylinder(surface_id=22, x0=0.0, y0=69.285, r=0.5199)
# Dowel
surf23 = openmc.ZCylinder(surface_id=23, x0=-2.078, y0=-0.678, r=0.315)
# Lower end plug
surf24 = openmc.ZCylinder(surface_id=24, x0=-1.078, y0=0.0, r=0.5199)
# Upper end plug
surf25 = openmc.ZCylinder(surface_id=25, x0=69.285, y0=70.748, r=0.5199)
# Clad
surf26 = openmc.ZCylinder(surface_id=26, x0=-1.030, y0=70.700, r=0.54685)
# Air and water
# surf27: Unsupported surface type "rev" with params ['4', '-2.348', '0.320', '-1.078', '0.320', '-1.078', '0.5555', '70.748', '0.5555', 'tr', '0', '0', '0', '0', '0', '1', '0', '1', '0']
# surf31: Error converting surface type "c": could not convert string to float: 'tr'
# surf32: Error converting surface type "c": could not convert string to float: 'tr'
# surf33: Error converting surface type "c": could not convert string to float: 'tr'
# surf34: Error converting surface type "c": could not convert string to float: 'tr'
# surf35: Error converting surface type "c": could not convert string to float: 'tr'
# surf36: Error converting surface type "c": could not convert string to float: 'tr'
# surf37: Error converting surface type "c": could not convert string to float: 'tr'
# surf38: Error converting surface type "c": could not convert string to float: 'tr'
# Inner portion with drain holes
surf41 = openmc.model.RectangularParallelepiped(-46.90125, 46.90125, -45.65055, 45.65055, -2.348, 999.9)
# Outer portion without drain holes
surf42 = openmc.model.RectangularParallelepiped(-47.48125, 47.48125, -46.2759, 46.2759, -2.348, 999.9)
surf51 = openmc.model.RectangularParallelepiped(-20.0112, 20.0112, -42.6924, -40.0224, -1.078, 67.872)
surf52 = openmc.model.RectangularParallelepiped(-22.6812, -20.0112, -42.6924, -20.0112, -1.078, 67.872)
surf53 = openmc.model.RectangularParallelepiped(-40.0224, -22.6812, -22.6812, -20.0112, -1.078, 67.872)
surf54 = openmc.model.RectangularParallelepiped(-42.6924, -40.0224, -22.6812, 22.6812, -1.078, 67.872)
surf55 = openmc.model.RectangularParallelepiped(-40.0224, -22.6812, 20.0112, 22.6812, -1.078, 67.872)
surf56 = openmc.model.RectangularParallelepiped(-22.6812, -20.0112, 20.0112, 42.6924, -1.078, 67.872)
surf57 = openmc.model.RectangularParallelepiped(-20.0112, 20.0112, 40.0224, 42.6924, -1.078, 67.872)
surf58 = openmc.model.RectangularParallelepiped(20.0112, 22.6812, 20.0112, 42.6924, -1.078, 67.872)
surf59 = openmc.model.RectangularParallelepiped(22.6812, 40.0224, 20.0112, 22.6812, -1.078, 67.872)
surf60 = openmc.model.RectangularParallelepiped(40.0224, 42.6924, -22.6812, 22.6812, -1.078, 67.872)
surf61 = openmc.model.RectangularParallelepiped(22.6812, 40.0224, -22.6812, -20.0112, -1.078, 67.872)
surf62 = openmc.model.RectangularParallelepiped(20.0112, 22.6812, -42.6924, -20.0112, -1.078, 67.872)
# Air
surf71 = openmc.ZCylinder(surface_id=71, x0=0.0, y0=69.326, r=0.3422)
# Inner clad
surf72 = openmc.ZCylinder(surface_id=72, x0=0.0, y0=69.326, r=0.3551)
# Borosilicate glass
surf73 = openmc.ZCylinder(surface_id=73, x0=0.0, y0=69.326, r=0.50225)
# Air
surf74 = openmc.ZCylinder(surface_id=74, x0=0.0, y0=69.326, r=0.52175)
# Lower end plug
surf75 = openmc.ZCylinder(surface_id=75, x0=-1.078, y0=0.0, r=0.52175)
# Upper end plug
surf76 = openmc.ZCylinder(surface_id=76, x0=69.326, y0=71.720, r=0.52175)
# Dowel
surf77 = openmc.ZCylinder(surface_id=77, x0=-2.078, y0=-0.678, r=0.315)
# Outer clad
surf78 = openmc.ZCylinder(surface_id=78, x0=-1.030, y0=70.700, r=0.54585)
# Air and water
# surf79: Unsupported surface type "rev" with params ['4', '-2.348', '0.320', '-1.078', '0.320', '-1.078', '0.5555', '71.720', '0.5555', 'tr', '0', '0', '0', '0', '0', '1', '0', '1', '0']

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat9)
u1_cell0.region = -surf1 & -surf5
u1_cell1 = openmc.Cell(fill=mat9)
u1_cell1.region = -surf1 & -surf6
u1_cell2 = openmc.Cell(fill=mat10)
u1_cell2.region = -surf1 & +surf5 & -surf7
u1_cell3 = openmc.Cell(fill=mat10)
u1_cell3.region = -surf1 & +surf6 & -surf8
u1_cell4 = openmc.Cell(fill=mat12)
u1_cell4.region = -surf1 & +surf5 & +surf6 & +surf7 & +surf8
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat12)
u2_cell0.region = -surf1 & -surf2 & +surf3 & +surf4 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & +surf17 & +surf18 & +surf19
u2_cell1 = openmc.Cell(fill=mat7)
u2_cell1.region = -surf3
u2_cell2 = openmc.Cell(fill=mat8)
u2_cell2.region = -surf4
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = -surf21 & -surf22
u3_cell1 = openmc.Cell(fill=mat2)
u3_cell1.region = +surf21 & -surf22
u3_cell2 = openmc.Cell(fill=mat5)
u3_cell2.region = +surf21 & +surf22 & +surf23 & -surf24
u3_cell3 = openmc.Cell(fill=mat4)
u3_cell3.region = +surf21 & +surf22 & -surf25
u3_cell4 = openmc.Cell(fill=mat3)
u3_cell4.region = +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & -surf26
u3_cell5 = openmc.Cell(fill=mat6)
u3_cell5.region = -surf23
u3_cell6 = openmc.Cell(fill=mat12)
u3_cell6.region = +surf23 & +surf24 & +surf25 & +surf26 & -surf2
u3_cell7 = openmc.Cell()
u3_cell7.region = +surf23 & +surf24 & +surf25 & +surf26 & +surf2
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5, u3_cell6, u3_cell7])

u4_cell0 = openmc.Cell(fill=mat12)
u4_cell0.region = 
u4_cell1 = openmc.Cell(fill=mat12)
u4_cell1.region = 
u4_cell2 = openmc.Cell(fill=mat12)
u4_cell2.region = 
u4_cell3 = openmc.Cell(fill=mat12)
u4_cell3.region = 
u4_cell4 = openmc.Cell()
u4_cell4.region = 
u4_cell5 = openmc.Cell()
u4_cell5.region = 
u4_cell6 = openmc.Cell()
u4_cell6.region = 
u4_cell7 = openmc.Cell()
u4_cell7.region = 
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4, u4_cell5, u4_cell6, u4_cell7])

u5_cell0 = openmc.Cell()
u5_cell0.region = +surf2
u5_cell1 = openmc.Cell(fill=mat12)
u5_cell1.region = -surf2
u5_cell2 = openmc.Cell(fill=mat12)
u5_cell2.region = 
u5_cell3 = openmc.Cell(fill=mat12)
u5_cell3.region = 
u5_cell4 = openmc.Cell(fill=mat12)
u5_cell4.region = 
u5_cell5 = openmc.Cell(fill=mat12)
u5_cell5.region = 
u5_cell6 = openmc.Cell()
u5_cell6.region = 
u5_cell7 = openmc.Cell()
u5_cell7.region = 
u5_cell8 = openmc.Cell()
u5_cell8.region = 
u5_cell9 = openmc.Cell()
u5_cell9.region = 
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0, u5_cell1, u5_cell2, u5_cell3, u5_cell4, u5_cell5, u5_cell6, u5_cell7, u5_cell8, u5_cell9])

u6_cell0 = openmc.Cell()
u6_cell0.region = +surf2
u6_cell1 = openmc.Cell(fill=mat12)
u6_cell1.region = -surf2
universe6 = openmc.Universe(universe_id=6, cells=[u6_cell0, u6_cell1])

u7_cell0 = openmc.Cell()
u7_cell0.region = -surf71 & -surf74
u7_cell1 = openmc.Cell(fill=mat15)
u7_cell1.region = +surf71 & -surf72 & -surf74
u7_cell2 = openmc.Cell(fill=mat13)
u7_cell2.region = +surf72 & -surf73 & -surf74
u7_cell3 = openmc.Cell()
u7_cell3.region = +surf73 & -surf74
u7_cell4 = openmc.Cell(fill=mat17)
u7_cell4.region = +surf74 & -surf75 & +surf77
u7_cell5 = openmc.Cell(fill=mat6)
u7_cell5.region = -surf77
u7_cell6 = openmc.Cell(fill=mat16)
u7_cell6.region = +surf74 & -surf76
u7_cell7 = openmc.Cell(fill=mat14)
u7_cell7.region = +surf74 & +surf75 & +surf76 & -surf78
u7_cell8 = openmc.Cell()
u7_cell8.region = +surf76 & +surf78 & +surf2
u7_cell9 = openmc.Cell(fill=mat12)
u7_cell9.region = +surf75 & +surf77 & +surf78 & -surf2
universe7 = openmc.Universe(universe_id=7, cells=[u7_cell0, u7_cell1, u7_cell2, u7_cell3, u7_cell4, u7_cell5, u7_cell6, u7_cell7, u7_cell8, u7_cell9])

u8_cell0 = openmc.Cell(fill=mat12)
u8_cell0.region = 
u8_cell1 = openmc.Cell(fill=mat12)
u8_cell1.region = 
u8_cell2 = openmc.Cell(fill=mat12)
u8_cell2.region = 
u8_cell3 = openmc.Cell(fill=mat12)
u8_cell3.region = 
u8_cell4 = openmc.Cell()
u8_cell4.region = 
u8_cell5 = openmc.Cell()
u8_cell5.region = 
u8_cell6 = openmc.Cell()
u8_cell6.region = 
u8_cell7 = openmc.Cell()
u8_cell7.region = 
universe8 = openmc.Universe(universe_id=8, cells=[u8_cell0, u8_cell1, u8_cell2, u8_cell3, u8_cell4, u8_cell5, u8_cell6, u8_cell7])

# Lattice 9: 76x74 array
lattice9 = openmc.RectLattice(lattice_id=9)
lattice9.lower_left = [-47.5266, -46.2759]
lattice9.pitch = [1.250700, 1.250700]
lattice9.universes = [
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe8, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe8, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe8, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe8, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
]
universe9 = openmc.Universe(universe_id=9)
universe9.add_cell(openmc.Cell(fill=lattice9))

# Lattice 10: 76x74 array
lattice10 = openmc.RectLattice(lattice_id=10)
lattice10.lower_left = [-47.5266, -46.2759]
lattice10.pitch = [1.250700, 1.250700]
lattice10.universes = [
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
]
universe10 = openmc.Universe(universe_id=10)
universe10.add_cell(openmc.Cell(fill=lattice10))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Baffle
cell1 = openmc.Cell(cell_id=1, fill=mat11)
cell1.region = -surf1 & -surf41 & -surf51

# Baffle
cell2 = openmc.Cell(cell_id=2, fill=mat11)
cell2.region = -surf1 & -surf41 & +surf51 & -surf52

# Baffle
cell3 = openmc.Cell(cell_id=3, fill=mat11)
cell3.region = -surf1 & -surf41 & +surf52 & -surf53

# Baffle
cell4 = openmc.Cell(cell_id=4, fill=mat11)
cell4.region = -surf1 & -surf41 & +surf53 & -surf54

# Baffle
cell5 = openmc.Cell(cell_id=5, fill=mat11)
cell5.region = -surf1 & -surf41 & +surf54 & -surf55

# Baffle
cell6 = openmc.Cell(cell_id=6, fill=mat11)
cell6.region = -surf1 & -surf41 & +surf55 & -surf56

# Baffle
cell7 = openmc.Cell(cell_id=7, fill=mat11)
cell7.region = -surf1 & -surf41 & +surf56 & -surf57

# Baffle
cell8 = openmc.Cell(cell_id=8, fill=mat11)
cell8.region = -surf1 & -surf41 & +surf57 & -surf58

# Baffle
cell9 = openmc.Cell(cell_id=9, fill=mat11)
cell9.region = -surf1 & -surf41 & +surf58 & -surf59

# Baffle
cell10 = openmc.Cell(cell_id=10, fill=mat11)
cell10.region = -surf1 & -surf41 & +surf59 & -surf60

# Baffle
cell11 = openmc.Cell(cell_id=11, fill=mat11)
cell11.region = -surf1 & -surf41 & +surf60 & -surf61

# Baffle
cell12 = openmc.Cell(cell_id=12, fill=mat11)
cell12.region = -surf1 & -surf41 & +surf61 & -surf62

# Iarray
cell13 = openmc.Cell(cell_id=13, fill=universe9)
cell13.region = -surf1 & -surf41 & +surf51 & +surf52 & +surf53 & +surf54 & +surf55 & +surf56 & +surf57 & +surf58 & +surf59 & +surf60 & +surf61 & +surf62

# Earray
cell14 = openmc.Cell(cell_id=14, fill=universe10)
cell14.region = -surf1 & +surf41 & -surf42

# Alles
cell15 = openmc.Cell(cell_id=15, fill=universe2)
cell15.region = -surf1 & +surf42

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15])
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
source.space = openmc.stats.Box((-1.62535, -1.62535, 24.77), (1.62535, 1.62535, 26.77))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
