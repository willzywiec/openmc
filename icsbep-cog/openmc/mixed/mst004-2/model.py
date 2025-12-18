"""
MIX-SOL-THERM-004-2: Exp. No. 070 with 118.90 gPu/l and 174.53 gU/L with 1.03M
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 8.722900e-08)
mat1.add_nuclide("Pu239", 2.729200e-04)
mat1.add_nuclide("Pu240", 2.478700e-05)
mat1.add_nuclide("Pu241", 1.336700e-06)
mat1.add_nuclide("Pu242", 2.751000e-07)
mat1.add_nuclide("U234", 3.143600e-08)
mat1.add_nuclide("U235", 2.522000e-06)
mat1.add_nuclide("U236", 1.024100e-07)
mat1.add_nuclide("U238", 4.389000e-04)
mat1.add_nuclide("Am241", 1.546700e-06)
mat1.add_nuclide("H1", 5.832000e-02)
mat1.add_element("N", 2.737500e-03)
mat1.add_nuclide("O16", 3.794900e-02)
mat1.add_nuclide("B10", 6.457900e-08)
mat1.add_element("Cd", 3.630700e-08)
mat1.add_element("Fe", 3.763000e-06)
mat1.add_element("Gd", 5.008700e-09)
mat1.add_nuclide("Li6", 2.321000e-09)
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

# Dump line, inner
surf1 = openmc.ZCylinder(surface_id=1, r=2.625)
# Dump line, outer
surf2 = openmc.ZCylinder(surface_id=2, x0=-16.953, y0=-0.953, r=3.016)
# Solution tank, inner
surf3 = openmc.ZCylinder(surface_id=3, x0=0.0, y0=90.6, r=17.695)
# Solution tank, outer
surf4 = openmc.ZCylinder(surface_id=4, x0=-0.953, y0=91.553, r=17.774)
# Sol'n height
surf5 = openmc.ZPlane(surface_id=5, z0=41.08)
# Dump line, inner
surf6_cyl = openmc.ZCylinder(surface_id=6, x0=tr, y0=0, r=2.625)
surf6_zmin = openmc.ZPlane(z0=80.01)
surf6_zmax = openmc.ZPlane(z0=0.0)
surf6 = (surf6_cyl, surf6_zmin, surf6_zmax)
# Dump line, outer
# surf7: Error converting surface type "c": could not convert string to float: 'tr'
# Empty tank, inner
# surf8: Error converting surface type "c": could not convert string to float: 'tr'
# Empty tank, outer
# surf9: Error converting surface type "c": could not convert string to float: 'tr'
# Reflector tank, inner
surf10 = openmc.model.RectangularParallelepiped(-48.745, 48.745, -46.845, 130.665, -16.953, 139.107)
# Reflector tank, outer
surf11 = openmc.model.RectangularParallelepiped(-48.895, 48.895, -46.995, 130.815, -17.588, 139.257)
# Concrete tank, inner
surf12 = openmc.model.RectangularParallelepiped(-866.105, 200.895, -509.190, 557.810, -144.528, 495.442)
# Concrete tank, outer
surf13 = openmc.model.RectangularParallelepiped(-1018.105, 352.895, -600.190, 709.810, -205.528, 556.442, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SS304L
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = +surf1 & -surf2 & -surf10

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = -surf3 & -surf5

# SS304L
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & +surf3 & -surf4 & -surf10

# SS304L
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf6 & -surf10

# SS304L
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = -surf10

# CSTEEL
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf10 & -surf11

# Cncrt
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf12 & -surf13

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7])
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
source.space = openmc.stats.Point((0.0, 0.0, 20.54))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
