"""
PU-SOL-THERM-033-12: 140.8 gPu(4.23)/L at H/X=176.9 with no poisons
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.338700e-10)
mat1.add_nuclide("U238", 1.875000e-08)
mat1.add_nuclide("Pu238", 2.600200e-08)
mat1.add_nuclide("Pu239", 3.385800e-04)
mat1.add_nuclide("Pu240", 1.493900e-05)
mat1.add_nuclide("Pu241", 1.019900e-06)
mat1.add_nuclide("Pu242", 5.604700e-08)
mat1.add_nuclide("Am241", 1.224100e-07)
mat1.add_nuclide("H1", 6.006800e-02)
mat1.add_nuclide("O16", 3.757300e-02)
mat1.add_element("N", 2.728700e-03)
mat1.add_element("Fe", 2.857500e-06)
mat1.add_element("Cr", 1.141500e-07)
mat1.add_element("Ni", 3.005000e-07)
mat1.add_element("Mn", 1.234700e-07)
mat1.add_element("Ca", 1.692500e-06)
mat1.add_element("Cu", 1.067500e-07)
mat1.add_element("Mg", 2.093200e-07)
mat1.add_element("Zn", 3.890100e-07)
mat1.add_element("Na", 3.688200e-07)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SST
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
surf1 = openmc.ZPlane(surface_id=1, z0=19.14)
# SST solution tank, inner
# surf2: Unsupported surface type "rev" with params ['3', '0.0', '0.0', '0.6', '17.98', '80.7', '17.98']
# SST solution  tank, outer
surf3 = openmc.ZCylinder(surface_id=3, r=18.28)
# SST reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, r=54.6)
# SST refelctor tank, top
surf5 = openmc.ZPlane(surface_id=5, z0=63.2)
# SST reflector tank, outer, and BCD
surf6 = openmc.ZCylinder(surface_id=6, r=55.0, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1006, z0=-0.3)
surf3_zmax = openmc.ZPlane(surface_id=1007, z0=80.7)
surf4_zmin = openmc.ZPlane(surface_id=1008, z0=-25.9)
surf4_zmax = openmc.ZPlane(surface_id=1009, z0=62.8)
surf6_zmin = openmc.ZPlane(surface_id=1010, z0=-26.3, boundary_type="vacuum")
surf6_zmax = openmc.ZPlane(surface_id=1011, z0=85.7, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

# Air
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

# H2O
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = -surf1 & +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# Air
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf1 & +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)

# Air
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 9.57))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
