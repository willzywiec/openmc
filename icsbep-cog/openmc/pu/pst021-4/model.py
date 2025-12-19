"""
PU-SOL-THERM-021 (Case 4) 0.760 kg Pu(95.4) @ H/X = 1082 in a water reflected 15.2" SS304L sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 3.825000e-09)
mat1.add_nuclide("Pu239", 6.032900e-05)
mat1.add_nuclide("Pu240", 2.951600e-06)
mat1.add_nuclide("Pu241", 1.781600e-07)
mat1.add_nuclide("Pu242", 5.642500e-09)
mat1.add_element("N", 5.790500e-04)
mat1.add_nuclide("H1", 6.548600e-02)
mat1.add_nuclide("O16", 3.431700e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.665500e-02)
mat3.add_nuclide("O16", 3.332700e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# = Hc per Table 5a
surf1 = openmc.ZPlane(surface_id=1, z0=18.7540)
# SST/Inner
surf2 = openmc.Sphere(surface_id=2, r=19.3163)
# SST/Outer
surf3 = openmc.Sphere(surface_id=3, r=19.6414)
# H2O/Outer
surf4 = openmc.Sphere(surface_id=4, r=49.6414)
# Support Tube/Inner
surf5 = openmc.ZCylinder(surface_id=5, x0=-3.811, y0=0.0, r=2.695)
# Support Tube/Outer
surf6 = openmc.ZCylinder(surface_id=6, x0=-3.811, y0=0.0, r=2.86)
# Inlet Tube/Inner
surf7 = openmc.ZCylinder(surface_id=7, r=2.555)
# Inlet Tube/Outer
surf8 = openmc.ZCylinder(surface_id=8, r=2.86)

# Z-plane surfaces for bounded cylinders
surf7_zmin = openmc.ZPlane(z0=-99.0)
surf7_zmax = openmc.ZPlane(z0=0.0)
surf8_zmin = openmc.ZPlane(z0=-99.0)
surf8_zmax = openmc.ZPlane(z0=0.0)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# SOLN
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = -surf1 & +surf2 & -surf3 & -surf5

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & -surf3 & -surf4 & +surf5

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf3 & -surf4 & +surf5 & -surf6

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf3 & -surf4 & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf3 & -surf4 & +surf6 & (+surf8 | -surf8_zmin | +surf8_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
