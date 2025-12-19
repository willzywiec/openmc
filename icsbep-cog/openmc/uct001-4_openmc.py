"""
U233-COMP-THERM-001: SB-3
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

# 233UO2-ThO2 Blanket
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U233", 2.228300e-04)
mat5.add_nuclide("U234", 3.538500e-06)
mat5.add_nuclide("U238", 2.760700e-06)
mat5.add_element("Th", 2.131100e-02)
mat5.add_nuclide("O16", 4.308000e-02)
mat5.add_element("Gd", 1.572300e-07)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Water/OR
surf1 = openmc.ZCylinder(surface_id=1, r=91.44, boundary_type="vacuum")
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
surf12 = openmc.ZCylinder(surface_id=12, x0=0.0, y0=0.0, r=0.32385)
# Fuel/Lower
surf13 = openmc.ZPlane(surface_id=13, z0=-19.05)
# Fuel/Upper
surf14 = openmc.ZPlane(surface_id=14, z0=19.05)
# Fuel/OR
surf15 = openmc.ZCylinder(surface_id=15, r=0.6223)
# Clad/IR
surf16 = openmc.ZCylinder(surface_id=16, r=0.63246)
# Clad/OR
surf17 = openmc.ZCylinder(surface_id=17, x0=0.0, y0=0.0, r=0.72263)
surf100 = openmc.model.RectangularParallelepiped(-500.0, 500.0, -500.0, 500.0, -500.0, 500.0)
surf101 = openmc.ZCylinder(surface_id=101, x0=-6.8961, y0=-7.81558, r=0.32385)
surf102 = openmc.ZCylinder(surface_id=102, x0=-5.97662, y0=-7.81558, r=0.32385)
surf103 = openmc.ZCylinder(surface_id=103, x0=-5.05714, y0=-7.81558, r=0.32385)
surf104 = openmc.ZCylinder(surface_id=104, x0=-4.13766, y0=-7.81558, r=0.32385)
surf105 = openmc.ZCylinder(surface_id=105, x0=-3.21818, y0=-7.81558, r=0.32385)
surf106 = openmc.ZCylinder(surface_id=106, x0=-2.2987, y0=-7.81558, r=0.32385)
surf107 = openmc.ZCylinder(surface_id=107, x0=-1.37922, y0=-7.81558, r=0.32385)
surf108 = openmc.ZCylinder(surface_id=108, x0=-0.45974, y0=-7.81558, r=0.32385)
surf109 = openmc.ZCylinder(surface_id=109, x0=0.45974, y0=-7.81558, r=0.32385)
surf110 = openmc.ZCylinder(surface_id=110, x0=1.37922, y0=-7.81558, r=0.32385)
surf111 = openmc.ZCylinder(surface_id=111, x0=2.2987, y0=-7.81558, r=0.32385)
surf112 = openmc.ZCylinder(surface_id=112, x0=3.21818, y0=-7.81558, r=0.32385)
surf113 = openmc.ZCylinder(surface_id=113, x0=4.13766, y0=-7.81558, r=0.32385)
surf114 = openmc.ZCylinder(surface_id=114, x0=5.05714, y0=-7.81558, r=0.32385)
surf115 = openmc.ZCylinder(surface_id=115, x0=5.97662, y0=-7.81558, r=0.32385)
surf116 = openmc.ZCylinder(surface_id=116, x0=6.8961, y0=-7.81558, r=0.32385)
surf120 = openmc.YPlane(surface_id=120, y0=-7.35584)
surf125 = openmc.YPlane(surface_id=125, y0=-2.75844)
surf130 = openmc.YPlane(surface_id=130, y0=1.83896)
surf135 = openmc.YPlane(surface_id=135, y0=6.43636)
# Seed Region/Long
surf141 = openmc.model.RectangularParallelepiped(-7.35584, 7.35584, -0.91948, 0.91948, -500.0, 500.0)
# Seed Region/Short
surf142 = openmc.model.RectangularParallelepiped(-5.51688, 5.51688, -8.27532, 8.27532, -500.0, 500.0)
surf201 = openmc.ZCylinder(surface_id=201, x0=-28.50388, y0=0.0, r=0.72263)
surf202 = openmc.ZCylinder(surface_id=202, x0=-26.66492, y0=0.0, r=0.72263)
surf203 = openmc.ZCylinder(surface_id=203, x0=-24.82596, y0=0.0, r=0.72263)
surf204 = openmc.ZCylinder(surface_id=204, x0=-22.987, y0=0.0, r=0.72263)
surf205 = openmc.ZCylinder(surface_id=205, x0=-21.14804, y0=0.0, r=0.72263)
surf206 = openmc.ZCylinder(surface_id=206, x0=-19.30908, y0=0.0, r=0.72263)
surf207 = openmc.ZCylinder(surface_id=207, x0=-17.47012, y0=0.0, r=0.72263)
surf208 = openmc.ZCylinder(surface_id=208, x0=-15.63116, y0=0.0, r=0.72263)
surf209 = openmc.ZCylinder(surface_id=209, x0=-13.7922, y0=0.0, r=0.72263)
surf210 = openmc.ZCylinder(surface_id=210, x0=-11.95324, y0=0.0, r=0.72263)
surf211 = openmc.ZCylinder(surface_id=211, x0=-10.11428, y0=0.0, r=0.72263)
surf212 = openmc.ZCylinder(surface_id=212, x0=-8.27532, y0=0.0, r=0.72263)
surf213 = openmc.ZCylinder(surface_id=213, x0=-6.43636, y0=0.0, r=0.72263)
surf214 = openmc.ZCylinder(surface_id=214, x0=-4.5974, y0=0.0, r=0.72263)
surf215 = openmc.ZCylinder(surface_id=215, x0=-2.75844, y0=0.0, r=0.72263)
surf216 = openmc.ZCylinder(surface_id=216, x0=-0.91948, y0=0.0, r=0.72263)
surf217 = openmc.ZCylinder(surface_id=217, x0=0.91948, y0=0.0, r=0.72263)
surf218 = openmc.ZCylinder(surface_id=218, x0=2.75844, y0=0.0, r=0.72263)
surf219 = openmc.ZCylinder(surface_id=219, x0=4.5974, y0=0.0, r=0.72263)
surf220 = openmc.ZCylinder(surface_id=220, x0=6.43636, y0=0.0, r=0.72263)
surf221 = openmc.ZCylinder(surface_id=221, x0=8.27532, y0=0.0, r=0.72263)
surf222 = openmc.ZCylinder(surface_id=222, x0=10.11428, y0=0.0, r=0.72263)
surf223 = openmc.ZCylinder(surface_id=223, x0=11.95324, y0=0.0, r=0.72263)
surf224 = openmc.ZCylinder(surface_id=224, x0=13.7922, y0=0.0, r=0.72263)
surf225 = openmc.ZCylinder(surface_id=225, x0=15.63116, y0=0.0, r=0.72263)
surf226 = openmc.ZCylinder(surface_id=226, x0=17.47012, y0=0.0, r=0.72263)
surf227 = openmc.ZCylinder(surface_id=227, x0=19.30908, y0=0.0, r=0.72263)
surf228 = openmc.ZCylinder(surface_id=228, x0=21.14804, y0=0.0, r=0.72263)
surf229 = openmc.ZCylinder(surface_id=229, x0=22.987, y0=0.0, r=0.72263)
surf230 = openmc.ZCylinder(surface_id=230, x0=24.82596, y0=0.0, r=0.72263)
surf231 = openmc.ZCylinder(surface_id=231, x0=26.66492, y0=0.0, r=0.72263)
surf232 = openmc.ZCylinder(surface_id=232, x0=28.50388, y0=0.0, r=0.72263)
surf240 = openmc.YPlane(surface_id=240, y0=-30.34284)
surf245 = openmc.YPlane(surface_id=245, y0=-21.14804)
surf250 = openmc.YPlane(surface_id=250, y0=-11.95324)
surf255 = openmc.YPlane(surface_id=255, y0=-2.75844)
surf260 = openmc.YPlane(surface_id=260, y0=6.43636)
surf265 = openmc.YPlane(surface_id=265, y0=15.63116)
surf270 = openmc.YPlane(surface_id=270, y0=24.82596)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1270, z0=-56.2991, boundary_type="vacuum")
surf1_zmax = openmc.ZPlane(surface_id=1271, z0=56.2991, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = -surf10 & -surf12 & +surf13 & -surf14
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = -surf10 & -surf12 & -surf13
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = -surf10 & -surf12 & +surf14
u1_cell3 = openmc.Cell()
u1_cell3.region = +surf10 & -surf11 & -surf12
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf11 & -surf12
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf100 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf111 & +surf112 & +surf113 & +surf114 & +surf115 & +surf116
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat5)
u4_cell0.region = -surf15 & -surf17 & +surf13 & -surf14
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf15 & -surf17 & -surf13
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf15 & -surf17 & +surf14
u4_cell3 = openmc.Cell()
u4_cell3.region = +surf15 & -surf16 & -surf17
u4_cell4 = openmc.Cell(fill=mat4)
u4_cell4.region = +surf16 & -surf17
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

u5_cell0 = openmc.Cell(fill=mat1)
u5_cell0.region = -surf100 & +surf201 & +surf202 & +surf203 & +surf204 & +surf205 & +surf206 & +surf207 & +surf208 & +surf209 & +surf210
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0])

universe6 = openmc.Universe(universe_id=6, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Cntrl
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf2

# Cntrl
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf3

# Cntrl
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf4

# Cntrl
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf5

# Zr2
cell17 = openmc.Cell(cell_id=17, fill=mat4)
cell17.region = +surf11 & -surf12

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
