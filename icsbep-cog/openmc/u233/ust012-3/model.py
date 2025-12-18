"""
U233-SOL-THERM-012: Case No. 3
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 233U(97.57)O2(NO3)2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 4.374800e-04)
mat1.add_nuclide("U234", 4.678700e-06)
mat1.add_nuclide("U235", 1.156200e-07)
mat1.add_nuclide("U236", 4.428000e-09)
mat1.add_nuclide("U238", 6.085500e-06)
mat1.add_nuclide("H1", 6.197100e-02)
mat1.add_element("N", 1.037300e-03)
mat1.add_nuclide("O16", 3.493500e-02)
mat1.add_element("Th", 5.625000e-06)
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
mat3.add_nuclide("H1", 6.659500e-02)
mat3.add_nuclide("O16", 3.329700e-02)
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
surf3 = openmc.ZCylinder(surface_id=3, x0=-10., y0=20., r=1.1227)
# Fill Pipe/Outer
surf4 = openmc.ZCylinder(surface_id=4, x0=-10., y0=20., r=1.3335)
# Vent Pipe/Inner
surf5 = openmc.ZCylinder(surface_id=5, x0=25., y0=130., r=1.33225)
# Vent Pipe/Outer
surf6 = openmc.ZCylinder(surface_id=6, x0=25., y0=130., r=1.67005)
# Refl Tank/Inner
surf7 = openmc.ZCylinder(surface_id=7, x0=0., y0=130., r=45.72)
# Refl Tank/Outer; BCD
surf8 = openmc.ZCylinder(surface_id=8, x0=-1.27, y0=127., r=46.0375, boundary_type="vacuum")
# Critical Height; A + 18
# surf9: Unsupported surface type "analytic" with params ['1.', 'z', '-37.5630', 'constant']
# Water Height; C
# surf10: Unsupported surface type "analytic" with params ['1.', 'z', '-67.5', 'constant']

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Air
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf1 & +surf9

# Air
cell2 = openmc.Cell(cell_id=2)
cell2.region = +surf1 & -surf5 & -surf8

# Air
cell3 = openmc.Cell(cell_id=3)
cell3.region = +surf2 & +surf4 & +surf6 & -surf7 & -surf8 & +surf10

# Soln
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = -surf1 & -surf9

# Soln
cell5 = openmc.Cell(cell_id=5, fill=mat1)
cell5.region = +surf1 & -surf3 & -surf8

# Alum
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf1 & -surf2 & +surf3 & +surf5

# Alum
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = +surf2 & +surf3 & -surf4 & -surf8

# Alum
cell8 = openmc.Cell(cell_id=8, fill=mat2)
cell8.region = +surf2 & +surf5 & -surf6 & -surf8

# Alum
cell9 = openmc.Cell(cell_id=9, fill=mat2)
cell9.region = +surf4 & +surf6 & +surf7 & -surf8

# Water
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = +surf2 & +surf4 & +surf6 & -surf7 & -surf8 & -surf10

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
source.space = openmc.stats.Point((0.0, 0.0, 28.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
