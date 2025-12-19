"""
PMF025-1D: 1.550cm steel reflected spherical assembly of 13.847 kg delta-239Pu(98%): detailed model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.618200e-02)
mat1.add_nuclide("Pu240", 6.614300e-04)
mat1.add_element("Ga", 2.148600e-03)
mat1.add_element("Fe", 1.606300e-04)
mat1.add_element("C", 2.987400e-04)
mat1.add_element("Ni", 4.252900e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu239", 3.682600e-02)
mat2.add_nuclide("Pu240", 6.732000e-04)
mat2.add_element("Ga", 2.200000e-03)
mat2.add_element("Fe", 1.471400e-04)
mat2.add_element("C", 3.040600e-04)
mat2.add_element("Ni", 1.572200e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Pu239", 3.671100e-02)
mat3.add_nuclide("Pu240", 6.711700e-04)
mat3.add_element("Ga", 2.219400e-03)
mat3.add_element("Fe", 1.303900e-04)
mat3.add_element("C", 3.031500e-04)
mat3.add_element("Ni", 1.940000e-03)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Pu239", 3.663200e-02)
mat4.add_nuclide("Pu240", 6.695800e-04)
mat4.add_element("Ga", 2.201200e-03)
mat4.add_element("Fe", 1.300900e-04)
mat4.add_element("C", 2.268200e-04)
mat4.add_element("Ni", 2.313200e-03)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Pu239", 3.672500e-02)
mat5.add_nuclide("Pu240", 6.715000e-04)
mat5.add_element("Ga", 2.220500e-03)
mat5.add_element("Fe", 1.467700e-04)
mat5.add_element("C", 3.032900e-04)
mat5.add_element("Ni", 1.870600e-03)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("Pu239", 3.665400e-02)
mat6.add_nuclide("Pu240", 6.699800e-04)
mat6.add_element("Ga", 2.176400e-03)
mat6.add_element("Fe", 1.464300e-04)
mat6.add_element("C", 3.026100e-04)
mat6.add_element("Ni", 1.981400e-03)

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Fe", 7.955700e-02)
mat7.add_element("C", 1.128900e-03)
mat7.add_element("Si", 1.609300e-04)
mat7.add_element("Cr", 2.607800e-04)
mat7.add_element("Mn", 3.290900e-04)
mat7.add_element("Ni", 2.310400e-04)
mat7.add_element("Cu", 2.133800e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=1.400)
surf2 = openmc.Sphere(surface_id=2, r=3.150)
surf3 = openmc.Sphere(surface_id=3, r=4.020)
surf4 = openmc.Sphere(surface_id=4, r=4.660)
surf5 = openmc.Sphere(surface_id=5, r=5.350)
surf6 = openmc.Sphere(surface_id=6, r=6.000)
surf7 = openmc.Sphere(surface_id=7, r=7.550, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# dPu1
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# dPu2
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# dPu3
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

# dPu4
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf3 & -surf4

# dPu5
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf4 & -surf5

# dPu6
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf5 & -surf6

# Steel
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = +surf6 & -surf7

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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
