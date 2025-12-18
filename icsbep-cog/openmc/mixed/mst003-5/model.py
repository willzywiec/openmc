"""
MIX-SOL-THERM-003-5: AWRE SCAMP
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution B
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 7.470000e-05)
mat1.add_nuclide("Pu240", 4.500000e-06)
mat1.add_nuclide("Pu241", 3.300000e-07)
mat1.add_nuclide("U235", 1.200000e-06)
mat1.add_nuclide("U238", 1.791000e-04)
mat1.add_nuclide("H1", 6.330000e-02)
mat1.add_element("N", 1.280000e-03)
mat1.add_nuclide("O16", 3.620000e-02)
mat1.add_element("Fe", 7.000000e-09)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.328700e-02)
mat2.add_element("Cr", 1.653400e-02)
mat2.add_element("Ni", 6.509300e-03)

# Polyethylene
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 7.986700e-02)
mat3.add_element("C", 3.993300e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.672900e-02)
mat4.add_nuclide("O16", 3.336600e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Hc
surf1 = openmc.ZPlane(surface_id=1, z0=46.18)
# Steel plate
surf2 = openmc.ZCylinder(surface_id=2, x0=46.18, y0=46.497, r=15.11)
# Polyethylene
surf3 = openmc.ZCylinder(surface_id=3, x0=46.497, y0=61.497, r=15.11)
# Vessel, inner
surf4 = openmc.ZCylinder(surface_id=4, x0=0.0, y0=107.0, r=15.31)
# Vessel, outer
surf5 = openmc.ZCylinder(surface_id=5, x0=-1.0, y0=107.0, r=15.56)
# Vessel, flange
surf6 = openmc.ZCylinder(surface_id=6, x0=-1.0, y0=0.0, r=20.56)
# Water reflector
surf7 = openmc.ZCylinder(surface_id=7, x0=-16.0, y0=107.0, r=42.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf4

# SS304L
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# Poly
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

# SS304L
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf4 & -surf5 & -surf7

# SS304L
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf5 & -surf6

# Water
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf5 & +surf6 & -surf7

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
source.space = openmc.stats.Point((0.0, 0.0, 23.09))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
