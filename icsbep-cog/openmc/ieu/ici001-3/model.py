"""
IEU-COMP-THERM-001-3: KBR-20
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

# Can-U(90)O2
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_element("Fe", 5.983900e-02)
mat11.add_element("Cr", 1.620600e-02)
mat11.add_element("Ni", 8.320700e-03)
mat11.add_element("Mn", 1.045800e-03)
mat11.add_element("Ti", 5.999600e-04)
mat11.add_element("Si", 8.523400e-04)
mat11.add_element("C", 3.986100e-04)

# Th
mat20 = openmc.Material(material_id=20)
mat20.set_density("sum")
mat20.add_nuclide("Th232", 2.881800e-02)
mat20.add_element("Fe", 9.586400e-05)

# Can-Th
mat21 = openmc.Material(material_id=21)
mat21.set_density("sum")
mat21.add_element("Al", 6.352500e-02)

materials = openmc.Materials([mat1, mat2, mat10, mat11, mat20, mat21])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# SST tube/inner
surf1 = openmc.ZCylinder(surface_id=1, r=2.4)
# SST tube/outer
surf2 = openmc.ZCylinder(surface_id=2, r=2.5)
# BCD/lower
surf3 = openmc.ZPlane(surface_id=3, z0=0.0, boundary_type="periodic")
# BCD/upper
surf4 = openmc.ZPlane(surface_id=4, z0=1.413, boundary_type="periodic")
# BCD/planar
# Prism 5: 6-sided polygon
surf5_0 = openmc.Plane(a=0.5000000035, b=-0.8660254018, c=0, d=2.5500000176)
surf5_1 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=2.5500000000)
surf5_2 = openmc.Plane(a=0.5000000035, b=0.8660254018, c=0, d=2.5500000176)
surf5_3 = openmc.Plane(a=-0.5000000035, b=0.8660254018, c=0, d=2.5500000176)
surf5_4 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=2.5500000000)
surf5_5 = openmc.Plane(a=-0.5000000035, b=-0.8660254018, c=0, d=2.5500000176)
# CH2/lower
surf6 = openmc.ZCylinder(surface_id=6, r=2.35)
# CH2/upper
surf7 = openmc.ZCylinder(surface_id=7, r=2.35)
# U(90)O2
surf10 = openmc.ZCylinder(surface_id=10, r=2.32)
# Can-U(90)O2
surf11 = openmc.ZCylinder(surface_id=11, r=2.34)
# Th
surf20 = openmc.ZCylinder(surface_id=20, r=2.3)
# Can-Th
surf21 = openmc.ZCylinder(surface_id=21, r=2.33)

# Z-plane surfaces for bounded cylinders
surf6_zmin = openmc.ZPlane(surface_id=1021, z0=0.0)
surf6_zmax = openmc.ZPlane(surface_id=1022, z0=0.12)
surf7_zmin = openmc.ZPlane(surface_id=1023, z0=1.12)
surf7_zmax = openmc.ZPlane(surface_id=1024, z0=1.24)
surf10_zmin = openmc.ZPlane(surface_id=1025, z0=1.26)
surf10_zmax = openmc.ZPlane(surface_id=1026, z0=1.393)
surf11_zmin = openmc.ZPlane(surface_id=1027, z0=1.24)
surf11_zmax = openmc.ZPlane(surface_id=1028, z0=1.413)
surf20_zmin = openmc.ZPlane(surface_id=1029, z0=0.15)
surf20_zmax = openmc.ZPlane(surface_id=1030, z0=1.09)
surf21_zmin = openmc.ZPlane(surface_id=1031, z0=0.12)
surf21_zmax = openmc.ZPlane(surface_id=1032, z0=1.12)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat10)
u1_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax)
u1_cell1 = openmc.Cell(fill=mat11)
u1_cell1.region = (+surf10 | -surf10_zmin | +surf10_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = (-surf7 & +surf7_zmin & -surf7_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf21 | -surf21_zmin | +surf21_zmax)
u1_cell3 = openmc.Cell(fill=mat20)
u1_cell3.region = (-surf20 & +surf20_zmin & -surf20_zmax)
u1_cell4 = openmc.Cell(fill=mat21)
u1_cell4.region = (+surf20 | -surf20_zmin | +surf20_zmax) & (-surf21 & +surf21_zmin & -surf21_zmax)
u1_cell5 = openmc.Cell(fill=mat2)
u1_cell5.region = (-surf6 & +surf6_zmin & -surf6_zmax) & (+surf21 | -surf21_zmin | +surf21_zmax)
u1_cell6 = openmc.Cell(fill=mat1)
u1_cell6.region = +surf1 & -surf2 & +surf3 & -surf4
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SST-Tube
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
source.space = openmc.stats.Point((0.0, 0.0, 1.3265))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
