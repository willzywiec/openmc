"""
MIX-SOL-THERM-001-5: Exp. No. 093
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution in annulus
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 5.446400e-02)
mat1.add_element("N", 3.348100e-03)
mat1.add_nuclide("O16", 3.927100e-02)
mat1.add_nuclide("Pu238", 7.916600e-08)
mat1.add_nuclide("Pu239", 2.476900e-04)
mat1.add_nuclide("Pu240", 2.257200e-05)
mat1.add_nuclide("Pu241", 1.137600e-06)
mat1.add_nuclide("Pu242", 2.526300e-07)
mat1.add_nuclide("U234", 6.836300e-08)
mat1.add_nuclide("U235", 6.846100e-06)
mat1.add_nuclide("U236", 5.132100e-07)
mat1.add_nuclide("U238", 9.528300e-04)
mat1.add_nuclide("Am241", 1.479000e-06)
mat1.add_nuclide("B10", 5.896400e-08)
mat1.add_element("Cd", 3.295100e-08)
mat1.add_element("Fe", 3.415200e-06)
mat1.add_element("Gd", 4.545700e-09)
mat1.add_nuclide("Li6", 2.016500e-09)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

# Water (093)
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.667700e-02)
mat3.add_nuclide("O16", 3.333800e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Concrete (093)
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 1.059900e-02)
mat4.add_element("C", 1.526300e-03)
mat4.add_nuclide("O16", 3.689600e-02)
mat4.add_element("Al", 2.214200e-03)
mat4.add_nuclide("B10", 1.226000e-03)
mat4.add_nuclide("B11", 4.897700e-03)
mat4.add_element("Ba", 5.762200e-06)
mat4.add_element("Ca", 4.606900e-03)
mat4.add_element("Cu", 2.075400e-06)
mat4.add_element("Fe", 9.823900e-04)
mat4.add_element("K", 4.587500e-04)
mat4.add_element("Li", 3.800000e-05)
mat4.add_element("Mg", 6.185900e-04)
mat4.add_element("Mn", 1.680400e-05)
mat4.add_element("Na", 8.318100e-04)
mat4.add_element("Si", 9.673400e-03)
mat4.add_element("Sr", 4.515500e-06)
mat4.add_element("Ti", 1.514900e-04)
mat4.add_element("Zr", 5.782900e-06)
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

# Solution in bottle B-2
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 5.478100e-02)
mat6.add_element("N", 3.374900e-03)
mat6.add_nuclide("O16", 3.912500e-02)
mat6.add_nuclide("Pu238", 7.582800e-08)
mat6.add_nuclide("Pu239", 2.372500e-04)
mat6.add_nuclide("Pu240", 2.162000e-05)
mat6.add_nuclide("Pu241", 1.089700e-06)
mat6.add_nuclide("Pu242", 2.417200e-07)
mat6.add_nuclide("U234", 6.543600e-08)
mat6.add_nuclide("U235", 6.553000e-06)
mat6.add_nuclide("U236", 4.912400e-07)
mat6.add_nuclide("U238", 9.120400e-04)
mat6.add_nuclide("Am241", 1.416700e-06)
mat6.add_nuclide("B10", 5.647700e-08)
mat6.add_element("Cd", 3.156200e-08)
mat6.add_element("Fe", 3.271200e-06)
mat6.add_element("Gd", 4.354100e-09)
mat6.add_nuclide("Li6", 2.017700e-09)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Central cavity
surf1 = openmc.ZCylinder(surface_id=1, r=12.7)
# SS304L central tank
surf2 = openmc.ZCylinder(surface_id=2, r=12.774)
# Sol'n or void in annular tank
surf3 = openmc.ZCylinder(surface_id=3, r=26.596)
# SS304L annular tank
surf4 = openmc.ZCylinder(surface_id=4, r=26.67)
# Boundary condition
surf5 = openmc.model.RectangularParallelepiped(-49.38, 49.38, -50.655, 50.655, 0.0, 137.0, boundary_type="vacuum")
# Critical solution height (case 093)
surf6 = openmc.ZPlane(surface_id=6, z0=51.10)
# Water reflector height (cases 087-099)
surf7 = openmc.ZPlane(surface_id=7, z0=104.43)
# Carbon steel disc
surf11 = openmc.ZCylinder(surface_id=11, r=12.541)
# Cavity
surf12 = openmc.ZCylinder(surface_id=12, r=7.5465)
# 6% B4C concrete insert
surf13 = openmc.ZCylinder(surface_id=13, r=12.541)
# Carbon steel rebar
surf14 = openmc.ZCylinder(surface_id=14, x0=-4.0, y0=-10.0, r=0.635)
# Carbon steel rebar
surf15 = openmc.ZCylinder(surface_id=15, x0=4.0, y0=-10.0, r=0.635)
# Carbon steel rebar
surf16 = openmc.ZCylinder(surface_id=16, x0=-4.0, y0=10.0, r=0.635)
# Carbon steel rebar
surf17 = openmc.ZCylinder(surface_id=17, x0=4.0, y0=10.0, r=0.635)
# Bottle, inner
surf21 = openmc.ZCylinder(surface_id=21, r=7.28)
# Bottle, outer
surf22 = openmc.ZCylinder(surface_id=22, r=7.345)
# Bottle 2, solution height
surf23 = openmc.ZPlane(surface_id=23, z0=81.235)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1023, z0=1.27)
surf1_zmax = openmc.ZPlane(surface_id=1024, z0=128.53)
surf2_zmin = openmc.ZPlane(surface_id=1025, z0=0.0)
surf2_zmax = openmc.ZPlane(surface_id=1026, z0=128.53)
surf3_zmin = openmc.ZPlane(surface_id=1027, z0=22.005)
surf3_zmax = openmc.ZPlane(surface_id=1028, z0=127.577)
surf4_zmin = openmc.ZPlane(surface_id=1029, z0=21.37)
surf4_zmax = openmc.ZPlane(surface_id=1030, z0=128.53)
surf11_zmin = openmc.ZPlane(surface_id=1031, z0=1.27)
surf11_zmax = openmc.ZPlane(surface_id=1032, z0=2.54)
surf13_zmin = openmc.ZPlane(surface_id=1033, z0=2.54)
surf13_zmax = openmc.ZPlane(surface_id=1034, z0=128.27)
surf21_zmin = openmc.ZPlane(surface_id=1035, z0=21.835)
surf21_zmax = openmc.ZPlane(surface_id=1036, z0=136.5)
surf22_zmin = openmc.ZPlane(surface_id=1037, z0=21.2)
surf22_zmax = openmc.ZPlane(surface_id=1038, z0=137.0)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SS304L
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & -surf5

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf6

# SS304L
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & -surf7

# CStl
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = (-surf11 & +surf11_zmin & -surf11_zmax)

# Conc
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = (+surf11 | -surf11_zmin | +surf11_zmax) & +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax) & +surf14 & +surf15 & +surf16 & +surf17

# CStl
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = (+surf11 | -surf11_zmin | +surf11_zmax) & +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax) & -surf14

# CStl
cell8 = openmc.Cell(cell_id=8, fill=mat5)
cell8.region = (+surf11 | -surf11_zmin | +surf11_zmax) & +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax) & -surf15

# CStl
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = (+surf11 | -surf11_zmin | +surf11_zmax) & +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax) & -surf16

# CStl
cell10 = openmc.Cell(cell_id=10, fill=mat5)
cell10.region = (+surf11 | -surf11_zmin | +surf11_zmax) & +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax) & -surf17

# Soln
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = -surf5 & (-surf21 & +surf21_zmin & -surf21_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax) & -surf23

# SS304L
cell12 = openmc.Cell(cell_id=12, fill=mat2)
cell12.region = -surf5 & (+surf21 | -surf21_zmin | +surf21_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax)

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
source.space = openmc.stats.Box((-20.7, -1.0, 46.555), (20.7, 1.0, 52.535))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
