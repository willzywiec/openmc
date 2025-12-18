"""
IEU-SOL-THERM-002-9: Unreflected 38-inch i.d. U(30.45) solution sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 4.119300e-05)
mat1.add_nuclide("U234", 5.162700e-07)
mat1.add_nuclide("U236", 1.077600e-07)
mat1.add_nuclide("U238", 9.228400e-05)
mat1.add_nuclide("H1", 6.635300e-02)
mat1.add_element("F", 2.682000e-04)
mat1.add_nuclide("O16", 3.344500e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Aluminum
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Mg", 3.357300e-05)
mat2.add_element("Al", 5.992800e-02)
mat2.add_element("Si", 1.452700e-04)
mat2.add_element("Ti", 1.704200e-05)
mat2.add_element("Mn", 1.485300e-05)
mat2.add_element("Fe", 1.168900e-04)
mat2.add_element("Cu", 1.284100e-05)
mat2.add_element("Zn", 1.747000e-05)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.Sphere(surface_id=1, r=48.4263)
surf2 = openmc.Sphere(surface_id=2, r=48.7514, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# BA995
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
