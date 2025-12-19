"""
LMT007-2: 266 U(4.948) Metal Rods in Water; Pitch=1.530cm; Hf=30cm; Hw=59.74-21.59=38.15cm
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

# H2O @ 22.3 C for Case 2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.671800e-02)
mat2.add_nuclide("O16", 3.335900e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Fuel rod
surf1 = openmc.ZCylinder(surface_id=1, r=0.38645)
# 17x18 lattice region
surf2 = openmc.model.RectangularParallelepiped(-13.005, 13.005, -13.77, 13.77, -499.95, 499.95)
# Water/boundary
surf3 = openmc.ZCylinder(surface_id=3, r=50.53)
surf101 = openmc.XPlane(surface_id=101, x0=-13.005)
surf102 = openmc.XPlane(surface_id=102, x0=-11.475)
surf103 = openmc.XPlane(surface_id=103, x0=-9.945)
surf104 = openmc.XPlane(surface_id=104, x0=-8.415)
surf105 = openmc.XPlane(surface_id=105, x0=-6.885)
surf106 = openmc.XPlane(surface_id=106, x0=-5.355)
surf107 = openmc.XPlane(surface_id=107, x0=-3.825)
surf108 = openmc.XPlane(surface_id=108, x0=-2.295)
surf109 = openmc.XPlane(surface_id=109, x0=-0.765)
surf110 = openmc.XPlane(surface_id=110, x0=0.765)
surf111 = openmc.XPlane(surface_id=111, x0=2.295)
surf112 = openmc.XPlane(surface_id=112, x0=3.825)
surf113 = openmc.XPlane(surface_id=113, x0=5.355)
surf114 = openmc.XPlane(surface_id=114, x0=6.885)
surf115 = openmc.XPlane(surface_id=115, x0=8.415)
surf116 = openmc.XPlane(surface_id=116, x0=9.945)
surf117 = openmc.XPlane(surface_id=117, x0=11.475)
surf118 = openmc.XPlane(surface_id=118, x0=13.005)
surf201 = openmc.YPlane(surface_id=201, y0=-13.77)
surf202 = openmc.YPlane(surface_id=202, y0=-12.24)
surf203 = openmc.YPlane(surface_id=203, y0=-10.71)
surf204 = openmc.YPlane(surface_id=204, y0=-9.18)
surf205 = openmc.YPlane(surface_id=205, y0=-7.65)
surf206 = openmc.YPlane(surface_id=206, y0=-6.12)
surf207 = openmc.YPlane(surface_id=207, y0=-4.59)
surf208 = openmc.YPlane(surface_id=208, y0=-3.06)
surf209 = openmc.YPlane(surface_id=209, y0=-1.53)
surf210 = openmc.YPlane(surface_id=210, y0=0.)
surf211 = openmc.YPlane(surface_id=211, y0=1.53)
surf212 = openmc.YPlane(surface_id=212, y0=3.06)
surf213 = openmc.YPlane(surface_id=213, y0=4.59)
surf214 = openmc.YPlane(surface_id=214, y0=6.12)
surf215 = openmc.YPlane(surface_id=215, y0=7.65)
surf216 = openmc.YPlane(surface_id=216, y0=9.18)
surf217 = openmc.YPlane(surface_id=217, y0=10.71)
surf218 = openmc.YPlane(surface_id=218, y0=12.24)
surf219 = openmc.YPlane(surface_id=219, y0=13.77)
surf301 = openmc.ZPlane(surface_id=301, z0=-999.0)
surf302 = openmc.ZPlane(surface_id=302, z0=999.0)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=0.0)
surf1_zmax = openmc.ZPlane(z0=30.0)
surf3_zmin = openmc.ZPlane(z0=-21.59, boundary_type="vacuum")
surf3_zmax = openmc.ZPlane(z0=38.15, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & -surf2
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1])

universe2 = openmc.Universe(universe_id=2, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CORE
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.region = -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

# H2O
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

# H2O
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = (+surf1 | -surf1_zmin | +surf1_zmax) & -surf2

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
source.space = openmc.stats.Box((-1.0, -1.7650000000000001, 14.0), (1.0, 1.7650000000000001, 16.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
