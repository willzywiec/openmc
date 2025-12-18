"""
IEU-COMP-THERM-001-2: KBR-19
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

# CH2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 7.258800e-02)
mat2.add_element("C", 3.629400e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

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

materials = openmc.Materials([mat1, mat2, mat10, mat11, mat12, mat20, mat21])

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
surf4 = openmc.ZPlane(surface_id=4, z0=2.782, boundary_type="periodic")
# BCD/planar
# Prism 5: 6-sided polygon
surf5_0 = openmc.Plane(a=0.5000000035, b=-0.8660254018, c=0, d=2.5500000176)
surf5_1 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=2.5500000000)
surf5_2 = openmc.Plane(a=0.5000000035, b=0.8660254018, c=0, d=2.5500000176)
surf5_3 = openmc.Plane(a=-0.5000000035, b=0.8660254018, c=0, d=2.5500000176)
surf5_4 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=2.5500000000)
surf5_5 = openmc.Plane(a=-0.5000000035, b=-0.8660254018, c=0, d=2.5500000176)
# CH2/1
surf11 = openmc.ZCylinder(surface_id=11, x0=0.000, y0=0.015, r=2.35)
# U(90)O2
surf20 = openmc.ZCylinder(surface_id=20, x0=0.035, y0=0.168, r=2.32)
# Can-UO2
surf21 = openmc.ZCylinder(surface_id=21, x0=0.015, y0=0.188, r=2.34)
# CH2/2
surf31 = openmc.ZCylinder(surface_id=31, x0=0.188, y0=0.203, r=2.35)
# Th
surf40 = openmc.ZCylinder(surface_id=40, x0=0.233, y0=1.173, r=2.3)
# Can-Th
surf41 = openmc.ZCylinder(surface_id=41, x0=0.203, y0=1.203, r=2.33)
# CH2/3
surf51 = openmc.ZCylinder(surface_id=51, x0=1.203, y0=1.218, r=2.35)
# U(36)O2
surf60 = openmc.ZCylinder(surface_id=60, x0=1.238, y0=1.371, r=2.32)
# Can-UO2
surf61 = openmc.ZCylinder(surface_id=61, x0=1.218, y0=1.391, r=2.34)
# CH2/4
surf71 = openmc.ZCylinder(surface_id=71, x0=1.391, y0=1.406, r=2.35)
# U(90)O2
surf80 = openmc.ZCylinder(surface_id=80, x0=1.426, y0=1.559, r=2.32)
# Can-UO2
surf81 = openmc.ZCylinder(surface_id=81, x0=1.406, y0=1.579, r=2.34)
# CH2/5
surf91 = openmc.ZCylinder(surface_id=91, x0=1.579, y0=1.594, r=2.35)
# Th
surf100 = openmc.ZCylinder(surface_id=100, x0=1.624, y0=2.564, r=2.3)
# Can-Th
surf101 = openmc.ZCylinder(surface_id=101, x0=1.594, y0=2.594, r=2.33)
# CH2/6
surf111 = openmc.ZCylinder(surface_id=111, x0=2.594, y0=2.609, r=2.35)
# U(90)O2
surf120 = openmc.ZCylinder(surface_id=120, x0=2.629, y0=2.762, r=2.32)
# Can-UO2
surf121 = openmc.ZCylinder(surface_id=121, x0=2.609, y0=2.782, r=2.34)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat2)
u1_cell0.region = -surf11 & +surf3
u1_cell1 = openmc.Cell(fill=mat10)
u1_cell1.region = -surf21 & +surf11
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = -surf31 & +surf21
u1_cell3 = openmc.Cell(fill=mat20)
u1_cell3.region = +surf21 & -surf41 & +surf31
u1_cell4 = openmc.Cell(fill=mat2)
u1_cell4.region = -surf51 & +surf41
u1_cell5 = openmc.Cell(fill=mat11)
u1_cell5.region = -surf61 & +surf51
u1_cell6 = openmc.Cell(fill=mat2)
u1_cell6.region = -surf71 & +surf61
u1_cell7 = openmc.Cell(fill=mat10)
u1_cell7.region = -surf81 & +surf71
u1_cell8 = openmc.Cell(fill=mat2)
u1_cell8.region = -surf91 & +surf81
u1_cell9 = openmc.Cell(fill=mat20)
u1_cell9.region = +surf21 & -surf101 & +surf91
u1_cell10 = openmc.Cell(fill=mat2)
u1_cell10.region = -surf111 & +surf101
u1_cell11 = openmc.Cell(fill=mat10)
u1_cell11.region = -surf121 & +surf111 & -surf4
u1_cell12 = openmc.Cell(fill=mat1)
u1_cell12.region = +surf1 & -surf2 & +surf3 & -surf4
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11, u1_cell12])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SS-Tube
cell14 = openmc.Cell(cell_id=14, fill=mat1)
cell14.region = +surf1 & -surf2 & +surf3 & -surf4

root_universe = openmc.Universe(cells=[cell14])
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
source.space = openmc.stats.Box((-1.0, -1.0, -0.8985), (1.0, 1.0, 3.6955))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
