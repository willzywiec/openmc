"""
PU-SOL-THERM-030-15: Exp. No. 500 with H/X=864 with AIR+CADMIUM in the central cavity
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 7.389800e-05)
mat1.add_nuclide("Pu240", 1.121000e-06)
mat1.add_nuclide("Pu241", 2.232700e-08)
mat1.add_nuclide("H1", 6.390800e-02)
mat1.add_nuclide("O16", 3.195400e-02)
mat1.add_nuclide("O16", 3.327000e-03)
mat1.add_element("N", 1.269600e-03)
mat1.add_element("Fe", 1.962500e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless steel
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.954600e-02)
mat2.add_element("Si", 1.693900e-03)
mat2.add_element("C", 1.188300e-04)
mat2.add_element("Cr", 1.646900e-02)
mat2.add_element("Mn", 8.659700e-04)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("P", 6.143900e-05)
mat2.add_element("S", 4.464000e-05)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.672200e-02)
mat3.add_nuclide("O16", 3.336100e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("O16", 1.126300e-05)
mat4.add_element("N", 4.198500e-05)

# Cadmium
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cd", 4.634030e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Hc
surf1 = openmc.ZPlane(surface_id=1, z0=38.09)
# Cavity, bottom
surf2 = openmc.ZPlane(surface_id=2, z0=-25.3)
# Inner tank, inner
surf3 = openmc.ZCylinder(surface_id=3, x0=1.2, y0=120.1, r=9.6875)
# Inner tank, outer
surf4 = openmc.ZCylinder(surface_id=4, x0=1.2, y0=120.1, r=9.9875)
# Outer tank, inner
surf5 = openmc.ZCylinder(surface_id=5, x0=1.2, y0=118.3, r=25.0)
# Outer tank, outer
surf6 = openmc.ZCylinder(surface_id=6, x0=0.0, y0=120.1, r=25.3)
# Water
surf7 = openmc.ZCylinder(surface_id=7, x0=-31.3, y0=120.1, r=56.6, boundary_type="vacuum")
# Cadmium
surf30 = openmc.ZCylinder(surface_id=30, r=9.6075)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Air
cell1 = openmc.Cell(cell_id=1, fill=mat4)
cell1.region = +surf2 & -surf3 & -surf30

# Cd
cell2 = openmc.Cell(cell_id=2, fill=mat5)
cell2.region = +surf2 & -surf3 & +surf30

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & +surf3 & -surf4

# Soln
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = -surf1 & +surf2 & +surf4 & -surf5

# Air
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf1 & +surf2 & +surf4 & -surf5

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf2 & +surf4 & +surf5 & -surf6

# SST
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = -surf2 & -surf6

# H2O
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = -surf1 & +surf6 & -surf7

# Air
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = +surf1 & +surf6 & -surf7

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9])
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
source.space = openmc.stats.Point((0.0, 0.0, 19.045))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
