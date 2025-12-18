"""
U233-SOL-THERM-002 (Exp't 12 in 9"-Diam. Vessel) 621 g U-233 @ H/X = 355
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 233U(98.7)O2(NO3)2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 1.821600e-04)
mat1.add_nuclide("U234", 8.456800e-07)
mat1.add_nuclide("U238", 1.590600e-06)
mat1.add_nuclide("H1", 6.461800e-02)
mat1.add_nuclide("O16", 3.420700e-02)
mat1.add_element("N", 5.375300e-04)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Al-2S
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 5.810800e-04)

# Paraffin
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 7.991100e-02)
mat3.add_nuclide("O16", 3.841900e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Vessel/Inner
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0000, y0=23.0033, r=11.4351)
# Vessel/Outer
surf2 = openmc.ZCylinder(surface_id=2, x0=-0.1291, y0=23.1324, r=11.5642)
# Paraffin/Outer
surf3 = openmc.ZCylinder(surface_id=3, x0=-15.3691, y0=38.3724, r=26.8042, boundary_type="vacuum")
# Hc
# surf4: Unsupported surface type "analytic" with params ['1.', 'z', '-21.4331', 'constant']

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf1

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = -surf1

# Al2S
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf1 & -surf2

# Prffn
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf2 & -surf3

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4])
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
source.space = openmc.stats.Point((0.0, 0.0, 10.7))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
