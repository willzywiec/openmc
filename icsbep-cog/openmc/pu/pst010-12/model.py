"""
PU-SOL-THERM-010 (Case 12-2) 0.779 kg Pu(97.15) @ H/X = 618 in a water reflected 12" diameter SS-347 cylinder
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 1.034500e-04)
mat1.add_nuclide("Pu240", 3.076600e-06)
mat1.add_element("N", 1.229600e-03)
mat1.add_nuclide("H1", 6.396800e-02)
mat1.add_nuclide("O16", 3.527100e-02)
mat1.add_element("Fe", 1.876300e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.038600e-02)
mat2.add_element("Cr", 1.667800e-02)
mat2.add_element("Ni", 9.850400e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.658700e-02)
mat3.add_nuclide("O16", 3.329300e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Pipe/Inner
surf1 = openmc.ZCylinder(surface_id=1, r=1.0465)
# Pipe/Outer
surf2 = openmc.ZCylinder(surface_id=2, r=1.3335)
# Piston/Inner; Z1 = Hc + 0.1575; Z2 = Z1 + 30.48
surf3 = openmc.ZCylinder(surface_id=3, r=14.9545)
# Piston/Outer; Z1 = Hc; Z2 = Z1 + 30.7950
surf4 = openmc.ZCylinder(surface_id=4, r=15.112)
# = Hc
surf5 = openmc.ZPlane(surface_id=5, z0=25.2476)
# Cylinder/Inner
surf6 = openmc.ZCylinder(surface_id=6, r=15.239)
# Cylinder/Outer
surf7 = openmc.ZCylinder(surface_id=7, r=15.3965)
# Reflector/Inner
surf8 = openmc.ZCylinder(surface_id=8, r=45.72, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1008, z0=25.4051)
surf3_zmax = openmc.ZPlane(surface_id=1009, z0=55.8851)
surf4_zmin = openmc.ZPlane(surface_id=1010, z0=25.2476)
surf4_zmax = openmc.ZPlane(surface_id=1011, z0=56.0426)
surf6_zmin = openmc.ZPlane(surface_id=1012, z0=0.0)
surf6_zmax = openmc.ZPlane(surface_id=1013, z0=97.9488)
surf7_zmin = openmc.ZPlane(surface_id=1014, z0=-0.1575)
surf7_zmax = openmc.ZPlane(surface_id=1015, z0=97.9488)
surf8_zmin = openmc.ZPlane(surface_id=1016, z0=-30.1575, boundary_type="vacuum")
surf8_zmax = openmc.ZPlane(surface_id=1017, z0=97.9488, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# VOID
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax)

# SS347
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2 & (-surf4 & +surf4_zmin & -surf4_zmax)

# WATER
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# SS347
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# VOID
cell5 = openmc.Cell(cell_id=5)
cell5.region = (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)

# SOLN
cell6 = openmc.Cell(cell_id=6, fill=mat1)
cell6.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)

# SS347
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)

# WATER
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 12.6))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
