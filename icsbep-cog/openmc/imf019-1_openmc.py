"""
IEU-MET-FAST-019-1: Type 1 Assembly: U(45.5) metal hexagon on an aluminum support plate
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(45.5)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 3.634100e-04)
mat1.add_nuclide("U235", 2.110800e-02)
mat1.add_nuclide("U238", 2.460700e-02)
mat1.add_element("C", 7.739900e-04)
mat1.add_element("H", 2.230700e-04)
mat1.add_nuclide("O16", 1.132900e-04)
mat1.add_element("Al", 1.212400e-04)
mat1.add_element("Si", 1.164700e-04)
mat1.add_element("Fe", 7.810000e-05)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 6.010700e-02)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Prism 1: 6-sided polygon
surf1_0 = openmc.Plane(a=0.8660254039, b=-0.4999999999, c=0, d=14.0620499963)
surf1_1 = openmc.Plane(a=0.8660254039, b=0.4999999999, c=0, d=14.0620499963)
surf1_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=14.0620500000)
surf1_3 = openmc.Plane(a=-0.8660254039, b=0.4999999999, c=0, d=14.0620499963)
surf1_4 = openmc.Plane(a=-0.8660254039, b=-0.4999999999, c=0, d=14.0620499963)
surf1_5 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=14.0620500000)
surf2 = openmc.ZPlane(surface_id=2, z0=0.0)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U45.5
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1_0 & -surf1_1 & -surf1_2 & -surf1_3 & -surf1_4 & -surf1_5) & +surf2

# Al
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (-surf1_0 & -surf1_1 & -surf1_2 & -surf1_3 & -surf1_4 & -surf1_5) & -surf2

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
source.space = openmc.stats.Point((0.0, 0.0, 9.2202))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
