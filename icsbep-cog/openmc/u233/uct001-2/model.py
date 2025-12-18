"""
U233-COMP-THERM-001: SB-2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Water at 20C
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 6.673500e-02)
mat1.add_nuclide("O16", 3.336800e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Borated SST
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.925900e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Mn", 8.681600e-04)
mat2.add_element("Ni", 7.517100e-03)
mat2.add_nuclide("B10", 3.748800e-03)

# 233UO2-ZrO2 Seed
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U233", 3.989100e-03)
mat3.add_nuclide("U234", 6.369000e-05)
mat3.add_nuclide("U238", 4.575900e-05)
mat3.add_nuclide("O16", 5.393200e-02)
mat3.add_element("Zr", 2.286700e-02)

# Zircalloy-2
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Zr", 4.253700e-02)
mat4.add_element("Sn", 4.991800e-04)

# ThO2 Blanket with Gd
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Th", 2.164100e-02)
mat5.add_nuclide("O16", 4.328200e-02)
mat5.add_element("Gd", 9.260700e-08)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Water/OR
surf1 = openmc.ZCylinder(surface_id=1, x0=-56.2991, y0=56.2991, r=91.44, boundary_type="vacuum")
# Z-Lo = -200/2 + 115.765 = 15.765 cm
surf2 = openmc.model.RectangularParallelepiped(-3.81, 3.81, -5.605779999999999, -5.42798, 15.765, 215.765)
surf3 = openmc.model.RectangularParallelepiped(-3.81, 3.81, -1.92786, -1.75006, 15.765, 215.765)
surf4 = openmc.model.RectangularParallelepiped(-3.81, 3.81, 1.75006, 1.92786, 15.765, 215.765)
surf5 = openmc.model.RectangularParallelepiped(-3.81, 3.81, 5.42798, 5.605779999999999, 15.765, 215.765)
# Fuel/OR
surf10 = openmc.ZCylinder(surface_id=10, r=0.26797)
# Clad/IR
surf11 = openmc.ZCylinder(surface_id=11, r=0.2794)
# Clad/OR
# surf12: Error converting surface type "cylinder": could not convert string to float: 'tr'
# Fuel/Lower
surf13 = openmc.ZPlane(surface_id=13, z0=-19.05)
# Fuel/Upper
surf14 = openmc.ZPlane(surface_id=14, z0=19.05)
# Fuel/OR
surf15 = openmc.ZCylinder(surface_id=15, r=0.62103)
# Clad/IR
surf16 = openmc.ZCylinder(surface_id=16, r=0.63373)
# Clad/OR
# surf17: Error converting surface type "cylinder": could not convert string to float: 'tr'
surf100 = openmc.model.RectangularParallelepiped(-500.0, 500.0, -500.0, 500.0, -500.0, 500.0)
# surf101: Unsupported surface type "sameas" with params ['12', 'tr', '-9.65454', '-9.65454', '0', '102', 'sameas', '12', 'tr', '-8.73506', '-9.65454', '0', '103', 'sameas', '12', 'tr', '-7.81558', '-9.65454', '0']
# surf104: Unsupported surface type "sameas" with params ['12', 'tr', '-6.89610', '-9.65454', '0', '105', 'sameas', '12', 'tr', '-5.97662', '-9.65454', '0', '106', 'sameas', '12', 'tr', '-5.05714', '-9.65454', '0']
# surf107: Unsupported surface type "sameas" with params ['12', 'tr', '-4.13766', '-9.65454', '0', '108', 'sameas', '12', 'tr', '-3.21818', '-9.65454', '0', '109', 'sameas', '12', 'tr', '-2.29870', '-9.65454', '0']
# surf110: Unsupported surface type "sameas" with params ['12', 'tr', '-1.37922', '-9.65454', '0', '111', 'sameas', '12', 'tr', '-0.45974', '-9.65454', '0', '112', 'sameas', '12', 'tr', '0.45974', '-9.65454', '0']
# surf113: Unsupported surface type "sameas" with params ['12', 'tr', '1.37922', '-9.65454', '0', '114', 'sameas', '12', 'tr', '2.29870', '-9.65454', '0', '115', 'sameas', '12', 'tr', '3.21818', '-9.65454', '0']
# surf116: Unsupported surface type "sameas" with params ['12', 'tr', '4.13766', '-9.65454', '0', '117', 'sameas', '12', 'tr', '5.05714', '-9.65454', '0', '118', 'sameas', '12', 'tr', '5.97662', '-9.65454', '0']
# surf119: Unsupported surface type "sameas" with params ['12', 'tr', '6.89610', '-9.65454', '0', '120', 'sameas', '12', 'tr', '7.81558', '-9.65454', '0', '121', 'sameas', '12', 'tr', '8.73506', '-9.65454', '0']
# surf122: Unsupported surface type "sameas" with params ['12', 'tr', '9.65454', '-9.65454', '0']
surf130 = openmc.YPlane(surface_id=130, y0=-9.19480)
surf135 = openmc.YPlane(surface_id=135, y0=-4.59740)
surf140 = openmc.YPlane(surface_id=140, y0=0.00000)
surf145 = openmc.YPlane(surface_id=145, y0=4.59740)
surf150 = openmc.YPlane(surface_id=150, y0=9.19480)
# Seed Region/Wide
surf151 = openmc.model.RectangularParallelepiped(-10.11428, 10.11428, -0.91948, 0.91948, -500.0, 500.0)
# Seed Region/Square
surf152 = openmc.model.RectangularParallelepiped(-8.27532, 8.27532, -8.27532, 8.27532, -500.0, 500.0)
# Seed Region/High
surf153 = openmc.model.RectangularParallelepiped(-0.91948, 0.91948, -10.11428, 10.11428, -500.0, 500.0)
# surf201: Unsupported surface type "sameas" with params ['17', 'tr', '-31.26232', '0', '0', '202', 'sameas', '17', 'tr', '-29.42336', '0', '0', '203', 'sameas', '17', 'tr', '-27.58440', '0', '0']
# surf204: Unsupported surface type "sameas" with params ['17', 'tr', '-25.74544', '0', '0', '205', 'sameas', '17', 'tr', '-23.90648', '0', '0', '206', 'sameas', '17', 'tr', '-22.06752', '0', '0']
# surf207: Unsupported surface type "sameas" with params ['17', 'tr', '-20.22856', '0', '0', '208', 'sameas', '17', 'tr', '-18.38960', '0', '0', '209', 'sameas', '17', 'tr', '-16.55064', '0', '0']
# surf210: Unsupported surface type "sameas" with params ['17', 'tr', '-14.71168', '0', '0', '211', 'sameas', '17', 'tr', '-12.87272', '0', '0', '212', 'sameas', '17', 'tr', '-11.03376', '0', '0']
# surf213: Unsupported surface type "sameas" with params ['17', 'tr', '-9.19480', '0', '0', '214', 'sameas', '17', 'tr', '-7.35584', '0', '0', '215', 'sameas', '17', 'tr', '-5.51688', '0', '0']
# surf216: Unsupported surface type "sameas" with params ['17', 'tr', '-3.67792', '0', '0', '217', 'sameas', '17', 'tr', '-1.83896', '0', '0', '218', 'sameas', '17']
# surf219: Unsupported surface type "sameas" with params ['17', 'tr', '1.83896', '0', '0', '220', 'sameas', '17', 'tr', '3.67792', '0', '0', '221', 'sameas', '17', 'tr', '5.51688', '0', '0']
# surf222: Unsupported surface type "sameas" with params ['17', 'tr', '7.35584', '0', '0', '223', 'sameas', '17', 'tr', '9.19480', '0', '0', '224', 'sameas', '17', 'tr', '11.03376', '0', '0']
# surf225: Unsupported surface type "sameas" with params ['17', 'tr', '12.87272', '0', '0', '226', 'sameas', '17', 'tr', '14.71168', '0', '0', '227', 'sameas', '17', 'tr', '16.55064', '0', '0']
# surf228: Unsupported surface type "sameas" with params ['17', 'tr', '18.38960', '0', '0', '229', 'sameas', '17', 'tr', '20.22856', '0', '0', '230', 'sameas', '17', 'tr', '22.06752', '0', '0']
# surf231: Unsupported surface type "sameas" with params ['17', 'tr', '23.90648', '0', '0', '232', 'sameas', '17', 'tr', '25.74544', '0', '0', '233', 'sameas', '17', 'tr', '27.58440', '0', '0']
# surf234: Unsupported surface type "sameas" with params ['17', 'tr', '29.42336', '0', '0', '235', 'sameas', '17', 'tr', '31.26232', '0', '0']
surf240 = openmc.YPlane(surface_id=240, y0=-30.34284)
surf245 = openmc.YPlane(surface_id=245, y0=-21.14804)
surf250 = openmc.YPlane(surface_id=250, y0=-11.95324)
surf255 = openmc.YPlane(surface_id=255, y0=-2.75844)
surf260 = openmc.YPlane(surface_id=260, y0=6.43636)
surf265 = openmc.YPlane(surface_id=265, y0=15.63116)
surf270 = openmc.YPlane(surface_id=270, y0=24.82596)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = -surf10 & +surf13 & -surf14
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = -surf10 & -surf13
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = -surf10 & +surf14
u1_cell3 = openmc.Cell()
u1_cell3.region = +surf10 & -surf11
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf11
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf100
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat5)
u4_cell0.region = -surf15 & +surf13 & -surf14
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf15 & -surf13
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf15 & +surf14
u4_cell3 = openmc.Cell()
u4_cell3.region = +surf15 & -surf16
u4_cell4 = openmc.Cell(fill=mat4)
u4_cell4.region = +surf16
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

u5_cell0 = openmc.Cell(fill=mat1)
u5_cell0.region = -surf100
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0])

universe6 = openmc.Universe(universe_id=6, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Cntrl
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = -surf1 & -surf2

# Cntrl
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = -surf1 & -surf3

# Cntrl
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = -surf1 & -surf4

# Cntrl
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = -surf1 & -surf5

# Zr2
cell17 = openmc.Cell(cell_id=17, fill=mat4)
cell17.region = +surf11

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell17])
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
source.space = openmc.stats.Box((-1.4, -1.4, -1.0), (1.4, 1.4, 1.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
