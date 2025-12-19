"""
PU-SOL-THERM-013 (Case 20) Seven cylinders with 10 cm surface-to-surface
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 2.096500e-08)
mat1.add_nuclide("Pu239", 2.767300e-04)
mat1.add_nuclide("Pu240", 1.221000e-05)
mat1.add_nuclide("Pu241", 8.856400e-07)
mat1.add_nuclide("Pu242", 4.581700e-08)
mat1.add_nuclide("Am241", 1.279600e-07)
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
surf1 = openmc.ZPlane(surface_id=1, z0=33.69)
# Tank/Inner per Figure 6
surf2 = openmc.ZCylinder(surface_id=2, r=12.494)
# Tank/Outer per Figure 6
surf3 = openmc.ZCylinder(surface_id=3, r=12.794)
# Room/Inner per Figure 5
surf4 = openmc.model.RectangularParallelepiped(-370.0, 840.0, -460.0, 420.0, -105.35500000000002, 894.645)
# Room/Outer per Figure 5
surf5 = openmc.model.RectangularParallelepiped(-515.0, 985.0, -605.0, 565.0, -145.35500000000002, 964.645, boundary_type="vacuum")
surf11 = openmc.ZCylinder(surface_id=11, x0=-17.794, y0=30.8201, r=12.794)
surf12 = openmc.ZCylinder(surface_id=12, x0=17.794, y0=30.8201, r=12.794)
surf13 = openmc.ZCylinder(surface_id=13, x0=-35.588, y0=0.0, r=12.794)
surf14 = openmc.ZCylinder(surface_id=14, x0=35.588, y0=0.0, r=12.794)
surf15 = openmc.ZCylinder(surface_id=15, x0=-17.794, y0=-30.8201, r=12.794)
surf16 = openmc.ZCylinder(surface_id=16, x0=17.794, y0=-30.8201, r=12.794)

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(surface_id=1016, z0=0.0)
surf2_zmax = openmc.ZPlane(surface_id=1017, z0=101.145)
surf3_zmin = openmc.ZPlane(surface_id=1018, z0=-1.355)
surf3_zmax = openmc.ZPlane(surface_id=1019, z0=102.345)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell()
u1_cell0.region = +surf1 & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell(fill=mat1)
u1_cell1.region = -surf1 & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = (+surf3 | -surf3_zmin | +surf3_zmax) & -surf4 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16

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
source.space = openmc.stats.Point((0.0, 0.0, 16.845))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
