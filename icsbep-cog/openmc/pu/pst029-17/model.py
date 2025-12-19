"""
PU-SOL-THERM-029 (Case 20; No. 175) Hc=72.17cm; D=30.0cm; 40.6 gPu/l; H/X=632; 2.98 wt-% Pu-240; Air/Water; Water
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 9.922900e-05)
mat1.add_nuclide("Pu240", 3.035160e-06)
mat1.add_nuclide("H1", 6.269220e-02)
mat1.add_nuclide("O16", 3.597780e-02)
mat1.add_element("N", 1.767720e-03)
mat1.add_element("Fe", 3.558460e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.954600e-02)
mat2.add_element("Si", 1.693920e-03)
mat2.add_element("C", 1.188280e-04)
mat2.add_element("Cr", 1.646940e-02)
mat2.add_element("Mn", 8.659690e-04)
mat2.add_element("Ni", 8.106080e-03)
mat2.add_element("P", 6.143860e-05)
mat2.add_element("S", 4.464010e-05)

# Air per Table 15
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("O16", 1.263300e-05)
mat3.add_element("N", 4.180500e-05)

# H2O per Table 15
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.672200e-02)
mat4.add_nuclide("O16", 3.336100e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Tank/Sloped Bottom
surf1 = openmc.Plane(surface_id=1, a=-25.0, b=0.0, c=0.3, d=0.0)
# = Hc per Table 1
surf2 = openmc.ZPlane(surface_id=2, z0=72.17)
surf3 = openmc.ZPlane(surface_id=3, z0=117.2)
surf4 = openmc.ZCylinder(surface_id=4, r=14.7)
surf5 = openmc.ZCylinder(surface_id=5, r=15.0)
surf6 = openmc.ZCylinder(surface_id=6, r=25.0)
# Tank/Outermost
surf7 = openmc.ZCylinder(surface_id=7, r=25.3)
# dX = L = 160.6 + D
surf8 = openmc.XPlane(surface_id=8, x0=0.0)
# dY = 111.0 (fixed)
surf9 = openmc.model.RectangularParallelepiped(-95.3, 95.3, -55.5, 55.5, -32.800000000000004, 119.0)

# Z-plane surfaces for bounded cylinders
surf7_zmin = openmc.ZPlane(surface_id=1009, z0=-1.5)
surf7_zmax = openmc.ZPlane(surface_id=1010, z0=119.0)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = +surf1 & -surf2 & +surf5 & -surf6
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = -surf1 & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf1 & +surf4 & -surf5 & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell3 = openmc.Cell(fill=mat2)
u1_cell3.region = +surf3 & +surf5 & -surf6 & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell4 = openmc.Cell(fill=mat2)
u1_cell4.region = +surf1 & +surf6 & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = +surf1 & +surf3 & -surf4 & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell6 = openmc.Cell(fill=mat3)
u1_cell6.region = +surf2 & -surf3 & +surf5 & -surf6
u1_cell7 = openmc.Cell(fill=mat3)
u1_cell7.region = +surf2 & (+surf7 | -surf7_zmin | +surf7_zmax) & -surf9
u1_cell8 = openmc.Cell(fill=mat4)
u1_cell8.region = +surf1 & -surf3 & -surf4 & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell9 = openmc.Cell(fill=mat4)
u1_cell9.region = -surf2 & (+surf7 | -surf7_zmin | +surf7_zmax) & -surf9
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = +surf1 & -surf2 & +surf5 & -surf6
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = -surf1 & (-surf7 & +surf7_zmin & -surf7_zmax)
u2_cell2 = openmc.Cell(fill=mat2)
u2_cell2.region = +surf1 & +surf4 & -surf5 & (-surf7 & +surf7_zmin & -surf7_zmax)
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = +surf3 & +surf5 & -surf6 & (-surf7 & +surf7_zmin & -surf7_zmax)
u2_cell4 = openmc.Cell(fill=mat2)
u2_cell4.region = +surf1 & +surf6 & (-surf7 & +surf7_zmin & -surf7_zmax)
u2_cell5 = openmc.Cell(fill=mat3)
u2_cell5.region = +surf1 & -surf4 & (-surf7 & +surf7_zmin & -surf7_zmax)
u2_cell6 = openmc.Cell(fill=mat3)
u2_cell6.region = +surf2 & -surf3 & +surf5 & -surf6
u2_cell7 = openmc.Cell(fill=mat3)
u2_cell7.region = +surf2 & (+surf7 | -surf7_zmin | +surf7_zmax) & -surf9
u2_cell8 = openmc.Cell(fill=mat4)
u2_cell8.region = -surf2 & (+surf7 | -surf7_zmin | +surf7_zmax) & -surf9
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# WATER
cell11 = openmc.Cell(cell_id=11, fill=mat4)
cell11.region = -surf2 & (+surf7 | -surf7_zmin | +surf7_zmax) & -surf9

# WATER
cell21 = openmc.Cell(cell_id=21, fill=mat4)
cell21.region = -surf2 & (+surf7 | -surf7_zmin | +surf7_zmax) & -surf9

root_universe = openmc.Universe(cells=[cell11, cell21])
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
source.space = openmc.stats.Box((-21.0, -1.0, 35.1), (21.0, 1.0, 37.1))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
