"""
PU-SOL-THERM-014 (Case 14) Three cylinders with 10 cm s-to-s
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 2.096500e-08)
mat1.add_nuclide("Pu239", 2.767200e-04)
mat1.add_nuclide("Pu240", 1.220900e-05)
mat1.add_nuclide("Pu241", 9.031700e-07)
mat1.add_nuclide("Pu242", 4.581700e-08)
mat1.add_nuclide("Am241", 1.101300e-07)
mat1.add_element("N", 2.383700e-03)
mat1.add_nuclide("H1", 6.093000e-02)
mat1.add_element("Fe", 2.512500e-06)
mat1.add_element("Cr", 6.671100e-07)
mat1.add_element("Ni", 5.315100e-07)
mat1.add_element("Ca", 1.383900e-06)
mat1.add_nuclide("O16", 3.701100e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 1.035000e-02)
mat2.add_nuclide("B10", 1.602000e-06)
mat2.add_nuclide("O16", 4.347000e-02)
mat2.add_element("Al", 1.563000e-03)
mat2.add_element("Si", 1.417000e-02)
mat2.add_element("Ca", 6.424000e-03)
mat2.add_element("Fe", 7.621000e-04)
mat2.add_s_alpha_beta("c_H_in_H2O")

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.868600e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Mn", 1.731900e-03)
mat3.add_element("Si", 1.693900e-03)
mat3.add_element("C", 1.585700e-04)
mat3.add_element("P", 6.143900e-05)
mat3.add_element("S", 4.451800e-05)

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Hc per Table 1
surf1 = openmc.ZPlane(surface_id=1, z0=31.26)
# Tank/Inner per Figure 6
surf2 = openmc.ZCylinder(surface_id=2, x0=0.000, y0=101.171, r=14.7)
# Tank/Outer per Figure 6
surf3 = openmc.ZCylinder(surface_id=3, x0=-1.329, y0=102.371, r=15.0)
# Room/Inner per Figure 5
surf4 = openmc.model.RectangularParallelepiped(-370.0, 840.0, -460.0, 420.0, -105.32900000000001, 894.671)
# Room/Outer per Figure 5
surf5 = openmc.model.RectangularParallelepiped(-515.0, 985.0, -605.0, 565.0, -145.329, 964.671, boundary_type="vacuum")
# Array dimensions per
# surf11: Error converting surface type "cylinder": could not convert string to float: 'tr'
# Table 1 and Figure 7
# surf12: Error converting surface type "cylinder": could not convert string to float: 'tr'
# Table 1 and Figure 7
# surf13: Error converting surface type "cylinder": could not convert string to float: 'tr'

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell()
u1_cell0.region = +surf1 & -surf2
u1_cell1 = openmc.Cell(fill=mat1)
u1_cell1.region = -surf1 & -surf2
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = +surf2 & -surf3
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf4 & +surf11 & +surf12 & +surf13

# Conc
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf4 & -surf5

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
source.space = openmc.stats.Box((-12.5, -21.0, 14.6), (24.1, 21.0, 16.6))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
