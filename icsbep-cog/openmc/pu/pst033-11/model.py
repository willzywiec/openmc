"""
PU-SOL-THERM-033-11: 99.05 gPu(3.13)/L at H/X=250.4 with no poisons
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 7.283400e-11)
mat1.add_nuclide("U238", 1.020100e-08)
mat1.add_nuclide("Pu239", 2.413700e-04)
mat1.add_nuclide("Pu240", 7.788900e-06)
mat1.add_nuclide("Pu241", 2.969400e-07)
mat1.add_nuclide("Pu242", 2.957100e-08)
mat1.add_nuclide("Am241", 3.464300e-08)
mat1.add_nuclide("H1", 6.052100e-02)
mat1.add_nuclide("O16", 3.706200e-02)
mat1.add_element("N", 2.519100e-03)
mat1.add_element("Fe", 1.466500e-06)
mat1.add_element("Cr", 1.720800e-07)
mat1.add_element("Ni", 2.032700e-07)
mat1.add_element("Mn", 6.514500e-08)
mat1.add_element("Ca", 8.929900e-07)
mat1.add_element("Cu", 1.220300e-07)
mat1.add_element("Mg", 4.908400e-07)
mat1.add_element("Zn", 1.368300e-07)
mat1.add_element("Na", 6.486300e-07)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.954600e-02)
mat2.add_element("Si", 1.646900e-03)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Mn", 8.659700e-04)
mat2.add_element("Si", 1.693900e-03)
mat2.add_element("S", 4.450400e-05)
mat2.add_element("P", 6.143900e-05)
mat2.add_element("C", 1.188300e-04)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.670600e-02)
mat3.add_nuclide("O16", 3.335300e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("N", 4.198500e-05)
mat4.add_nuclide("O16", 1.126300e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical solution height, Hc
surf1 = openmc.ZPlane(surface_id=1, z0=18.93)
# SST solution tank, inner
# surf2: Unsupported surface type "rev" with params ['3', '0.0', '0.0', '0.6', '17.98', '80.7', '17.98']
# SST solution  tank, outer
surf3 = openmc.ZCylinder(surface_id=3, x0=-0.3, y0=80.7, r=18.28)
# SST reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, x0=-25.9, y0=62.8, r=54.6)
# SST refelctor tank, top
surf5 = openmc.ZPlane(surface_id=5, z0=63.2)
# SST reflector tank, outer, and BCD
surf6 = openmc.ZCylinder(surface_id=6, x0=-26.3, y0=85.7, r=55.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf3

# Air
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = +surf1 & -surf3

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = -surf3

# H2O
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = -surf1 & +surf3 & -surf4

# Air
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf1 & +surf3 & -surf4

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf3 & +surf4 & -surf5 & -surf6

# Air
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf3 & +surf4 & +surf5 & -surf6

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
source.space = openmc.stats.Point((0.0, 0.0, 9.465))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
