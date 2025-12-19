"""
MIX-SOL-THERM-004-8: Exp. No. 068 with 118.71 gPu/l and 173.98 gU/L with 1.02M
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 8.709000e-08)
mat1.add_nuclide("Pu239", 2.724900e-04)
mat1.add_nuclide("Pu240", 2.474700e-05)
mat1.add_nuclide("Pu241", 1.334500e-06)
mat1.add_nuclide("Pu242", 2.746600e-07)
mat1.add_nuclide("U234", 3.133700e-08)
mat1.add_nuclide("U235", 2.514100e-06)
mat1.add_nuclide("U236", 1.020900e-07)
mat1.add_nuclide("U238", 4.375100e-04)
mat1.add_nuclide("Am241", 1.543000e-06)
mat1.add_nuclide("H1", 5.839700e-02)
mat1.add_element("N", 2.726700e-03)
mat1.add_nuclide("O16", 3.795500e-02)
mat1.add_nuclide("B10", 6.447600e-08)
mat1.add_element("Cd", 3.624900e-08)
mat1.add_element("Fe", 3.757000e-06)
mat1.add_element("Gd", 5.000700e-09)
mat1.add_nuclide("Li6", 2.317300e-09)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.137600e-02)
mat2.add_element("Cr", 1.764800e-02)
mat2.add_element("Ni", 8.229200e-03)
mat2.add_element("C", 1.206300e-04)

# Carbon
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 8.366500e-02)
mat3.add_element("P", 4.561200e-06)
mat3.add_element("S", 2.790400e-05)
mat3.add_element("Mn", 3.257400e-04)
mat3.add_element("Si", 3.185900e-04)
mat3.add_element("C", 7.449500e-04)

# Concrete
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("O16", 4.552500e-02)
mat4.add_element("Si", 1.154100e-02)
mat4.add_element("Ca", 4.201200e-03)
mat4.add_element("Al", 2.491000e-03)
mat4.add_element("Fe", 8.467000e-04)
mat4.add_nuclide("H1", 1.461700e-02)
mat4.add_element("Na", 8.727800e-04)
mat4.add_element("Mg", 5.311200e-04)
mat4.add_element("K", 2.583900e-04)
mat4.add_element("S", 1.662800e-04)
mat4.add_element("Ti", 9.670200e-05)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Dump line, inner
surf1 = openmc.ZCylinder(surface_id=1, r=2.625)
# Dump line, outer
surf2 = openmc.ZCylinder(surface_id=2, r=3.016)
# Solution tank, inner
surf3 = openmc.ZCylinder(surface_id=3, r=17.695)
# Solution tank, outer
surf4 = openmc.ZCylinder(surface_id=4, r=17.774)
# Sol'n height
surf5 = openmc.ZPlane(surface_id=5, z0=27.03)
# Dump line, inner
surf6 = openmc.ZCylinder(surface_id=6, x0=0.0, y0=80.01, r=2.625)
# Dump line, outer
surf7 = openmc.ZCylinder(surface_id=7, x0=0.0, y0=80.01, r=3.016)
# Empty tank, inner
surf8 = openmc.ZCylinder(surface_id=8, x0=0.0, y0=80.01, r=34.34)
# Empty tank, outer
surf9 = openmc.ZCylinder(surface_id=9, x0=0.0, y0=80.01, r=34.419)
# Reflector tank, inner
surf10 = openmc.model.RectangularParallelepiped(-48.745, 48.745, -46.845, 130.665, -16.953, 139.107)
# Reflector tank, outer
surf11 = openmc.model.RectangularParallelepiped(-48.895, 48.895, -46.995, 130.815, -17.588, 139.257)
# Concrete tank, inner
surf12 = openmc.model.RectangularParallelepiped(-866.105, 200.895, -509.190, 557.810, -144.528, 495.442)
# Concrete tank, outer
surf13 = openmc.model.RectangularParallelepiped(-1018.105, 352.895, -600.190, 709.810, -205.528, 556.442, boundary_type="vacuum")
# Concrete, inner, upper
surf21 = openmc.ZCylinder(surface_id=21, x0=-0.6, y0=0.3, r=18.415)
# Concrete, outer, upper
surf22 = openmc.ZCylinder(surface_id=22, x0=-0.6, y0=0.3, r=43.615)
# Concrete
surf23 = openmc.XPlane(surface_id=23, x0=-30.5)
# female
surf24 = openmc.XPlane(surface_id=24, x0=30.5)
# nesting
surf25 = openmc.YPlane(surface_id=25, y0=-7.62)
# feature
surf26 = openmc.YPlane(surface_id=26, y0=0.0)
# Concrete, inner, lower
surf31 = openmc.ZCylinder(surface_id=31, x0=-0.4, y0=-1.5, r=18.415)
# Concrete, outer, lower
surf32 = openmc.ZCylinder(surface_id=32, x0=-0.4, y0=-1.5, r=43.615)
# Concrete
surf33 = openmc.XPlane(surface_id=33, x0=-29.5)
# male
surf34 = openmc.XPlane(surface_id=34, x0=29.5)
# nesting
surf35 = openmc.YPlane(surface_id=35, y0=-7.62)
# feature
surf36 = openmc.YPlane(surface_id=36, y0=0.0)

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(surface_id=1036, z0=-16.953)
surf2_zmax = openmc.ZPlane(surface_id=1037, z0=-0.953)
surf3_zmin = openmc.ZPlane(surface_id=1038, z0=0.0)
surf3_zmax = openmc.ZPlane(surface_id=1039, z0=90.6)
surf4_zmin = openmc.ZPlane(surface_id=1040, z0=-0.953)
surf4_zmax = openmc.ZPlane(surface_id=1041, z0=91.553)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SS304L
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = +surf1 & (-surf2 & +surf2_zmin & -surf2_zmax) & -surf10

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = (-surf3 & +surf3_zmin & -surf3_zmax) & -surf5

# SS304L
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf10

# SS304L
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf6 & -surf7 & -surf10

# SS304L
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf7 & +surf8 & -surf9 & -surf10

# CSTEEL
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf10 & -surf11

# Cncrt
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf12 & -surf13

# Cncrt
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = -surf10 & +surf21 & -surf22 & +surf26

# Cncrt
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = -surf10 & +surf21 & -surf22 & -surf23 & +surf25 & -surf26

# Cncrt
cell10 = openmc.Cell(cell_id=10, fill=mat4)
cell10.region = -surf10 & +surf21 & -surf22 & +surf24 & +surf25 & -surf26

# Cncrt
cell11 = openmc.Cell(cell_id=11, fill=mat4)
cell11.region = -surf10 & +surf31 & -surf32 & +surf33 & -surf34 & +surf35 & -surf36

# Cncrt
cell12 = openmc.Cell(cell_id=12, fill=mat4)
cell12.region = -surf10 & +surf31 & -surf32 & -surf35 & -surf36

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12])
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
source.space = openmc.stats.Point((0.0, 0.0, 13.515))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
