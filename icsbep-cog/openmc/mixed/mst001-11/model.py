"""
MIX-SOL-THERM-001-11: Exp. No. 099
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution in annulus
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 5.903100e-02)
mat1.add_element("N", 2.344100e-03)
mat1.add_nuclide("O16", 3.766000e-02)
mat1.add_nuclide("Pu238", 5.402500e-08)
mat1.add_nuclide("Pu239", 1.690300e-04)
mat1.add_nuclide("Pu240", 1.540300e-05)
mat1.add_nuclide("Pu241", 7.763400e-07)
mat1.add_nuclide("Pu242", 1.722100e-07)
mat1.add_nuclide("U234", 4.508300e-08)
mat1.add_nuclide("U235", 4.514700e-06)
mat1.add_nuclide("U236", 3.384500e-07)
mat1.add_nuclide("U238", 6.283600e-04)
mat1.add_nuclide("Am241", 1.013800e-06)
mat1.add_nuclide("B10", 4.023800e-08)
mat1.add_element("Cd", 2.248700e-08)
mat1.add_element("Fe", 2.330600e-06)
mat1.add_element("Gd", 3.102100e-09)
mat1.add_nuclide("Li6", 1.437500e-09)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

# Water (099)
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.671600e-02)
mat3.add_nuclide("O16", 3.335800e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Polyethylene (099)
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 7.678900e-02)
mat4.add_element("C", 3.868100e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

# Solution in bottle B-2
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 5.478100e-02)
mat6.add_element("N", 3.374900e-03)
mat6.add_nuclide("O16", 3.912400e-02)
mat6.add_nuclide("Pu238", 7.582800e-08)
mat6.add_nuclide("Pu239", 2.372500e-04)
mat6.add_nuclide("Pu240", 2.162000e-05)
mat6.add_nuclide("Pu241", 1.089700e-06)
mat6.add_nuclide("Pu242", 2.417200e-07)
mat6.add_nuclide("U234", 6.543600e-08)
mat6.add_nuclide("U235", 6.553000e-06)
mat6.add_nuclide("U236", 4.912400e-07)
mat6.add_nuclide("U238", 9.120400e-04)
mat6.add_nuclide("Am241", 1.422900e-06)
mat6.add_nuclide("B10", 5.647700e-08)
mat6.add_element("Cd", 3.156200e-08)
mat6.add_element("Fe", 3.271200e-06)
mat6.add_element("Gd", 4.354100e-09)
mat6.add_nuclide("Li6", 2.017700e-09)
mat6.add_s_alpha_beta("c_H_in_H2O")

# Cadmium (099)
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Cd", 4.634000e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

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
# Critical solution height (case 099)
surf6 = openmc.ZPlane(surface_id=6, z0=79.18)
# Water reflector height (cases 087-099)
surf7 = openmc.ZPlane(surface_id=7, z0=104.43)
# Cadmium, lower
surf10 = openmc.ZCylinder(surface_id=10, r=12.615)
# Cadmium/SS304L, inner
surf11 = openmc.ZCylinder(surface_id=11, r=7.409)
# Polyethylene, inner
surf12 = openmc.ZCylinder(surface_id=12, r=7.483)
# Polyethylene, outer
surf13 = openmc.ZCylinder(surface_id=13, r=12.541)
# Cadmium, outer
surf14 = openmc.ZCylinder(surface_id=14, r=12.615)
# SS304L, upper
surf15 = openmc.ZCylinder(surface_id=15, r=12.615)
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
surf10_zmin = openmc.ZPlane(surface_id=1031, z0=1.27)
surf10_zmax = openmc.ZPlane(surface_id=1032, z0=1.344)
surf12_zmin = openmc.ZPlane(surface_id=1033, z0=1.344)
surf12_zmax = openmc.ZPlane(surface_id=1034, z0=128.114)
surf13_zmin = openmc.ZPlane(surface_id=1035, z0=1.344)
surf13_zmax = openmc.ZPlane(surface_id=1036, z0=128.114)
surf14_zmin = openmc.ZPlane(surface_id=1037, z0=1.344)
surf14_zmax = openmc.ZPlane(surface_id=1038, z0=128.114)
surf15_zmin = openmc.ZPlane(surface_id=1039, z0=128.114)
surf15_zmax = openmc.ZPlane(surface_id=1040, z0=128.59)
surf21_zmin = openmc.ZPlane(surface_id=1041, z0=21.835)
surf21_zmax = openmc.ZPlane(surface_id=1042, z0=136.5)
surf22_zmin = openmc.ZPlane(surface_id=1043, z0=21.2)
surf22_zmax = openmc.ZPlane(surface_id=1044, z0=137.0)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SS304L
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & -surf5 & (+surf10 | -surf10_zmin | +surf10_zmax)

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf6

# SS304L
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & -surf7

# Cd
cell5 = openmc.Cell(cell_id=5, fill=mat7)
cell5.region = (-surf10 & +surf10_zmin & -surf10_zmax)

# Cd
cell6 = openmc.Cell(cell_id=6, fill=mat7)
cell6.region = (+surf10 | -surf10_zmin | +surf10_zmax) & +surf11 & (-surf12 & +surf12_zmin & -surf12_zmax)

# Poly
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = (+surf10 | -surf10_zmin | +surf10_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)

# Cd
cell8 = openmc.Cell(cell_id=8, fill=mat7)
cell8.region = (+surf10 | -surf10_zmin | +surf10_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)

# SS304L
cell9 = openmc.Cell(cell_id=9, fill=mat2)
cell9.region = +surf11 & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)

# Soln
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = -surf5 & (-surf21 & +surf21_zmin & -surf21_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax) & -surf23

# SS304L
cell11 = openmc.Cell(cell_id=11, fill=mat2)
cell11.region = -surf5 & (+surf21 | -surf21_zmin | +surf21_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11])
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
source.space = openmc.stats.Box((-20.7, -1.0, 50.535), (20.7, 1.0, 62.595))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
