"""
LST007-1: Unreflected 60-cm-diameter cylindrical tank with 10% enriched uranyl nitrate solution @ H/X=709 (Run 14)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution: Run 14
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 6.443000e-07)
mat1.add_nuclide("U235", 7.999540e-05)
mat1.add_nuclide("U236", 7.985400e-08)
mat1.add_nuclide("U238", 7.121600e-04)
mat1.add_nuclide("H1", 5.670700e-02)
mat1.add_element("N", 2.940600e-03)
mat1.add_nuclide("O16", 3.808400e-02)
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
surf2 = openmc.ZCylinder(surface_id=2, r=29.8)
# Hc
surf3 = openmc.ZPlane(surface_id=3, z0=46.83)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=0.0)
surf1_zmax = openmc.ZPlane(z0=150.0)
surf2_zmin = openmc.ZPlane(z0=-2.0, boundary_type="vacuum")
surf2_zmax = openmc.ZPlane(z0=152.5, boundary_type="vacuum")

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
source.space = openmc.stats.Point((0.0, 0.0, 23.415))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
