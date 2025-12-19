"""
PU-SOL-THERM-008 (Case 24) 0.845 kg Pu(95.43) @ H/X = 671 in 14" SS304L sphere with l0" concrete
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 5.585700e-09)
mat1.add_nuclide("Pu239", 8.807900e-05)
mat1.add_nuclide("Pu240", 4.309400e-06)
mat1.add_nuclide("Pu241", 2.822400e-07)
mat1.add_nuclide("Pu242", 8.239800e-09)
mat1.add_element("N", 3.032500e-03)
mat1.add_nuclide("H1", 5.925700e-02)
mat1.add_nuclide("O16", 3.739500e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 1.737600e-02)
mat3.add_nuclide("O16", 4.529400e-02)
mat3.add_element("Mg", 7.619500e-04)
mat3.add_element("Al", 3.353300e-03)
mat3.add_element("Ca", 2.609500e-03)
mat3.add_element("Fe", 1.341700e-03)
mat3.add_element("Na", 1.141600e-04)
mat3.add_element("K", 4.356900e-04)
mat3.add_element("Mn", 2.767300e-05)
mat3.add_element("Si", 1.293100e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# = Hc ------------ Table 5b
surf1 = openmc.ZPlane(surface_id=1, z0=15.5303)
# Sphere/Inner ---- Table 6b
surf2 = openmc.Sphere(surface_id=2, r=17.6955)
# Sphere/Outer ---- Table 6b
surf3 = openmc.Sphere(surface_id=3, r=17.8073)
# Concrete/Outer -- Table 6b
surf4 = openmc.Sphere(surface_id=4, r=43.2073)
# Support Tube/Inner -- Figure 7
surf5 = openmc.ZCylinder(surface_id=5, x0=-3.811, y0=0.0, r=2.695)
# Support Tube/Outer -- Figure 7
surf6 = openmc.ZCylinder(surface_id=6, x0=-3.811, y0=0.0, r=2.86)
# Inlet Tube/Inner -- Figure 7
surf7 = openmc.ZCylinder(surface_id=7, r=2.555)
# Inlet Tube/Outer -- Figure 7
surf8 = openmc.ZCylinder(surface_id=8, r=2.86)

# Z-plane surfaces for bounded cylinders
surf7_zmin = openmc.ZPlane(z0=-99.0)
surf7_zmax = openmc.ZPlane(z0=0.0)
surf8_zmin = openmc.ZPlane(z0=-99.0)
surf8_zmax = openmc.ZPlane(z0=0.0)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# SOLN
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = -surf1 & +surf2 & -surf5

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & -surf3 & +surf5

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf3 & -surf4 & +surf5 & -surf6

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf3 & -surf4 & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# CONCRETE
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf3 & -surf4 & +surf6 & (+surf8 | -surf8_zmin | +surf8_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
