"""
LST010-2: Polyethylene (P60) reflected 60-cm-diameter cylindrical tank with 10% enriched uranyl nitrate solution @ H/X=945 (Run 85)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution: Run 85
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.991800e-07)
mat1.add_nuclide("U235", 6.194500e-05)
mat1.add_nuclide("U236", 6.186800e-08)
mat1.add_nuclide("U238", 5.517500e-04)
mat1.add_nuclide("H1", 5.852600e-02)
mat1.add_element("N", 2.487100e-03)
mat1.add_nuclide("O16", 3.732300e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless Steel [1] Core Tank
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

# Stainless Steel [2] Reflector Upper Plate
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 1.988000e-04)
mat3.add_element("Si", 9.181900e-04)
mat3.add_element("Mn", 1.051800e-03)
mat3.add_element("P", 4.008700e-05)
mat3.add_element("S", 5.956400e-06)
mat3.add_element("Ni", 6.769900e-03)
mat3.add_element("Cr", 1.671600e-02)
mat3.add_element("Fe", 6.126900e-02)

# Stainless Steel [3] Reflector Lower Support
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 1.590400e-04)
mat4.add_element("Si", 9.351900e-04)
mat4.add_element("Mn", 1.121300e-03)
mat4.add_element("P", 4.471200e-05)
mat4.add_element("S", 2.978200e-06)
mat4.add_element("Ni", 6.851200e-03)
mat4.add_element("Cr", 1.689000e-02)
mat4.add_element("Fe", 6.095100e-02)

# Aluminum Alloy
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 5.952300e-02)
mat5.add_element("Si", 5.767900e-05)
mat5.add_element("Ti", 6.766700e-06)
mat5.add_element("Mn", 2.948700e-06)
mat5.add_element("Fe", 1.711400e-04)
mat5.add_element("Cu", 3.568900e-05)

# Polyethylene (P60)
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 8.105100e-02)
mat6.add_element("C", 4.066500e-02)
mat6.add_s_alpha_beta("c_H_in_CH2")

# Air
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("N", 3.901600e-05)
mat7.add_nuclide("O16", 1.040900e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Solution
surf1 = openmc.ZCylinder(surface_id=1, r=29.5)
# 60-cm diam. tank
surf2 = openmc.ZCylinder(surface_id=2, r=29.8)
# Hc
surf3 = openmc.ZPlane(surface_id=3, z0=77.81)
# Steel support/inner
surf11 = openmc.ZCylinder(surface_id=11, r=31.7)
# Steel support/outer
surf12 = openmc.ZCylinder(surface_id=12, r=68.5)
# =A
surf13 = openmc.ZCylinder(surface_id=13, r=32.04)
# =B
surf14 = openmc.ZCylinder(surface_id=14, r=32.35)
# =C
surf15 = openmc.ZCylinder(surface_id=15, r=38.46)
# =D
surf16 = openmc.ZCylinder(surface_id=16, r=39.26)
surf17 = openmc.ZPlane(surface_id=17, z0=-1.5)
surf18 = openmc.ZPlane(surface_id=18, z0=0.0)
surf19 = openmc.ZPlane(surface_id=19, z0=142.0)
surf20 = openmc.ZPlane(surface_id=20, z0=142.6)
# BCD
surf21 = openmc.ZCylinder(surface_id=21, r=68.5, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1021, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1022, z0=149.86)
surf2_zmin = openmc.ZPlane(surface_id=1023, z0=-2.02)
surf2_zmax = openmc.ZPlane(surface_id=1024, z0=152.8)
surf12_zmin = openmc.ZPlane(surface_id=1025, z0=-4.0)
surf12_zmax = openmc.ZPlane(surface_id=1026, z0=-1.5)
surf21_zmin = openmc.ZPlane(surface_id=1027, z0=-4.0, boundary_type="vacuum")
surf21_zmax = openmc.ZPlane(surface_id=1028, z0=152.8, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf3

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = +surf11 & (-surf12 & +surf12_zmin & -surf12_zmax)

# Alum
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = (+surf12 | -surf12_zmin | +surf12_zmax) & +surf13 & -surf16 & +surf17 & -surf18

# Alum
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf13 & -surf14 & +surf18 & -surf19

# CH2
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf14 & -surf15 & +surf18 & -surf19

# Alum
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = +surf15 & -surf16 & +surf18 & -surf19

# SST
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf13 & -surf16 & +surf19 & -surf20

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
source.space = openmc.stats.Point((0.0, 0.0, 38.905))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
