"""
LST019-1: Concrete reflected 28-cm-thick slab tank with 10% enriched uranyl nitrate solution @ H/X=725 (Run 183)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution: Run 183
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 6.527400e-07)
mat1.add_nuclide("U235", 8.100100e-05)
mat1.add_nuclide("U236", 8.090000e-08)
mat1.add_nuclide("U238", 7.214900e-04)
mat1.add_nuclide("H1", 5.876000e-02)
mat1.add_element("N", 2.187600e-03)
mat1.add_nuclide("O16", 3.725800e-02)
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

# Polyethylene
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 8.380600e-02)
mat5.add_element("C", 4.150100e-02)
mat5.add_s_alpha_beta("c_H_in_CH2")

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
surf3 = openmc.ZPlane(surface_id=3, z0=82.52)
# P10          [ dX=C-B; Xo=-(B+C)/2 ]
surf10 = openmc.model.RectangularParallelepiped(-18.62, -17.59, -35.4, 35.4, 0.0, 150.5)
# Gap          [ dX=C-B; Xo=-(B+C)/2 ]
surf11 = openmc.model.RectangularParallelepiped(-18.62, -17.59, -35.7, 35.7, 0.0, 150.5)
# Steel Frame  [ dX=C-B; Xo=-(B+C)/2 ]
surf12 = openmc.model.RectangularParallelepiped(-18.62, -17.59, -38.7, 38.7, -3.0, 153.5)
# Aluminum     [ dX=D-A; Xo=-(D+A)/2 ]
surf13 = openmc.model.RectangularParallelepiped(-19.43, -16.78, -38.7, 38.7, -3.0, 153.5)
# P10          [ dx=C-B; Xo=+(B+C)/2 ]
surf20 = openmc.model.RectangularParallelepiped(17.59, 18.62, -35.4, 35.4, 0.0, 150.5)
# Gap          [ dX=C-B; Xo=+(B+C)/2 ]
surf21 = openmc.model.RectangularParallelepiped(17.59, 18.62, -35.7, 35.7, 0.0, 150.5)
# Steel Frame  [ dx=C-B; Xo=+(B+C)/2 ]
surf22 = openmc.model.RectangularParallelepiped(17.59, 18.62, -38.7, 38.7, -3.0, 153.5)
# Aluminum     [ dx=D-A; Xo=+(D+A)/2 ]
surf23 = openmc.model.RectangularParallelepiped(16.78, 19.43, -38.7, 38.7, -3.0, 153.5)
# BCD
surf99 = openmc.model.RectangularParallelepiped(-20.0, 20.0, -39.0, 39.0, -4.0, 156.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf3

# Tank
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# Poly
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = -surf10 & -surf11 & -surf12 & -surf13

# Frame
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf10 & +surf11 & -surf12 & -surf13

# Alum
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf10 & +surf11 & +surf12 & -surf13

# Poly
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = -surf20 & -surf21 & -surf22 & -surf23

# Frame
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf20 & +surf21 & -surf22 & -surf23

# Alum
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = +surf20 & +surf21 & +surf22 & -surf23

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
source.space = openmc.stats.Point((0.0, 0.0, 41.26))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
