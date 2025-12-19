"""
PU-MET-FAST-041; 5.070 kg a-Pu(88) in 1.6 D-38
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat101 = openmc.Material(material_id=101)
mat101.set_density("sum")
mat101.add_nuclide("Pu239", 4.247700e-02)
mat101.add_nuclide("Pu240", 4.972100e-03)
mat101.add_nuclide("Pu241", 8.260400e-04)
mat101.add_element("Fe", 3.316800e-04)
mat101.add_element("C", 1.412800e-03)
mat101.add_element("H", 3.576500e-04)
mat101.add_element("N", 3.860400e-05)
mat101.add_nuclide("O16", 5.722700e-05)

mat102 = openmc.Material(material_id=102)
mat102.set_density("sum")
mat102.add_nuclide("Pu239", 4.083200e-02)
mat102.add_nuclide("Pu240", 4.764600e-03)
mat102.add_nuclide("Pu241", 8.925300e-04)
mat102.add_element("Fe", 2.994200e-04)
mat102.add_element("C", 1.954900e-03)
mat102.add_element("H", 8.178900e-04)
mat102.add_element("N", 8.828100e-05)
mat102.add_nuclide("O16", 1.308700e-04)

mat103 = openmc.Material(material_id=103)
mat103.set_density("sum")
mat103.add_nuclide("Pu239", 4.227600e-02)
mat103.add_nuclide("Pu240", 4.606000e-03)
mat103.add_nuclide("Pu241", 6.714700e-04)
mat103.add_element("Fe", 2.653400e-04)
mat103.add_element("C", 1.105300e-03)
mat103.add_element("H", 2.001100e-04)
mat103.add_element("N", 2.160000e-05)
mat103.add_nuclide("O16", 3.202000e-05)

mat104 = openmc.Material(material_id=104)
mat104.set_density("sum")
mat104.add_nuclide("Pu239", 4.168100e-02)
mat104.add_nuclide("Pu240", 4.717600e-03)
mat104.add_nuclide("Pu241", 7.407900e-04)
mat104.add_element("Fe", 3.035600e-04)
mat104.add_element("C", 1.192200e-03)
mat104.add_element("H", 2.750500e-04)
mat104.add_element("N", 2.968800e-05)
mat104.add_nuclide("O16", 4.401100e-05)

mat201 = openmc.Material(material_id=201)
mat201.set_density("sum")
mat201.add_nuclide("U235", 2.100000e-04)
mat201.add_nuclide("U238", 4.668200e-02)
mat201.add_element("C", 2.895300e-03)
mat201.add_element("Fe", 3.816600e-04)

mat202 = openmc.Material(material_id=202)
mat202.set_density("sum")
mat202.add_nuclide("U235", 2.099700e-04)
mat202.add_nuclide("U238", 4.667600e-02)
mat202.add_element("C", 2.895000e-03)
mat202.add_element("Fe", 3.816100e-04)

mat203 = openmc.Material(material_id=203)
mat203.set_density("sum")
mat203.add_nuclide("U235", 2.141300e-04)
mat203.add_nuclide("U238", 4.653700e-02)
mat203.add_element("C", 2.886700e-03)
mat203.add_element("Fe", 3.805100e-04)

mat204 = openmc.Material(material_id=204)
mat204.set_density("sum")
mat204.add_nuclide("U235", 2.106100e-04)
mat204.add_nuclide("U238", 4.681700e-02)
mat204.add_element("C", 2.903700e-03)
mat204.add_element("Fe", 3.827600e-04)

mat205 = openmc.Material(material_id=205)
mat205.set_density("sum")
mat205.add_nuclide("U235", 2.103100e-04)
mat205.add_nuclide("U238", 4.675100e-02)
mat205.add_element("C", 2.899700e-03)
mat205.add_element("Fe", 3.822200e-04)

mat206 = openmc.Material(material_id=206)
mat206.set_density("sum")
mat206.add_nuclide("U235", 2.104400e-04)
mat206.add_nuclide("U238", 4.678000e-02)
mat206.add_element("C", 2.901500e-03)
mat206.add_element("Fe", 3.824600e-04)

mat207 = openmc.Material(material_id=207)
mat207.set_density("sum")
mat207.add_nuclide("U235", 2.104700e-04)
mat207.add_nuclide("U238", 4.678600e-02)
mat207.add_element("C", 2.901800e-03)
mat207.add_element("Fe", 3.825100e-04)

mat208 = openmc.Material(material_id=208)
mat208.set_density("sum")
mat208.add_nuclide("U235", 2.191200e-04)
mat208.add_nuclide("U238", 4.558600e-02)
mat208.add_element("C", 2.828200e-03)
mat208.add_element("Fe", 3.728100e-04)

mat209 = openmc.Material(material_id=209)
mat209.set_density("sum")
mat209.add_nuclide("U235", 2.105900e-04)
mat209.add_nuclide("U238", 4.576700e-02)
mat209.add_element("C", 2.838900e-03)
mat209.add_element("Fe", 3.742200e-04)

mat210 = openmc.Material(material_id=210)
mat210.set_density("sum")
mat210.add_nuclide("U235", 2.068700e-04)
mat210.add_nuclide("U238", 4.598600e-02)
mat210.add_element("C", 2.852200e-03)
mat210.add_element("Fe", 3.759700e-04)

mat211 = openmc.Material(material_id=211)
mat211.set_density("sum")
mat211.add_nuclide("U235", 2.029800e-04)
mat211.add_nuclide("U238", 4.512000e-02)
mat211.add_element("C", 2.798500e-03)
mat211.add_element("Fe", 3.688900e-04)

mat212 = openmc.Material(material_id=212)
mat212.set_density("sum")
mat212.add_nuclide("U235", 2.157700e-04)
mat212.add_nuclide("U238", 4.587000e-02)
mat212.add_element("C", 2.845600e-03)
mat212.add_element("Fe", 3.750900e-04)

mat213 = openmc.Material(material_id=213)
mat213.set_density("sum")
mat213.add_nuclide("U235", 2.069200e-04)
mat213.add_nuclide("U238", 4.599700e-02)
mat213.add_element("C", 2.852900e-03)
mat213.add_element("Fe", 3.760600e-04)

mat214 = openmc.Material(material_id=214)
mat214.set_density("sum")
mat214.add_nuclide("U235", 2.111600e-04)
mat214.add_nuclide("U238", 4.693900e-02)
mat214.add_element("C", 2.911300e-03)
mat214.add_element("Fe", 3.837600e-04)

mat215 = openmc.Material(material_id=215)
mat215.set_density("sum")
mat215.add_nuclide("U235", 2.079900e-04)
mat215.add_nuclide("U238", 4.623600e-02)
mat215.add_element("C", 2.867700e-03)
mat215.add_element("Fe", 3.780100e-04)

mat216 = openmc.Material(material_id=216)
mat216.set_density("sum")
mat216.add_nuclide("U235", 2.067800e-04)
mat216.add_nuclide("U238", 4.596500e-02)
mat216.add_element("C", 2.850900e-03)
mat216.add_element("Fe", 3.758000e-04)

mat217 = openmc.Material(material_id=217)
mat217.set_density("sum")
mat217.add_nuclide("U235", 2.064200e-04)
mat217.add_nuclide("U238", 4.588700e-02)
mat217.add_element("C", 2.846000e-03)
mat217.add_element("Fe", 3.751600e-04)

materials = openmc.Materials([mat101, mat102, mat103, mat104, mat201, mat202, mat203, mat204, mat205, mat206, mat207, mat208, mat209, mat210, mat211, mat212, mat213, mat214, mat215, mat216, mat217])

# ==============================================================================
# Geometry
# ==============================================================================

surf100 = openmc.Sphere(surface_id=100, r=0.901)
surf101 = openmc.Sphere(surface_id=101, r=1.000)
surf102 = openmc.Sphere(surface_id=102, r=1.400)
surf103 = openmc.Sphere(surface_id=103, r=3.150)
surf104 = openmc.Sphere(surface_id=104, r=4.020)
surf201 = openmc.Sphere(surface_id=201, r=4.660)
surf202 = openmc.Sphere(surface_id=202, r=5.350)
surf203 = openmc.Sphere(surface_id=203, r=6.000)
surf204 = openmc.Sphere(surface_id=204, r=6.750)
surf205 = openmc.Sphere(surface_id=205, r=7.550)
surf206 = openmc.Sphere(surface_id=206, r=8.350)
surf207 = openmc.Sphere(surface_id=207, r=9.150)
surf208 = openmc.Sphere(surface_id=208, r=11.000)
surf209 = openmc.Sphere(surface_id=209, r=12.250)
surf210 = openmc.Sphere(surface_id=210, r=13.250)
surf211 = openmc.Sphere(surface_id=211, r=14.000)
surf212 = openmc.Sphere(surface_id=212, r=15.000)
surf213 = openmc.Sphere(surface_id=213, r=16.500)
surf214 = openmc.Sphere(surface_id=214, r=18.000)
surf215 = openmc.Sphere(surface_id=215, r=21.500)
surf216 = openmc.Sphere(surface_id=216, r=23.000)
surf217 = openmc.Sphere(surface_id=217, r=25.000, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# VOID
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf100

# LAYER1
cell2 = openmc.Cell(cell_id=2, fill=mat101)
cell2.region = +surf100 & -surf101

# LAYER2
cell3 = openmc.Cell(cell_id=3, fill=mat102)
cell3.region = +surf101 & -surf102

# LAYER3
cell4 = openmc.Cell(cell_id=4, fill=mat103)
cell4.region = +surf102 & -surf103

# LAYER4
cell5 = openmc.Cell(cell_id=5, fill=mat104)
cell5.region = +surf103 & -surf104

# DU01
cell6 = openmc.Cell(cell_id=6, fill=mat201)
cell6.region = +surf104 & -surf201

# DU02
cell7 = openmc.Cell(cell_id=7, fill=mat202)
cell7.region = +surf201 & -surf202

# DU03
cell8 = openmc.Cell(cell_id=8, fill=mat203)
cell8.region = +surf202 & -surf203

# DU04
cell9 = openmc.Cell(cell_id=9, fill=mat204)
cell9.region = +surf203 & -surf204

# DU05
cell10 = openmc.Cell(cell_id=10, fill=mat205)
cell10.region = +surf204 & -surf205

# DU06
cell11 = openmc.Cell(cell_id=11, fill=mat206)
cell11.region = +surf205 & -surf206

# DU07
cell12 = openmc.Cell(cell_id=12, fill=mat207)
cell12.region = +surf206 & -surf207

# DU08
cell13 = openmc.Cell(cell_id=13, fill=mat208)
cell13.region = +surf207 & -surf208

# DU09
cell14 = openmc.Cell(cell_id=14, fill=mat209)
cell14.region = +surf208 & -surf209

# DU10
cell15 = openmc.Cell(cell_id=15, fill=mat210)
cell15.region = +surf209 & -surf210

# DU11
cell16 = openmc.Cell(cell_id=16, fill=mat211)
cell16.region = +surf210 & -surf211

# DU12
cell17 = openmc.Cell(cell_id=17, fill=mat212)
cell17.region = +surf211 & -surf212

# DU13
cell18 = openmc.Cell(cell_id=18, fill=mat213)
cell18.region = +surf212 & -surf213

# DU14
cell19 = openmc.Cell(cell_id=19, fill=mat214)
cell19.region = +surf213 & -surf214

# DU15
cell20 = openmc.Cell(cell_id=20, fill=mat215)
cell20.region = +surf214 & -surf215

# DU16
cell21 = openmc.Cell(cell_id=21, fill=mat216)
cell21.region = +surf215 & -surf216

# DU17
cell22 = openmc.Cell(cell_id=22, fill=mat217)
cell22.region = +surf216 & -surf217

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22])
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0001))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
