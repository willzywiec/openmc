"""
LST012-2: TRACY R203-Hc2 (transient)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Fuel
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 7.991000e-07)
mat1.add_nuclide("U235", 9.926200e-05)
mat1.add_nuclide("U236", 9.903900e-08)
mat1.add_nuclide("U238", 8.831600e-04)
mat1.add_nuclide("H1", 5.767400e-02)
mat1.add_element("N", 2.315900e-03)
mat1.add_nuclide("O16", 3.757700e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 9.512500e-06)
mat2.add_element("Si", 6.053400e-04)
mat2.add_element("Mn", 8.215300e-04)
mat2.add_element("P", 1.816000e-05)
mat2.add_element("S", 1.729500e-06)
mat2.add_element("Ni", 8.708300e-03)
mat2.add_element("Cr", 1.567800e-02)
mat2.add_element("Co", 3.459100e-05)
mat2.add_element("Fe", 6.060000e-02)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, r=3.445)
surf2 = openmc.ZCylinder(surface_id=2, r=3.81)
surf3 = openmc.ZCylinder(surface_id=3, x0=0.00, y0=200.0, r=25.035)
surf4 = openmc.ZCylinder(surface_id=4, x0=-8.06, y0=202.6, r=26.085)
# critical
surf5 = openmc.ZPlane(surface_id=5, z0=62.376, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SST
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = +surf1 & -surf2 & -surf4

# SOLN
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf2 & -surf3 & -surf5

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & +surf3 & -surf4

root_universe = openmc.Universe(cells=[cell1, cell2, cell3])
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
source.space = openmc.stats.Point((0.0, 0.0, 31.188))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
