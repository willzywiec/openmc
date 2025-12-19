"""
SMF014-1: Np-237 sphere surrounded by HEU shells and low carbon steel (detailed model)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Np sphere
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Np237", 5.092600e-02)
mat1.add_nuclide("U233", 1.857700e-06)
mat1.add_nuclide("U234", 2.963300e-07)
mat1.add_nuclide("U235", 1.407400e-05)
mat1.add_nuclide("U236", 7.834900e-08)
mat1.add_nuclide("U238", 1.562600e-06)
mat1.add_nuclide("Pu238", 8.234000e-07)
mat1.add_nuclide("Pu239", 1.627100e-05)
mat1.add_nuclide("Pu240", 1.161900e-06)
mat1.add_nuclide("Pu241", 3.116600e-08)
mat1.add_nuclide("Pu242", 1.603200e-07)
mat1.add_nuclide("Am241", 3.337500e-07)
mat1.add_nuclide("Am243", 9.157500e-05)

# Tungsten sheild
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("W", 5.669700e-02)
mat2.add_element("Ni", 3.507900e-03)
mat2.add_element("Fe", 3.686400e-03)

# Inner nickel cladding
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Ni", 9.023400e-02)

# Outer nickel cladding
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Ni", 8.503000e-02)

# SS304
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 6.048300e-02)
mat5.add_element("Cr", 1.646900e-02)
mat5.add_element("Ni", 6.484900e-03)

# SS301
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 6.275800e-02)
mat6.add_element("Cr", 1.438000e-02)
mat6.add_element("Ni", 4.777500e-03)

# Aluminum spacer
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Al", 5.897300e-02)

# Other aluminum parts
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 6.037600e-02)

# Bottom Fe reflector
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Fe", 8.302000e-02)

# Top Fe reflector
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("Fe", 8.293500e-02)

# HEU shells
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_nuclide("U234", 4.876600e-04)
mat11.add_nuclide("U235", 4.434900e-02)
mat11.add_nuclide("U236", 2.228000e-04)
mat11.add_nuclide("U238", 2.514700e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Al mounting plate
surf1 = openmc.model.RectangularParallelepiped(-15.24, 15.24, -15.24, 15.24, -41.9351, -41.3001)
# SS304 lower base
surf2 = openmc.model.RectangularParallelepiped(-13.335, 13.335, -7.62, 7.62, -41.3001, -40.0301)
# SS304 middle base
surf3 = openmc.model.RectangularParallelepiped(-9.8425, 9.8425, -8.255, 8.255, -40.0301, -31.4576)
# SS304 table
surf4 = openmc.model.RectangularParallelepiped(-12.7, 12.7, -7.62, 7.62, -31.4576, -28.9176)
# Al mounting tube: spherical contour
# surf5: Unsupported surface type "s" with params ['15.00124', 'tr', '0', '0', '-6.0042']
# Al mounting tube: large hole
surf6 = openmc.ZCylinder(surface_id=6, r=5.08)
# Al mounting tube: small hole
surf7 = openmc.ZCylinder(surface_id=7, r=0.35179)
# Al mounting tube: upper portion
surf8 = openmc.ZCylinder(surface_id=8, r=10.16)
# Al mounting tube: lower portion
surf9 = openmc.ZCylinder(surface_id=9, r=10.16)
# Al bottom/top shell: top/bottom; Al spacer: bottom
surf10 = openmc.ZPlane(surface_id=10, z0=0.0)
# Al bottom shell: inner
# surf11: Unsupported surface type "s" with params ['4.83108']
# Al bottom shell: outer
# surf12: Unsupported surface type "s" with params ['4.99872']
# Al bottom shell: stem
surf13 = openmc.ZCylinder(surface_id=13, r=0.3302)
# Al spacer: inner
surf17 = openmc.ZCylinder(surface_id=17, r=8.34644)
# Al spacer: outer
surf18 = openmc.ZCylinder(surface_id=18, r=20.066)
# Al spacer: top
surf19 = openmc.ZPlane(surface_id=19, z0=2.54)
# Np sphere
# surf21: Unsupported surface type "s" with params ['4.14909']
# W shield: inner
# surf22: Unsupported surface type "s" with params ['4.16814']
# W shield: outer
# surf23: Unsupported surface type "s" with params ['4.42722']
# Inner Ni cladding: inner
# surf24: Unsupported surface type "s" with params ['4.4323']
# Inner Ni cladding: outer
# surf25: Unsupported surface type "s" with params ['4.6228']
# Outer Ni cladding: inner
# surf26: Unsupported surface type "s" with params ['4.62788']
# Outer Ni cladding: outer
# surf27: Unsupported surface type "s" with params ['4.81838']
# Hole in top Al support plate
surf31 = openmc.ZCylinder(surface_id=31, r=20.32)
# Top Al support plate
surf32 = openmc.model.RectangularParallelepiped(-27.305, 27.305, -27.305, 27.305, 1.27, 2.54)
# Square hole in Al top plate
surf45 = openmc.model.RectangularParallelepiped(-22.098, 22.098, -22.098, 22.098, -49.995, 49.995)
# Al top plate
surf46 = openmc.model.RectangularParallelepiped(-57.15, 57.15, -57.15, 57.15, -1.27, 1.27)
# Al top shell: inner
# surf51: Unsupported surface type "s" with params ['4.83108']
# Al top shell: outer
# surf52: Unsupported surface type "s" with params ['4.99872']
# Al top shell: stem
surf53 = openmc.ZCylinder(surface_id=53, r=0.3302)
# Central z-hole in all HEU shells
surf200 = openmc.ZCylinder(surface_id=200, r=0.35687)
# Bottom HEU shell no. 21
# surf211: Unsupported surface type "s" with params ['5.017', '212', 's', '5.337']
# Top HEU shell no. 22
# surf221: Unsupported surface type "s" with params ['5.013', '222', 's', '5.336']
# Bottom HEU shell no. 23
# surf231: Unsupported surface type "s" with params ['5.346', '232', 's', '5.669']
# Top HEU shell no. 24
# surf241: Unsupported surface type "s" with params ['5.346', '242', 's', '5.669']
# Bottom HEU shell no. 25
# surf251: Unsupported surface type "s" with params ['5.679', '252', 's', '6.003']
# Top HEU shell no. 26
# surf261: Unsupported surface type "s" with params ['5.679', '262', 's', '6.001']
# Bottom HEU shell no. 27
# surf271: Unsupported surface type "s" with params ['6.011', '272', 's', '6.335']
# Top HEU shell no. 28
# surf281: Unsupported surface type "s" with params ['6.012', '282', 's', '6.334']
# Bottom HEU shell no. 29
# surf291: Unsupported surface type "s" with params ['6.345', '292', 's', '6.671']
# Top HEU shell no. 30
# surf301: Unsupported surface type "s" with params ['6.344', '302', 's', '6.670']
# Bottom HEU shell no. 31
# surf311: Unsupported surface type "s" with params ['6.678', '312', 's', '7.002']
# Top HEU shell no. 32
# surf321: Unsupported surface type "s" with params ['6.679', '322', 's', '7.003']
# Bottom HEU shell no. 33
# surf331: Unsupported surface type "s" with params ['7.006', '332', 's', '7.330']
# Top HEU shell no. 34
# surf341: Unsupported surface type "s" with params ['7.010', '342', 's', '7.334']
# Bottom HEU shell no. 35
# surf351: Unsupported surface type "s" with params ['7.342', '352', 's', '7.666']
# Top HEU shell no. 36
# surf361: Unsupported surface type "s" with params ['7.343', '362', 's', '7.666']
# Bottom HEU shell no. 37
# surf371: Unsupported surface type "s" with params ['7.682', '372', 's', '8.003']
# Top HEU shell no. 38
# surf381: Unsupported surface type "s" with params ['7.671', '382', 's', '8.003']
# Bottom  HEU shell no. 39
# surf391: Unsupported surface type "s" with params ['8.013', '392', 's', '8.336']
# Top HEU shell no. 40
# surf401: Unsupported surface type "s" with params ['8.007', '402', 's', '8.329']
# Bottom Fe reflector
# surf601: Unsupported surface type "s" with params ['8.34644', '602', 's', '20.066', '603', 'c', 'z', '0.35179']
# Top Fe reflector
# surf611: Unsupported surface type "s" with params ['8.34644', 'tr', '0', '0', '0.635', '612', 's', '21.59', 'tr', '0', '0', '0.635']

# Z-plane surfaces for bounded cylinders
surf6_zmin = openmc.ZPlane(surface_id=1611, z0=-24.7774)
surf6_zmax = openmc.ZPlane(surface_id=1612, z0=-17.7924)
surf7_zmin = openmc.ZPlane(surface_id=1613, z0=-28.9176)
surf7_zmax = openmc.ZPlane(surface_id=1614, z0=-24.7774)
surf8_zmin = openmc.ZPlane(surface_id=1615, z0=-24.7774)
surf8_zmax = openmc.ZPlane(surface_id=1616, z0=-17.7924)
surf9_zmin = openmc.ZPlane(surface_id=1617, z0=-28.9176)
surf9_zmax = openmc.ZPlane(surface_id=1618, z0=-24.7774)
surf13_zmin = openmc.ZPlane(surface_id=1619, z0=-6.985)
surf13_zmax = openmc.ZPlane(surface_id=1620, z0=-1.0)
surf53_zmin = openmc.ZPlane(surface_id=1621, z0=1.0)
surf53_zmax = openmc.ZPlane(surface_id=1622, z0=6.985)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Al
cell1 = openmc.Cell(cell_id=1, fill=mat8)
cell1.region = -surf1

# SS304
cell2 = openmc.Cell(cell_id=2, fill=mat5)
cell2.region = +surf1 & -surf2

# SS304
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = +surf2 & -surf3

# SS304
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = +surf3 & -surf4

# Al
cell5 = openmc.Cell(cell_id=5, fill=mat8)
cell5.region = +surf5 & (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# Al
cell6 = openmc.Cell(cell_id=6, fill=mat8)
cell6.region = +surf4 & (+surf7 | -surf7_zmin | +surf7_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax) & (-surf9 & +surf9_zmin & -surf9_zmax)

# Al
cell7 = openmc.Cell(cell_id=7, fill=mat8)
cell7.region = -surf10 & +surf11 & -surf12

# Al
cell8 = openmc.Cell(cell_id=8, fill=mat8)
cell8.region = +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax)

# Al
cell9 = openmc.Cell(cell_id=9, fill=mat7)
cell9.region = +surf10 & +surf17 & -surf18 & -surf19

# Np
cell10 = openmc.Cell(cell_id=10, fill=mat1)
cell10.region = -surf21

# W
cell11 = openmc.Cell(cell_id=11, fill=mat2)
cell11.region = +surf22 & -surf23

# Ni
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = +surf24 & -surf25

# Ni
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = +surf26 & -surf27

# Al
cell14 = openmc.Cell(cell_id=14, fill=mat8)
cell14.region = +surf31 & -surf32

# Al
cell15 = openmc.Cell(cell_id=15, fill=mat8)
cell15.region = +surf45 & -surf46

# Al
cell16 = openmc.Cell(cell_id=16, fill=mat8)
cell16.region = +surf10 & +surf51 & -surf52

# Al
cell17 = openmc.Cell(cell_id=17, fill=mat8)
cell17.region = +surf10 & +surf52 & (-surf53 & +surf53_zmin & -surf53_zmax)

# HEU
cell18 = openmc.Cell(cell_id=18, fill=mat11)
cell18.region = -surf10 & +surf200 & +surf211

# HEU
cell19 = openmc.Cell(cell_id=19, fill=mat11)
cell19.region = -surf10 & +surf200 & +surf231

# HEU
cell20 = openmc.Cell(cell_id=20, fill=mat11)
cell20.region = -surf10 & +surf200 & +surf251

# HEU
cell21 = openmc.Cell(cell_id=21, fill=mat11)
cell21.region = -surf10 & +surf200 & +surf271

# HEU
cell22 = openmc.Cell(cell_id=22, fill=mat11)
cell22.region = -surf10 & +surf200 & +surf291

# HEU
cell23 = openmc.Cell(cell_id=23, fill=mat11)
cell23.region = -surf10 & +surf200 & +surf311

# HEU
cell24 = openmc.Cell(cell_id=24, fill=mat11)
cell24.region = -surf10 & +surf200 & +surf331

# HEU
cell25 = openmc.Cell(cell_id=25, fill=mat11)
cell25.region = -surf10 & +surf200 & +surf351

# HEU
cell26 = openmc.Cell(cell_id=26, fill=mat11)
cell26.region = -surf10 & +surf200 & +surf371

# HEU
cell27 = openmc.Cell(cell_id=27, fill=mat11)
cell27.region = -surf10 & +surf200 & +surf391

# Fe
cell28 = openmc.Cell(cell_id=28, fill=mat9)
cell28.region = +surf32 & -surf10 & +surf601

# HEU
cell29 = openmc.Cell(cell_id=29, fill=mat11)
cell29.region = +surf10 & +surf200 & +surf221

# HEU
cell30 = openmc.Cell(cell_id=30, fill=mat11)
cell30.region = +surf10 & +surf200 & +surf241

# HEU
cell31 = openmc.Cell(cell_id=31, fill=mat11)
cell31.region = +surf10 & +surf200 & +surf261

# HEU
cell32 = openmc.Cell(cell_id=32, fill=mat11)
cell32.region = +surf10 & +surf200 & +surf281

# HEU
cell33 = openmc.Cell(cell_id=33, fill=mat11)
cell33.region = +surf10 & +surf200 & +surf301

# HEU
cell34 = openmc.Cell(cell_id=34, fill=mat11)
cell34.region = +surf10 & +surf200 & +surf321

# HEU
cell35 = openmc.Cell(cell_id=35, fill=mat11)
cell35.region = +surf10 & +surf200 & +surf341

# HEU
cell36 = openmc.Cell(cell_id=36, fill=mat11)
cell36.region = +surf10 & +surf200 & +surf361

# HEU
cell37 = openmc.Cell(cell_id=37, fill=mat11)
cell37.region = +surf10 & +surf200 & +surf381

# HEU
cell38 = openmc.Cell(cell_id=38, fill=mat11)
cell38.region = +surf10 & +surf200 & +surf401

# Fe
cell39 = openmc.Cell(cell_id=39, fill=mat10)
cell39.region = +surf19 & +surf611

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39])
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
