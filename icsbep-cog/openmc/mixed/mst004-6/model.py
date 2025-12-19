"""
MIX-SOL-THERM-004-6: Exp. No. 078 with 172.82 gPu/l and 262.55 gU/l with 1.23M
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.267900e-07)
mat1.add_nuclide("Pu239", 3.966900e-04)
mat1.add_nuclide("Pu240", 3.602800e-05)
mat1.add_nuclide("Pu241", 1.942800e-06)
mat1.add_nuclide("Pu242", 3.998600e-07)
mat1.add_nuclide("U234", 4.729000e-08)
mat1.add_nuclide("U235", 3.793900e-06)
mat1.add_nuclide("U236", 1.540600e-07)
mat1.add_nuclide("U238", 6.602400e-04)
mat1.add_nuclide("Am241", 2.260800e-06)
mat1.add_nuclide("H1", 5.412100e-02)
mat1.add_element("N", 3.862900e-03)
mat1.add_nuclide("O16", 3.961200e-02)
mat1.add_nuclide("B10", 9.386500e-08)
mat1.add_element("Cd", 5.277200e-08)
mat1.add_element("Fe", 5.469500e-06)
mat1.add_element("Gd", 7.280100e-09)
mat1.add_nuclide("Li6", 3.373600e-09)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.137600e-02)
mat2.add_element("Cr", 1.764800e-02)
mat2.add_element("Ni", 8.229200e-03)
mat2.add_element("C", 1.206300e-04)

# Water (078)
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.674300e-02)
mat3.add_nuclide("O16", 3.337200e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Dump line, inner
surf1 = openmc.ZCylinder(surface_id=1, r=2.625)
# Dump line, outer
surf2 = openmc.ZCylinder(surface_id=2, r=3.016)
# Solution tank, inner
surf3 = openmc.ZCylinder(surface_id=3, r=17.695)
# Solution tank, outer
surf4 = openmc.ZCylinder(surface_id=4, r=17.774)
# Boundary
surf5 = openmc.model.RectangularParallelepiped(-49.38, 49.38, -46.75, 46.75, -16.953, 91.553, boundary_type="vacuum")
# Sol'n height
surf6 = openmc.ZPlane(surface_id=6, z0=28.93)
# Water height
surf7 = openmc.ZPlane(surface_id=7, z0=89.013)

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(surface_id=1007, z0=-16.953)
surf2_zmax = openmc.ZPlane(surface_id=1008, z0=-0.953)
surf3_zmin = openmc.ZPlane(surface_id=1009, z0=0.0)
surf3_zmax = openmc.ZPlane(surface_id=1010, z0=90.6)
surf4_zmin = openmc.ZPlane(surface_id=1011, z0=-0.953)
surf4_zmax = openmc.ZPlane(surface_id=1012, z0=91.553)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf1 & (-surf2 & +surf2_zmin & -surf2_zmax) & -surf5

# SS304L
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & (-surf2 & +surf2_zmin & -surf2_zmax) & -surf5

# Soln
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = (-surf3 & +surf3_zmin & -surf3_zmax) & -surf6

# Void
cell4 = openmc.Cell(cell_id=4)
cell4.region = (-surf3 & +surf3_zmin & -surf3_zmax) & +surf6

# SS304L
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf5

# Water
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & -surf7

# Void
cell7 = openmc.Cell(cell_id=7)
cell7.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & +surf7

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
source.space = openmc.stats.Point((0.0, 0.0, 14.465))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
