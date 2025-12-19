"""
PMF032-1D: 0.700cm cavity; 7.9699 kg alpha-239Pu(88%); 4.49cm Steel reflected; simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# a-Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu241", 9.094800e-04)
mat1.add_element("Fe", 3.051000e-04)
mat1.add_element("C", 1.992000e-03)
mat1.add_element("H", 8.334200e-04)
mat1.add_element("N", 8.995800e-05)
mat1.add_nuclide("O16", 1.333600e-04)

# a-Pu
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu241", 6.714700e-04)
mat2.add_element("Fe", 2.653400e-04)
mat2.add_element("C", 1.105300e-03)
mat2.add_element("H", 2.001100e-04)
mat2.add_element("N", 2.160000e-05)
mat2.add_nuclide("O16", 3.202000e-05)

# a-Pu
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Pu241", 7.407900e-04)
mat3.add_element("Fe", 3.035600e-04)
mat3.add_element("C", 1.192200e-03)
mat3.add_element("H", 2.750500e-04)
mat3.add_element("N", 2.968800e-05)
mat3.add_nuclide("O16", 4.401100e-05)

# a-Pu
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Pu241", 5.942500e-04)
mat4.add_element("Fe", 2.850000e-04)
mat4.add_element("C", 1.395600e-03)
mat4.add_element("H", 4.330800e-04)
mat4.add_element("N", 4.674600e-05)
mat4.add_nuclide("O16", 6.929700e-05)

# Steel
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 7.992400e-02)
mat5.add_element("C", 1.134100e-03)
mat5.add_element("Si", 1.616700e-04)
mat5.add_element("Cr", 2.619800e-04)
mat5.add_element("Mn", 3.306100e-04)
mat5.add_element("Ni", 2.321000e-04)
mat5.add_element("Cu", 2.143700e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=0.700)
surf2 = openmc.Sphere(surface_id=2, r=1.400)
surf3 = openmc.Sphere(surface_id=3, r=3.150)
surf4 = openmc.Sphere(surface_id=4, r=4.020)
surf5 = openmc.Sphere(surface_id=5, r=4.660)
surf6 = openmc.Sphere(surface_id=6, r=9.150, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# aPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# aPu
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# aPu
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf3 & -surf4

# aPu
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf4 & -surf5

# Steel
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf5 & -surf6

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5])
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
