"""
PU-SOL-THERM-024 (Case 19) 5.742 kg Pu(80.45) at H/X = 457 with H/SQRT(A) = 0.306; 18.4 wt-% Pu-240
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 66.5 gPu/L
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 3.196400e-07)
mat1.add_nuclide("Pu239", 1.271800e-04)
mat1.add_nuclide("Pu240", 3.069600e-05)
mat1.add_nuclide("Pu241", 7.525700e-06)
mat1.add_nuclide("Pu242", 1.588300e-06)
mat1.add_nuclide("Am241", 4.651700e-07)
mat1.add_element("N", 2.091900e-03)
mat1.add_nuclide("O16", 3.637300e-02)
mat1.add_nuclide("H1", 6.161500e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS-304L
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

# Concrete per PUST026
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

# Plexiglas
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 5.678200e-02)
mat4.add_element("C", 3.548900e-02)
mat4.add_nuclide("O16", 1.419600e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Hc
surf1 = openmc.ZPlane(surface_id=1, z0=40.3377)
# Tank/Inner:  Width = Tc
surf2 = openmc.model.RectangularParallelepiped(-337.509, -230.82899999999998, 138.83700000000002, 158.903, -192.929, -86.249)
# Tank/Outer:  Width = Tc +  0.318
surf3 = openmc.model.RectangularParallelepiped(-337.959, -230.379, 138.678, 159.062, -193.379, -85.799)
# Plex/Outer:  Width = Tc +  5.398
surf4 = openmc.model.RectangularParallelepiped(-337.959, -230.379, 136.138, 161.602, -193.379, -85.799)
# Frame/Outer: Width = Tc + 23.178
surf5 = openmc.model.RectangularParallelepiped(-337.959, -230.379, 127.248, 170.49200000000002, -193.379, -85.799)
# U-Frame/Inner
surf6 = openmc.model.RectangularParallelepiped(-355.289, -213.04899999999998, 111.87, 180.45, -211.344, -67.834)
# U-Frame/Outer
surf7 = openmc.model.RectangularParallelepiped(-355.765, -212.57299999999998, 111.87, 180.45, -211.82, -67.834)
# Hood/Inner
surf8 = openmc.model.RectangularParallelepiped(-380.365, -103.113, 76.83500000000001, 319.405, -311.78499999999997, 144.145)
# Hood/Outer
surf9 = openmc.model.RectangularParallelepiped(-381.0, -102.47800000000001, 76.2, 320.04, -312.41999999999996, 144.78)
# Room/Inner
surf10 = openmc.model.RectangularParallelepiped(-533.4, 533.4, -563.88, 502.91999999999996, -312.42, 312.42)
# Room/Outer
surf11 = openmc.model.RectangularParallelepiped(-685.8, 685.8, -655.32, 655.32, -373.38, 373.38, boundary_type="vacuum")
# Square Holes
surf12 = openmc.model.RectangularParallelepiped(-5.14125, 5.14125, -500.0, 500.0, -5.14125, 5.14125)
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
cell2.region = +surf2 & -surf3 & -surf5

# Crate
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf3 & -surf5 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110

# Plex
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf3 & -surf4 & -surf101 & +surf4 & +surf3 & -surf4 & -surf102 & +surf4 & +surf3 & -surf4 & -surf103

# Plex
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf3 & -surf4 & -surf104 & +surf4 & +surf3 & -surf4 & -surf105 & +surf4 & +surf3 & -surf4 & -surf106

# Plex
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf3 & -surf4 & -surf107 & +surf4 & +surf3 & -surf4 & -surf108 & +surf4 & +surf3 & -surf4 & -surf109

# Plex
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf3 & -surf4 & -surf110

# Plex
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = +surf3 & -surf4 & -surf111 & +surf4 & +surf3 & -surf4 & -surf112 & +surf4 & +surf3 & -surf4 & -surf113

# Plex
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = +surf3 & -surf4 & -surf114 & +surf4 & +surf3 & -surf4 & -surf115 & +surf4 & +surf3 & -surf4 & -surf116

# Plex
cell10 = openmc.Cell(cell_id=10, fill=mat4)
cell10.region = +surf3 & -surf4 & -surf117 & +surf4 & +surf3 & -surf4 & -surf118 & +surf4 & +surf3 & -surf4 & -surf119

# Plex
cell11 = openmc.Cell(cell_id=11, fill=mat4)
cell11.region = +surf3 & -surf4 & -surf120

# Plex
cell12 = openmc.Cell(cell_id=12, fill=mat4)
cell12.region = +surf3 & -surf4 & -surf121 & +surf4 & +surf3 & -surf4 & -surf122 & +surf4 & +surf3 & -surf4 & -surf123

# Plex
cell13 = openmc.Cell(cell_id=13, fill=mat4)
cell13.region = +surf3 & -surf4 & -surf124 & +surf4 & +surf3 & -surf4 & -surf125 & +surf4 & +surf3 & -surf4 & -surf126

# Plex
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = +surf3 & -surf4 & -surf127 & +surf4 & +surf3 & -surf4 & -surf128 & +surf4 & +surf3 & -surf4 & -surf129

# Plex
cell15 = openmc.Cell(cell_id=15, fill=mat4)
cell15.region = +surf3 & -surf4 & -surf130

# Plex
cell16 = openmc.Cell(cell_id=16, fill=mat4)
cell16.region = +surf3 & -surf4 & -surf131 & +surf4 & +surf3 & -surf4 & -surf132 & +surf4 & +surf3 & -surf4 & -surf133

# Plex
cell17 = openmc.Cell(cell_id=17, fill=mat4)
cell17.region = +surf3 & -surf4 & -surf134 & +surf4 & +surf3 & -surf4 & -surf135 & +surf4 & +surf3 & -surf4 & -surf136

# Plex
cell18 = openmc.Cell(cell_id=18, fill=mat4)
cell18.region = +surf3 & -surf4 & -surf137 & +surf4 & +surf3 & -surf4 & -surf138 & +surf4 & +surf3 & -surf4 & -surf139

# Plex
cell19 = openmc.Cell(cell_id=19, fill=mat4)
cell19.region = +surf3 & -surf4 & -surf140

# Plex
cell20 = openmc.Cell(cell_id=20, fill=mat4)
cell20.region = +surf3 & -surf4 & -surf141 & +surf4 & +surf3 & -surf4 & -surf142 & +surf4 & +surf3 & -surf4 & -surf143

# Plex
cell21 = openmc.Cell(cell_id=21, fill=mat4)
cell21.region = +surf3 & -surf4 & -surf144 & +surf4 & +surf3 & -surf4 & -surf145 & +surf4 & +surf3 & -surf4 & -surf146

# Plex
cell22 = openmc.Cell(cell_id=22, fill=mat4)
cell22.region = +surf3 & -surf4 & -surf147 & +surf4 & +surf3 & -surf4 & -surf148 & +surf4 & +surf3 & -surf4 & -surf149

# Plex
cell23 = openmc.Cell(cell_id=23, fill=mat4)
cell23.region = +surf3 & -surf4 & -surf150

# Plex
cell24 = openmc.Cell(cell_id=24, fill=mat4)
cell24.region = +surf3 & -surf4 & -surf151 & +surf4 & +surf3 & -surf4 & -surf152 & +surf4 & +surf3 & -surf4 & -surf153

# Plex
cell25 = openmc.Cell(cell_id=25, fill=mat4)
cell25.region = +surf3 & -surf4 & -surf154 & +surf4 & +surf3 & -surf4 & -surf155 & +surf4 & +surf3 & -surf4 & -surf156

# Plex
cell26 = openmc.Cell(cell_id=26, fill=mat4)
cell26.region = +surf3 & -surf4 & -surf157 & +surf4 & +surf3 & -surf4 & -surf158 & +surf4 & +surf3 & -surf4 & -surf159

# Plex
cell27 = openmc.Cell(cell_id=27, fill=mat4)
cell27.region = +surf3 & -surf4 & -surf160

# Plex
cell28 = openmc.Cell(cell_id=28, fill=mat4)
cell28.region = +surf3 & -surf4 & -surf161 & +surf4 & +surf3 & -surf4 & -surf162 & +surf4 & +surf3 & -surf4 & -surf163

# Plex
cell29 = openmc.Cell(cell_id=29, fill=mat4)
cell29.region = +surf3 & -surf4 & -surf164 & +surf4 & +surf3 & -surf4 & -surf165 & +surf4 & +surf3 & -surf4 & -surf166

# Plex
cell30 = openmc.Cell(cell_id=30, fill=mat4)
cell30.region = +surf3 & -surf4 & -surf167 & +surf4 & +surf3 & -surf4 & -surf168 & +surf4 & +surf3 & -surf4 & -surf169

# Plex
cell31 = openmc.Cell(cell_id=31, fill=mat4)
cell31.region = +surf3 & -surf4 & -surf170

# Plex
cell32 = openmc.Cell(cell_id=32, fill=mat4)
cell32.region = +surf3 & -surf4 & -surf171 & +surf4 & +surf3 & -surf4 & -surf172 & +surf4 & +surf3 & -surf4 & -surf173

# Plex
cell33 = openmc.Cell(cell_id=33, fill=mat4)
cell33.region = +surf3 & -surf4 & -surf174 & +surf4 & +surf3 & -surf4 & -surf175 & +surf4 & +surf3 & -surf4 & -surf176

# Plex
cell34 = openmc.Cell(cell_id=34, fill=mat4)
cell34.region = +surf3 & -surf4 & -surf177 & +surf4 & +surf3 & -surf4 & -surf178 & +surf4 & +surf3 & -surf4 & -surf179

# Plex
cell35 = openmc.Cell(cell_id=35, fill=mat4)
cell35.region = +surf3 & -surf4 & -surf180

# Plex
cell36 = openmc.Cell(cell_id=36, fill=mat4)
cell36.region = +surf3 & -surf4 & -surf181 & +surf4 & +surf3 & -surf4 & -surf182 & +surf4 & +surf3 & -surf4 & -surf183

# Plex
cell37 = openmc.Cell(cell_id=37, fill=mat4)
cell37.region = +surf3 & -surf4 & -surf184 & +surf4 & +surf3 & -surf4 & -surf185 & +surf4 & +surf3 & -surf4 & -surf186

# Plex
cell38 = openmc.Cell(cell_id=38, fill=mat4)
cell38.region = +surf3 & -surf4 & -surf187 & +surf4 & +surf3 & -surf4 & -surf188 & +surf4 & +surf3 & -surf4 & -surf189

# Plex
cell39 = openmc.Cell(cell_id=39, fill=mat4)
cell39.region = +surf3 & -surf4 & -surf190

# Plex
cell40 = openmc.Cell(cell_id=40, fill=mat4)
cell40.region = +surf3 & -surf4 & -surf191 & +surf4 & +surf3 & -surf4 & -surf192 & +surf4 & +surf3 & -surf4 & -surf193

# Plex
cell41 = openmc.Cell(cell_id=41, fill=mat4)
cell41.region = +surf3 & -surf4 & -surf194 & +surf4 & +surf3 & -surf4 & -surf195 & +surf4 & +surf3 & -surf4 & -surf196

# Plex
cell42 = openmc.Cell(cell_id=42, fill=mat4)
cell42.region = +surf3 & -surf4 & -surf197 & +surf4 & +surf3 & -surf4 & -surf198 & +surf4 & +surf3 & -surf4 & -surf199

# Plex
cell43 = openmc.Cell(cell_id=43, fill=mat4)
cell43.region = +surf3 & -surf4 & -surf200

# Frame
cell44 = openmc.Cell(cell_id=44, fill=mat2)
cell44.region = +surf6 & -surf7

# Hood
cell45 = openmc.Cell(cell_id=45, fill=mat2)
cell45.region = +surf8 & -surf9

# Room
cell46 = openmc.Cell(cell_id=46, fill=mat3)
cell46.region = +surf10 & -surf11

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46])
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
source.space = openmc.stats.Point((-284.0, 149.0, -173.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
