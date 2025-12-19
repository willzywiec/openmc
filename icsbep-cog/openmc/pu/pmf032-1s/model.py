"""
PMF032-1S: 0.700cm cavity; 7.9716 kg alpha-239Pu(88%); 4.49cm Steel reflected; simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# a-Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu241", 6.727100e-04)
mat1.add_element("Fe", 2.861900e-04)
mat1.add_element("C", 1.260000e-03)
mat1.add_element("H", 3.240000e-04)
mat1.add_element("N", 3.497200e-05)
mat1.add_nuclide("O16", 5.184300e-05)

# Steel
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 7.992400e-02)
mat2.add_element("C", 1.134100e-03)
mat2.add_element("Si", 1.616700e-04)
mat2.add_element("Cr", 2.619800e-04)
mat2.add_element("Mn", 3.306100e-04)
mat2.add_element("Ni", 2.321000e-04)
mat2.add_element("Cu", 2.143700e-04)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.Sphere(surface_id=1, r=0.700)
surf2 = openmc.Sphere(surface_id=2, r=4.660)
surf3 = openmc.Sphere(surface_id=3, r=9.150, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# aPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# Steel
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

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
source.space = openmc.stats.Box((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
