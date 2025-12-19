"""
IEU-COMP-THERM-001-1: KBR-18
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# SST Tube
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_element("Fe", 6.121600e-02)
mat1.add_element("Cr", 1.657900e-02)
mat1.add_element("Ni", 8.512200e-03)
mat1.add_element("Mn", 1.069800e-03)
mat1.add_element("Ti", 6.137700e-04)
mat1.add_element("Si", 8.719600e-04)
mat1.add_element("C", 4.077800e-04)

# U(90)O2
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("U235", 1.353600e-02)
mat10.add_nuclide("U238", 1.466300e-03)
mat10.add_nuclide("O16", 3.037700e-02)

# U(36)O2
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_nuclide("U235", 5.389800e-03)
mat11.add_nuclide("U238", 9.534900e-03)
mat11.add_nuclide("O16", 3.000000e-02)

# Can-UO2
mat12 = openmc.Material(material_id=12)
mat12.set_density("sum")
mat12.add_element("Fe", 5.983900e-02)
mat12.add_element("Cr", 1.620600e-02)
mat12.add_element("Ni", 8.320700e-03)
mat12.add_element("Mn", 1.045800e-03)
mat12.add_element("Ti", 5.999600e-04)
mat12.add_element("Si", 8.523400e-04)
mat12.add_element("C", 3.986100e-04)

# Th
mat20 = openmc.Material(material_id=20)
mat20.set_density("sum")
mat20.add_nuclide("Th232", 2.881800e-02)
mat20.add_element("Fe", 9.586400e-05)

# Can-Th
mat21 = openmc.Material(material_id=21)
mat21.set_density("sum")
mat21.add_element("Al", 6.352500e-02)

materials = openmc.Materials([mat1, mat10, mat11, mat12, mat20, mat21])

# ==============================================================================
# Geometry
# ==============================================================================

# SST tube/inner
surf1 = openmc.ZCylinder(surface_id=1, r=2.4)
# SST tube/outer
surf2 = openmc.ZCylinder(surface_id=2, r=2.5)
# BCD/lower
surf3 = openmc.ZPlane(surface_id=3, z0=0.0, boundary_type="periodic")
# BCD/upper
surf4 = openmc.ZPlane(surface_id=4, z0=2.692, boundary_type="periodic")
# BCD/planar
# Prism 5: 6-sided polygon
surf5_0 = openmc.Plane(a=0.5000000035, b=-0.8660254018, c=0, d=2.5500000176)
surf5_1 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=2.5500000000)
surf5_2 = openmc.Plane(a=0.5000000035, b=0.8660254018, c=0, d=2.5500000176)
surf5_3 = openmc.Plane(a=-0.5000000035, b=0.8660254018, c=0, d=2.5500000176)
surf5_4 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=2.5500000000)
surf5_5 = openmc.Plane(a=-0.5000000035, b=-0.8660254018, c=0, d=2.5500000176)
# U(90)O2
surf10 = openmc.ZCylinder(surface_id=10, r=2.32)
# Can-UO2
surf11 = openmc.ZCylinder(surface_id=11, r=2.34)
# Th
surf20 = openmc.ZCylinder(surface_id=20, r=2.3)
# Can-Th
surf21 = openmc.ZCylinder(surface_id=21, r=2.33)
# U(36)O2
surf30 = openmc.ZCylinder(surface_id=30, r=2.32)
# Can-UO2
surf31 = openmc.ZCylinder(surface_id=31, r=2.34)
# U(90)O2
surf40 = openmc.ZCylinder(surface_id=40, r=2.32)
# Can-UO2
surf41 = openmc.ZCylinder(surface_id=41, r=2.34)
# Th
surf50 = openmc.ZCylinder(surface_id=50, r=2.3)
# Can-Th
surf51 = openmc.ZCylinder(surface_id=51, r=2.33)
# U(90)O2
surf60 = openmc.ZCylinder(surface_id=60, r=2.32)
# Can-UO2
surf61 = openmc.ZCylinder(surface_id=61, r=2.34)

# Z-plane surfaces for bounded cylinders
surf10_zmin = openmc.ZPlane(z0=0.02)
surf10_zmax = openmc.ZPlane(z0=0.153)
surf11_zmin = openmc.ZPlane(z0=0.0)
surf11_zmax = openmc.ZPlane(z0=0.173)
surf20_zmin = openmc.ZPlane(z0=0.203)
surf20_zmax = openmc.ZPlane(z0=1.143)
surf21_zmin = openmc.ZPlane(z0=0.173)
surf21_zmax = openmc.ZPlane(z0=1.173)
surf30_zmin = openmc.ZPlane(z0=1.193)
surf30_zmax = openmc.ZPlane(z0=1.326)
surf31_zmin = openmc.ZPlane(z0=1.173)
surf31_zmax = openmc.ZPlane(z0=1.346)
surf40_zmin = openmc.ZPlane(z0=1.366)
surf40_zmax = openmc.ZPlane(z0=1.499)
surf41_zmin = openmc.ZPlane(z0=1.346)
surf41_zmax = openmc.ZPlane(z0=1.519)
surf50_zmin = openmc.ZPlane(z0=1.549)
surf50_zmax = openmc.ZPlane(z0=2.489)
surf51_zmin = openmc.ZPlane(z0=1.519)
surf51_zmax = openmc.ZPlane(z0=2.519)
surf60_zmin = openmc.ZPlane(z0=2.539)
surf60_zmax = openmc.ZPlane(z0=2.672)
surf61_zmin = openmc.ZPlane(z0=2.519)
surf61_zmax = openmc.ZPlane(z0=2.692)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat10)
u1_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf10 | -surf10_zmin | +surf10_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax) & +surf3
u1_cell1 = openmc.Cell(fill=mat20)
u1_cell1.region = (-surf20 & +surf20_zmin & -surf20_zmax) & (+surf21 | -surf21_zmin | +surf21_zmax) & (+surf20 | -surf20_zmin | +surf20_zmax) & (-surf21 & +surf21_zmin & -surf21_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax)
u1_cell2 = openmc.Cell(fill=mat11)
u1_cell2.region = (-surf30 & +surf30_zmin & -surf30_zmax) & (+surf30 | -surf30_zmin | +surf30_zmax) & (-surf31 & +surf31_zmin & -surf31_zmax) & (+surf21 | -surf21_zmin | +surf21_zmax)
u1_cell3 = openmc.Cell(fill=mat10)
u1_cell3.region = (-surf40 & +surf40_zmin & -surf40_zmax) & (+surf40 | -surf40_zmin | +surf40_zmax) & (-surf41 & +surf41_zmin & -surf41_zmax) & (+surf31 | -surf31_zmin | +surf31_zmax)
u1_cell4 = openmc.Cell(fill=mat20)
u1_cell4.region = (-surf50 & +surf50_zmin & -surf50_zmax) & (+surf21 | -surf21_zmin | +surf21_zmax) & (+surf50 | -surf50_zmin | +surf50_zmax) & (-surf51 & +surf51_zmin & -surf51_zmax) & (+surf41 | -surf41_zmin | +surf41_zmax)
u1_cell5 = openmc.Cell(fill=mat10)
u1_cell5.region = (-surf60 & +surf60_zmin & -surf60_zmax) & (+surf60 | -surf60_zmin | +surf60_zmax) & (-surf61 & +surf61_zmin & -surf61_zmax) & (+surf41 | -surf41_zmin | +surf41_zmax) & -surf4
u1_cell6 = openmc.Cell(fill=mat1)
u1_cell6.region = +surf1 & -surf2 & +surf3 & -surf4
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SS-Tube
cell8 = openmc.Cell(cell_id=8, fill=mat1)
cell8.region = +surf1 & -surf2 & +surf3 & -surf4

root_universe = openmc.Universe(cells=[cell8])
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
source.space = openmc.stats.Box((-1.0, -1.0, -0.9135), (1.0, 1.0, 3.6055))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
