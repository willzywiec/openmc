"""
U233-SOL-THERM-003 (Exp't 40 in 5"-Diam. Vessel) 2350 g U-233 @ H/X = 74
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 233U(98.7)O2F2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 8.579700e-04)
mat1.add_nuclide("U234", 4.000200e-06)
mat1.add_nuclide("U238", 7.652600e-06)
mat1.add_nuclide("H1", 6.330200e-02)
mat1.add_nuclide("O16", 3.339000e-02)
mat1.add_element("F", 1.801600e-03)
mat1.add_element("Al", 1.239200e-05)
mat1.add_element("Cr", 1.286000e-07)
mat1.add_element("Fe", 5.987100e-07)
mat1.add_element("Na", 2.363300e-05)
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
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0000, y0=91.2928, r=6.323)
# Vessel/Outer
surf2 = openmc.ZCylinder(surface_id=2, x0=-0.1291, y0=91.4219, r=6.4521)
# Paraffin/Outer
surf3 = openmc.ZCylinder(surface_id=3, x0=-15.3691, y0=91.4219, r=21.6921, boundary_type="vacuum")
# Hc
# surf4: Unsupported surface type "analytic" with params ['1.', 'z', '-56.3528', 'constant']

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
source.space = openmc.stats.Point((0.0, 0.0, 28.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
