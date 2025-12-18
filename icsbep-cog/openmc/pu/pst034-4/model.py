"""
PU-SOL-THERM-034-4: 11.700 kg Pu(8.3) @ H/X=228 with 1.42 gGd/L
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
mat1.add_element("Gd", 5.438000e-06)
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

# Hc per Table 33
surf1 = openmc.ZPlane(surface_id=1, z0=34.48)
# Soln tank/inner
surf2 = openmc.ZCylinder(surface_id=2, x0=0.0, y0=105.651, r=30.514)
# Soln tank/outer
surf3 = openmc.ZCylinder(surface_id=3, x0=-0.950, y0=105.730, r=30.593)
# Water height
surf4 = openmc.ZPlane(surface_id=4, z0=105.73)
# Refl tank/inner
surf5 = openmc.ZCylinder(surface_id=5, x0=-21.9, y0=120.823, r=50.523)
# Refl tank/outer
surf6 = openmc.ZCylinder(surface_id=6, x0=-22.177, y0=120.823, r=50.8)
# Tube/void
surf7 = openmc.ZCylinder(surface_id=7, x0=-22.177, y0=-0.950, r=2.555)
# Tube/wall
surf8 = openmc.ZCylinder(surface_id=8, x0=-22.177, y0=-0.950, r=2.86)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# Water
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf3 & -surf4 & -surf5 & -surf6 & +surf7 & +surf8

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf5 & -surf6 & +surf7 & +surf8

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf7 & -surf8

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
source.space = openmc.stats.Point((0.0, 0.0, 17.24))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
