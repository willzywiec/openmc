"""
PMF003-4: LLNL Pu Array - 3x3x3 with polyethylene reflection on one side - case 104
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium billet
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.601000e-02)
mat1.add_nuclide("Pu240", 2.923600e-03)
mat1.add_nuclide("Pu241", 2.243300e-04)
mat1.add_nuclide("Pu242", 4.856600e-06)

# Aluminum tube, spacer, and can walls and bottoms
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 6.026300e-02)

# Aluminum table top
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.303100e-02)

# Aluminum "top" heat sinks
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 3.674200e-02)

# Aluminum "bottom" heat sinks
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 3.013900e-02)

# Iron (steel) lid
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 8.412200e-02)

# Iron (steel) table support
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Fe", 5.888500e-03)

# Homogenized "shoe"
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 2.926000e-02)
mat8.add_element("Fe", 7.791100e-03)

# Polyethylene (CH2) reflector
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_nuclide("H1", 7.899600e-02)
mat9.add_element("C", 3.949800e-02)
mat9.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9])

# ==============================================================================
# Geometry
# ==============================================================================

# Boundary condition
surf1 = openmc.model.RectangularParallelepiped(-66.0, 66.0, -23.0, 23.0, -32.54, 45.733)
# Table/botom
surf2 = openmc.ZPlane(surface_id=2, z0=-2.54)
# Table/top
surf3 = openmc.ZPlane(surface_id=3, z0=0.0)
# Shoe
surf4 = openmc.ZCylinder(surface_id=4, r=3.425)
# Tube/inner
surf5 = openmc.ZCylinder(surface_id=5, r=3.425)
# Tube/outer
surf6 = openmc.ZCylinder(surface_id=6, r=3.609)
# Spacer/inner
surf10 = openmc.ZCylinder(surface_id=10, r=3.104)
# Spacer/outer
surf11 = openmc.ZCylinder(surface_id=11, x0=0.0, y0=0.0, r=3.326)
# Bottom heat sink
surf12 = openmc.ZCylinder(surface_id=12, x0=0.0, y0=0.0, r=3.2995)
# Lid
surf13 = openmc.ZCylinder(surface_id=13, x0=0.0, y0=0.0, r=3.2995)
# Pu/outer & Can wall/inner
surf14 = openmc.ZCylinder(surface_id=14, r=3.2625)
# Can wall/outer
surf15 = openmc.ZCylinder(surface_id=15, x0=0.0, y0=0.0, r=3.2995)
# Can bottom
surf16 = openmc.ZCylinder(surface_id=16, x0=0.0, y0=0.0, r=3.2995)
# Top heat sink
surf17 = openmc.ZCylinder(surface_id=17, x0=0.0, y0=0.0, r=3.2995)
# Spacer/outer
surf21 = openmc.ZCylinder(surface_id=21, x0=0.0, y0=0.0, r=3.326)
# Bottom heat sink
surf22 = openmc.ZCylinder(surface_id=22, x0=0.0, y0=0.0, r=3.2995)
# Lid
surf23 = openmc.ZCylinder(surface_id=23, x0=0.0, y0=0.0, r=3.2995)
# Pu/outer & Can wall/inner
surf24 = openmc.ZCylinder(surface_id=24, r=3.2625)
# Can wall/outer
surf25 = openmc.ZCylinder(surface_id=25, x0=0.0, y0=0.0, r=3.2995)
# Can bottom
surf26 = openmc.ZCylinder(surface_id=26, x0=0.0, y0=0.0, r=3.2995)
# Top heat sink
surf27 = openmc.ZCylinder(surface_id=27, x0=0.0, y0=0.0, r=3.2995)
# Spacer/outer
surf31 = openmc.ZCylinder(surface_id=31, x0=0.0, y0=0.0, r=3.326)
# Bottom heat sink
surf32 = openmc.ZCylinder(surface_id=32, x0=0.0, y0=0.0, r=3.2995)
# Lid
surf33 = openmc.ZCylinder(surface_id=33, x0=0.0, y0=0.0, r=3.2995)
# Pu/outer & Can wall/inner
surf34 = openmc.ZCylinder(surface_id=34, r=3.2625)
# Can wall/outer
surf35 = openmc.ZCylinder(surface_id=35, x0=0.0, y0=0.0, r=3.2995)
# Can bottom
surf36 = openmc.ZCylinder(surface_id=36, x0=0.0, y0=0.0, r=3.2995)
# Top heat sink
surf37 = openmc.ZCylinder(surface_id=37, x0=0.0, y0=0.0, r=3.2995)
# 1st
surf41 = openmc.ZCylinder(surface_id=41, x0=-10.15, y0=10.15, r=3.609)
# 2nd
surf42 = openmc.ZCylinder(surface_id=42, x0=-10.15, y0=0.0, r=3.609)
# 3rd
surf43 = openmc.ZCylinder(surface_id=43, x0=-10.15, y0=-10.15, r=3.609)
# 4th
surf44 = openmc.ZCylinder(surface_id=44, x0=0.0, y0=10.15, r=3.609)
# 5th
surf45 = openmc.ZCylinder(surface_id=45, x0=0.0, y0=0.0, r=3.609)
# 6th
surf46 = openmc.ZCylinder(surface_id=46, x0=0.0, y0=-10.15, r=3.609)
# 7th
surf47 = openmc.ZCylinder(surface_id=47, x0=10.15, y0=10.15, r=3.609)
# 8th
surf48 = openmc.ZCylinder(surface_id=48, x0=10.15, y0=0.0, r=3.609)
# 9th
surf49 = openmc.ZCylinder(surface_id=49, x0=10.15, y0=-10.15, r=3.609)
surf51 = openmc.model.RectangularParallelepiped(-34.4825, -13.842500000000001, -17.515, 17.515, 0.0, 45.08)

# Z-plane surfaces for bounded cylinders
surf4_zmin = openmc.ZPlane(surface_id=1051, z0=0.0)
surf4_zmax = openmc.ZPlane(surface_id=1052, z0=8.3)
surf6_zmin = openmc.ZPlane(surface_id=1053, z0=0.0)
surf6_zmax = openmc.ZPlane(surface_id=1054, z0=45.734)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat8)
u1_cell0.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = (-surf6 & +surf6_zmin & -surf6_zmax) & +surf10 & -surf11
u1_cell3 = openmc.Cell(fill=mat5)
u1_cell3.region = +surf11 & -surf12
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = +surf12 & -surf13
u1_cell5 = openmc.Cell(fill=mat1)
u1_cell5.region = +surf13 & -surf14 & -surf15
u1_cell6 = openmc.Cell(fill=mat2)
u1_cell6.region = +surf13 & +surf14 & -surf15
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = +surf15 & -surf16
u1_cell8 = openmc.Cell(fill=mat4)
u1_cell8.region = +surf16 & -surf17
u1_cell9 = openmc.Cell(fill=mat2)
u1_cell9.region = +surf10 & +surf17 & -surf21
u1_cell10 = openmc.Cell(fill=mat5)
u1_cell10.region = +surf21 & -surf22
u1_cell11 = openmc.Cell(fill=mat6)
u1_cell11.region = +surf22 & -surf23
u1_cell12 = openmc.Cell(fill=mat1)
u1_cell12.region = +surf23 & -surf14 & -surf25
u1_cell13 = openmc.Cell(fill=mat2)
u1_cell13.region = +surf23 & +surf24 & -surf25
u1_cell14 = openmc.Cell(fill=mat2)
u1_cell14.region = +surf25 & -surf26
u1_cell15 = openmc.Cell(fill=mat4)
u1_cell15.region = +surf26 & -surf27
u1_cell16 = openmc.Cell(fill=mat2)
u1_cell16.region = +surf10 & +surf27 & -surf31
u1_cell17 = openmc.Cell(fill=mat5)
u1_cell17.region = +surf31 & -surf32
u1_cell18 = openmc.Cell(fill=mat6)
u1_cell18.region = +surf32 & -surf33
u1_cell19 = openmc.Cell(fill=mat1)
u1_cell19.region = +surf33 & -surf34 & -surf35
u1_cell20 = openmc.Cell(fill=mat2)
u1_cell20.region = +surf33 & +surf34 & -surf35
u1_cell21 = openmc.Cell(fill=mat2)
u1_cell21.region = +surf35 & -surf36
u1_cell22 = openmc.Cell(fill=mat4)
u1_cell22.region = +surf36 & -surf37
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11, u1_cell12, u1_cell13, u1_cell14, u1_cell15, u1_cell16, u1_cell17, u1_cell18, u1_cell19, u1_cell20, u1_cell21, u1_cell22])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Spprt
cell1 = openmc.Cell(cell_id=1, fill=mat7)
cell1.region = -surf1 & -surf2

# Table
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = -surf1 & +surf2 & -surf3

# Stack1
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (-10.15, 10.15, 0.0)
cell3.region = -surf1 & +surf3 & -surf41

# Stack2
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (-10.15, 0.0, 0.0)
cell4.region = -surf1 & +surf3 & -surf42

# Stack3
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (-10.15, -10.15, 0.0)
cell5.region = -surf1 & +surf3 & -surf43

# Stack4
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (0.0, 10.15, 0.0)
cell6.region = -surf1 & +surf3 & -surf44

# Stack5
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.translation = (0.0, 0.0, 0.0)
cell7.region = -surf1 & +surf3 & -surf45

# Stack6
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.translation = (0.0, -10.15, 0.0)
cell8.region = -surf1 & +surf3 & -surf46

# Stack7
cell9 = openmc.Cell(cell_id=9, fill=universe1)
cell9.translation = (10.15, 10.15, 0.0)
cell9.region = -surf1 & +surf3 & -surf47

# Stack8
cell10 = openmc.Cell(cell_id=10, fill=universe1)
cell10.translation = (10.15, 0.0, 0.0)
cell10.region = -surf1 & +surf3 & -surf48

# Stack9
cell11 = openmc.Cell(cell_id=11, fill=universe1)
cell11.translation = (10.15, -10.15, 0.0)
cell11.region = -surf1 & +surf3 & -surf49

# Poly
cell12 = openmc.Cell(cell_id=12, fill=mat9)
cell12.region = +surf3 & -surf51

# THS
cell36 = openmc.Cell(cell_id=36, fill=mat4)
cell36.region = +surf36 & -surf37

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell36])
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
source.space = openmc.stats.Box((-11.15, -11.15, 16.5), (11.15, 11.15, 33.8))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
