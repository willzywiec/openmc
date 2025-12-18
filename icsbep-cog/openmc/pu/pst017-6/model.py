"""
PU-SOL-THERM-017 (Case 6) 300 and 256 mm cylinders with 115.1 gPu/L at 15 cm s-to-s
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 115.1 gPu/L Sol'n
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 2.096500e-08)
mat1.add_nuclide("Pu239", 2.767200e-04)
mat1.add_nuclide("Pu240", 1.221000e-05)
mat1.add_nuclide("Pu241", 8.962700e-07)
mat1.add_nuclide("Pu242", 4.581700e-08)
mat1.add_nuclide("Am241", 1.167400e-07)
mat1.add_element("N", 2.383700e-03)
mat1.add_nuclide("H1", 6.093100e-02)
mat1.add_element("Fe", 2.512500e-06)
mat1.add_element("Cr", 6.671100e-07)
mat1.add_element("Ni", 5.315100e-07)
mat1.add_element("Ca", 1.383900e-06)
mat1.add_nuclide("O16", 3.701100e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Z3 CN 18-10 SST
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.868600e-02)
mat2.add_element("Cr", 1.646900e-02)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Mn", 1.731900e-03)
mat2.add_element("Si", 1.693900e-03)
mat2.add_element("C", 1.585700e-04)
mat2.add_element("P", 6.143900e-05)
mat2.add_element("S", 4.451800e-05)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# 256-mm Tank/Hc'   per Table 1
surf1 = openmc.ZPlane(surface_id=1, z0=20.00)
# 256-mm Tank/Inner per Section 3.2
surf2 = openmc.ZCylinder(surface_id=2, x0=0.000, y0=101.145, r=12.49)
# 256-mm Tank/Outer per Section 3.2
surf3 = openmc.ZCylinder(surface_id=3, x0=-1.355, y0=102.345, r=12.8)
# 300-mm Tank/Hc-0.326 from Table 1
surf4 = openmc.ZPlane(surface_id=4, z0=40.014)
# 300-mm Tank/Inner per Figure 5
# surf5: Error converting surface type "cylinder": could not convert string to float: 'tr'
# 300-mm Tank/Outer per Figure 5
# surf6: Error converting surface type "cylinder": could not convert string to float: 'tr'

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = +surf1 & -surf2

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = -surf1 & -surf2

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & -surf3

# Void
cell4 = openmc.Cell(cell_id=4)
cell4.region = +surf4 & -surf5

# Soln
cell5 = openmc.Cell(cell_id=5, fill=mat1)
cell5.region = -surf4 & -surf5

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf5 & -surf6

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6])
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
source.space = openmc.stats.Box((-1.0, -1.0, 9.0), (43.79, 1.0, 21.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
