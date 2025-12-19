"""
U233-SOL-THERM-005 (Case 1) 233U(98.7)O2(NO3)2 @ H/U233=406; N/U=2.653
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# H/U-233 = 406
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 1.601100e-04)
mat1.add_nuclide("U234", 7.433200e-07)
mat1.add_nuclide("U238", 1.398100e-06)
mat1.add_nuclide("H1", 6.502800e-02)
mat1.add_nuclide("O16", 3.407700e-02)
mat1.add_element("N", 4.304700e-04)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Al-2S per Table 12
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 5.810800e-04)

# Water per Table 13
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.673500e-02)
mat3.add_nuclide("O16", 3.336800e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.Sphere(surface_id=1, r=13.2118)
surf2 = openmc.Sphere(surface_id=2, r=13.3409)
surf3 = openmc.Sphere(surface_id=3, r=28.5809, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Al2S
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# Water
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

root_universe = openmc.Universe(cells=[cell1, cell2, cell3])
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
