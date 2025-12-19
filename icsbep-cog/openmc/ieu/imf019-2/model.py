"""
IEU-MET-FAST-019-2: Type 2 Assembly: U(45.5) metal cylinder on an aluminum support plate
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(45.5)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 3.635000e-04)
mat1.add_nuclide("U235", 2.111400e-02)
mat1.add_nuclide("U238", 2.461300e-02)
mat1.add_element("C", 7.976900e-04)
mat1.add_element("H", 2.563700e-04)
mat1.add_nuclide("O16", 1.209700e-04)
mat1.add_element("Al", 1.212700e-04)
mat1.add_element("Si", 1.165000e-04)
mat1.add_element("Fe", 7.812000e-05)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 6.010700e-02)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.ZCylinder(surface_id=1, r=21.5538, boundary_type="vacuum")
surf2 = openmc.ZPlane(surface_id=2, z0=0.0)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1002, z0=-0.47244, boundary_type="vacuum")
surf1_zmax = openmc.ZPlane(surface_id=1003, z0=13.8938, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U45.5
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & +surf2

# Al
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf2

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
source.space = openmc.stats.Point((0.0, 0.0, 6.9469))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
