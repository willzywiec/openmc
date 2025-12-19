"""
PU-MET-FAST-045: LAMPRE Assembly I (Simplified Model)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 2.760000e-02)
mat1.add_element("Ni", 6.530000e-03)
mat1.add_element("Ta", 3.850000e-03)
mat1.add_element("Al", 4.400000e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Ni", 8.885900e-02)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Ta", 4.869000e-02)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 2.008700e-02)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 8.464800e-02)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.676600e-02)
mat6.add_nuclide("O16", 3.338300e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("H1", 7.899600e-02)
mat7.add_element("C", 3.949800e-02)
mat7.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

surf3 = openmc.ZCylinder(surface_id=3, r=5.7404)
surf4 = openmc.ZCylinder(surface_id=4, r=5.8674)
surf5 = openmc.ZCylinder(surface_id=5, r=6.0706)
surf6 = openmc.ZCylinder(surface_id=6, r=6.1976)
surf7 = openmc.ZCylinder(surface_id=7, r=10.0076)
surf8 = openmc.ZCylinder(surface_id=8, r=10.0584)
surf9 = openmc.ZCylinder(surface_id=9, r=10.3632)
surf10 = openmc.ZCylinder(surface_id=10, r=48.26, boundary_type="vacuum")
# surf11: Unsupported surface type "analytic" with params ['1.', 'z', '42.0370']
# surf12: Unsupported surface type "analytic" with params ['1.', 'z', '11.5570']
# surf13: Unsupported surface type "analytic" with params ['1.', 'z', '9.5758']
# surf14: Unsupported surface type "analytic" with params ['1.', 'z', '-35.6201']

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1014, z0=0.0)
surf3_zmax = openmc.ZPlane(surface_id=1015, z0=13.3443)
surf4_zmin = openmc.ZPlane(surface_id=1016, z0=-0.2032)
surf4_zmax = openmc.ZPlane(surface_id=1017, z0=13.5475)
surf5_zmin = openmc.ZPlane(surface_id=1018, z0=-1.9558)
surf5_zmax = openmc.ZPlane(surface_id=1019, z0=15.3001)
surf6_zmin = openmc.ZPlane(surface_id=1020, z0=-1.9558)
surf6_zmax = openmc.ZPlane(surface_id=1021, z0=15.3001)
surf10_zmin = openmc.ZPlane(surface_id=1022, z0=-42.037, boundary_type="vacuum")
surf10_zmax = openmc.ZPlane(surface_id=1023, z0=43.7478, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf3 & +surf3_zmin & -surf3_zmax)

# Ta
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# Al
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# Gap
cell4 = openmc.Cell(cell_id=4)
cell4.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)

# Ni
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & -surf7 & +surf13 & -surf14

# Al
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & -surf7 & +surf12 & -surf13

# CH2
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & -surf7 & +surf11 & -surf12

# Gap
cell8 = openmc.Cell(cell_id=8)
cell8.region = +surf7 & -surf8 & +surf11 & -surf14

# Gap
cell9 = openmc.Cell(cell_id=9)
cell9.region = -surf8 & (-surf10 & +surf10_zmin & -surf10_zmax) & +surf14

# Fe
cell10 = openmc.Cell(cell_id=10, fill=mat5)
cell10.region = +surf8 & -surf9 & (-surf10 & +surf10_zmin & -surf10_zmax)

# H2O
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = +surf9 & (-surf10 & +surf10_zmin & -surf10_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11])
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
source.space = openmc.stats.Point((0.0, 0.0, 6.73))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
