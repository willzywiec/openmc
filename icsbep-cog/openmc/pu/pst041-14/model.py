"""
PU-SOL-THERM-041-14: Experiment 311 with 33.74 gPu(3)/L at H/X=726; Hc=37.22
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 8.235300e-05)
mat1.add_nuclide("Pu240", 2.539250e-06)
mat1.add_nuclide("Pu241", 9.271850e-08)
mat1.add_element("N", 2.795100e-03)
mat1.add_nuclide("O16", 3.710200e-02)
mat1.add_nuclide("H1", 5.987830e-02)
mat1.add_element("Fe", 3.396710e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Water
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.672200e-02)
mat2.add_nuclide("O16", 3.336100e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

# Stainless steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.869400e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Mn", 8.659700e-04)
mat3.add_element("Si", 1.693900e-03)
mat3.add_element("P", 6.143900e-05)
mat3.add_element("S", 4.464000e-05)
mat3.add_element("C", 1.188300e-04)

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("O16", 1.126300e-05)
mat4.add_element("N", 4.198500e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, r=9.688)
surf2 = openmc.ZCylinder(surface_id=2, r=9.988)
surf3 = openmc.ZCylinder(surface_id=3, r=25.0)
surf4 = openmc.ZCylinder(surface_id=4, x0=0.0, y0=120.1, r=25.3)
surf5 = openmc.ZCylinder(surface_id=5, x0=-31.3, y0=120.1, r=56.6, boundary_type="vacuum")
surf6 = openmc.ZPlane(surface_id=6, z0=-25)
surf7 = openmc.ZPlane(surface_id=7, z0=37.22)
surf8 = openmc.ZPlane(surface_id=8, z0=118.3)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SST
cell1 = openmc.Cell(cell_id=1, fill=mat3)
cell1.region = +surf1 & -surf2 & +surf6 & -surf8

# SOLN
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf2 & -surf3 & +surf6 & -surf7

# AIR
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = +surf2 & -surf3 & +surf7 & -surf8

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf3 & -surf4 & -surf5 & +surf6 & -surf8

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = -surf4 & -surf5 & -surf6

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = -surf4 & -surf5 & +surf8

# WATER
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = +surf4 & -surf5 & -surf7

# AIR
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = +surf4 & -surf5 & +surf7

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
source.space = openmc.stats.Box((-18.5, -18.5, 18.36), (18.5, 18.5, 20.36))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
