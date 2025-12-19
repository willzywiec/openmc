"""
PMF042-5S: Pu hemisphere reflected by 1.333 cm steel and infinite oil; simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu, oil,
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 4.262200e-06)
mat1.add_nuclide("Pu239", 3.971800e-02)
mat1.add_nuclide("Pu240", 2.493700e-03)
mat1.add_nuclide("Pu241", 2.062400e-04)
mat1.add_nuclide("Pu242", 8.383200e-06)
mat1.add_nuclide("H1", 5.434900e-03)
mat1.add_nuclide("Li6", 1.989100e-06)
mat1.add_nuclide("Li7", 2.103300e-05)
mat1.add_element("C", 2.802000e-03)
mat1.add_element("N", 1.455900e-06)
mat1.add_nuclide("O16", 2.862400e-04)
mat1.add_element("Si", 2.470900e-04)
mat1.add_element("Ar", 8.707600e-09)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Steel, oil,
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 1.079500e-03)
mat2.add_element("C", 1.265400e-03)
mat2.add_element("N", 5.091000e-07)
mat2.add_nuclide("O16", 1.398300e-07)
mat2.add_element("P", 3.019200e-05)
mat2.add_element("S", 3.577200e-05)
mat2.add_element("Ar", 3.044800e-08)
mat2.add_element("Mn", 6.264600e-04)
mat2.add_element("Fe", 8.137500e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

# Oil
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.796200e-02)
mat3.add_element("C", 3.878100e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 4.104900e-07)
mat4.add_element("N", 3.205300e-05)
mat4.add_nuclide("O16", 8.803400e-06)
mat4.add_element("Ar", 1.917000e-07)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Hemi
surf1 = openmc.XPlane(surface_id=1, x0=-2.37375)
# Pu
# surf2: Unsupported surface type "s" with params ['6.333', 'tr', '-2.37375', '0', '-6.333']
# Steel
# surf3: Unsupported surface type "s" with params ['7.666', 'tr', '-2.37375', '0', '-6.333']
# Hc
surf4 = openmc.ZPlane(surface_id=4, z0=0.09)
# BCD
surf5 = openmc.ZCylinder(surface_id=5, r=25.0)

# Z-plane surfaces for bounded cylinders
surf5_zmin = openmc.ZPlane(z0=-31.333, boundary_type="vacuum")
surf5_zmax = openmc.ZPlane(z0=18.667, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Pu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# Steel
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & +surf2 & -surf3

# Oil
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf1 & +surf3 & -surf4 & (-surf5 & +surf5_zmin & -surf5_zmax)

# Oil
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = -surf1 & -surf4 & (-surf5 & +surf5_zmin & -surf5_zmax)

# Air
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = -surf1 & +surf4 & (-surf5 & +surf5_zmin & -surf5_zmax)

# Air
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf1 & +surf3 & +surf4 & (-surf5 & +surf5_zmin & -surf5_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, -6.333))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
