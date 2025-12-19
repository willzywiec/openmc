"""
LST002-1: Full 174-liter sphere of U(4.9)O2F2 solution; 15-cm thick water reflection
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution 1
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 2.327100e-07)
mat1.add_nuclide("U235", 5.665500e-05)
mat1.add_nuclide("U238", 1.087800e-03)
mat1.add_element("F", 2.289300e-03)
mat1.add_nuclide("O16", 3.340200e-02)
mat1.add_nuclide("H1", 6.222600e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Al-1100
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.969900e-02)
mat2.add_element("Si", 5.520200e-04)
mat2.add_element("Cu", 5.136400e-05)
mat2.add_element("Zn", 2.495800e-05)
mat2.add_element("Mn", 1.485300e-05)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.665900e-02)
mat3.add_nuclide("O16", 3.332900e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=34.3990)
surf2 = openmc.Sphere(surface_id=2, r=34.5578)
surf3 = openmc.Sphere(surface_id=3, r=49.5578, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Al1100
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
