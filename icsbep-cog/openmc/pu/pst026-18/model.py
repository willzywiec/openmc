"""
PU-SOL-THERM-026 (Case 18) 43.755 kg Pu(81.6) at H/X = 109 with H/SQRT(A) = 0.235
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.157400e-06)
mat1.add_nuclide("Pu239", 4.605400e-04)
mat1.add_nuclide("Pu240", 1.111500e-04)
mat1.add_nuclide("Pu241", 2.725100e-05)
mat1.add_nuclide("Pu242", 5.751200e-06)
mat1.add_nuclide("Am241", 1.684400e-06)
mat1.add_nuclide("H1", 5.314400e-02)
mat1.add_element("N", 4.921600e-03)
mat1.add_nuclide("O16", 4.009000e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("P", 8.020000e+00)
mat2.add_element("Fe", 6.944800e+01)
mat2.add_element("Cr", 1.900000e+01)
mat2.add_element("Ni", 1.000000e+01)
mat2.add_element("Mn", 1.000000e+00)
mat2.add_element("C", 1.500000e-02)
mat2.add_element("Si", 5.000000e-01)
mat2.add_element("S", 1.500000e-02)
mat2.add_element("P", 2.200000e-02)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("P", 2.330000e+00)
mat3.add_nuclide("O16", 5.191000e+01)
mat3.add_element("Si", 2.310000e+01)
mat3.add_element("Ca", 1.200000e+01)
mat3.add_element("Al", 4.790000e+00)
mat3.add_element("Fe", 3.370000e+00)
mat3.add_element("Na", 1.430000e+00)
mat3.add_nuclide("H1", 1.050000e+00)
mat3.add_element("Mg", 9.200000e-01)
mat3.add_element("K", 7.200000e-01)
mat3.add_element("S", 3.800000e-01)
mat3.add_element("Ti", 3.300000e-01)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Hc
surf1 = openmc.ZPlane(surface_id=1, z0=78.892)
# Tank/Inner:  Width = Tc
surf2 = openmc.model.RectangularParallelepiped(-337.509, -230.82899999999998, 138.07500000000002, 159.665, -192.929, -86.249)
# Tank/Outer:  Width = Tc +  0.318
surf3 = openmc.model.RectangularParallelepiped(-337.959, -230.379, 137.916, 159.824, -193.379, -85.799)
# Frame/Outer: Width = Tc + 23.178
surf4 = openmc.model.RectangularParallelepiped(-337.959, -230.379, 126.486, 171.25400000000002, -193.379, -85.799)
# U-Frame/Inner
surf5 = openmc.model.RectangularParallelepiped(-355.289, -213.04899999999998, 111.87, 180.45, -211.344, -67.834)
# U-Frame/Outer
surf6 = openmc.model.RectangularParallelepiped(-355.765, -212.57299999999998, 111.87, 180.45, -211.82, -67.834)
# Hood/Inner
surf7 = openmc.model.RectangularParallelepiped(-380.365, -103.113, 76.83500000000001, 319.405, -311.78499999999997, 144.145)
# Hood/Outer
surf8 = openmc.model.RectangularParallelepiped(-381.0, -102.47800000000001, 76.2, 320.04, -312.41999999999996, 144.78)
# Room/Inner
surf9 = openmc.model.RectangularParallelepiped(-533.4, 533.4, -563.88, 502.91999999999996, -312.42, 312.42)
# Room/Outer
surf10 = openmc.model.RectangularParallelepiped(-685.8, 685.8, -655.32, 655.32, -373.38, 373.38, boundary_type="vacuum")
# Square Holes
surf11 = openmc.model.RectangularParallelepiped(-5.14125, 5.14125, -500.0, 500.0, -5.14125, 5.14125)
surf101 = openmc.model.RectangularParallelepiped(-337.01025000000004, -326.72775, -500.0, 500.0, -192.43025, -182.14774999999997)
surf102 = openmc.model.RectangularParallelepiped(-326.41025, -316.12775, -500.0, 500.0, -192.43025, -182.14774999999997)
surf103 = openmc.model.RectangularParallelepiped(-315.81025, -305.52774999999997, -500.0, 500.0, -192.43025, -182.14774999999997)
surf104 = openmc.model.RectangularParallelepiped(-305.21025000000003, -294.92775, -500.0, 500.0, -192.43025, -182.14774999999997)
surf105 = openmc.model.RectangularParallelepiped(-294.61025, -284.32775, -500.0, 500.0, -192.43025, -182.14774999999997)
surf106 = openmc.model.RectangularParallelepiped(-284.01025000000004, -273.72775, -500.0, 500.0, -192.43025, -182.14774999999997)
surf107 = openmc.model.RectangularParallelepiped(-273.41025, -263.12775, -500.0, 500.0, -192.43025, -182.14774999999997)
surf108 = openmc.model.RectangularParallelepiped(-262.81025, -252.52774999999997, -500.0, 500.0, -192.43025, -182.14774999999997)
surf109 = openmc.model.RectangularParallelepiped(-252.21025, -241.92774999999997, -500.0, 500.0, -192.43025, -182.14774999999997)
surf110 = openmc.model.RectangularParallelepiped(-241.61025, -231.32774999999998, -500.0, 500.0, -192.43025, -182.14774999999997)
surf111 = openmc.model.RectangularParallelepiped(-337.01025000000004, -326.72775, -500.0, 500.0, -181.83025, -171.54774999999998)
surf112 = openmc.model.RectangularParallelepiped(-326.41025, -316.12775, -500.0, 500.0, -181.83025, -171.54774999999998)
surf113 = openmc.model.RectangularParallelepiped(-315.81025, -305.52774999999997, -500.0, 500.0, -181.83025, -171.54774999999998)
surf114 = openmc.model.RectangularParallelepiped(-305.21025000000003, -294.92775, -500.0, 500.0, -181.83025, -171.54774999999998)
surf115 = openmc.model.RectangularParallelepiped(-294.61025, -284.32775, -500.0, 500.0, -181.83025, -171.54774999999998)
surf116 = openmc.model.RectangularParallelepiped(-284.01025000000004, -273.72775, -500.0, 500.0, -181.83025, -171.54774999999998)
surf117 = openmc.model.RectangularParallelepiped(-273.41025, -263.12775, -500.0, 500.0, -181.83025, -171.54774999999998)
surf118 = openmc.model.RectangularParallelepiped(-262.81025, -252.52774999999997, -500.0, 500.0, -181.83025, -171.54774999999998)
surf119 = openmc.model.RectangularParallelepiped(-252.21025, -241.92774999999997, -500.0, 500.0, -181.83025, -171.54774999999998)
surf120 = openmc.model.RectangularParallelepiped(-241.61025, -231.32774999999998, -500.0, 500.0, -181.83025, -171.54774999999998)
surf121 = openmc.model.RectangularParallelepiped(-337.01025000000004, -326.72775, -500.0, 500.0, -171.23025, -160.94774999999998)
surf122 = openmc.model.RectangularParallelepiped(-326.41025, -316.12775, -500.0, 500.0, -171.23025, -160.94774999999998)
surf123 = openmc.model.RectangularParallelepiped(-315.81025, -305.52774999999997, -500.0, 500.0, -171.23025, -160.94774999999998)
surf124 = openmc.model.RectangularParallelepiped(-305.21025000000003, -294.92775, -500.0, 500.0, -171.23025, -160.94774999999998)
surf125 = openmc.model.RectangularParallelepiped(-294.61025, -284.32775, -500.0, 500.0, -171.23025, -160.94774999999998)
surf126 = openmc.model.RectangularParallelepiped(-284.01025000000004, -273.72775, -500.0, 500.0, -171.23025, -160.94774999999998)
surf127 = openmc.model.RectangularParallelepiped(-273.41025, -263.12775, -500.0, 500.0, -171.23025, -160.94774999999998)
surf128 = openmc.model.RectangularParallelepiped(-262.81025, -252.52774999999997, -500.0, 500.0, -171.23025, -160.94774999999998)
surf129 = openmc.model.RectangularParallelepiped(-252.21025, -241.92774999999997, -500.0, 500.0, -171.23025, -160.94774999999998)
surf130 = openmc.model.RectangularParallelepiped(-241.61025, -231.32774999999998, -500.0, 500.0, -171.23025, -160.94774999999998)
surf131 = openmc.model.RectangularParallelepiped(-337.01025000000004, -326.72775, -500.0, 500.0, -160.63025000000002, -150.34775)
surf132 = openmc.model.RectangularParallelepiped(-326.41025, -316.12775, -500.0, 500.0, -160.63025000000002, -150.34775)
surf133 = openmc.model.RectangularParallelepiped(-315.81025, -305.52774999999997, -500.0, 500.0, -160.63025000000002, -150.34775)
surf134 = openmc.model.RectangularParallelepiped(-305.21025000000003, -294.92775, -500.0, 500.0, -160.63025000000002, -150.34775)
surf135 = openmc.model.RectangularParallelepiped(-294.61025, -284.32775, -500.0, 500.0, -160.63025000000002, -150.34775)
surf136 = openmc.model.RectangularParallelepiped(-284.01025000000004, -273.72775, -500.0, 500.0, -160.63025000000002, -150.34775)
surf137 = openmc.model.RectangularParallelepiped(-273.41025, -263.12775, -500.0, 500.0, -160.63025000000002, -150.34775)
surf138 = openmc.model.RectangularParallelepiped(-262.81025, -252.52774999999997, -500.0, 500.0, -160.63025000000002, -150.34775)
surf139 = openmc.model.RectangularParallelepiped(-252.21025, -241.92774999999997, -500.0, 500.0, -160.63025000000002, -150.34775)
surf140 = openmc.model.RectangularParallelepiped(-241.61025, -231.32774999999998, -500.0, 500.0, -160.63025000000002, -150.34775)
surf141 = openmc.model.RectangularParallelepiped(-337.01025000000004, -326.72775, -500.0, 500.0, -150.03025000000002, -139.74775)
surf142 = openmc.model.RectangularParallelepiped(-326.41025, -316.12775, -500.0, 500.0, -150.03025000000002, -139.74775)
surf143 = openmc.model.RectangularParallelepiped(-315.81025, -305.52774999999997, -500.0, 500.0, -150.03025000000002, -139.74775)
surf144 = openmc.model.RectangularParallelepiped(-305.21025000000003, -294.92775, -500.0, 500.0, -150.03025000000002, -139.74775)
surf145 = openmc.model.RectangularParallelepiped(-294.61025, -284.32775, -500.0, 500.0, -150.03025000000002, -139.74775)
surf146 = openmc.model.RectangularParallelepiped(-284.01025000000004, -273.72775, -500.0, 500.0, -150.03025000000002, -139.74775)
surf147 = openmc.model.RectangularParallelepiped(-273.41025, -263.12775, -500.0, 500.0, -150.03025000000002, -139.74775)
surf148 = openmc.model.RectangularParallelepiped(-262.81025, -252.52774999999997, -500.0, 500.0, -150.03025000000002, -139.74775)
surf149 = openmc.model.RectangularParallelepiped(-252.21025, -241.92774999999997, -500.0, 500.0, -150.03025000000002, -139.74775)
surf150 = openmc.model.RectangularParallelepiped(-241.61025, -231.32774999999998, -500.0, 500.0, -150.03025000000002, -139.74775)
surf151 = openmc.model.RectangularParallelepiped(-337.01025000000004, -326.72775, -500.0, 500.0, -139.43025, -129.14774999999997)
surf152 = openmc.model.RectangularParallelepiped(-326.41025, -316.12775, -500.0, 500.0, -139.43025, -129.14774999999997)
surf153 = openmc.model.RectangularParallelepiped(-315.81025, -305.52774999999997, -500.0, 500.0, -139.43025, -129.14774999999997)
surf154 = openmc.model.RectangularParallelepiped(-305.21025000000003, -294.92775, -500.0, 500.0, -139.43025, -129.14774999999997)
surf155 = openmc.model.RectangularParallelepiped(-294.61025, -284.32775, -500.0, 500.0, -139.43025, -129.14774999999997)
surf156 = openmc.model.RectangularParallelepiped(-284.01025000000004, -273.72775, -500.0, 500.0, -139.43025, -129.14774999999997)
surf157 = openmc.model.RectangularParallelepiped(-273.41025, -263.12775, -500.0, 500.0, -139.43025, -129.14774999999997)
surf158 = openmc.model.RectangularParallelepiped(-262.81025, -252.52774999999997, -500.0, 500.0, -139.43025, -129.14774999999997)
surf159 = openmc.model.RectangularParallelepiped(-252.21025, -241.92774999999997, -500.0, 500.0, -139.43025, -129.14774999999997)
surf160 = openmc.model.RectangularParallelepiped(-241.61025, -231.32774999999998, -500.0, 500.0, -139.43025, -129.14774999999997)
surf161 = openmc.model.RectangularParallelepiped(-337.01025000000004, -326.72775, -500.0, 500.0, -128.83025, -118.54775)
surf162 = openmc.model.RectangularParallelepiped(-326.41025, -316.12775, -500.0, 500.0, -128.83025, -118.54775)
surf163 = openmc.model.RectangularParallelepiped(-315.81025, -305.52774999999997, -500.0, 500.0, -128.83025, -118.54775)
surf164 = openmc.model.RectangularParallelepiped(-305.21025000000003, -294.92775, -500.0, 500.0, -128.83025, -118.54775)
surf165 = openmc.model.RectangularParallelepiped(-294.61025, -284.32775, -500.0, 500.0, -128.83025, -118.54775)
surf166 = openmc.model.RectangularParallelepiped(-284.01025000000004, -273.72775, -500.0, 500.0, -128.83025, -118.54775)
surf167 = openmc.model.RectangularParallelepiped(-273.41025, -263.12775, -500.0, 500.0, -128.83025, -118.54775)
surf168 = openmc.model.RectangularParallelepiped(-262.81025, -252.52774999999997, -500.0, 500.0, -128.83025, -118.54775)
surf169 = openmc.model.RectangularParallelepiped(-252.21025, -241.92774999999997, -500.0, 500.0, -128.83025, -118.54775)
surf170 = openmc.model.RectangularParallelepiped(-241.61025, -231.32774999999998, -500.0, 500.0, -128.83025, -118.54775)
surf171 = openmc.model.RectangularParallelepiped(-337.01025000000004, -326.72775, -500.0, 500.0, -118.23025, -107.94775)
surf172 = openmc.model.RectangularParallelepiped(-326.41025, -316.12775, -500.0, 500.0, -118.23025, -107.94775)
surf173 = openmc.model.RectangularParallelepiped(-315.81025, -305.52774999999997, -500.0, 500.0, -118.23025, -107.94775)
surf174 = openmc.model.RectangularParallelepiped(-305.21025000000003, -294.92775, -500.0, 500.0, -118.23025, -107.94775)
surf175 = openmc.model.RectangularParallelepiped(-294.61025, -284.32775, -500.0, 500.0, -118.23025, -107.94775)
surf176 = openmc.model.RectangularParallelepiped(-284.01025000000004, -273.72775, -500.0, 500.0, -118.23025, -107.94775)
surf177 = openmc.model.RectangularParallelepiped(-273.41025, -263.12775, -500.0, 500.0, -118.23025, -107.94775)
surf178 = openmc.model.RectangularParallelepiped(-262.81025, -252.52774999999997, -500.0, 500.0, -118.23025, -107.94775)
surf179 = openmc.model.RectangularParallelepiped(-252.21025, -241.92774999999997, -500.0, 500.0, -118.23025, -107.94775)
surf180 = openmc.model.RectangularParallelepiped(-241.61025, -231.32774999999998, -500.0, 500.0, -118.23025, -107.94775)
surf181 = openmc.model.RectangularParallelepiped(-337.01025000000004, -326.72775, -500.0, 500.0, -107.63025, -97.34775)
surf182 = openmc.model.RectangularParallelepiped(-326.41025, -316.12775, -500.0, 500.0, -107.63025, -97.34775)
surf183 = openmc.model.RectangularParallelepiped(-315.81025, -305.52774999999997, -500.0, 500.0, -107.63025, -97.34775)
surf184 = openmc.model.RectangularParallelepiped(-305.21025000000003, -294.92775, -500.0, 500.0, -107.63025, -97.34775)
surf185 = openmc.model.RectangularParallelepiped(-294.61025, -284.32775, -500.0, 500.0, -107.63025, -97.34775)
surf186 = openmc.model.RectangularParallelepiped(-284.01025000000004, -273.72775, -500.0, 500.0, -107.63025, -97.34775)
surf187 = openmc.model.RectangularParallelepiped(-273.41025, -263.12775, -500.0, 500.0, -107.63025, -97.34775)
surf188 = openmc.model.RectangularParallelepiped(-262.81025, -252.52774999999997, -500.0, 500.0, -107.63025, -97.34775)
surf189 = openmc.model.RectangularParallelepiped(-252.21025, -241.92774999999997, -500.0, 500.0, -107.63025, -97.34775)
surf190 = openmc.model.RectangularParallelepiped(-241.61025, -231.32774999999998, -500.0, 500.0, -107.63025, -97.34775)
surf191 = openmc.model.RectangularParallelepiped(-337.01025000000004, -326.72775, -500.0, 500.0, -97.03025, -86.74775)
surf192 = openmc.model.RectangularParallelepiped(-326.41025, -316.12775, -500.0, 500.0, -97.03025, -86.74775)
surf193 = openmc.model.RectangularParallelepiped(-315.81025, -305.52774999999997, -500.0, 500.0, -97.03025, -86.74775)
surf194 = openmc.model.RectangularParallelepiped(-305.21025000000003, -294.92775, -500.0, 500.0, -97.03025, -86.74775)
surf195 = openmc.model.RectangularParallelepiped(-294.61025, -284.32775, -500.0, 500.0, -97.03025, -86.74775)
surf196 = openmc.model.RectangularParallelepiped(-284.01025000000004, -273.72775, -500.0, 500.0, -97.03025, -86.74775)
surf197 = openmc.model.RectangularParallelepiped(-273.41025, -263.12775, -500.0, 500.0, -97.03025, -86.74775)
surf198 = openmc.model.RectangularParallelepiped(-262.81025, -252.52774999999997, -500.0, 500.0, -97.03025, -86.74775)
surf199 = openmc.model.RectangularParallelepiped(-252.21025, -241.92774999999997, -500.0, 500.0, -97.03025, -86.74775)
surf200 = openmc.model.RectangularParallelepiped(-241.61025, -231.32774999999998, -500.0, 500.0, -97.03025, -86.74775)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# Tank
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3 & -surf4

# Crate
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf3 & -surf4 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110

# Frame
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf5 & -surf6

# Hood
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf7 & -surf8

# Room
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf9 & -surf10

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
source.space = openmc.stats.Point((-284.0, 149.0, -153.5))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
