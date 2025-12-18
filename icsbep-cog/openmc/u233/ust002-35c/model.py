"""
U233-SOL-THERM-002 (Exp't 35 in 8"-Diam. Vessel) 745 g U-233 @ H/X = 212
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 233U(98.7)O2(NO3)2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 2.996900e-04)
mat1.add_nuclide("U234", 1.391300e-06)
mat1.add_nuclide("U238", 2.616800e-06)
mat1.add_nuclide("H1", 6.358000e-02)
mat1.add_nuclide("O16", 3.471500e-02)
mat1.add_element("N", 8.055800e-04)
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
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0000, y0=20.6485, r=10.2645)
# Vessel/Outer
surf2 = openmc.ZCylinder(surface_id=2, x0=-0.1291, y0=20.7776, r=10.3936)
# Paraffin/Outer
surf3 = openmc.ZCylinder(surface_id=3, x0=-15.3691, y0=36.0176, r=25.6336, boundary_type="vacuum")
# Hc
# surf4: Unsupported surface type "analytic" with params ['1.', 'z', '-19.4195', 'constant']

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
source.space = openmc.stats.Point((0.0, 0.0, 9.7))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
