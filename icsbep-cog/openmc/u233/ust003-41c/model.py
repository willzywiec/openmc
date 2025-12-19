"""
U233-SOL-THERM-003 (Exp't 41 in 5.5"-Diam. Vessel) 2359 g U-233 @ H/X = 74
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 233U(98.7)O2F2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 8.579700e-04)
mat1.add_nuclide("U234", 4.000200e-06)
mat1.add_nuclide("U238", 7.652600e-06)
mat1.add_nuclide("H1", 6.328000e-02)
mat1.add_nuclide("O16", 3.337900e-02)
mat1.add_element("F", 1.808200e-03)
mat1.add_element("Al", 1.433800e-05)
mat1.add_element("Cr", 1.607600e-07)
mat1.add_element("Fe", 9.030100e-07)
mat1.add_element("Mg", 1.563200e-08)
mat1.add_element("Mo", 1.440100e-08)
mat1.add_element("Na", 2.346700e-05)
mat1.add_element("Ni", 2.942400e-08)
mat1.add_element("Sn", 1.309300e-08)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Unichrome
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 5.284300e-02)
mat2.add_element("C", 3.319500e-02)
mat2.add_nuclide("O16", 3.952100e-03)
mat2.add_element("Cl", 5.507900e-03)
mat2.add_s_alpha_beta("c_H_in_CH2")

# Al-2S
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.988100e-02)
mat3.add_element("Si", 5.810800e-04)

# Paraffin
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 7.991100e-02)
mat4.add_nuclide("O16", 3.841900e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Unichrome/Inner
surf1 = openmc.ZCylinder(surface_id=1, r=6.8265)
# Unichrome/Outer=Vessel/Inner
surf2 = openmc.ZCylinder(surface_id=2, r=7.0045)
# Vessel/Outer
surf3 = openmc.ZCylinder(surface_id=3, r=7.1336)
# Paraffin/Outer
surf4 = openmc.ZCylinder(surface_id=4, r=22.3736)
# Hc
# surf5: Unsupported surface type "analytic" with params ['1.', 'z', '-48.5411', 'constant']

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=0.0)
surf1_zmax = openmc.ZPlane(z0=91.2811)
surf2_zmin = openmc.ZPlane(z0=-0.178)
surf2_zmax = openmc.ZPlane(z0=91.4591)
surf3_zmin = openmc.ZPlane(z0=-0.3071)
surf3_zmax = openmc.ZPlane(z0=91.5882)
surf4_zmin = openmc.ZPlane(z0=-15.5471, boundary_type="vacuum")
surf4_zmax = openmc.ZPlane(z0=91.5882, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & +surf5

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf5

# UNCHRM
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# Al2S
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# Prffn
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5])
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
source.space = openmc.stats.Point((0.0, 0.0, 24.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
