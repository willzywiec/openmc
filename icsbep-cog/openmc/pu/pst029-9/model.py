"""
PU-SOL-THERM-029 (Case 12; No. 185) Hc=70.47cm; D=3.5cm; 40.6 gPu/l; H/X=632; 2.98 wt-% Pu-240; Air/Cd; Air/Cd; Water
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

# Cd  per Table 15
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cd", 4.634020e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Tank/Sloped Bottom
surf1 = openmc.Plane(surface_id=1, a=-25.0, b=0.0, c=0.3, d=0.0)
# = Hc per Table 1
surf2 = openmc.ZPlane(surface_id=2, z0=70.47)
surf3 = openmc.ZPlane(surface_id=3, z0=117.2)
# Cd/Inner
surf4 = openmc.ZCylinder(surface_id=4, r=14.43)
# Cd/Outer
surf5 = openmc.ZCylinder(surface_id=5, r=14.5)
# SST/Inner
surf6 = openmc.ZCylinder(surface_id=6, r=14.6)
surf7 = openmc.ZCylinder(surface_id=7, r=14.7)
surf8 = openmc.ZCylinder(surface_id=8, r=15.0)
surf9 = openmc.ZCylinder(surface_id=9, r=25.0)
# Tank/Outermost
surf10 = openmc.ZCylinder(surface_id=10, r=25.3)
# dX = L = 160.6 + D
surf11 = openmc.XPlane(surface_id=11, x0=0.0)
# dY = 111.0 (fixed)
surf12 = openmc.model.RectangularParallelepiped(-82.05, 82.05, -55.5, 55.5, -32.800000000000004, 119.0)

# Z-plane surfaces for bounded cylinders
surf10_zmin = openmc.ZPlane(surface_id=1012, z0=-1.5)
surf10_zmax = openmc.ZPlane(surface_id=1013, z0=119.0)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = +surf1 & -surf2 & +surf8 & -surf9
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = -surf1 & (-surf10 & +surf10_zmin & -surf10_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf1 & +surf7 & -surf8 & (-surf10 & +surf10_zmin & -surf10_zmax)
u1_cell3 = openmc.Cell(fill=mat2)
u1_cell3.region = +surf3 & +surf8 & -surf9 & (-surf10 & +surf10_zmin & -surf10_zmax)
u1_cell4 = openmc.Cell(fill=mat2)
u1_cell4.region = +surf1 & +surf9 & (-surf10 & +surf10_zmin & -surf10_zmax)
u1_cell5 = openmc.Cell(fill=mat2)
u1_cell5.region = +surf1 & -surf3 & +surf5 & -surf6 & (-surf10 & +surf10_zmin & -surf10_zmax)
u1_cell6 = openmc.Cell(fill=mat3)
u1_cell6.region = +surf1 & -surf4 & (-surf10 & +surf10_zmin & -surf10_zmax)
u1_cell7 = openmc.Cell(fill=mat3)
u1_cell7.region = +surf1 & -surf3 & +surf6 & -surf7 & (-surf10 & +surf10_zmin & -surf10_zmax)
u1_cell8 = openmc.Cell(fill=mat3)
u1_cell8.region = +surf2 & -surf3 & +surf8 & -surf9
u1_cell9 = openmc.Cell(fill=mat3)
u1_cell9.region = +surf2 & (+surf10 | -surf10_zmin | +surf10_zmax) & -surf12
u1_cell10 = openmc.Cell(fill=mat3)
u1_cell10.region = +surf1 & +surf3 & +surf4 & -surf7 & (-surf10 & +surf10_zmin & -surf10_zmax)
u1_cell11 = openmc.Cell(fill=mat4)
u1_cell11.region = -surf2 & (+surf10 | -surf10_zmin | +surf10_zmax) & -surf12
u1_cell12 = openmc.Cell(fill=mat5)
u1_cell12.region = +surf1 & -surf3 & +surf4 & -surf5 & (-surf10 & +surf10_zmin & -surf10_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11, u1_cell12])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Cd
cell14 = openmc.Cell(cell_id=14, fill=mat5)
cell14.region = +surf1 & -surf3 & +surf4 & -surf5 & (-surf10 & +surf10_zmin & -surf10_zmax)

root_universe = openmc.Universe(cells=[cell14])
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
source.space = openmc.stats.Box((-7.75, -1.0, 34.2), (7.75, 1.0, 36.2))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
