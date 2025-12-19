"""
MCT011-3: 151 Rapsodie pins with 1.9 cm pitch and Hc = 35.02 cm
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Rapsodie
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.221400e-04)
mat1.add_nuclide("U235", 1.045100e-02)
mat1.add_nuclide("U238", 6.836200e-03)
mat1.add_nuclide("Pu239", 5.286500e-03)
mat1.add_nuclide("Pu240", 5.749500e-04)
mat1.add_nuclide("Pu241", 5.126800e-05)
mat1.add_nuclide("Pu242", 4.106300e-06)
mat1.add_nuclide("Am241", 2.000600e-05)
mat1.add_nuclide("O16", 4.633100e-02)

# U(nat)O2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 1.670000e-04)
mat2.add_nuclide("U238", 2.302700e-02)
mat2.add_nuclide("O16", 4.638800e-02)

# Air
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("N", 4.198500e-05)
mat3.add_nuclide("O16", 1.126300e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.670600e-02)
mat4.add_nuclide("O16", 3.335300e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Z2 CN 18-10
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 5.869400e-02)
mat5.add_element("Cr", 1.646900e-02)
mat5.add_element("Ni", 8.106100e-03)
mat5.add_element("Mn", 1.731900e-03)
mat5.add_element("Si", 1.693900e-03)
mat5.add_element("P", 6.143800e-05)
mat5.add_element("S", 4.464000e-05)
mat5.add_element("C", 1.188300e-04)

# Z3 CND 18-12
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 5.723200e-02)
mat6.add_element("Cr", 1.541100e-02)
mat6.add_element("Ni", 9.742400e-03)
mat6.add_element("Mn", 1.364700e-03)
mat6.add_element("Si", 6.818600e-04)
mat6.add_element("P", 5.564500e-05)
mat6.add_element("S", 1.946600e-07)
mat6.add_element("C", 1.893300e-06)
mat6.add_element("C", 1.893300e-06)
mat6.add_element("Mo", 1.275500e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Rapsodie MOX fuel
surf1 = openmc.ZCylinder(surface_id=1, r=0.27865)
# U(nat)O2
surf2 = openmc.ZCylinder(surface_id=2, r=0.27865)
# Z3 CND 18-12 SST pellet
surf3 = openmc.ZCylinder(surface_id=3, r=0.27865)
# Air gaps
surf4 = openmc.ZCylinder(surface_id=4, r=0.29)
# Z3 CND 18-12 SST clad and end plugs
surf5 = openmc.ZCylinder(surface_id=5, r=0.335)
# Z2 CN  18-10 SST positioning ring, inner
surf6 = openmc.ZCylinder(surface_id=6, r=0.335)
# Z2 CN  18-10 SST positioning ring, outer
surf7 = openmc.ZCylinder(surface_id=7, r=0.425)
# Top of lower positioning ring
surf8 = openmc.ZPlane(surface_id=8, z0=-0.6)
# Critical water height
surf9 = openmc.ZPlane(surface_id=9, z0=35.02)
# Bottom of upper positioning ring
surf10 = openmc.ZPlane(surface_id=10, z0=46.3)
# Boundary condition
surf11 = openmc.ZCylinder(surface_id=11, r=38.0, boundary_type="vacuum")
# Z2 CN 18-10 SST lower support plate
surf12 = openmc.ZCylinder(surface_id=12, r=17.5)
# Z2 CN 18-10 SST bottom grid
surf13 = openmc.ZCylinder(surface_id=13, r=17.5)
# Z2 CN 18-10 SST upper  grid
surf14 = openmc.ZCylinder(surface_id=14, r=17.5)
# Z2 CN 18-10 SST upper support annular plate, inner
surf15 = openmc.ZCylinder(surface_id=15, r=15.0)
# Z2 CN 18-10 SST upper support annular plate, outer
surf16 = openmc.ZCylinder(surface_id=16, r=17.5)
# Z2 CN 18-10 SST tie rod
surf17 = openmc.ZCylinder(surface_id=17, x0=-16.6, y0=0.0, r=0.4)
# Z2 CN 18-10 SST tie rod
surf18 = openmc.ZCylinder(surface_id=18, x0=0.0, y0=16.6, r=0.4)
# Z2 CN 18-10 SST tie rod
surf19 = openmc.ZCylinder(surface_id=19, x0=0.0, y0=-16.6, r=0.4)
# Z2 CN 18-10 SST tie rod
surf20 = openmc.ZCylinder(surface_id=20, x0=16.6, y0=0.0, r=0.4)
# Unit
surf21 = openmc.ZCylinder(surface_id=21, x0=-0.95, y0=1.645448, r=0.425)
# triangular
surf22 = openmc.ZCylinder(surface_id=22, x0=0.95, y0=1.645448, r=0.425)
# cell
surf23 = openmc.ZCylinder(surface_id=23, x0=-1.9, y0=0.0, r=0.425)
# of seven
surf24 = openmc.ZCylinder(surface_id=24, x0=1.9, y0=0.0, r=0.425)
# fuel
surf25 = openmc.ZCylinder(surface_id=25, x0=-0.95, y0=-1.645448, r=0.425)
# pins
surf26 = openmc.ZCylinder(surface_id=26, x0=0.95, y0=-1.645448, r=0.425)
# Hexagonal prism
# Prism 30: 6-sided polygon
surf30_0 = openmc.Plane(a=0.8660253686, b=0.5000000609, c=0, d=12.3408615029)
surf30_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=12.3408600000)
surf30_2 = openmc.Plane(a=-0.8660253686, b=0.5000000609, c=0, d=12.3408615029)
surf30_3 = openmc.Plane(a=-0.8660253686, b=-0.5000000609, c=0, d=12.3408615029)
surf30_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=12.3408600000)
surf30_5 = openmc.Plane(a=0.8660253686, b=-0.5000000609, c=0, d=12.3408615029)
# Hexagonal prism
# Prism 31: 6-sided polygon
surf31_0 = openmc.Plane(a=0.8660253686, b=0.5000000609, c=0, d=13.9863097033)
surf31_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=13.9863080000)
surf31_2 = openmc.Plane(a=-0.8660253686, b=0.5000000609, c=0, d=13.9863097033)
surf31_3 = openmc.Plane(a=-0.8660253686, b=-0.5000000609, c=0, d=13.9863097033)
surf31_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=13.9863080000)
surf31_5 = openmc.Plane(a=0.8660253686, b=-0.5000000609, c=0, d=13.9863097033)
# No hole
surf41 = openmc.ZCylinder(surface_id=41, x0=-14.25, y0=1.645448, r=0.43)
# No hole
surf42 = openmc.ZCylinder(surface_id=42, x0=-14.25, y0=-1.645448, r=0.43)
# No hole
surf43 = openmc.ZCylinder(surface_id=43, x0=-8.55, y0=11.518136, r=0.43)
# No hole
surf44 = openmc.ZCylinder(surface_id=44, x0=-8.55, y0=-11.518136, r=0.43)
# No hole
surf45 = openmc.ZCylinder(surface_id=45, x0=-5.7, y0=13.163584, r=0.43)
# No hole
surf46 = openmc.ZCylinder(surface_id=46, x0=-5.7, y0=-13.163584, r=0.43)
# No hole
surf47 = openmc.ZCylinder(surface_id=47, x0=5.7, y0=13.163584, r=0.43)
# No hole
surf48 = openmc.ZCylinder(surface_id=48, x0=5.7, y0=-13.163584, r=0.43)
# No hole
surf49 = openmc.ZCylinder(surface_id=49, x0=8.55, y0=11.518136, r=0.43)
# No hole
surf50 = openmc.ZCylinder(surface_id=50, x0=8.55, y0=-11.518136, r=0.43)
# No hole
surf51 = openmc.ZCylinder(surface_id=51, x0=14.25, y0=1.645448, r=0.43)
# No hole
surf52 = openmc.ZCylinder(surface_id=52, x0=14.25, y0=-1.645448, r=0.43)
# No hole
surf61 = openmc.ZCylinder(surface_id=61, x0=-15.2, y0=6.581792, r=0.43)
# No hole
surf62 = openmc.ZCylinder(surface_id=62, x0=-15.2, y0=-6.581792, r=0.43)
# No hole
surf63 = openmc.ZCylinder(surface_id=63, x0=-13.3, y0=9.872688, r=0.43)
# No hole
surf64 = openmc.ZCylinder(surface_id=64, x0=-13.3, y0=-9.872688, r=0.43)
# No hole
surf65 = openmc.ZCylinder(surface_id=65, x0=15.2, y0=6.581792, r=0.43)
# No hole
surf66 = openmc.ZCylinder(surface_id=66, x0=15.2, y0=-6.581792, r=0.43)
# No hole
surf67 = openmc.ZCylinder(surface_id=67, x0=13.3, y0=9.872688, r=0.43)
# No hole
surf68 = openmc.ZCylinder(surface_id=68, x0=13.3, y0=-9.872688, r=0.43)
# Hole
surf71 = openmc.ZCylinder(surface_id=71, x0=-13.3, y0=0.0, r=0.43)
# Hole
surf72 = openmc.ZCylinder(surface_id=72, x0=-12.35, y0=1.645448, r=0.43)
# Hole
surf73 = openmc.ZCylinder(surface_id=73, x0=-12.35, y0=-1.645448, r=0.43)
# Hole
surf74 = openmc.ZCylinder(surface_id=74, x0=-7.6, y0=9.872688, r=0.43)
# Hole
surf75 = openmc.ZCylinder(surface_id=75, x0=-6.65, y0=11.58136, r=0.43)
# Hole
surf76 = openmc.ZCylinder(surface_id=76, x0=-4.75, y0=11.58136, r=0.43)
# Hole
surf77 = openmc.ZCylinder(surface_id=77, x0=-7.6, y0=-9.872688, r=0.43)
# Hole
surf78 = openmc.ZCylinder(surface_id=78, x0=-6.65, y0=-11.58136, r=0.43)
# Hole
surf79 = openmc.ZCylinder(surface_id=79, x0=-4.75, y0=-11.58136, r=0.43)
# Hole
surf80 = openmc.ZCylinder(surface_id=80, x0=7.6, y0=9.872688, r=0.43)
# Hole
surf81 = openmc.ZCylinder(surface_id=81, x0=6.65, y0=11.58136, r=0.43)
# Hole
surf82 = openmc.ZCylinder(surface_id=82, x0=4.75, y0=11.58136, r=0.43)
# Hole
surf83 = openmc.ZCylinder(surface_id=83, x0=7.6, y0=-9.872688, r=0.43)
# Hole
surf84 = openmc.ZCylinder(surface_id=84, x0=6.65, y0=-11.58136, r=0.43)
# Hole
surf85 = openmc.ZCylinder(surface_id=85, x0=4.75, y0=-11.58136, r=0.43)
# Hole
surf86 = openmc.ZCylinder(surface_id=86, x0=13.3, y0=0.0, r=0.43)
# Hole
surf87 = openmc.ZCylinder(surface_id=87, x0=12.35, y0=1.645448, r=0.43)
# Hole
surf88 = openmc.ZCylinder(surface_id=88, x0=12.35, y0=-1.645448, r=0.43)
# Z3 CND 18-12 SST fin
surf99 = openmc.model.RectangularParallelepiped(-0.4144, 0, -0.0238, 0.0238, -0.3, 45.6)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1099, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1100, z0=34.55)
surf2_zmin = openmc.ZPlane(surface_id=1101, z0=-0.3)
surf2_zmax = openmc.ZPlane(surface_id=1102, z0=34.85)
surf3_zmin = openmc.ZPlane(surface_id=1103, z0=34.85)
surf3_zmax = openmc.ZPlane(surface_id=1104, z0=34.95)
surf4_zmin = openmc.ZPlane(surface_id=1105, z0=-0.3)
surf4_zmax = openmc.ZPlane(surface_id=1106, z0=45.6)
surf5_zmin = openmc.ZPlane(surface_id=1107, z0=-1.134)
surf5_zmax = openmc.ZPlane(surface_id=1108, z0=46.763)
surf7_zmin = openmc.ZPlane(surface_id=1109, z0=-1.4)
surf7_zmax = openmc.ZPlane(surface_id=1110, z0=47.1)
surf11_zmin = openmc.ZPlane(surface_id=1111, z0=-34.0, boundary_type="vacuum")
surf11_zmax = openmc.ZPlane(surface_id=1112, z0=81.8, boundary_type="vacuum")
surf12_zmin = openmc.ZPlane(surface_id=1113, z0=-1.9)
surf12_zmax = openmc.ZPlane(surface_id=1114, z0=-1.4)
surf13_zmin = openmc.ZPlane(surface_id=1115, z0=-0.9)
surf13_zmax = openmc.ZPlane(surface_id=1116, z0=-0.8)
surf14_zmin = openmc.ZPlane(surface_id=1117, z0=46.4)
surf14_zmax = openmc.ZPlane(surface_id=1118, z0=46.5)
surf16_zmin = openmc.ZPlane(surface_id=1119, z0=81.3)
surf16_zmax = openmc.ZPlane(surface_id=1120, z0=81.8)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell2 = openmc.Cell(fill=mat6)
u1_cell2.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)
u1_cell5 = openmc.Cell(fill=mat6)
u1_cell5.region = (+surf5 | -surf5_zmin | +surf5_zmax) & +surf6 & -surf99
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = (+surf5 | -surf5_zmin | +surf5_zmax) & +surf6 & (-surf7 & +surf7_zmin & -surf7_zmax) & -surf8
u1_cell7 = openmc.Cell(fill=mat5)
u1_cell7.region = (+surf5 | -surf5_zmin | +surf5_zmax) & +surf6 & (-surf7 & +surf7_zmin & -surf7_zmax) & +surf10
u1_cell8 = openmc.Cell(fill=mat3)
u1_cell8.region = (+surf5 | -surf5_zmin | +surf5_zmax) & -surf6 & (-surf7 & +surf7_zmin & -surf7_zmax) & +surf9
u1_cell9 = openmc.Cell(fill=mat4)
u1_cell9.region = (+surf5 | -surf5_zmin | +surf5_zmax) & -surf6 & (-surf7 & +surf7_zmin & -surf7_zmax) & -surf9
u1_cell10 = openmc.Cell(fill=mat3)
u1_cell10.region = (+surf5 | -surf5_zmin | +surf5_zmax) & +surf6 & (-surf7 & +surf7_zmin & -surf7_zmax) & +surf9 & -surf10 & +surf99
u1_cell11 = openmc.Cell(fill=mat4)
u1_cell11.region = (+surf5 | -surf5_zmin | +surf5_zmax) & +surf6 & (-surf7 & +surf7_zmin & -surf7_zmax) & +surf8 & -surf9 & +surf99
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = +surf9 & (-surf11 & +surf11_zmin & -surf11_zmax)
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = -surf9 & (-surf11 & +surf11_zmin & -surf11_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1])

u3_cell0 = openmc.Cell(fill=mat5)
u3_cell0.region = (-surf12 & +surf12_zmin & -surf12_zmax)
u3_cell1 = openmc.Cell(fill=mat5)
u3_cell1.region = (-surf13 & +surf13_zmin & -surf13_zmax)
u3_cell2 = openmc.Cell(fill=mat5)
u3_cell2.region = (-surf14 & +surf14_zmin & -surf14_zmax)
u3_cell3 = openmc.Cell(fill=mat5)
u3_cell3.region = +surf15 & (-surf16 & +surf16_zmin & -surf16_zmax)
u3_cell4 = openmc.Cell(fill=mat5)
u3_cell4.region = (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & -surf17
u3_cell5 = openmc.Cell(fill=mat5)
u3_cell5.region = (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & -surf18
u3_cell6 = openmc.Cell(fill=mat5)
u3_cell6.region = (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & -surf19
u3_cell7 = openmc.Cell(fill=mat5)
u3_cell7.region = (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & -surf20
u3_cell8 = openmc.Cell(fill=mat3)
u3_cell8.region = -surf15 & (-surf16 & +surf16_zmin & -surf16_zmax)
u3_cell9 = openmc.Cell(fill=mat3)
u3_cell9.region = +surf9 & (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & +surf17 & +surf18 & +surf19 & +surf20
u3_cell10 = openmc.Cell(fill=mat4)
u3_cell10.region = -surf9 & (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & +surf17 & +surf18 & +surf19 & +surf20
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5, u3_cell6, u3_cell7, u3_cell8, u3_cell9, u3_cell10])

universe4 = openmc.Universe(universe_id=4, cells=[])

universe5 = openmc.Universe(universe_id=5, cells=[])

# Lattice 6: 11x11 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-20.9, -18.099928]
lattice6.pitch = [3.800000, 3.290896]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

# Lattice 7: 11x11 array
lattice7 = openmc.RectLattice(lattice_id=7)
lattice7.lower_left = [-20.9, -18.099928]
lattice7.pitch = [3.800000, 3.290896]
lattice7.universes = [
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
]
universe7 = openmc.Universe(universe_id=7)
universe7.add_cell(openmc.Cell(fill=lattice7))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Farray
cell1 = openmc.Cell(cell_id=1, fill=universe6)
cell1.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & +surf71 & +surf72 & +surf73 & +surf74 & +surf75 & +surf76 & +surf77 & +surf78 & +surf79 & +surf80 & +surf81 & +surf82 & +surf83 & +surf84 & +surf85 & +surf86 & +surf87 & +surf88

# Hole
cell2 = openmc.Cell(cell_id=2, fill=universe7)
cell2.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf71

# Hole
cell3 = openmc.Cell(cell_id=3, fill=universe7)
cell3.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf72

# Hole
cell4 = openmc.Cell(cell_id=4, fill=universe7)
cell4.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf73

# Hole
cell5 = openmc.Cell(cell_id=5, fill=universe7)
cell5.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf74

# Hole
cell6 = openmc.Cell(cell_id=6, fill=universe7)
cell6.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf75

# Hole
cell7 = openmc.Cell(cell_id=7, fill=universe7)
cell7.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf76

# Hole
cell8 = openmc.Cell(cell_id=8, fill=universe7)
cell8.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf77

# Hole
cell9 = openmc.Cell(cell_id=9, fill=universe7)
cell9.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf78

# Hole
cell10 = openmc.Cell(cell_id=10, fill=universe7)
cell10.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf79

# Hole
cell11 = openmc.Cell(cell_id=11, fill=universe7)
cell11.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf80

# Hole
cell12 = openmc.Cell(cell_id=12, fill=universe7)
cell12.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf81

# Hole
cell13 = openmc.Cell(cell_id=13, fill=universe7)
cell13.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf82

# Hole
cell14 = openmc.Cell(cell_id=14, fill=universe7)
cell14.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf83

# Hole
cell15 = openmc.Cell(cell_id=15, fill=universe7)
cell15.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf84

# Hole
cell16 = openmc.Cell(cell_id=16, fill=universe7)
cell16.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf85

# Hole
cell17 = openmc.Cell(cell_id=17, fill=universe7)
cell17.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf86

# Hole
cell18 = openmc.Cell(cell_id=18, fill=universe7)
cell18.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf87

# Hole
cell19 = openmc.Cell(cell_id=19, fill=universe7)
cell19.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf88

# Harray
cell20 = openmc.Cell(cell_id=20, fill=universe7)
cell20.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & +surf41 & +surf42 & +surf43 & +surf44 & +surf45 & +surf46 & +surf47 & +surf48 & +surf49 & +surf50 & +surf51 & +surf52

# NoHole
cell21 = openmc.Cell(cell_id=21, fill=universe3)
cell21.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf41

# NoHole
cell22 = openmc.Cell(cell_id=22, fill=universe3)
cell22.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf42

# NoHole
cell23 = openmc.Cell(cell_id=23, fill=universe3)
cell23.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf43

# NoHole
cell24 = openmc.Cell(cell_id=24, fill=universe3)
cell24.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf44

# NoHole
cell25 = openmc.Cell(cell_id=25, fill=universe3)
cell25.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf45

# NoHole
cell26 = openmc.Cell(cell_id=26, fill=universe3)
cell26.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf46

# NoHole
cell27 = openmc.Cell(cell_id=27, fill=universe3)
cell27.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf47

# NoHole
cell28 = openmc.Cell(cell_id=28, fill=universe3)
cell28.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf48

# NoHole
cell29 = openmc.Cell(cell_id=29, fill=universe3)
cell29.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf49

# NoHole
cell30 = openmc.Cell(cell_id=30, fill=universe3)
cell30.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf50

# NoHole
cell31 = openmc.Cell(cell_id=31, fill=universe3)
cell31.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf51

# NoHole
cell32 = openmc.Cell(cell_id=32, fill=universe3)
cell32.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf52

# Alles
cell33 = openmc.Cell(cell_id=33, fill=universe3)
cell33.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & +surf61 & +surf62 & +surf63 & +surf64 & +surf65 & +surf66 & +surf67 & +surf68

# Hole
cell34 = openmc.Cell(cell_id=34, fill=universe7)
cell34.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf61

# Hole
cell35 = openmc.Cell(cell_id=35, fill=universe7)
cell35.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf62

# Hole
cell36 = openmc.Cell(cell_id=36, fill=universe7)
cell36.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf63

# Hole
cell37 = openmc.Cell(cell_id=37, fill=universe7)
cell37.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf64

# Hole
cell38 = openmc.Cell(cell_id=38, fill=universe7)
cell38.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf65

# Hole
cell39 = openmc.Cell(cell_id=39, fill=universe7)
cell39.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf66

# Hole
cell40 = openmc.Cell(cell_id=40, fill=universe7)
cell40.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf67

# Hole
cell41 = openmc.Cell(cell_id=41, fill=universe7)
cell41.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf68

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41])
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
source.space = openmc.stats.Point((0.0, 0.0, 17.51))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
