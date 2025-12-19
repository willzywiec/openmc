"""
PU-SOL-THERM-034-3: 8.815 kg Pu(8.3) @ H/X=228 with 0.96 gGd/L
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 116.0 gPu(8.3)/L Sol'n
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.291200e-07)
mat1.add_nuclide("Pu239", 2.649800e-04)
mat1.add_nuclide("Pu240", 2.438300e-05)
mat1.add_nuclide("Pu241", 2.466100e-06)
mat1.add_nuclide("Pu242", 1.414100e-07)
mat1.add_nuclide("H1", 6.097300e-02)
mat1.add_element("N", 2.320300e-03)
mat1.add_nuclide("O16", 3.689000e-02)
mat1.add_element("Gd", 3.676400e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless Steel
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.327800e-02)
mat2.add_element("Cr", 1.653200e-02)
mat2.add_element("Ni", 6.509500e-03)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.669100e-02)
mat3.add_nuclide("O16", 3.334600e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Hc per Table 33
surf1 = openmc.ZPlane(surface_id=1, z0=25.98)
# Soln tank/inner
surf2 = openmc.ZCylinder(surface_id=2, r=30.514)
# Soln tank/outer
surf3 = openmc.ZCylinder(surface_id=3, r=30.593)
# Water height
surf4 = openmc.ZPlane(surface_id=4, z0=105.73)
# Refl tank/inner
surf5 = openmc.ZCylinder(surface_id=5, r=50.523)
# Refl tank/outer
surf6 = openmc.ZCylinder(surface_id=6, r=50.8)
# Tube/void
surf7 = openmc.ZCylinder(surface_id=7, r=2.555)
# Tube/wall
surf8 = openmc.ZCylinder(surface_id=8, r=2.86)

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(surface_id=1008, z0=0.0)
surf2_zmax = openmc.ZPlane(surface_id=1009, z0=105.651)
surf3_zmin = openmc.ZPlane(surface_id=1010, z0=-0.95)
surf3_zmax = openmc.ZPlane(surface_id=1011, z0=105.73)
surf5_zmin = openmc.ZPlane(surface_id=1012, z0=-21.9)
surf5_zmax = openmc.ZPlane(surface_id=1013, z0=120.823)
surf6_zmin = openmc.ZPlane(surface_id=1014, z0=-22.177)
surf6_zmax = openmc.ZPlane(surface_id=1015, z0=120.823)
surf7_zmin = openmc.ZPlane(surface_id=1016, z0=-22.177)
surf7_zmax = openmc.ZPlane(surface_id=1017, z0=-0.95)
surf8_zmin = openmc.ZPlane(surface_id=1018, z0=-22.177)
surf8_zmax = openmc.ZPlane(surface_id=1019, z0=-0.95)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & (-surf2 & +surf2_zmin & -surf2_zmax)

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# Water
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = (+surf3 | -surf3_zmin | +surf3_zmax) & -surf4 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax)

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax)

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5])
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
source.space = openmc.stats.Point((0.0, 0.0, 12.99))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
