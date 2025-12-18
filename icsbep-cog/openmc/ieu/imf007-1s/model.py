"""
IEU-MET-FAST-007-1: Big Ten [Rev. 2]
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(10)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 2.476100e-05)
mat1.add_nuclide("U235", 4.846100e-03)
mat1.add_nuclide("U236", 4.334800e-05)
mat1.add_nuclide("U238", 4.269500e-02)

# HEU & Nat-U
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 5.405800e-05)
mat2.add_nuclide("U235", 4.983100e-03)
mat2.add_nuclide("U236", 1.373300e-05)
mat2.add_nuclide("U238", 4.310800e-02)

# Nat-U
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U234", 2.651800e-06)
mat3.add_nuclide("U235", 3.470100e-04)
mat3.add_nuclide("U238", 4.784600e-02)

# D38
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U234", 2.867200e-07)
mat4.add_nuclide("U235", 1.005800e-04)
mat4.add_nuclide("U236", 1.146800e-06)
mat4.add_nuclide("U238", 4.767700e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# U10
surf1 = openmc.ZCylinder(surface_id=1, x0=23.81250, y0=39.05250, r=2.25014)
# U10
surf2 = openmc.ZCylinder(surface_id=2, x0=4.35102, y0=23.81250, r=3.10996)
# U10
surf3 = openmc.ZCylinder(surface_id=3, x0=-22.39010, y0=4.35102, r=12.54604)
# U10
surf4 = openmc.ZCylinder(surface_id=4, x0=-41.73361, y0=-22.39010, r=7.62)
# Nat-U
surf5 = openmc.ZCylinder(surface_id=5, x0=-41.73361, y0=-38.24644, r=26.67)
# HEU+Nat-U
surf6 = openmc.ZCylinder(surface_id=6, x0=-38.24644, y0=17.16665, r=26.67)
# Nat-U
surf7 = openmc.ZCylinder(surface_id=7, x0=17.16665, y0=23.81250, r=26.67)
# D38
surf8 = openmc.ZCylinder(surface_id=8, x0=-57.46750, y0=39.05250, r=41.91, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U10
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf8

# U10
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf1 & -surf2

# U10
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = +surf2 & -surf3

# U10
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = +surf3 & -surf4

# HEU-NatU
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf2 & +surf4 & +surf5 & -surf6

# Nat-U
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf4 & -surf5 & +surf6

# Nat-U
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf1 & +surf2 & +surf6 & -surf7

# D38
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = +surf1 & +surf2 & +surf4 & +surf5 & +surf6 & +surf7 & -surf8

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8])
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
source.space = openmc.stats.Point((0.0, 0.0, -9.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
