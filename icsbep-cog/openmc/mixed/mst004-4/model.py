"""
MIX-SOL-THERM-004-4: Exp. No. 066 with 41.89 gPu/l and 63.65 gU/L with 0.61M
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 3.073200e-08)
mat1.add_nuclide("Pu239", 9.615500e-05)
mat1.add_nuclide("Pu240", 8.732700e-06)
mat1.add_nuclide("Pu241", 4.709200e-07)
mat1.add_nuclide("Pu242", 9.692200e-08)
mat1.add_nuclide("U234", 1.146400e-08)
mat1.add_nuclide("U235", 9.197600e-07)
mat1.add_nuclide("U236", 3.734900e-08)
mat1.add_nuclide("U238", 1.600600e-04)
mat1.add_nuclide("Am241", 5.439800e-07)
mat1.add_nuclide("H1", 6.347600e-02)
mat1.add_element("N", 1.124200e-03)
mat1.add_nuclide("O16", 3.525000e-02)
mat1.add_nuclide("B10", 2.275200e-08)
mat1.add_element("Cd", 1.279100e-08)
mat1.add_element("Fe", 1.325800e-06)
mat1.add_element("Gd", 1.764600e-09)
mat1.add_nuclide("Li6", 8.177200e-10)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.137600e-02)
mat2.add_element("Cr", 1.764800e-02)
mat2.add_element("Ni", 8.229200e-03)
mat2.add_element("C", 1.206300e-04)

# Water (066)
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.681100e-02)
mat3.add_nuclide("O16", 3.340500e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Dump line, inner
surf1 = openmc.ZCylinder(surface_id=1, r=2.625)
# Dump line, outer
surf2 = openmc.ZCylinder(surface_id=2, x0=-16.953, y0=-0.953, r=3.016)
# Solution tank, inner
surf3 = openmc.ZCylinder(surface_id=3, x0=0.0, y0=90.6, r=17.695)
# Solution tank, outer
surf4 = openmc.ZCylinder(surface_id=4, x0=-0.953, y0=91.553, r=17.774)
# Boundary
surf5 = openmc.model.RectangularParallelepiped(-49.38, 49.38, -46.75, 46.75, -16.953, 91.553, boundary_type="vacuum")
# Sol'n height
surf6 = openmc.ZPlane(surface_id=6, z0=28.11)
# Water height
surf7 = openmc.ZPlane(surface_id=7, z0=89.013)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf1 & -surf2 & -surf5

# SS304L
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2 & -surf5

# Soln
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = -surf3 & -surf6

# Void
cell4 = openmc.Cell(cell_id=4)
cell4.region = -surf3 & +surf6

# SS304L
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf2 & +surf3 & -surf4 & -surf5

# Water
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf2 & +surf4 & -surf5 & -surf7

# Void
cell7 = openmc.Cell(cell_id=7)
cell7.region = +surf2 & +surf4 & -surf5 & +surf7

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7])
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
source.space = openmc.stats.Point((0.0, 0.0, 14.055))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
