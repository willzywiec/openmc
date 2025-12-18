"""
MIX-MET-FAST-002-3: Composite core of Ni-clad a-Pu(16.1) and HEU reflected by Nat-U
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# a-Pu(16.1)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.934900e-02)
mat1.add_nuclide("Pu240", 7.872800e-03)
mat1.add_nuclide("Pu241", 1.427900e-03)

# Ni
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Ni", 9.134200e-02)

# HEU
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 4.489200e-02)
mat3.add_nuclide("U238", 3.234000e-03)

# Nat-U
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U234", 2.643800e-06)
mat4.add_nuclide("U235", 3.461000e-04)
mat4.add_nuclide("U238", 4.772100e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.Sphere(surface_id=1, r=2.7051)
surf2 = openmc.Sphere(surface_id=2, r=2.7305)
surf3 = openmc.Sphere(surface_id=3, r=2.7356)
surf4 = openmc.Sphere(surface_id=4, r=5.3747)
surf5 = openmc.Sphere(surface_id=5, r=24.1199, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# aPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Ni
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# Gap
cell3 = openmc.Cell(cell_id=3)
cell3.region = +surf2 & -surf3

# HEU
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf3 & -surf4

# NatU
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf4 & -surf5

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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
