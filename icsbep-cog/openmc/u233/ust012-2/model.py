"""
U233-SOL-THERM-012: Case No. 2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 233U(97.57)O2(NO3)2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 4.799200e-04)
mat1.add_nuclide("U234", 5.132700e-06)
mat1.add_nuclide("U235", 1.268400e-07)
mat1.add_nuclide("U236", 4.857600e-09)
mat1.add_nuclide("U238", 6.675900e-06)
mat1.add_nuclide("H1", 6.118600e-02)
mat1.add_element("N", 1.137900e-03)
mat1.add_nuclide("O16", 3.492600e-02)
mat1.add_element("Th", 6.170800e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Al-1100
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.974600e-02)
mat2.add_element("Si", 2.753900e-04)
mat2.add_element("Mn", 1.482000e-05)
mat2.add_element("Fe", 1.385000e-04)
mat2.add_element("Cu", 3.203000e-05)
mat2.add_element("Zn", 2.490200e-05)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.666700e-02)
mat3.add_nuclide("O16", 3.333300e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Vessel/Inner; Zo = B + 18 cm
surf1 = openmc.Sphere(surface_id=1, x0=11.1768, y0=tr, z0=0., r=0.)
# Vessel/Outer; THK = 0.127 cm
surf2 = openmc.Sphere(surface_id=2, x0=11.3038, y0=tr, z0=0., r=0.)
# Fill Pipe/Inner
surf3 = openmc.ZCylinder(surface_id=3, r=1.1227)
# Fill Pipe/Outer
surf4 = openmc.ZCylinder(surface_id=4, r=1.3335)
# Vent Pipe/Inner
surf5 = openmc.ZCylinder(surface_id=5, r=1.33225)
# Vent Pipe/Outer
surf6 = openmc.ZCylinder(surface_id=6, r=1.67005)
# Refl Tank/Inner
surf7 = openmc.ZCylinder(surface_id=7, r=45.72)
# Refl Tank/Outer; BCD
surf8 = openmc.ZCylinder(surface_id=8, r=46.0375, boundary_type="vacuum")
# Critical Height; A + 18
# surf9: Unsupported surface type "analytic" with params ['1.', 'z', '-36.6060', 'constant']
# Water Height; C
# surf10: Unsupported surface type "analytic" with params ['1.', 'z', '-67.5', 'constant']

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1010, z0=-10.0)
surf3_zmax = openmc.ZPlane(surface_id=1011, z0=20.0)
surf4_zmin = openmc.ZPlane(surface_id=1012, z0=-10.0)
surf4_zmax = openmc.ZPlane(surface_id=1013, z0=20.0)
surf5_zmin = openmc.ZPlane(surface_id=1014, z0=25.0)
surf5_zmax = openmc.ZPlane(surface_id=1015, z0=130.0)
surf6_zmin = openmc.ZPlane(surface_id=1016, z0=25.0)
surf6_zmax = openmc.ZPlane(surface_id=1017, z0=130.0)
surf7_zmin = openmc.ZPlane(surface_id=1018, z0=0.0)
surf7_zmax = openmc.ZPlane(surface_id=1019, z0=130.0)
surf8_zmin = openmc.ZPlane(surface_id=1020, z0=-1.27, boundary_type="vacuum")
surf8_zmax = openmc.ZPlane(surface_id=1021, z0=127.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Air
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf1 & +surf9

# Air
cell2 = openmc.Cell(cell_id=2)
cell2.region = +surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# Air
cell3 = openmc.Cell(cell_id=3)
cell3.region = +surf2 & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax) & +surf10

# Soln
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = -surf1 & -surf9

# Soln
cell5 = openmc.Cell(cell_id=5, fill=mat1)
cell5.region = +surf1 & (-surf3 & +surf3_zmin & -surf3_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# Alum
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf1 & -surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax)

# Alum
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# Alum
cell8 = openmc.Cell(cell_id=8, fill=mat2)
cell8.region = +surf2 & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# Alum
cell9 = openmc.Cell(cell_id=9, fill=mat2)
cell9.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# Water
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = +surf2 & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax) & -surf10

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10])
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
source.space = openmc.stats.Point((0.0, 0.0, 29.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
