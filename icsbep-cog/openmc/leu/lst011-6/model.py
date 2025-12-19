"""
LST011-6: Water reflected 80-cm-diameter cylindrical tank with 6% enriched uranyl nitrate solution @ H/X=1,037 (Run 485)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution: Run 485
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.647000e-07)
mat1.add_nuclide("U235", 5.561900e-05)
mat1.add_nuclide("U236", 9.215100e-08)
mat1.add_nuclide("U238", 8.582800e-04)
mat1.add_nuclide("H1", 5.768100e-02)
mat1.add_element("N", 2.449200e-03)
mat1.add_nuclide("O16", 3.770700e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless Steel
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 4.373600e-05)
mat2.add_element("Si", 1.062700e-03)
mat2.add_element("Mn", 1.156100e-03)
mat2.add_element("P", 4.317000e-05)
mat2.add_element("S", 2.978200e-06)
mat2.add_element("Ni", 8.340300e-03)
mat2.add_element("Cr", 1.677500e-02)
mat2.add_element("Fe", 5.942100e-02)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.665800e-02)
mat3.add_nuclide("O16", 3.332900e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("N", 3.901600e-05)
mat4.add_nuclide("O16", 1.041000e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# 60-cm diam. tank/inner
surf1 = openmc.ZCylinder(surface_id=1, r=39.505)
# 60-cm diam. tank/outer
surf2 = openmc.ZCylinder(surface_id=2, r=39.815)
# Water reflector /outer
surf3 = openmc.ZCylinder(surface_id=3, r=69.815, boundary_type="vacuum")
# Hc
surf4 = openmc.ZPlane(surface_id=4, z0=92.23)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1004, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1005, z0=149.71)
surf2_zmin = openmc.ZPlane(surface_id=1006, z0=-2.06)
surf2_zmax = openmc.ZPlane(surface_id=1007, z0=152.64)
surf3_zmin = openmc.ZPlane(surface_id=1008, z0=-32.06, boundary_type="vacuum")
surf3_zmax = openmc.ZPlane(surface_id=1009, z0=172.64, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf4

# Air
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & +surf4

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 46.115))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
