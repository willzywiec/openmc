"""
MIX-SOL-THERM-001-12: Exp. No. 100
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution in annulus
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 5.902900e-02)
mat1.add_element("N", 2.362300e-03)
mat1.add_nuclide("O16", 3.772000e-02)
mat1.add_nuclide("Pu238", 5.447200e-08)
mat1.add_nuclide("Pu239", 1.704300e-04)
mat1.add_nuclide("Pu240", 1.553100e-05)
mat1.add_nuclide("Pu241", 7.827800e-07)
mat1.add_nuclide("Pu242", 1.736400e-07)
mat1.add_nuclide("U234", 4.532500e-08)
mat1.add_nuclide("U235", 4.538900e-06)
mat1.add_nuclide("U236", 3.402600e-07)
mat1.add_nuclide("U238", 6.317200e-04)
mat1.add_nuclide("Am241", 1.022900e-06)
mat1.add_nuclide("B10", 4.057100e-08)
mat1.add_element("Cd", 2.267300e-08)
mat1.add_element("Fe", 2.349900e-06)
mat1.add_element("Gd", 3.127800e-09)
mat1.add_nuclide("Li6", 1.449400e-09)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

# Water (100)
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.668100e-02)
mat3.add_nuclide("O16", 3.334100e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Polyethylene (100)
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 7.678900e-02)
mat4.add_element("C", 3.868100e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

# Cadmium (100)
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Cd", 4.634000e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat7])

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
# Critical solution height (case 100)
surf6 = openmc.ZPlane(surface_id=6, z0=104.62)
# Water reflector height (cases 100 & 108)
surf7 = openmc.ZPlane(surface_id=7, z0=126.63)
# Polyethylene
surf11 = openmc.ZCylinder(surface_id=11, x0=1.344, y0=128.434, r=12.452)
# Cadmium
surf12 = openmc.ZCylinder(surface_id=12, x0=1.27, y0=128.434, r=12.526)
# SS304L
surf13 = openmc.ZCylinder(surface_id=13, x0=128.434, y0=128.91, r=12.526)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SS304L
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = +surf1 & -surf2 & -surf5 & +surf12

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf2 & -surf3 & -surf6

# SS304L
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & +surf3 & -surf4

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf2 & +surf4 & -surf5 & -surf7

# Poly
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = -surf11 & -surf12

# Cd
cell6 = openmc.Cell(cell_id=6, fill=mat7)
cell6.region = +surf11 & -surf12

# SS304L
cell7 = openmc.Cell(cell_id=7, fill=mat2)
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
source.space = openmc.stats.Box((-20.7, -1.0, 50.535), (20.7, 1.0, 75.315))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
