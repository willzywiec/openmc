"""
HEU-MET-FAST-001-3i: Idealized Model of Jemima Configuration #3 with Tu-Oy-Tu Disk Triplets, Fillers In
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Al-2024
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_element("Mg", 1.029500e-03)
mat1.add_element("Al", 5.786800e-02)
mat1.add_element("Mn", 1.518200e-04)
mat1.add_element("Cu", 1.155000e-03)

# SST
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cr", 1.653200e-02)
mat2.add_element("Fe", 6.327800e-02)
mat2.add_element("Ni", 6.509500e-03)

# Tu
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U234", 2.641800e-06)
mat3.add_nuclide("U235", 3.458300e-04)
mat3.add_nuclide("U238", 4.768400e-02)

# Oy
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U234", 4.917200e-04)
mat4.add_nuclide("U235", 4.484900e-02)
mat4.add_nuclide("U238", 2.630500e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, r=1.74625)
surf2 = openmc.ZCylinder(surface_id=2, r=4.60375)
surf3 = openmc.ZCylinder(surface_id=3, r=12.065)
surf4 = openmc.ZCylinder(surface_id=4, r=12.66939)
surf5 = openmc.ZCylinder(surface_id=5, r=12.7)
surf6 = openmc.ZCylinder(surface_id=6, r=13.335)
surf7 = openmc.ZCylinder(surface_id=7, r=13.67711)
surf8 = openmc.ZCylinder(surface_id=8, r=15.29416)
surf9 = openmc.ZCylinder(surface_id=9, r=15.82055)
surf10 = openmc.ZCylinder(surface_id=10, r=17.1965)
surf11 = openmc.ZCylinder(surface_id=11, r=19.22627, boundary_type="vacuum")
surf21 = openmc.ZPlane(surface_id=21, z0=-8.5725)
surf22 = openmc.ZPlane(surface_id=22, z0=-6.0325)
surf23 = openmc.ZPlane(surface_id=23, z0=-4.7625)
surf24 = openmc.ZPlane(surface_id=24, z0=-3.1750)
surf25 = openmc.ZPlane(surface_id=25, z0=-0.9525)
surf26 = openmc.ZPlane(surface_id=26, z0=-0.3175)
surf27 = openmc.ZPlane(surface_id=27, z0=0.000)
surf28 = openmc.ZPlane(surface_id=28, z0=0.604)
surf29 = openmc.ZPlane(surface_id=29, z0=1.408)
surf30 = openmc.ZPlane(surface_id=30, z0=2.616)
surf31 = openmc.ZPlane(surface_id=31, z0=3.420)
surf32 = openmc.ZPlane(surface_id=32, z0=4.628)
surf33 = openmc.ZPlane(surface_id=33, z0=5.432)
surf34 = openmc.ZPlane(surface_id=34, z0=6.640)
surf35 = openmc.ZPlane(surface_id=35, z0=7.444)
surf36 = openmc.ZPlane(surface_id=36, z0=8.652)
surf37 = openmc.ZPlane(surface_id=37, z0=9.456)
surf38 = openmc.ZPlane(surface_id=38, z0=10.664)
surf39 = openmc.ZPlane(surface_id=39, z0=11.468)
surf40 = openmc.ZPlane(surface_id=40, z0=12.676)
surf41 = openmc.ZPlane(surface_id=41, z0=13.480)
surf42 = openmc.ZPlane(surface_id=42, z0=14.084)
surf43 = openmc.ZPlane(surface_id=43, z0=14.688)
surf44 = openmc.ZPlane(surface_id=44, z0=15.492)
surf45 = openmc.ZPlane(surface_id=45, z0=16.700)
surf46 = openmc.ZPlane(surface_id=46, z0=17.504)
surf47 = openmc.ZPlane(surface_id=47, z0=18.712)
surf48 = openmc.ZPlane(surface_id=48, z0=19.516)
surf49 = openmc.ZPlane(surface_id=49, z0=20.724)
surf50 = openmc.ZPlane(surface_id=50, z0=21.528)
surf51 = openmc.ZPlane(surface_id=51, z0=22.736)
surf52 = openmc.ZPlane(surface_id=52, z0=23.540)
surf53 = openmc.ZPlane(surface_id=53, z0=24.748)
surf54 = openmc.ZPlane(surface_id=54, z0=24.9729)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Tu
cell1 = openmc.Cell(cell_id=1, fill=mat3)
cell1.region = -surf6 & +surf53 & -surf54

# Tu
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = -surf6 & +surf52 & -surf53

# Oy
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf6 & +surf51 & -surf52

# Tu
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = -surf6 & +surf50 & -surf51

# Oy
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = -surf6 & +surf49 & -surf50

# Tu
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = -surf6 & +surf48 & -surf49

# Oy
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = -surf6 & +surf47 & -surf48

# Tu
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = -surf6 & +surf46 & -surf47

# Oy
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = -surf6 & +surf45 & -surf46

# Tu
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = -surf6 & +surf44 & -surf45

# Oy
cell11 = openmc.Cell(cell_id=11, fill=mat4)
cell11.region = -surf6 & +surf43 & -surf44

# Tu
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = -surf4 & +surf42 & -surf43

# Tu
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = -surf6 & +surf41 & -surf42

# Oy
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = -surf6 & +surf40 & -surf41

# Tu
cell15 = openmc.Cell(cell_id=15, fill=mat3)
cell15.region = -surf6 & +surf39 & -surf40

# Oy
cell16 = openmc.Cell(cell_id=16, fill=mat4)
cell16.region = -surf6 & +surf38 & -surf39

# Tu
cell17 = openmc.Cell(cell_id=17, fill=mat3)
cell17.region = -surf6 & +surf37 & -surf38

# Oy
cell18 = openmc.Cell(cell_id=18, fill=mat4)
cell18.region = -surf6 & +surf36 & -surf37

# Tu
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = -surf6 & +surf35 & -surf36

# Oy
cell20 = openmc.Cell(cell_id=20, fill=mat4)
cell20.region = -surf6 & +surf34 & -surf35

# Tu
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = -surf6 & +surf33 & -surf34

# Oy
cell22 = openmc.Cell(cell_id=22, fill=mat4)
cell22.region = -surf6 & +surf32 & -surf33

# Tu
cell23 = openmc.Cell(cell_id=23, fill=mat3)
cell23.region = -surf6 & +surf31 & -surf32

# Oy
cell24 = openmc.Cell(cell_id=24, fill=mat4)
cell24.region = -surf6 & +surf30 & -surf31

# Tu
cell25 = openmc.Cell(cell_id=25, fill=mat3)
cell25.region = -surf6 & +surf29 & -surf30

# Oy
cell26 = openmc.Cell(cell_id=26, fill=mat4)
cell26.region = -surf6 & +surf28 & -surf29

# Tu
cell27 = openmc.Cell(cell_id=27, fill=mat3)
cell27.region = -surf6 & +surf27 & -surf28

# Al
cell28 = openmc.Cell(cell_id=28, fill=mat1)
cell28.region = +surf4 & -surf8 & +surf42 & -surf43

# Al
cell29 = openmc.Cell(cell_id=29, fill=mat1)
cell29.region = +surf3 & -surf9 & +surf25 & -surf27

# Al
cell30 = openmc.Cell(cell_id=30, fill=mat1)
cell30.region = +surf6 & -surf7 & +surf23 & -surf25

# Al
cell31 = openmc.Cell(cell_id=31, fill=mat1)
cell31.region = +surf5 & -surf10 & +surf22 & -surf23

# Al
cell32 = openmc.Cell(cell_id=32, fill=mat1)
cell32.region = -surf1 & +surf24 & -surf26

# Al
cell33 = openmc.Cell(cell_id=33, fill=mat1)
cell33.region = -surf2 & +surf22 & -surf24

# SS
cell34 = openmc.Cell(cell_id=34, fill=mat2)
cell34.region = -surf11 & +surf21 & -surf22

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34])
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
source.space = openmc.stats.Box((-9.0, -9.0, 0.006000000000000005), (9.0, 9.0, 24.138))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
