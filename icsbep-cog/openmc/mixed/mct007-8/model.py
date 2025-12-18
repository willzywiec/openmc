"""
MCT007-8: Central B2 absorber rod and 193+6=199 MOX pins with 2.6670 cm pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# MOX fuel
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.427200e-04)
mat1.add_nuclide("Pu240", 6.988800e-05)
mat1.add_nuclide("Pu241", 7.523600e-06)
mat1.add_nuclide("Am241", 1.560900e-06)
mat1.add_nuclide("Pu242", 8.450700e-07)
mat1.add_nuclide("U234", 1.144800e-06)
mat1.add_nuclide("U235", 1.498700e-04)
mat1.add_nuclide("U238", 2.066400e-02)
mat1.add_nuclide("O16", 4.309100e-02)

# UO2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 1.137100e-06)
mat2.add_nuclide("U235", 1.488600e-04)
mat2.add_nuclide("U238", 2.052500e-02)
mat2.add_nuclide("O16", 4.194400e-02)

# Zr-2
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Zr", 4.262100e-02)
mat3.add_element("Sn", 4.832700e-04)
mat3.add_element("Fe", 9.564200e-05)
mat3.add_element("Ni", 3.033600e-05)
mat3.add_element("Cr", 7.609300e-05)

# Water (case 2)
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.669800e-02)
mat4.add_nuclide("O16", 3.334900e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Lucite
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("H", 5.678200e-02)
mat5.add_element("C", 3.548900e-02)
mat5.add_nuclide("O16", 1.419600e-02)

# Al-6061
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Al", 5.843300e-02)
mat6.add_element("Si", 3.460700e-04)
mat6.add_element("Fe", 1.015200e-04)
mat6.add_element("Cu", 6.373100e-05)
mat6.add_element("Mn", 2.215500e-05)
mat6.add_element("Mg", 6.665100e-04)
mat6.add_element("Cr", 6.231000e-05)
mat6.add_element("Zn", 3.096700e-05)
mat6.add_element("Ti", 2.537500e-05)

# B2 absorber
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("B10", 4.534900e-04)
mat7.add_nuclide("B11", 1.825400e-03)
mat7.add_element("Al", 5.503500e-02)
mat7.add_nuclide("O16", 1.259700e-04)
mat7.add_element("Mg", 1.974400e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# MOX fuel
surf1 = openmc.ZCylinder(surface_id=1, x0=3.1035, y0=94.0435, r=0.64135)
# UO2
surf2 = openmc.ZCylinder(surface_id=2, x0=2.6035, y0=3.1035, r=0.64135)
# Zr-2
surf3 = openmc.ZCylinder(surface_id=3, x0=1.9050, y0=94.8690, r=0.71755)
# Absorber
surf4 = openmc.ZCylinder(surface_id=4, x0=2.6035, y0=94.0435, r=0.46736)
# Zr-2
surf5 = openmc.ZCylinder(surface_id=5, x0=1.9050, y0=94.8690, r=0.53594)
# Water hole
surf6 = openmc.ZCylinder(surface_id=6, x0=1.9050, y0=94.8690, r=0.71755)
# Boundary condition
surf10 = openmc.ZCylinder(surface_id=10, x0=-16.1925, y0=115.3795, r=60.0, boundary_type="vacuum")
# Al
surf11 = openmc.ZPlane(surface_id=11, z0=-14.9225)
# Lucite, lower
surf12 = openmc.ZCylinder(surface_id=12, x0=0.0, y0=1.9050, r=99.9)
# Lucite, middle
surf13 = openmc.ZCylinder(surface_id=13, x0=24.4475, y0=26.3525, r=99.9)
# Lucite, upper
surf14 = openmc.ZCylinder(surface_id=14, x0=70.1675, y0=72.0725, r=99.9)
# Hexagonal
# Prism 20: 6-sided polygon
surf20_0 = openmc.Plane(a=0.8660254270, b=0.4999999597, c=0, d=17.3226736044)
surf20_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=17.3226750000)
surf20_2 = openmc.Plane(a=-0.8660254270, b=0.4999999597, c=0, d=17.3226736044)
surf20_3 = openmc.Plane(a=-0.8660254270, b=-0.4999999597, c=0, d=17.3226736044)
surf20_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=17.3226750000)
surf20_5 = openmc.Plane(a=0.8660254270, b=-0.4999999597, c=0, d=17.3226736044)
# X-Y prism for fuel
surf21 = openmc.model.RectangularParallelepiped(-6.6675, 6.6675, -19.632365, 19.632365, -499.9995, 499.9995)
# X-Y prism for fuel
surf22 = openmc.model.RectangularParallelepiped(-6.6675, 6.6675, -19.632365, 19.632365, -499.9995, 499.9995)
# X-Y prism for fuel
surf23 = openmc.model.RectangularParallelepiped(-6.6675, 6.6675, -19.632365, 19.632365, -499.9995, 499.9995)
# X-Y prism for Lucite
surf24 = openmc.model.RectangularParallelepiped(-21.336, 21.336, -20.7873, 20.7873, -499.9995, 499.9995)
# Unit
# surf31: Error converting surface type "c": could not convert string to float: 'tr'
# triangular
# surf32: Error converting surface type "c": could not convert string to float: 'tr'
# cell
# surf33: Error converting surface type "c": could not convert string to float: 'tr'
# of seven
# surf34: Error converting surface type "c": could not convert string to float: 'tr'
# fuel
# surf35: Error converting surface type "c": could not convert string to float: 'tr'
# pins
# surf36: Error converting surface type "c": could not convert string to float: 'tr'
# Peripheral rod #6
surf46_cyl = openmc.ZCylinder(surface_id=46, x0=tr, y0=-12.0015, r=0.72)
surf46_zmin = openmc.ZPlane(z0=-16.16783)
surf46_zmax = openmc.ZPlane(z0=0.0)
surf46 = (surf46_cyl, surf46_zmin, surf46_zmax)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf1 & -surf2
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = +surf1 & +surf2 & -surf3
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

u2_cell0 = openmc.Cell(fill=mat6)
u2_cell0.region = -surf10 & -surf11
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = -surf12 & -surf24
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = -surf13 & -surf24
u2_cell3 = openmc.Cell(fill=mat5)
u2_cell3.region = -surf14 & -surf24
u2_cell4 = openmc.Cell(fill=mat4)
u2_cell4.region = -surf10 & +surf11 & +surf12 & +surf13 & +surf14 & -surf24
u2_cell5 = openmc.Cell(fill=mat4)
u2_cell5.region = -surf10 & +surf11 & +surf24
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = -surf3
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf31
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf32
u4_cell3 = openmc.Cell(fill=mat4)
u4_cell3.region = -surf33
u4_cell4 = openmc.Cell(fill=mat4)
u4_cell4.region = -surf34
u4_cell5 = openmc.Cell(fill=mat4)
u4_cell5.region = -surf35
u4_cell6 = openmc.Cell(fill=mat4)
u4_cell6.region = -surf36
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4, u4_cell5, u4_cell6])

# Lattice 5: 9x11 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-24.003, -25.40659]
lattice5.pitch = [5.334000, 4.619380]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 9x11 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-24.003, -25.40659]
lattice6.pitch = [5.334000, 4.619380]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Absrbr
cell1 = openmc.Cell(cell_id=1, fill=mat7)
cell1.region = -surf4

# Zr2
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = +surf4 & -surf5 & -surf6

# Water
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = +surf4 & +surf5 & -surf6

# Farray
cell4 = openmc.Cell(cell_id=4, fill=universe5)
cell4.region = +surf6 & -surf10 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5)

# Farray
cell5 = openmc.Cell(cell_id=5, fill=universe5)
cell5.region = -surf10 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5) & -surf21

# Farray
cell6 = openmc.Cell(cell_id=6, fill=universe5)
cell6.region = -surf10 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5) & +surf21 & -surf22

# Farray
cell7 = openmc.Cell(cell_id=7, fill=universe5)
cell7.region = -surf10 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5) & +surf21 & +surf22 & -surf23

# Harray
cell8 = openmc.Cell(cell_id=8, fill=universe6)
cell8.region = -surf10 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5) & +surf21 & +surf22 & +surf23 & -surf24 & +surf46

# Fpin
cell9 = openmc.Cell(cell_id=9, fill=universe5)
cell9.region = -surf10 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5) & +surf21 & +surf22 & +surf23 & -surf24 & -surf46

# Alles
cell10 = openmc.Cell(cell_id=10, fill=universe2)
cell10.region = -surf10 & +surf24

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10])
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
source.space = openmc.stats.Box((-4.5204, -4.04879, 47.5735), (4.5204, 4.04879, 49.5735))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
