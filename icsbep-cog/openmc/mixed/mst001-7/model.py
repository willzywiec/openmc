"""
MIX-SOL-THERM-001-7: Exp. No. 095
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution in annulus
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 5.648200e-02)
mat1.add_element("N", 4.030400e-03)
mat1.add_nuclide("O16", 3.938200e-02)
mat1.add_nuclide("Pu238", 1.336100e-07)
mat1.add_nuclide("Pu239", 4.512400e-04)
mat1.add_nuclide("Pu240", 3.896300e-05)
mat1.add_nuclide("Pu241", 1.920500e-06)
mat1.add_nuclide("Pu242", 3.309200e-07)
mat1.add_nuclide("U234", 2.308100e-08)
mat1.add_nuclide("U235", 3.817000e-07)
mat1.add_nuclide("U236", 7.744300e-08)
mat1.add_nuclide("U238", 1.596700e-05)
mat1.add_nuclide("Am241", 2.394500e-06)
mat1.add_nuclide("B10", 4.798900e-08)
mat1.add_element("Cd", 3.772500e-08)
mat1.add_element("Fe", 5.452500e-06)
mat1.add_element("Gd", 6.741900e-09)
mat1.add_nuclide("Li6", 3.818400e-09)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

# Water (095)
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.670900e-02)
mat3.add_nuclide("O16", 3.335400e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Concrete (095)
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 1.138400e-02)
mat4.add_element("C", 4.721500e-04)
mat4.add_nuclide("O16", 3.869300e-02)
mat4.add_element("Al", 2.356000e-03)
mat4.add_nuclide("B10", 3.809700e-04)
mat4.add_nuclide("B11", 1.522000e-03)
mat4.add_element("Ba", 6.722500e-06)
mat4.add_element("Ca", 4.574000e-03)
mat4.add_element("Cu", 2.075400e-06)
mat4.add_element("Fe", 1.027300e-03)
mat4.add_element("K", 5.127200e-04)
mat4.add_element("Li", 3.800000e-05)
mat4.add_element("Mg", 6.240100e-04)
mat4.add_element("Mn", 1.680400e-05)
mat4.add_element("Na", 8.490200e-04)
mat4.add_element("Si", 1.037800e-02)
mat4.add_element("Sr", 4.515500e-06)
mat4.add_element("Ti", 1.597600e-04)
mat4.add_element("Zr", 1.445700e-05)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Carbon steel
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 8.366500e-02)
mat5.add_element("Mn", 3.257400e-04)
mat5.add_element("S", 2.790400e-05)
mat5.add_element("P", 4.561200e-06)
mat5.add_element("Si", 3.185900e-04)
mat5.add_element("C", 7.449500e-04)

# Solution in bottle B-3
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 5.643700e-02)
mat6.add_element("N", 4.034200e-03)
mat6.add_nuclide("O16", 3.935500e-02)
mat6.add_nuclide("Pu238", 1.331400e-07)
mat6.add_nuclide("Pu239", 4.496500e-04)
mat6.add_nuclide("Pu240", 3.882500e-05)
mat6.add_nuclide("Pu241", 1.913700e-06)
mat6.add_nuclide("Pu242", 3.297600e-07)
mat6.add_nuclide("U234", 1.810900e-08)
mat6.add_nuclide("U235", 2.994900e-07)
mat6.add_nuclide("U236", 6.076300e-08)
mat6.add_nuclide("U238", 1.252800e-05)
mat6.add_nuclide("Am241", 2.386100e-06)
mat6.add_nuclide("B10", 4.782000e-08)
mat6.add_element("Cd", 3.759200e-08)
mat6.add_element("Fe", 5.433300e-06)
mat6.add_element("Gd", 6.718100e-09)
mat6.add_nuclide("Li6", 3.085000e-09)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Central cavity
surf1 = openmc.ZCylinder(surface_id=1, x0=1.27, y0=128.53, r=12.7)
# SS304L central tank
surf2 = openmc.ZCylinder(surface_id=2, x0=0.0, y0=128.53, r=12.774)
# Sol'n or void in annular tank
surf3 = openmc.ZCylinder(surface_id=3, x0=22.005, y0=127.577, r=26.596)
# SS304L annular tank
surf4 = openmc.ZCylinder(surface_id=4, x0=21.37, y0=128.53, r=26.67)
# Boundary condition
surf5 = openmc.model.RectangularParallelepiped(-49.38, 49.38, -50.655, 50.655, 0.0, 137.0, boundary_type="vacuum")
# Critical solution height (case 095)
surf6 = openmc.ZPlane(surface_id=6, z0=27.51)
# Water reflector height (cases 087-099)
surf7 = openmc.ZPlane(surface_id=7, z0=104.43)
# Carbon steel disc
surf11 = openmc.ZCylinder(surface_id=11, x0=1.27, y0=2.54, r=12.541)
# Cavity
surf12 = openmc.ZCylinder(surface_id=12, r=7.5465)
# 2% B4C concrete insert
surf13 = openmc.ZCylinder(surface_id=13, x0=2.54, y0=128.27, r=12.541)
# Carbon steel rebar
surf14_cyl = openmc.ZCylinder(surface_id=14, x0=tr, y0=-4, r=0.635)
surf14_zmin = openmc.ZPlane(z0=-10.0)
surf14_zmax = openmc.ZPlane(z0=0.0)
surf14 = (surf14_cyl, surf14_zmin, surf14_zmax)
# Carbon steel rebar
surf15_cyl = openmc.ZCylinder(surface_id=15, x0=tr, y0=4, r=0.635)
surf15_zmin = openmc.ZPlane(z0=-10.0)
surf15_zmax = openmc.ZPlane(z0=0.0)
surf15 = (surf15_cyl, surf15_zmin, surf15_zmax)
# Carbon steel rebar
surf16_cyl = openmc.ZCylinder(surface_id=16, x0=tr, y0=-4, r=0.635)
surf16_zmin = openmc.ZPlane(z0=10.0)
surf16_zmax = openmc.ZPlane(z0=0.0)
surf16 = (surf16_cyl, surf16_zmin, surf16_zmax)
# Carbon steel rebar
surf17_cyl = openmc.ZCylinder(surface_id=17, x0=tr, y0=4, r=0.635)
surf17_zmin = openmc.ZPlane(z0=10.0)
surf17_zmax = openmc.ZPlane(z0=0.0)
surf17 = (surf17_cyl, surf17_zmin, surf17_zmax)
# Bottle, inner
surf21 = openmc.ZCylinder(surface_id=21, x0=21.835, y0=136.5, r=7.28)
# Bottle, outer
surf22 = openmc.ZCylinder(surface_id=22, x0=21.2, y0=137.0, r=7.345)
# Bottle 3, solution height
surf23 = openmc.ZPlane(surface_id=23, z0=58.635)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SS304L
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = +surf1 & -surf2 & -surf5

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf2 & -surf3 & -surf6

# SS304L
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & +surf3 & -surf4

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf2 & +surf4 & -surf5 & -surf7

# CStl
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = -surf11

# Conc
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf11 & +surf12 & -surf13 & +surf14 & +surf15 & +surf16 & +surf17

# CStl
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = +surf11 & +surf12 & -surf13 & -surf14

# CStl
cell8 = openmc.Cell(cell_id=8, fill=mat5)
cell8.region = +surf11 & +surf12 & -surf13 & -surf15

# CStl
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = +surf11 & +surf12 & -surf13 & -surf16

# CStl
cell10 = openmc.Cell(cell_id=10, fill=mat5)
cell10.region = +surf11 & +surf12 & -surf13 & -surf17

# Soln
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = -surf5 & -surf21 & -surf22 & -surf23

# SS304L
cell12 = openmc.Cell(cell_id=12, fill=mat2)
cell12.region = -surf5 & +surf21 & -surf22

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
source.space = openmc.stats.Box((-20.7, -1.0, 34.76), (20.7, 1.0, 41.235))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
