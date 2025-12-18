"""
MCT011-4: 127 Rapsodie pins with 2.5 cm pitch and Hc = 39.03 cm
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
surf9 = openmc.ZPlane(surface_id=9, z0=39.03)
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
surf30_0 = openmc.Plane(a=0.8660252067, b=0.5000003414, c=0, d=14.0729096086)
surf30_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=14.0729000000)
surf30_2 = openmc.Plane(a=-0.8660252067, b=0.5000003414, c=0, d=14.0729096086)
surf30_3 = openmc.Plane(a=-0.8660252067, b=-0.5000003414, c=0, d=14.0729096086)
surf30_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=14.0729000000)
surf30_5 = openmc.Plane(a=0.8660252067, b=-0.5000003414, c=0, d=14.0729096086)
# Inner X-Y prism for holes
surf31 = openmc.model.RectangularParallelepiped(-7.5, 7.5, -16.238, 16.238, -499.9995, 499.9995)
# Inner X-Y prism for holes
surf32 = openmc.model.RectangularParallelepiped(-7.5, 7.5, -16.238, 16.238, -499.9995, 499.9995)
# Inner X-Y prism for holes
surf33 = openmc.model.RectangularParallelepiped(-7.5, 7.5, -16.238, 16.238, -499.9995, 499.9995)
# Z3 CND 18-12 SST fin
surf91 = openmc.model.RectangularParallelepiped(-0.4144, 0, -0.0238, 0.0238, -0.3, 45.6)
surf99 = openmc.ZCylinder(surface_id=99, r=17.5)

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
u1_cell5.region = +surf5 & +surf6 & -surf91
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = +surf5 & +surf6 & -surf7 & -surf8
u1_cell7 = openmc.Cell(fill=mat5)
u1_cell7.region = +surf5 & +surf6 & -surf7 & +surf10
u1_cell8 = openmc.Cell(fill=mat3)
u1_cell8.region = +surf5 & -surf6 & -surf7 & +surf9
u1_cell9 = openmc.Cell(fill=mat4)
u1_cell9.region = +surf5 & -surf6 & -surf7 & -surf9
u1_cell10 = openmc.Cell(fill=mat3)
u1_cell10.region = +surf5 & +surf6 & -surf7 & +surf9 & -surf10 & +surf91
u1_cell11 = openmc.Cell(fill=mat4)
u1_cell11.region = +surf5 & +surf6 & -surf7 & +surf8 & -surf9 & +surf91
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
lattice6.lower_left = [-27.5, -23.8156985]
lattice6.pitch = [5.000000, 4.330127]
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
lattice7.lower_left = [-27.5, -23.8156985]
lattice7.pitch = [5.000000, 4.330127]
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
cell1.region = -surf11 & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & -surf99

# Harray
cell2 = openmc.Cell(cell_id=2, fill=universe7)
cell2.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & -surf31 & -surf99

# Harray
cell3 = openmc.Cell(cell_id=3, fill=universe7)
cell3.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & +surf31 & -surf32 & -surf99

# Harray
cell4 = openmc.Cell(cell_id=4, fill=universe7)
cell4.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & +surf31 & +surf32 & -surf33 & -surf99

# Alles
cell5 = openmc.Cell(cell_id=5, fill=universe3)
cell5.region = -surf11 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & +surf31 & +surf32 & +surf33 & -surf99

# Alles
cell6 = openmc.Cell(cell_id=6, fill=universe3)
cell6.region = -surf11 & +surf99

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6])
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
source.space = openmc.stats.Point((0.0, 0.0, 19.515))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
