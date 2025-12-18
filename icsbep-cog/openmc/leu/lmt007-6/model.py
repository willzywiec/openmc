"""
LMT007-6: 430 U(4.948) Metal Rods in Water; Pitch=2.900cm; Hf=30cm; Hw=30+11.65=41.65cm (with A=63.24 rather than 63.19)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# LEU
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 2.153100e-05)
mat1.add_nuclide("U235", 2.405400e-03)
mat1.add_nuclide("U236", 1.098900e-05)
mat1.add_nuclide("U238", 4.559300e-02)

# H2O @ 23.5 C for Case 6
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.669900e-02)
mat2.add_nuclide("O16", 3.335000e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Fuel rod
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0, y0=30.0, r=0.38645)
# 22x22 lattice region
surf2 = openmc.model.RectangularParallelepiped(-31.9, 31.9, -31.9, 31.9, -499.95, 499.95)
# Water/boundary
surf3 = openmc.ZCylinder(surface_id=3, x0=-21.59, y0=41.65, r=50.53, boundary_type="vacuum")
surf101 = openmc.XPlane(surface_id=101, x0=-31.9)
surf102 = openmc.XPlane(surface_id=102, x0=-29.)
surf103 = openmc.XPlane(surface_id=103, x0=-26.1)
surf104 = openmc.XPlane(surface_id=104, x0=-23.2)
surf105 = openmc.XPlane(surface_id=105, x0=-20.3)
surf106 = openmc.XPlane(surface_id=106, x0=-17.4)
surf107 = openmc.XPlane(surface_id=107, x0=-14.5)
surf108 = openmc.XPlane(surface_id=108, x0=-11.6)
surf109 = openmc.XPlane(surface_id=109, x0=-8.7)
surf110 = openmc.XPlane(surface_id=110, x0=-5.8)
surf111 = openmc.XPlane(surface_id=111, x0=-2.9)
surf112 = openmc.XPlane(surface_id=112, x0=0.)
surf113 = openmc.XPlane(surface_id=113, x0=2.9)
surf114 = openmc.XPlane(surface_id=114, x0=5.8)
surf115 = openmc.XPlane(surface_id=115, x0=8.7)
surf116 = openmc.XPlane(surface_id=116, x0=11.6)
surf117 = openmc.XPlane(surface_id=117, x0=14.5)
surf118 = openmc.XPlane(surface_id=118, x0=17.4)
surf119 = openmc.XPlane(surface_id=119, x0=20.3)
surf120 = openmc.XPlane(surface_id=120, x0=23.2)
surf121 = openmc.XPlane(surface_id=121, x0=26.1)
surf122 = openmc.XPlane(surface_id=122, x0=29.)
surf123 = openmc.XPlane(surface_id=123, x0=31.9)
surf201 = openmc.YPlane(surface_id=201, y0=-31.9)
surf202 = openmc.YPlane(surface_id=202, y0=-29.)
surf203 = openmc.YPlane(surface_id=203, y0=-26.1)
surf204 = openmc.YPlane(surface_id=204, y0=-23.2)
surf205 = openmc.YPlane(surface_id=205, y0=-20.3)
surf206 = openmc.YPlane(surface_id=206, y0=-17.4)
surf207 = openmc.YPlane(surface_id=207, y0=-14.5)
surf208 = openmc.YPlane(surface_id=208, y0=-11.6)
surf209 = openmc.YPlane(surface_id=209, y0=-8.7)
surf210 = openmc.YPlane(surface_id=210, y0=-5.8)
surf211 = openmc.YPlane(surface_id=211, y0=-2.9)
surf212 = openmc.YPlane(surface_id=212, y0=0.)
surf213 = openmc.YPlane(surface_id=213, y0=2.9)
surf214 = openmc.YPlane(surface_id=214, y0=5.8)
surf215 = openmc.YPlane(surface_id=215, y0=8.7)
surf216 = openmc.YPlane(surface_id=216, y0=11.6)
surf217 = openmc.YPlane(surface_id=217, y0=14.5)
surf218 = openmc.YPlane(surface_id=218, y0=17.4)
surf219 = openmc.YPlane(surface_id=219, y0=20.3)
surf220 = openmc.YPlane(surface_id=220, y0=23.2)
surf221 = openmc.YPlane(surface_id=221, y0=26.1)
surf222 = openmc.YPlane(surface_id=222, y0=29.)
surf223 = openmc.YPlane(surface_id=223, y0=31.9)
surf301 = openmc.ZPlane(surface_id=301, z0=-999.0)
surf302 = openmc.ZPlane(surface_id=302, z0=999.0)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf1 & -surf2
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1])

universe2 = openmc.Universe(universe_id=2, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CORE
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.region = -surf2 & -surf3

# H2O
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# H2O
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf1 & -surf2

root_universe = openmc.Universe(cells=[cell1, cell2, cell5])
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
source.space = openmc.stats.Box((-2.45, -2.45, 14.0), (2.45, 2.45, 16.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
