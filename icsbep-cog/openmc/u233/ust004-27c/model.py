"""
U233-SOL-THERM-004 (Exp't 27 in 7.5"-Diam. Vessel) 1780 g U-233 @ H/X = 57
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# H/U-233 = 57.144
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 9.836100e-04)
mat1.add_nuclide("U234", 4.566400e-06)
mat1.add_nuclide("U238", 8.588600e-06)
mat1.add_nuclide("H1", 5.620700e-02)
mat1.add_nuclide("O16", 3.770700e-02)
mat1.add_element("N", 2.645400e-03)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Al-2S
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 5.810800e-04)

# Paraffin
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 7.991100e-02)
mat3.add_element("C", 3.841900e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Al-2S/Inner
surf1 = openmc.ZCylinder(surface_id=1, r=9.5246)
# Al-2S/Outer
surf2 = openmc.ZCylinder(surface_id=2, r=9.6537)
# Paraffin/Outer
surf3 = openmc.ZCylinder(surface_id=3, r=24.8937, boundary_type="vacuum")
# Hc
# surf4: Unsupported surface type "analytic" with params ['1.', 'z', '-16.4109', 'constant']

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1004, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1005, z0=19.1609)
surf2_zmin = openmc.ZPlane(surface_id=1006, z0=-0.1291)
surf2_zmax = openmc.ZPlane(surface_id=1007, z0=19.29)
surf3_zmin = openmc.ZPlane(surface_id=1008, z0=-15.3691, boundary_type="vacuum")
surf3_zmax = openmc.ZPlane(surface_id=1009, z0=34.53, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & +surf4

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf4

# Al2S
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# Prffn
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
source.space = openmc.stats.Point((0.0, 0.0, 8.2))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
