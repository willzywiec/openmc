"""
MIX-SOL-THERM-001-6: Exp. No. 094
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution in annulus
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 5.450300e-02)
mat1.add_element("N", 3.422100e-03)
mat1.add_nuclide("O16", 3.925900e-02)
mat1.add_nuclide("Pu238", 7.943000e-08)
mat1.add_nuclide("Pu239", 2.485200e-04)
mat1.add_nuclide("Pu240", 2.264700e-05)
mat1.add_nuclide("Pu241", 1.141400e-06)
mat1.add_nuclide("Pu242", 2.532000e-07)
mat1.add_nuclide("U234", 6.851800e-08)
mat1.add_nuclide("U235", 6.861600e-06)
mat1.add_nuclide("U236", 5.143800e-07)
mat1.add_nuclide("U238", 9.549900e-04)
mat1.add_nuclide("Am241", 1.485900e-06)
mat1.add_nuclide("B10", 5.916000e-08)
mat1.add_element("Cd", 3.306100e-08)
mat1.add_element("Fe", 3.426600e-06)
mat1.add_element("Gd", 4.560900e-09)
mat1.add_nuclide("Li6", 2.113500e-09)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

# Water (094)
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.668700e-02)
mat3.add_nuclide("O16", 3.334400e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

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
mat6.add_nuclide("Am241", 1.418500e-06)
mat6.add_nuclide("B10", 5.647700e-08)
mat6.add_element("Cd", 3.156200e-08)
mat6.add_element("Fe", 3.271200e-06)
mat6.add_element("Gd", 4.354100e-09)
mat6.add_nuclide("Li6", 2.017700e-09)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat6])

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
surf5 = openmc.model.RectangularParallelepiped(-49.38, 49.38, -50.655, 50.655, 0.0, 137.00, boundary_type="vacuum")
# Critical solution height (case 094)
surf6 = openmc.ZPlane(surface_id=6, z0=32.86)
# Water reflector height (cases 087-099)
surf7 = openmc.ZPlane(surface_id=7, z0=104.43)
# Bottle, inner
surf21 = openmc.ZCylinder(surface_id=21, r=7.28)
# Bottle, outer
surf22 = openmc.ZCylinder(surface_id=22, r=7.345)
# Bottle 2, solution height
surf23 = openmc.ZPlane(surface_id=23, z0=81.235)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=1.27)
surf1_zmax = openmc.ZPlane(z0=128.53)
surf2_zmin = openmc.ZPlane(z0=0.0)
surf2_zmax = openmc.ZPlane(z0=128.53)
surf3_zmin = openmc.ZPlane(z0=22.005)
surf3_zmax = openmc.ZPlane(z0=127.577)
surf4_zmin = openmc.ZPlane(z0=21.37)
surf4_zmax = openmc.ZPlane(z0=128.53)
surf21_zmin = openmc.ZPlane(z0=21.835)
surf21_zmax = openmc.ZPlane(z0=136.5)
surf22_zmin = openmc.ZPlane(z0=21.2)
surf22_zmax = openmc.ZPlane(z0=137.0)

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

# Soln
cell5 = openmc.Cell(cell_id=5, fill=mat6)
cell5.region = -surf5 & (-surf21 & +surf21_zmin & -surf21_zmax) & -surf23

# SS304L
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = -surf5 & (+surf21 | -surf21_zmin | +surf21_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax)

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
source.space = openmc.stats.Box((-20.7, -1.0, 37.435), (20.7, 1.0, 52.535))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
