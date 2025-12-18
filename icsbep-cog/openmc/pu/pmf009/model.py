"""
PU-MET-FAST-009: 11.154 kg Pu(4.90)-1.00Ga @ 15.90 g/cc in 7.9248 cm Al-2014 @ 2.82 g/cc
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.759200e-02)
mat1.add_nuclide("Pu240", 1.934900e-03)
mat1.add_nuclide("Pu241", 1.179700e-04)
mat1.add_element("Ga", 1.373300e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.878700e-02)
mat2.add_element("Cu", 1.175900e-03)
mat2.add_element("Si", 2.418700e-04)
mat2.add_element("Mn", 2.472900e-04)
mat2.add_element("Mg", 3.493600e-04)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# per Section 3.2
surf1 = openmc.Sphere(surface_id=1, r=5.5118)
# TEK = 7.9248 cm
surf2 = openmc.Sphere(surface_id=2, r=13.4366, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# refl
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
