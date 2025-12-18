"""
MCT011-2: 163 Rapsodie pins with 1.9 cm pitch and Hc = 31.59 cm
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

# Rapsodie MOX fuel
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0, y0=34.55, r=0.27865)
# U(nat)O2
surf2 = openmc.ZCylinder(surface_id=2, x0=-0.3, y0=34.85, r=0.27865)
# Z3 CND 18-12 SST pellet
surf3 = openmc.ZCylinder(surface_id=3, x0=34.85, y0=34.95, r=0.27865)
# Air gaps
surf4 = openmc.ZCylinder(surface_id=4, x0=-0.3, y0=45.6, r=0.29)
# Z3 CND 18-12 SST clad and end plugs
surf5 = openmc.ZCylinder(surface_id=5, x0=-1.134, y0=46.763, r=0.335)
# Z2 CN  18-10 SST positioning ring, inner
surf6 = openmc.ZCylinder(surface_id=6, r=0.335)
# Z2 CN  18-10 SST positioning ring, outer
surf7 = openmc.ZCylinder(surface_id=7, x0=-1.4, y0=47.1, r=0.425)
# Top of lower positioning ring
surf8 = openmc.ZPlane(surface_id=8, z0=-0.6)
# Critical water height
surf9 = openmc.ZPlane(surface_id=9, z0=31.59)
# Bottom of upper positioning ring
surf10 = openmc.ZPlane(surface_id=10, z0=46.3)
# Boundary condition
surf11 = openmc.ZCylinder(surface_id=11, x0=-34.0, y0=81.8, r=38.0, boundary_type="vacuum")
# Z2 CN 18-10 SST lower support plate
surf12 = openmc.ZCylinder(surface_id=12, x0=-1.9, y0=-1.4, r=17.5)
# Z2 CN 18-10 SST bottom grid
surf13 = openmc.ZCylinder(surface_id=13, x0=-0.9, y0=-0.8, r=17.5)
# Z2 CN 18-10 SST upper  grid
surf14 = openmc.ZCylinder(surface_id=14, x0=46.4, y0=46.5, r=17.5)
# Z2 CN 18-10 SST upper support annular plate, inner
surf15 = openmc.ZCylinder(surface_id=15, r=15.0)
# Z2 CN 18-10 SST upper support annular plate, outer
surf16 = openmc.ZCylinder(surface_id=16, x0=81.3, y0=81.8, r=17.5)
# Z2 CN 18-10 SST tie rod
# surf17: Error converting surface type "c": could not convert string to float: 'tr'
# Z2 CN 18-10 SST tie rod
# surf18: Error converting surface type "c": could not convert string to float: 'tr'
# Z2 CN 18-10 SST tie rod
# surf19: Error converting surface type "c": could not convert string to float: 'tr'
# Z2 CN 18-10 SST tie rod
# surf20: Error converting surface type "c": could not convert string to float: 'tr'
# Unit
# surf21: Error converting surface type "c": could not convert string to float: 'tr'
# triangular
# surf22: Error converting surface type "c": could not convert string to float: 'tr'
# cell
# surf23: Error converting surface type "c": could not convert string to float: 'tr'
# of seven
# surf24: Error converting surface type "c": could not convert string to float: 'tr'
# fuel
# surf25: Error converting surface type "c": could not convert string to float: 'tr'
# pins
# surf26: Error converting surface type "c": could not convert string to float: 'tr'
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
surf41_cyl = openmc.ZCylinder(surface_id=41, x0=tr, y0=-14.25, r=0.43)
surf41_zmin = openmc.ZPlane(z0=1.645448)
surf41_zmax = openmc.ZPlane(z0=0.0)
surf41 = (surf41_cyl, surf41_zmin, surf41_zmax)
# No hole
surf42_cyl = openmc.ZCylinder(surface_id=42, x0=tr, y0=-14.25, r=0.43)
surf42_zmin = openmc.ZPlane(z0=-1.645448)
surf42_zmax = openmc.ZPlane(z0=0.0)
surf42 = (surf42_cyl, surf42_zmin, surf42_zmax)
# No hole
surf43_cyl = openmc.ZCylinder(surface_id=43, x0=tr, y0=-8.55, r=0.43)
surf43_zmin = openmc.ZPlane(z0=11.518136)
surf43_zmax = openmc.ZPlane(z0=0.0)
surf43 = (surf43_cyl, surf43_zmin, surf43_zmax)
# No hole
surf44_cyl = openmc.ZCylinder(surface_id=44, x0=tr, y0=-8.55, r=0.43)
surf44_zmin = openmc.ZPlane(z0=-11.518136)
surf44_zmax = openmc.ZPlane(z0=0.0)
surf44 = (surf44_cyl, surf44_zmin, surf44_zmax)
# No hole
surf45_cyl = openmc.ZCylinder(surface_id=45, x0=tr, y0=-5.70, r=0.43)
surf45_zmin = openmc.ZPlane(z0=13.163584)
surf45_zmax = openmc.ZPlane(z0=0.0)
surf45 = (surf45_cyl, surf45_zmin, surf45_zmax)
# No hole
surf46_cyl = openmc.ZCylinder(surface_id=46, x0=tr, y0=-5.70, r=0.43)
surf46_zmin = openmc.ZPlane(z0=-13.163584)
surf46_zmax = openmc.ZPlane(z0=0.0)
surf46 = (surf46_cyl, surf46_zmin, surf46_zmax)
# No hole
surf47_cyl = openmc.ZCylinder(surface_id=47, x0=tr, y0=5.70, r=0.43)
surf47_zmin = openmc.ZPlane(z0=13.163584)
surf47_zmax = openmc.ZPlane(z0=0.0)
surf47 = (surf47_cyl, surf47_zmin, surf47_zmax)
# No hole
surf48_cyl = openmc.ZCylinder(surface_id=48, x0=tr, y0=5.70, r=0.43)
surf48_zmin = openmc.ZPlane(z0=-13.163584)
surf48_zmax = openmc.ZPlane(z0=0.0)
surf48 = (surf48_cyl, surf48_zmin, surf48_zmax)
# No hole
surf49_cyl = openmc.ZCylinder(surface_id=49, x0=tr, y0=8.55, r=0.43)
surf49_zmin = openmc.ZPlane(z0=11.518136)
surf49_zmax = openmc.ZPlane(z0=0.0)
surf49 = (surf49_cyl, surf49_zmin, surf49_zmax)
# No hole
surf50_cyl = openmc.ZCylinder(surface_id=50, x0=tr, y0=8.55, r=0.43)
surf50_zmin = openmc.ZPlane(z0=-11.518136)
surf50_zmax = openmc.ZPlane(z0=0.0)
surf50 = (surf50_cyl, surf50_zmin, surf50_zmax)
# No hole
surf51_cyl = openmc.ZCylinder(surface_id=51, x0=tr, y0=14.25, r=0.43)
surf51_zmin = openmc.ZPlane(z0=1.645448)
surf51_zmax = openmc.ZPlane(z0=0.0)
surf51 = (surf51_cyl, surf51_zmin, surf51_zmax)
# No hole
surf52_cyl = openmc.ZCylinder(surface_id=52, x0=tr, y0=14.25, r=0.43)
surf52_zmin = openmc.ZPlane(z0=-1.645448)
surf52_zmax = openmc.ZPlane(z0=0.0)
surf52 = (surf52_cyl, surf52_zmin, surf52_zmax)
# No hole
surf61_cyl = openmc.ZCylinder(surface_id=61, x0=tr, y0=-15.20, r=0.43)
surf61_zmin = openmc.ZPlane(z0=6.581792)
surf61_zmax = openmc.ZPlane(z0=0.0)
surf61 = (surf61_cyl, surf61_zmin, surf61_zmax)
# No hole
surf62_cyl = openmc.ZCylinder(surface_id=62, x0=tr, y0=-15.20, r=0.43)
surf62_zmin = openmc.ZPlane(z0=-6.581792)
surf62_zmax = openmc.ZPlane(z0=0.0)
surf62 = (surf62_cyl, surf62_zmin, surf62_zmax)
# No hole
surf63_cyl = openmc.ZCylinder(surface_id=63, x0=tr, y0=-13.30, r=0.43)
surf63_zmin = openmc.ZPlane(z0=9.872688)
surf63_zmax = openmc.ZPlane(z0=0.0)
surf63 = (surf63_cyl, surf63_zmin, surf63_zmax)
# No hole
surf64_cyl = openmc.ZCylinder(surface_id=64, x0=tr, y0=-13.30, r=0.43)
surf64_zmin = openmc.ZPlane(z0=-9.872688)
surf64_zmax = openmc.ZPlane(z0=0.0)
surf64 = (surf64_cyl, surf64_zmin, surf64_zmax)
# No hole
surf65_cyl = openmc.ZCylinder(surface_id=65, x0=tr, y0=15.20, r=0.43)
surf65_zmin = openmc.ZPlane(z0=6.581792)
surf65_zmax = openmc.ZPlane(z0=0.0)
surf65 = (surf65_cyl, surf65_zmin, surf65_zmax)
# No hole
surf66_cyl = openmc.ZCylinder(surface_id=66, x0=tr, y0=15.20, r=0.43)
surf66_zmin = openmc.ZPlane(z0=-6.581792)
surf66_zmax = openmc.ZPlane(z0=0.0)
surf66 = (surf66_cyl, surf66_zmin, surf66_zmax)
# No hole
surf67_cyl = openmc.ZCylinder(surface_id=67, x0=tr, y0=13.30, r=0.43)
surf67_zmin = openmc.ZPlane(z0=9.872688)
surf67_zmax = openmc.ZPlane(z0=0.0)
surf67 = (surf67_cyl, surf67_zmin, surf67_zmax)
# No hole
surf68_cyl = openmc.ZCylinder(surface_id=68, x0=tr, y0=13.30, r=0.43)
surf68_zmin = openmc.ZPlane(z0=-9.872688)
surf68_zmax = openmc.ZPlane(z0=0.0)
surf68 = (surf68_cyl, surf68_zmin, surf68_zmax)
# Hole
surf71_cyl = openmc.ZCylinder(surface_id=71, x0=tr, y0=-13.30, r=0.43)
surf71_zmin = openmc.ZPlane(z0=0.0)
surf71_zmax = openmc.ZPlane(z0=0.0)
surf71 = (surf71_cyl, surf71_zmin, surf71_zmax)
# Hole
surf72_cyl = openmc.ZCylinder(surface_id=72, x0=tr, y0=-6.65, r=0.43)
surf72_zmin = openmc.ZPlane(z0=11.58136)
surf72_zmax = openmc.ZPlane(z0=0.0)
surf72 = (surf72_cyl, surf72_zmin, surf72_zmax)
# Hole
surf73_cyl = openmc.ZCylinder(surface_id=73, x0=tr, y0=-6.65, r=0.43)
surf73_zmin = openmc.ZPlane(z0=-11.58136)
surf73_zmax = openmc.ZPlane(z0=0.0)
surf73 = (surf73_cyl, surf73_zmin, surf73_zmax)
# Hole
surf74_cyl = openmc.ZCylinder(surface_id=74, x0=tr, y0=6.65, r=0.43)
surf74_zmin = openmc.ZPlane(z0=11.58136)
surf74_zmax = openmc.ZPlane(z0=0.0)
surf74 = (surf74_cyl, surf74_zmin, surf74_zmax)
# Hole
surf75_cyl = openmc.ZCylinder(surface_id=75, x0=tr, y0=6.65, r=0.43)
surf75_zmin = openmc.ZPlane(z0=-11.58136)
surf75_zmax = openmc.ZPlane(z0=0.0)
surf75 = (surf75_cyl, surf75_zmin, surf75_zmax)
# Hole
surf76_cyl = openmc.ZCylinder(surface_id=76, x0=tr, y0=13.30, r=0.43)
surf76_zmin = openmc.ZPlane(z0=0.0)
surf76_zmax = openmc.ZPlane(z0=0.0)
surf76 = (surf76_cyl, surf76_zmin, surf76_zmax)
# Z3 CND 18-12 SST fin
surf99 = openmc.model.RectangularParallelepiped(-0.4144, 0, -0.0238, 0.0238, -0.3, 45.6)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf1 & -surf2
u1_cell2 = openmc.Cell(fill=mat6)
u1_cell2.region = +surf2 & -surf3
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = +surf1 & +surf2 & +surf3 & -surf4
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = +surf4 & -surf5
u1_cell5 = openmc.Cell(fill=mat6)
u1_cell5.region = +surf5 & +surf6 & -surf99
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = +surf5 & +surf6 & -surf7 & -surf8
u1_cell7 = openmc.Cell(fill=mat5)
u1_cell7.region = +surf5 & +surf6 & -surf7 & +surf10
u1_cell8 = openmc.Cell(fill=mat3)
u1_cell8.region = +surf5 & -surf6 & -surf7 & +surf9
u1_cell9 = openmc.Cell(fill=mat4)
u1_cell9.region = +surf5 & -surf6 & -surf7 & -surf9
u1_cell10 = openmc.Cell(fill=mat3)
u1_cell10.region = +surf5 & +surf6 & -surf7 & +surf9 & -surf10 & +surf99
u1_cell11 = openmc.Cell(fill=mat4)
u1_cell11.region = +surf5 & +surf6 & -surf7 & +surf8 & -surf9 & +surf99
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = +surf9 & -surf11
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = -surf9 & -surf11
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1])

u3_cell0 = openmc.Cell(fill=mat5)
u3_cell0.region = -surf12
u3_cell1 = openmc.Cell(fill=mat5)
u3_cell1.region = -surf13
u3_cell2 = openmc.Cell(fill=mat5)
u3_cell2.region = -surf14
u3_cell3 = openmc.Cell(fill=mat5)
u3_cell3.region = +surf15 & -surf16
u3_cell4 = openmc.Cell(fill=mat5)
u3_cell4.region = +surf12 & +surf16 & -surf17
u3_cell5 = openmc.Cell(fill=mat5)
u3_cell5.region = +surf12 & +surf16 & -surf18
u3_cell6 = openmc.Cell(fill=mat5)
u3_cell6.region = +surf12 & +surf16 & -surf19
u3_cell7 = openmc.Cell(fill=mat5)
u3_cell7.region = +surf12 & +surf16 & -surf20
u3_cell8 = openmc.Cell(fill=mat3)
u3_cell8.region = -surf15 & -surf16
u3_cell9 = openmc.Cell(fill=mat3)
u3_cell9.region = +surf9 & -surf11 & +surf14 & +surf16 & +surf17 & +surf18 & +surf19 & +surf20
u3_cell10 = openmc.Cell(fill=mat4)
u3_cell10.region = -surf9 & -surf11 & +surf12 & +surf13 & +surf17 & +surf18 & +surf19 & +surf20
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
cell1.region = -surf11 & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & +surf71 & +surf72 & +surf73 & +surf74 & +surf75 & +surf76

# Hole
cell2 = openmc.Cell(cell_id=2, fill=universe7)
cell2.region = -surf11 & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf71

# Hole
cell3 = openmc.Cell(cell_id=3, fill=universe7)
cell3.region = -surf11 & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf72

# Hole
cell4 = openmc.Cell(cell_id=4, fill=universe7)
cell4.region = -surf11 & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf73

# Hole
cell5 = openmc.Cell(cell_id=5, fill=universe7)
cell5.region = -surf11 & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf74

# Hole
cell6 = openmc.Cell(cell_id=6, fill=universe7)
cell6.region = -surf11 & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf75

# Hole
cell7 = openmc.Cell(cell_id=7, fill=universe7)
cell7.region = -surf11 & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf76

# Harray
cell8 = openmc.Cell(cell_id=8, fill=universe7)
cell8.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & +surf41 & +surf42 & +surf43 & +surf44 & +surf45 & +surf46 & +surf47 & +surf48 & +surf49 & +surf50 & +surf51 & +surf52

# NoHole
cell9 = openmc.Cell(cell_id=9, fill=universe3)
cell9.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf41

# NoHole
cell10 = openmc.Cell(cell_id=10, fill=universe3)
cell10.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf42

# NoHole
cell11 = openmc.Cell(cell_id=11, fill=universe3)
cell11.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf43

# NoHole
cell12 = openmc.Cell(cell_id=12, fill=universe3)
cell12.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf44

# NoHole
cell13 = openmc.Cell(cell_id=13, fill=universe3)
cell13.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf45

# NoHole
cell14 = openmc.Cell(cell_id=14, fill=universe3)
cell14.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf46

# NoHole
cell15 = openmc.Cell(cell_id=15, fill=universe3)
cell15.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf47

# NoHole
cell16 = openmc.Cell(cell_id=16, fill=universe3)
cell16.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf48

# NoHole
cell17 = openmc.Cell(cell_id=17, fill=universe3)
cell17.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf49

# NoHole
cell18 = openmc.Cell(cell_id=18, fill=universe3)
cell18.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf50

# NoHole
cell19 = openmc.Cell(cell_id=19, fill=universe3)
cell19.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf51

# NoHole
cell20 = openmc.Cell(cell_id=20, fill=universe3)
cell20.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf52

# Alles
cell21 = openmc.Cell(cell_id=21, fill=universe3)
cell21.region = -surf11 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & +surf61 & +surf62 & +surf63 & +surf64 & +surf65 & +surf66 & +surf67 & +surf68

# Hole
cell22 = openmc.Cell(cell_id=22, fill=universe7)
cell22.region = -surf11 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf61

# Hole
cell23 = openmc.Cell(cell_id=23, fill=universe7)
cell23.region = -surf11 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf62

# Hole
cell24 = openmc.Cell(cell_id=24, fill=universe7)
cell24.region = -surf11 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf63

# Hole
cell25 = openmc.Cell(cell_id=25, fill=universe7)
cell25.region = -surf11 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf64

# Hole
cell26 = openmc.Cell(cell_id=26, fill=universe7)
cell26.region = -surf11 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf65

# Hole
cell27 = openmc.Cell(cell_id=27, fill=universe7)
cell27.region = -surf11 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf66

# Hole
cell28 = openmc.Cell(cell_id=28, fill=universe7)
cell28.region = -surf11 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf67

# Hole
cell29 = openmc.Cell(cell_id=29, fill=universe7)
cell29.region = -surf11 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf68

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29])
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
source.space = openmc.stats.Point((0.0, 0.0, 15.795))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
