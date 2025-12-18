"""
U233-SOL-THERM-009: 31.841 kg U-233 @ H/U-233 = 2,110 (Case 20)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 3.149800e-05)
mat1.add_nuclide("U234", 4.998700e-07)
mat1.add_nuclide("U235", 1.605600e-08)
mat1.add_nuclide("U238", 3.678000e-07)
mat1.add_nuclide("H1", 6.646800e-02)
mat1.add_element("N", 7.997600e-05)
mat1.add_nuclide("O16", 3.353200e-02)
mat1.add_element("Th", 2.585600e-07)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS316
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("P", 7.900000e+00)
mat2.add_element("Fe", 6.832000e+01)
mat2.add_element("Cr", 1.700000e+01)
mat2.add_element("Ni", 1.200000e+01)
mat2.add_element("Mo", 2.500000e+00)
mat2.add_element("N", 1.000000e-01)
mat2.add_element("C", 8.000000e-02)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZPlane(surface_id=1, z0=138.9126)
surf2 = openmc.ZCylinder(surface_id=2, x0=0.0, y0=243.84, r=77.3684)
surf3 = openmc.ZCylinder(surface_id=3, x0=-0.3302, y0=243.84, r=77.9686, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = +surf1 & -surf2 & -surf3

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = -surf1 & -surf2 & -surf3

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & -surf3

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
source.space = openmc.stats.Point((0.0, 0.0, 69.4563))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
