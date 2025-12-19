"""
MIX-SOL-THERM-002-1: Experiment No. 058
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Experiment
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 6.552300e-02)
mat1.add_element("N", 4.799200e-04)
mat1.add_nuclide("O16", 3.410700e-02)
mat1.add_nuclide("Pu238", 8.415000e-09)
mat1.add_nuclide("Pu239", 2.726500e-05)
mat1.add_nuclide("Pu240", 2.477200e-06)
mat1.add_nuclide("Pu241", 1.380100e-07)
mat1.add_nuclide("Pu242", 2.748700e-08)
mat1.add_nuclide("U234", 2.843300e-09)
mat1.add_nuclide("U235", 1.998800e-07)
mat1.add_nuclide("U236", 6.765900e-09)
mat1.add_nuclide("U238", 2.774700e-05)
mat1.add_nuclide("Am241", 1.522500e-07)
mat1.add_nuclide("B10", 6.491400e-09)
mat1.add_element("Cd", 3.627700e-09)
mat1.add_element("Fe", 3.759800e-07)
mat1.add_element("Gd", 5.004500e-10)
mat1.add_nuclide("Li6", 2.319100e-10)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

# Water at 20.9 C
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.672400e-02)
mat3.add_nuclide("O16", 3.336200e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Fill pipe, inner
surf1 = openmc.ZCylinder(surface_id=1, r=2.625)
# Fill pipe, outer
surf2 = openmc.ZCylinder(surface_id=2, r=3.016)
# Tank, inner
surf3 = openmc.ZCylinder(surface_id=3, r=34.34)
# Tank, outer
surf4 = openmc.ZCylinder(surface_id=4, r=34.419)
# BCD and entire problem
surf5 = openmc.model.RectangularParallelepiped(-49.38, 49.38, -50.655, 50.655, -16.953000000000003, 107.553, boundary_type="vacuum")
# Water reflector height
surf6 = openmc.ZPlane(surface_id=6, z0=106.283)
# Solution critical height
surf7 = openmc.ZPlane(surface_id=7, z0=76.800)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(z0=0.0)
surf3_zmax = openmc.ZPlane(z0=106.6)
surf4_zmin = openmc.ZPlane(z0=-0.953)
surf4_zmax = openmc.ZPlane(z0=107.553)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf3 & +surf3_zmin & -surf3_zmax) & -surf7

# SS3O4L
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# SS304L
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf1 & -surf2 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf2 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & -surf6

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
source.space = openmc.stats.Point((0.0, 0.0, 38.4))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
