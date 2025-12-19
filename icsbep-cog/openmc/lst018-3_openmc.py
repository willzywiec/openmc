"""
LST018-3: Concrete reflected 28-cm-thick slab tank with 10% enriched uranyl nitrate solution @ H/X=736 (Run 143)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution: Run 143
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 6.436900e-07)
mat1.add_nuclide("U235", 7.987700e-05)
mat1.add_nuclide("U236", 7.977700e-08)
mat1.add_nuclide("U238", 7.114700e-04)
mat1.add_nuclide("H1", 5.876200e-02)
mat1.add_element("N", 2.159300e-03)
mat1.add_nuclide("O16", 3.715500e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless Steel Tank
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

# Stainless Steel Frame Plates
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

# Concrete
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 1.452800e-02)
mat5.add_nuclide("O16", 7.263900e-03)
mat5.add_nuclide("O16", 3.732600e-02)
mat5.add_element("Na", 1.053300e-03)
mat5.add_element("Mg", 1.957300e-04)
mat5.add_element("Al", 1.553300e-03)
mat5.add_element("Si", 1.474900e-02)
mat5.add_element("S", 1.090600e-04)
mat5.add_element("Cl", 9.002700e-07)
mat5.add_element("K", 1.917900e-04)
mat5.add_element("Ca", 3.933700e-03)
mat5.add_element("Fe", 2.783000e-04)
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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Slab tank/inner
surf1 = openmc.model.RectangularParallelepiped(-14.04, 14.04, -34.515, 34.515, 0.0, 149.75)
# Slab tank/outer
surf2 = openmc.model.RectangularParallelepiped(-16.57, 16.57, -37.045, 37.045, -2.039999999999992, 152.63)
# Hc
surf3 = openmc.ZPlane(surface_id=3, z0=73.18)
# C50          [ dX=C-B; Xo=-(B+C)/2 ]
surf11 = openmc.model.RectangularParallelepiped(-22.599999999999998, -17.59, -35.7, 35.7, 0.0, 150.6)
# Steel Frame  [ dX=C-B; Xo=-(B+C)/2 ]
surf12 = openmc.model.RectangularParallelepiped(-22.599999999999998, -17.59, -38.7, 38.7, -3.0, 153.6)
# Aluminum     [ dX=D-A; Xo=-(D+A)/2 ]
surf13 = openmc.model.RectangularParallelepiped(-23.41, -16.779999999999998, -38.7, 38.7, -3.0, 153.6)
# C50          [ dx=C-B; Xo=+(B+C)/2 ]
surf21 = openmc.model.RectangularParallelepiped(17.59, 22.599999999999998, -35.7, 35.7, 0.0, 150.6)
# Steel Frame  [ dx=C-B; Xo=+(B+C)/2 ]
surf22 = openmc.model.RectangularParallelepiped(17.59, 22.599999999999998, -38.7, 38.7, -3.0, 153.6)
# Aluminum     [ dx=D-A; Xo=+(D+A)/2 ]
surf23 = openmc.model.RectangularParallelepiped(16.779999999999998, 23.41, -38.7, 38.7, -3.0, 153.6)
# BCD
surf99 = openmc.model.RectangularParallelepiped(-24.0, 24.0, -39.0, 39.0, -4.0, 156.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf3

# Tank
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# Cncrt
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = -surf11 & -surf12 & -surf13

# Frame
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf11 & -surf12 & -surf13

# Alum
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf11 & +surf12 & -surf13

# Cncrt
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = -surf21 & -surf22 & -surf23

# Frame
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf21 & -surf22 & -surf23

# Alum
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = +surf21 & +surf22 & -surf23

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
source.space = openmc.stats.Point((0.0, 0.0, 36.59))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
