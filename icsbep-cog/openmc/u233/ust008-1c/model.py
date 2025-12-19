"""
U233-SOL-THERM-008: 233U(97.67)O2(NO3)2 @ H/U233=1984; N/U=2.19
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# H/U-233 = 1984.3
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 3.344100e-05)
mat1.add_nuclide("U234", 5.250300e-07)
mat1.add_nuclide("U235", 1.018400e-08)
mat1.add_nuclide("U238", 2.547400e-07)
mat1.add_nuclide("H1", 6.635700e-02)
mat1.add_element("N", 7.494300e-05)
mat1.add_nuclide("O16", 3.346900e-02)
mat1.add_element("Th", 1.475600e-07)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Al-1100
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("P", 2.710000e+00)
mat2.add_element("Al", 9.900000e+01)
mat2.add_element("Si", 3.750000e-01)
mat2.add_element("Fe", 3.750000e-01)
mat2.add_element("Cu", 2.000000e-01)
mat2.add_element("Mn", 5.000000e-02)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=61.011)
surf2 = openmc.Sphere(surface_id=2, r=61.786, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Alum
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

root_universe = openmc.Universe(cells=[cell1, cell2])
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
