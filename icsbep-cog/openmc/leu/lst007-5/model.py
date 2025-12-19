"""
LST007-5: Unreflected 60-cm-diameter cylindrical tank with 10% enriched uranyl nitrate solution @ H/X=942 (Run 49)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution: Run 49
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.979500e-07)
mat1.add_nuclide("U235", 6.179200e-05)
mat1.add_nuclide("U236", 6.171500e-08)
mat1.add_nuclide("U238", 5.503900e-04)
mat1.add_nuclide("H1", 5.822300e-02)
mat1.add_element("N", 2.592500e-03)
mat1.add_nuclide("O16", 3.743100e-02)
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

# Air
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("N", 3.901600e-05)
mat3.add_nuclide("O16", 1.040900e-05)

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, r=29.5)
surf2 = openmc.ZCylinder(surface_id=2, r=29.8, boundary_type="vacuum")
# Hc
surf3 = openmc.ZPlane(surface_id=3, z0=112.27)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1003, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1004, z0=150.0)
surf2_zmin = openmc.ZPlane(surface_id=1005, z0=-2.0, boundary_type="vacuum")
surf2_zmax = openmc.ZPlane(surface_id=1006, z0=152.5, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf3

# Air
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & +surf3

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3])
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
source.space = openmc.stats.Point((0.0, 0.0, 56.135))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
