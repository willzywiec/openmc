"""
IEU-MET-FAST-012: ZPR-3/41; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 2.778900e-05)
mat1.add_nuclide("U235", 2.863190e-03)
mat1.add_nuclide("U236", 1.331750e-05)
mat1.add_nuclide("U238", 1.396810e-02)
mat1.add_element("Al", 1.078290e-02)
mat1.add_element("Fe", 8.713330e-03)
mat1.add_element("Ni", 9.226710e-04)
mat1.add_element("Cr", 2.182440e-03)
mat1.add_element("Mn", 8.826210e-05)
mat1.add_element("Si", 1.134240e-04)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 8.306140e-05)
mat2.add_nuclide("U238", 3.973560e-02)
mat2.add_element("Fe", 4.854930e-03)
mat2.add_element("Ni", 4.996150e-04)
mat2.add_element("Cr", 1.215700e-03)
mat2.add_element("Mn", 4.789580e-05)
mat2.add_element("Si", 6.604920e-05)
mat2.add_element("C", 1.271620e-06)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CORE
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# REFL
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
