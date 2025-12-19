"""
IEU-MET-FAST-004-1S: 15.222 kg graphite reflected spherical assembly of 212.080 kg U(36) [Simplified Model] Rev. 2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(36)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.565200e-04)
mat1.add_nuclide("U235", 1.738400e-02)
mat1.add_nuclide("U238", 2.966200e-02)
mat1.add_element("C", 6.575200e-04)
mat1.add_element("Fe", 1.209800e-04)
mat1.add_element("W", 1.012100e-05)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 7.771600e-02)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=2.788)
surf2 = openmc.Sphere(surface_id=2, r=14.0)
surf3 = openmc.Sphere(surface_id=3, r=17.2, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U36
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# C
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
source.space = openmc.stats.Box((-4.0, -4.0, -4.0), (4.0, 4.0, 4.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
