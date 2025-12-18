"""
LST022-2: STACY 28cm thick slab tank with 10% enriched uranyl nitrate solution @ H/X=749 reflected with (B050) borated concrete (Run 135)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution: Run 135
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 6.358600e-07)
mat1.add_nuclide("U235", 7.890600e-05)
mat1.add_nuclide("U236", 7.880800e-08)
mat1.add_nuclide("U238", 7.028300e-04)
mat1.add_nuclide("H1", 5.908700e-02)
mat1.add_element("N", 2.046700e-03)
mat1.add_nuclide("O16", 3.700700e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless Steel [1] Core Tank
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 7.156700e-05)
mat2.add_element("Si", 7.141500e-04)
mat2.add_element("Mn", 9.909500e-04)
mat2.add_element("P", 5.087900e-05)
mat2.add_element("S", 1.042400e-05)
mat2.add_element("Ni", 8.560000e-03)
mat2.add_element("Cr", 1.672500e-02)
mat2.add_element("Fe", 5.956000e-02)

# Stainless Steel [2] Reflector Frame Plates
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 2.067500e-04)
mat3.add_element("Si", 6.631400e-04)
mat3.add_element("Mn", 1.008300e-03)
mat3.add_element("P", 4.933700e-05)
mat3.add_element("S", 1.638000e-05)
mat3.add_element("Ni", 6.688500e-03)
mat3.add_element("Cr", 1.679800e-02)
mat3.add_element("Fe", 6.143500e-02)

# Aluminum Alloy
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 5.955900e-02)
mat4.add_element("Si", 8.075100e-05)
mat4.add_element("Fe", 1.711400e-04)
mat4.add_element("Cu", 1.784500e-05)

# Borated Concrete (B050)
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 1.704800e-02)
mat5.add_nuclide("O16", 8.524100e-03)
mat5.add_nuclide("O16", 3.377300e-02)
mat5.add_nuclide("B10", 6.118900e-04)
mat5.add_nuclide("B11", 2.462900e-03)
mat5.add_element("C", 7.671100e-04)
mat5.add_element("Na", 9.522000e-05)
mat5.add_element("Mg", 1.314900e-04)
mat5.add_element("Al", 7.619100e-04)
mat5.add_element("Si", 1.345900e-02)
mat5.add_element("S", 1.353800e-04)
mat5.add_element("Cl", 7.304000e-07)
mat5.add_element("K", 1.265800e-04)
mat5.add_element("Ca", 4.833600e-03)
mat5.add_element("Fe", 1.538600e-04)
mat5.add_s_alpha_beta("c_H_in_H2O")

# Air
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("N", 3.901400e-05)
mat6.add_nuclide("O16", 1.041000e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# SST tank, inner
surf1 = openmc.model.RectangularParallelepiped(-14.04, 14.04, -34.515, 34.515, 0.0, 149.75)
# SST tank, outer
surf2 = openmc.model.RectangularParallelepiped(-16.57, 16.57, -37.045, 37.045, -2.039999999999992, 152.63)
# Hc
surf3 = openmc.ZPlane(surface_id=3, z0=73.87)
# Borated concrete
surf11 = openmc.model.RectangularParallelepiped(-32.4, -17.52, -35.7, 35.7, 0.0, 150.6)
# Steel frames
surf12 = openmc.model.RectangularParallelepiped(-32.4, -17.52, -38.7, 38.7, -3.0, 153.6)
# Aluminum cover plates
surf13 = openmc.model.RectangularParallelepiped(-33.199999999999996, -16.71, -38.7, 38.7, -3.0, 153.6)
# Borated concrete
surf21 = openmc.model.RectangularParallelepiped(17.52, 32.4, -35.7, 35.7, 0.0, 150.6)
# Steel frames
surf22 = openmc.model.RectangularParallelepiped(17.52, 32.4, -38.7, 38.7, -3.0, 153.6)
# Aluminum cover plates
surf23 = openmc.model.RectangularParallelepiped(16.71, 33.199999999999996, -38.7, 38.7, -3.0, 153.6)
# BCD
surf99 = openmc.model.RectangularParallelepiped(-33.2, 33.2, -38.7, 38.7, -3.0, 153.6, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf3 & -surf99
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf1 & -surf2 & -surf99
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = -surf11
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = +surf11 & -surf12 & -surf13 & -surf99
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf11 & +surf12 & -surf13 & -surf99
u1_cell5 = openmc.Cell(fill=mat5)
u1_cell5.region = -surf21
u1_cell6 = openmc.Cell(fill=mat3)
u1_cell6.region = +surf21 & -surf22 & -surf23 & -surf99
u1_cell7 = openmc.Cell(fill=mat4)
u1_cell7.region = +surf21 & +surf22 & -surf23 & -surf99
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Prob
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.region = -surf99

root_universe = openmc.Universe(cells=[cell1])
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
source.space = openmc.stats.Point((0.0, 0.0, 36.935))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
