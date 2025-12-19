"""
PMF026-1S: 11.9cm steel reflected spherical assembly of 9.7602 kg delta-239Pu(98%): simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.660300e-02)
mat1.add_nuclide("Pu240", 6.691700e-04)
mat1.add_element("Ga", 2.204300e-03)
mat1.add_element("Fe", 1.390600e-04)
mat1.add_element("C", 2.843500e-04)
mat1.add_element("Ni", 1.964200e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 7.941600e-02)
mat2.add_element("C", 1.126900e-03)
mat2.add_element("Si", 1.606500e-04)
mat2.add_element("Cr", 2.603200e-04)
mat2.add_element("Mn", 3.285000e-04)
mat2.add_element("Ni", 2.306300e-04)
mat2.add_element("Cu", 2.130000e-04)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 7.891900e-02)
mat3.add_element("C", 1.119900e-03)
mat3.add_element("Si", 1.596400e-04)
mat3.add_element("Cr", 2.586900e-04)
mat3.add_element("Mn", 3.264500e-04)
mat3.add_element("Ni", 2.291800e-04)
mat3.add_element("Cu", 2.116700e-04)

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.Sphere(surface_id=1, r=0.770)
surf2 = openmc.Sphere(surface_id=2, r=5.350)
surf3 = openmc.Sphere(surface_id=3, r=11.000)
surf4 = openmc.Sphere(surface_id=4, r=17.250, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# dPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# Steel1
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# Steel2
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf3 & -surf4

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
source.space = openmc.stats.Box((-2.0, -2.0, -2.0), (2.0, 2.0, 2.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
