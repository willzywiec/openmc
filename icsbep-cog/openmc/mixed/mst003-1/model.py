"""
MIX-SOL-THERM-003-1: AWRE SCAMP
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution A
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 2.396000e-04)
mat1.add_nuclide("Pu240", 1.440000e-05)
mat1.add_nuclide("Pu241", 1.100000e-06)
mat1.add_nuclide("U235", 4.200000e-06)
mat1.add_nuclide("U238", 5.739000e-04)
mat1.add_nuclide("H1", 5.730000e-02)
mat1.add_element("N", 3.100000e-03)
mat1.add_nuclide("O16", 3.860000e-02)
mat1.add_element("Fe", 2.000000e-08)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.328700e-02)
mat2.add_element("Cr", 1.653400e-02)
mat2.add_element("Ni", 6.509300e-03)

# Polyethylene
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 7.986700e-02)
mat3.add_element("C", 3.993300e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.672900e-02)
mat4.add_nuclide("O16", 3.336600e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Hc
surf1 = openmc.ZPlane(surface_id=1, z0=56.31)
# Steel plate
surf2 = openmc.ZCylinder(surface_id=2, r=12.5125)
# Polyethylene
surf3 = openmc.ZCylinder(surface_id=3, r=12.5125)
# Vessel, inner
surf4 = openmc.ZCylinder(surface_id=4, r=12.7125)
# Vessel, outer
surf5 = openmc.ZCylinder(surface_id=5, r=12.9125)
# Vessel, flange
surf6 = openmc.ZCylinder(surface_id=6, r=17.9125)
# Water reflector
surf7 = openmc.ZCylinder(surface_id=7, r=42.0)

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(z0=56.31)
surf2_zmax = openmc.ZPlane(z0=56.627)
surf3_zmin = openmc.ZPlane(z0=56.627)
surf3_zmax = openmc.ZPlane(z0=71.627)
surf4_zmin = openmc.ZPlane(z0=0.0)
surf4_zmax = openmc.ZPlane(z0=107.0)
surf5_zmin = openmc.ZPlane(z0=-1.0)
surf5_zmax = openmc.ZPlane(z0=107.0)
surf6_zmin = openmc.ZPlane(z0=-1.0)
surf6_zmax = openmc.ZPlane(z0=0.0)
surf7_zmin = openmc.ZPlane(z0=-16.0, boundary_type="vacuum")
surf7_zmax = openmc.ZPlane(z0=107.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax)

# SS304L
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & (-surf2 & +surf2_zmin & -surf2_zmax)

# Poly
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# SS304L
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)

# SS304L
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)

# Water
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 28.155))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
