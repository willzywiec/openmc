"""
U233-COMP-THERM-001: SB-2-1/2
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

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Water/OR
surf1 = openmc.ZCylinder(surface_id=1, r=91.44, boundary_type="vacuum")
# Z-Lo = -200/2 + 116.05 = 16.05 cm
surf2 = openmc.model.RectangularParallelepiped(-3.81, 3.81, -5.605779999999999, -5.42798, 16.049999999999997, 216.05)
surf3 = openmc.model.RectangularParallelepiped(-3.81, 3.81, -1.92786, -1.75006, 16.049999999999997, 216.05)
surf4 = openmc.model.RectangularParallelepiped(-3.81, 3.81, 1.75006, 1.92786, 16.049999999999997, 216.05)
surf5 = openmc.model.RectangularParallelepiped(-3.81, 3.81, 5.42798, 5.605779999999999, 16.049999999999997, 216.05)
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
surf100 = openmc.model.RectangularParallelepiped(-500.0, 500.0, -500.0, 500.0, -500.0, 500.0)
surf101 = openmc.ZCylinder(surface_id=101, x0=-7.81558, y0=-6.8961, r=0.32385)
surf102 = openmc.ZCylinder(surface_id=102, x0=-6.8961, y0=-6.8961, r=0.32385)
surf103 = openmc.ZCylinder(surface_id=103, x0=-5.97662, y0=-6.8961, r=0.32385)
surf104 = openmc.ZCylinder(surface_id=104, x0=-5.05714, y0=-6.8961, r=0.32385)
surf105 = openmc.ZCylinder(surface_id=105, x0=-4.13766, y0=-6.8961, r=0.32385)
surf106 = openmc.ZCylinder(surface_id=106, x0=-3.21818, y0=-6.8961, r=0.32385)
surf107 = openmc.ZCylinder(surface_id=107, x0=-2.2987, y0=-6.8961, r=0.32385)
surf108 = openmc.ZCylinder(surface_id=108, x0=-1.37922, y0=-6.8961, r=0.32385)
surf109 = openmc.ZCylinder(surface_id=109, x0=-0.45974, y0=-6.8961, r=0.32385)
surf110 = openmc.ZCylinder(surface_id=110, x0=0.45974, y0=-6.8961, r=0.32385)
surf111 = openmc.ZCylinder(surface_id=111, x0=1.37922, y0=-6.8961, r=0.32385)
surf112 = openmc.ZCylinder(surface_id=112, x0=2.2987, y0=-6.8961, r=0.32385)
surf113 = openmc.ZCylinder(surface_id=113, x0=3.21818, y0=-6.8961, r=0.32385)
surf114 = openmc.ZCylinder(surface_id=114, x0=4.13766, y0=-6.8961, r=0.32385)
surf115 = openmc.ZCylinder(surface_id=115, x0=5.05714, y0=-6.8961, r=0.32385)
surf116 = openmc.ZCylinder(surface_id=116, x0=5.97662, y0=-6.8961, r=0.32385)
surf117 = openmc.ZCylinder(surface_id=117, x0=6.8961, y0=-6.8961, r=0.32385)
surf118 = openmc.ZCylinder(surface_id=118, x0=7.81558, y0=-6.8961, r=0.32385)
surf121 = openmc.YPlane(surface_id=121, y0=-6.43636)
surf126 = openmc.YPlane(surface_id=126, y0=-1.83896)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1126, z0=-56.2991, boundary_type="vacuum")
surf1_zmax = openmc.ZPlane(surface_id=1127, z0=56.2991, boundary_type="vacuum")

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
u2_cell0.region = -surf100 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf111 & +surf112 & +surf113 & +surf114 & +surf115 & +surf116 & +surf117 & +surf118
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = -surf100
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0])

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
cell12 = openmc.Cell(cell_id=12, fill=mat4)
cell12.region = +surf11 & -surf12

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell12])
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
