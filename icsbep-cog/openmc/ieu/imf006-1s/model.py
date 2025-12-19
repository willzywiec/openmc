"""
IEU-MET-FAST-006-1S: Spherical assembly of 178.853 kg U(36) reflected by 140.700 kg Duralumin [Simplified Model] Rev. 2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(36)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.551800e-04)
mat1.add_nuclide("U235", 1.716100e-02)
mat1.add_nuclide("U238", 2.931000e-02)
mat1.add_element("W", 1.072100e-05)
mat1.add_element("Fe", 1.234500e-04)
mat1.add_element("C", 6.488800e-04)
mat1.add_element("Cu", 2.675500e-04)
mat1.add_element("Ni", 2.896900e-04)

# 1st Duralumin layer
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.234200e-02)
mat2.add_element("Fe", 9.578800e-04)
mat2.add_element("Cu", 9.861400e-04)

# 2nd Duralumin layer
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.206700e-02)
mat3.add_element("Fe", 9.528600e-04)
mat3.add_element("Cu", 9.809700e-04)

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=2.100)
surf2 = openmc.Sphere(surface_id=2, r=13.25)
surf3 = openmc.Sphere(surface_id=3, r=15.00)
surf4 = openmc.Sphere(surface_id=4, r=25.00, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U36
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# DURAL1
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# DURAL2
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
source.space = openmc.stats.Box((-4.0, -4.0, -4.0), (4.0, 4.0, 4.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
