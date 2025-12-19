"""
PU-SOL-THERM-025 (Case 33) 19.738 kg Pu(80.45) at H/X = 109 with H/SQRT(A) = 0.256; 18.4 wt-% Pu-240
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 240.8 gPu/L
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

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.669100e-02)
mat3.add_nuclide("O16", 3.334500e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Hc (Solution)
surf1 = openmc.ZPlane(surface_id=1, z0=43.840)
# Sol'n Tank/Inner: Width = Tc
surf2 = openmc.model.RectangularParallelepiped(-53.34, 53.34, -6.053, 11.472999999999999, 0.0, 106.68)
# Sol'n Tank/Outer: Width = Tc +  0.318
surf3 = openmc.model.RectangularParallelepiped(-53.656, 53.656, -6.212000000000001, 11.632000000000001, -0.3159999999999954, 106.99600000000001)
# Egg Crate /Outer: Width = Tc + 23.178
surf4 = openmc.model.RectangularParallelepiped(-53.656, 53.656, -17.642, 23.062, -0.3159999999999954, 106.99600000000001)
# Water Reflector Level
surf5 = openmc.ZPlane(surface_id=5, z0=106.680)
# Water Tank/Inner
surf6 = openmc.model.RectangularParallelepiped(-71.12, 71.12, -34.29, 34.29, -18.414999999999992, 125.095)
# Water Tank/Outer
surf7 = openmc.model.RectangularParallelepiped(-71.596, 71.596, -34.925, 34.925, -18.891, 125.095, boundary_type="vacuum")
# Square Holes
surf8 = openmc.model.RectangularParallelepiped(-5.14125, 5.14125, -500.0, 500.0, -5.14125, 5.14125)
surf101 = openmc.model.RectangularParallelepiped(-52.84125, -42.55875, -500.0, 500.0, 0.49874999999999936, 10.78125)
surf102 = openmc.model.RectangularParallelepiped(-42.24125, -31.958750000000002, -500.0, 500.0, 0.49874999999999936, 10.78125)
surf103 = openmc.model.RectangularParallelepiped(-31.64125, -21.35875, -500.0, 500.0, 0.49874999999999936, 10.78125)
surf104 = openmc.model.RectangularParallelepiped(-21.04125, -10.75875, -500.0, 500.0, 0.49874999999999936, 10.78125)
surf105 = openmc.model.RectangularParallelepiped(-10.44125, -0.1587499999999995, -500.0, 500.0, 0.49874999999999936, 10.78125)
surf106 = openmc.model.RectangularParallelepiped(0.1587499999999995, 10.44125, -500.0, 500.0, 0.49874999999999936, 10.78125)
surf107 = openmc.model.RectangularParallelepiped(10.75875, 21.04125, -500.0, 500.0, 0.49874999999999936, 10.78125)
surf108 = openmc.model.RectangularParallelepiped(21.35875, 31.64125, -500.0, 500.0, 0.49874999999999936, 10.78125)
surf109 = openmc.model.RectangularParallelepiped(31.958750000000002, 42.24125, -500.0, 500.0, 0.49874999999999936, 10.78125)
surf110 = openmc.model.RectangularParallelepiped(42.55875, 52.84125, -500.0, 500.0, 0.49874999999999936, 10.78125)
surf111 = openmc.model.RectangularParallelepiped(-52.84125, -42.55875, -500.0, 500.0, 11.098749999999999, 21.381249999999998)
surf112 = openmc.model.RectangularParallelepiped(-42.24125, -31.958750000000002, -500.0, 500.0, 11.098749999999999, 21.381249999999998)
surf113 = openmc.model.RectangularParallelepiped(-31.64125, -21.35875, -500.0, 500.0, 11.098749999999999, 21.381249999999998)
surf114 = openmc.model.RectangularParallelepiped(-21.04125, -10.75875, -500.0, 500.0, 11.098749999999999, 21.381249999999998)
surf115 = openmc.model.RectangularParallelepiped(-10.44125, -0.1587499999999995, -500.0, 500.0, 11.098749999999999, 21.381249999999998)
surf116 = openmc.model.RectangularParallelepiped(0.1587499999999995, 10.44125, -500.0, 500.0, 11.098749999999999, 21.381249999999998)
surf117 = openmc.model.RectangularParallelepiped(10.75875, 21.04125, -500.0, 500.0, 11.098749999999999, 21.381249999999998)
surf118 = openmc.model.RectangularParallelepiped(21.35875, 31.64125, -500.0, 500.0, 11.098749999999999, 21.381249999999998)
surf119 = openmc.model.RectangularParallelepiped(31.958750000000002, 42.24125, -500.0, 500.0, 11.098749999999999, 21.381249999999998)
surf120 = openmc.model.RectangularParallelepiped(42.55875, 52.84125, -500.0, 500.0, 11.098749999999999, 21.381249999999998)
surf121 = openmc.model.RectangularParallelepiped(-52.84125, -42.55875, -500.0, 500.0, 21.69875, 31.98125)
surf122 = openmc.model.RectangularParallelepiped(-42.24125, -31.958750000000002, -500.0, 500.0, 21.69875, 31.98125)
surf123 = openmc.model.RectangularParallelepiped(-31.64125, -21.35875, -500.0, 500.0, 21.69875, 31.98125)
surf124 = openmc.model.RectangularParallelepiped(-21.04125, -10.75875, -500.0, 500.0, 21.69875, 31.98125)
surf125 = openmc.model.RectangularParallelepiped(-10.44125, -0.1587499999999995, -500.0, 500.0, 21.69875, 31.98125)
surf126 = openmc.model.RectangularParallelepiped(0.1587499999999995, 10.44125, -500.0, 500.0, 21.69875, 31.98125)
surf127 = openmc.model.RectangularParallelepiped(10.75875, 21.04125, -500.0, 500.0, 21.69875, 31.98125)
surf128 = openmc.model.RectangularParallelepiped(21.35875, 31.64125, -500.0, 500.0, 21.69875, 31.98125)
surf129 = openmc.model.RectangularParallelepiped(31.958750000000002, 42.24125, -500.0, 500.0, 21.69875, 31.98125)
surf130 = openmc.model.RectangularParallelepiped(42.55875, 52.84125, -500.0, 500.0, 21.69875, 31.98125)
surf131 = openmc.model.RectangularParallelepiped(-52.84125, -42.55875, -500.0, 500.0, 32.29875, 42.58125)
surf132 = openmc.model.RectangularParallelepiped(-42.24125, -31.958750000000002, -500.0, 500.0, 32.29875, 42.58125)
surf133 = openmc.model.RectangularParallelepiped(-31.64125, -21.35875, -500.0, 500.0, 32.29875, 42.58125)
surf134 = openmc.model.RectangularParallelepiped(-21.04125, -10.75875, -500.0, 500.0, 32.29875, 42.58125)
surf135 = openmc.model.RectangularParallelepiped(-10.44125, -0.1587499999999995, -500.0, 500.0, 32.29875, 42.58125)
surf136 = openmc.model.RectangularParallelepiped(0.1587499999999995, 10.44125, -500.0, 500.0, 32.29875, 42.58125)
surf137 = openmc.model.RectangularParallelepiped(10.75875, 21.04125, -500.0, 500.0, 32.29875, 42.58125)
surf138 = openmc.model.RectangularParallelepiped(21.35875, 31.64125, -500.0, 500.0, 32.29875, 42.58125)
surf139 = openmc.model.RectangularParallelepiped(31.958750000000002, 42.24125, -500.0, 500.0, 32.29875, 42.58125)
surf140 = openmc.model.RectangularParallelepiped(42.55875, 52.84125, -500.0, 500.0, 32.29875, 42.58125)
surf141 = openmc.model.RectangularParallelepiped(-52.84125, -42.55875, -500.0, 500.0, 42.89875, 53.18125)
surf142 = openmc.model.RectangularParallelepiped(-42.24125, -31.958750000000002, -500.0, 500.0, 42.89875, 53.18125)
surf143 = openmc.model.RectangularParallelepiped(-31.64125, -21.35875, -500.0, 500.0, 42.89875, 53.18125)
surf144 = openmc.model.RectangularParallelepiped(-21.04125, -10.75875, -500.0, 500.0, 42.89875, 53.18125)
surf145 = openmc.model.RectangularParallelepiped(-10.44125, -0.1587499999999995, -500.0, 500.0, 42.89875, 53.18125)
surf146 = openmc.model.RectangularParallelepiped(0.1587499999999995, 10.44125, -500.0, 500.0, 42.89875, 53.18125)
surf147 = openmc.model.RectangularParallelepiped(10.75875, 21.04125, -500.0, 500.0, 42.89875, 53.18125)
surf148 = openmc.model.RectangularParallelepiped(21.35875, 31.64125, -500.0, 500.0, 42.89875, 53.18125)
surf149 = openmc.model.RectangularParallelepiped(31.958750000000002, 42.24125, -500.0, 500.0, 42.89875, 53.18125)
surf150 = openmc.model.RectangularParallelepiped(42.55875, 52.84125, -500.0, 500.0, 42.89875, 53.18125)
surf151 = openmc.model.RectangularParallelepiped(-52.84125, -42.55875, -500.0, 500.0, 53.49875, 63.78125)
surf152 = openmc.model.RectangularParallelepiped(-42.24125, -31.958750000000002, -500.0, 500.0, 53.49875, 63.78125)
surf153 = openmc.model.RectangularParallelepiped(-31.64125, -21.35875, -500.0, 500.0, 53.49875, 63.78125)
surf154 = openmc.model.RectangularParallelepiped(-21.04125, -10.75875, -500.0, 500.0, 53.49875, 63.78125)
surf155 = openmc.model.RectangularParallelepiped(-10.44125, -0.1587499999999995, -500.0, 500.0, 53.49875, 63.78125)
surf156 = openmc.model.RectangularParallelepiped(0.1587499999999995, 10.44125, -500.0, 500.0, 53.49875, 63.78125)
surf157 = openmc.model.RectangularParallelepiped(10.75875, 21.04125, -500.0, 500.0, 53.49875, 63.78125)
surf158 = openmc.model.RectangularParallelepiped(21.35875, 31.64125, -500.0, 500.0, 53.49875, 63.78125)
surf159 = openmc.model.RectangularParallelepiped(31.958750000000002, 42.24125, -500.0, 500.0, 53.49875, 63.78125)
surf160 = openmc.model.RectangularParallelepiped(42.55875, 52.84125, -500.0, 500.0, 53.49875, 63.78125)
surf161 = openmc.model.RectangularParallelepiped(-52.84125, -42.55875, -500.0, 500.0, 64.09875, 74.38125)
surf162 = openmc.model.RectangularParallelepiped(-42.24125, -31.958750000000002, -500.0, 500.0, 64.09875, 74.38125)
surf163 = openmc.model.RectangularParallelepiped(-31.64125, -21.35875, -500.0, 500.0, 64.09875, 74.38125)
surf164 = openmc.model.RectangularParallelepiped(-21.04125, -10.75875, -500.0, 500.0, 64.09875, 74.38125)
surf165 = openmc.model.RectangularParallelepiped(-10.44125, -0.1587499999999995, -500.0, 500.0, 64.09875, 74.38125)
surf166 = openmc.model.RectangularParallelepiped(0.1587499999999995, 10.44125, -500.0, 500.0, 64.09875, 74.38125)
surf167 = openmc.model.RectangularParallelepiped(10.75875, 21.04125, -500.0, 500.0, 64.09875, 74.38125)
surf168 = openmc.model.RectangularParallelepiped(21.35875, 31.64125, -500.0, 500.0, 64.09875, 74.38125)
surf169 = openmc.model.RectangularParallelepiped(31.958750000000002, 42.24125, -500.0, 500.0, 64.09875, 74.38125)
surf170 = openmc.model.RectangularParallelepiped(42.55875, 52.84125, -500.0, 500.0, 64.09875, 74.38125)
surf171 = openmc.model.RectangularParallelepiped(-52.84125, -42.55875, -500.0, 500.0, 74.69875, 84.98125)
surf172 = openmc.model.RectangularParallelepiped(-42.24125, -31.958750000000002, -500.0, 500.0, 74.69875, 84.98125)
surf173 = openmc.model.RectangularParallelepiped(-31.64125, -21.35875, -500.0, 500.0, 74.69875, 84.98125)
surf174 = openmc.model.RectangularParallelepiped(-21.04125, -10.75875, -500.0, 500.0, 74.69875, 84.98125)
surf175 = openmc.model.RectangularParallelepiped(-10.44125, -0.1587499999999995, -500.0, 500.0, 74.69875, 84.98125)
surf176 = openmc.model.RectangularParallelepiped(0.1587499999999995, 10.44125, -500.0, 500.0, 74.69875, 84.98125)
surf177 = openmc.model.RectangularParallelepiped(10.75875, 21.04125, -500.0, 500.0, 74.69875, 84.98125)
surf178 = openmc.model.RectangularParallelepiped(21.35875, 31.64125, -500.0, 500.0, 74.69875, 84.98125)
surf179 = openmc.model.RectangularParallelepiped(31.958750000000002, 42.24125, -500.0, 500.0, 74.69875, 84.98125)
surf180 = openmc.model.RectangularParallelepiped(42.55875, 52.84125, -500.0, 500.0, 74.69875, 84.98125)
surf181 = openmc.model.RectangularParallelepiped(-52.84125, -42.55875, -500.0, 500.0, 85.29875, 95.58125)
surf182 = openmc.model.RectangularParallelepiped(-42.24125, -31.958750000000002, -500.0, 500.0, 85.29875, 95.58125)
surf183 = openmc.model.RectangularParallelepiped(-31.64125, -21.35875, -500.0, 500.0, 85.29875, 95.58125)
surf184 = openmc.model.RectangularParallelepiped(-21.04125, -10.75875, -500.0, 500.0, 85.29875, 95.58125)
surf185 = openmc.model.RectangularParallelepiped(-10.44125, -0.1587499999999995, -500.0, 500.0, 85.29875, 95.58125)
surf186 = openmc.model.RectangularParallelepiped(0.1587499999999995, 10.44125, -500.0, 500.0, 85.29875, 95.58125)
surf187 = openmc.model.RectangularParallelepiped(10.75875, 21.04125, -500.0, 500.0, 85.29875, 95.58125)
surf188 = openmc.model.RectangularParallelepiped(21.35875, 31.64125, -500.0, 500.0, 85.29875, 95.58125)
surf189 = openmc.model.RectangularParallelepiped(31.958750000000002, 42.24125, -500.0, 500.0, 85.29875, 95.58125)
surf190 = openmc.model.RectangularParallelepiped(42.55875, 52.84125, -500.0, 500.0, 85.29875, 95.58125)
surf191 = openmc.model.RectangularParallelepiped(-52.84125, -42.55875, -500.0, 500.0, 95.89875, 106.18125)
surf192 = openmc.model.RectangularParallelepiped(-42.24125, -31.958750000000002, -500.0, 500.0, 95.89875, 106.18125)
surf193 = openmc.model.RectangularParallelepiped(-31.64125, -21.35875, -500.0, 500.0, 95.89875, 106.18125)
surf194 = openmc.model.RectangularParallelepiped(-21.04125, -10.75875, -500.0, 500.0, 95.89875, 106.18125)
surf195 = openmc.model.RectangularParallelepiped(-10.44125, -0.1587499999999995, -500.0, 500.0, 95.89875, 106.18125)
surf196 = openmc.model.RectangularParallelepiped(0.1587499999999995, 10.44125, -500.0, 500.0, 95.89875, 106.18125)
surf197 = openmc.model.RectangularParallelepiped(10.75875, 21.04125, -500.0, 500.0, 95.89875, 106.18125)
surf198 = openmc.model.RectangularParallelepiped(21.35875, 31.64125, -500.0, 500.0, 95.89875, 106.18125)
surf199 = openmc.model.RectangularParallelepiped(31.958750000000002, 42.24125, -500.0, 500.0, 95.89875, 106.18125)
surf200 = openmc.model.RectangularParallelepiped(42.55875, 52.84125, -500.0, 500.0, 95.89875, 106.18125)

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

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf3 & -surf4 & -surf101 & +surf3 & +surf3 & -surf4 & -surf102 & +surf3 & +surf3 & -surf4 & -surf103

# Water
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf3 & -surf4 & -surf104 & +surf3 & +surf3 & -surf4 & -surf105 & +surf3 & +surf3 & -surf4 & -surf106

# Water
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf3 & -surf4 & -surf107 & +surf3 & +surf3 & -surf4 & -surf108 & +surf3 & +surf3 & -surf4 & -surf109

# Water
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf3 & -surf4 & -surf110

# Water
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf3 & -surf4 & -surf111 & +surf3 & +surf3 & -surf4 & -surf112 & +surf3 & +surf3 & -surf4 & -surf113

# Water
cell9 = openmc.Cell(cell_id=9, fill=mat3)
cell9.region = +surf3 & -surf4 & -surf114 & +surf3 & +surf3 & -surf4 & -surf115 & +surf3 & +surf3 & -surf4 & -surf116

# Water
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = +surf3 & -surf4 & -surf117 & +surf3 & +surf3 & -surf4 & -surf118 & +surf3 & +surf3 & -surf4 & -surf119

# Water
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = +surf3 & -surf4 & -surf120

# Water
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = +surf3 & -surf4 & -surf121 & +surf3 & +surf3 & -surf4 & -surf122 & +surf3 & +surf3 & -surf4 & -surf123

# Water
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = +surf3 & -surf4 & -surf124 & +surf3 & +surf3 & -surf4 & -surf125 & +surf3 & +surf3 & -surf4 & -surf126

# Water
cell14 = openmc.Cell(cell_id=14, fill=mat3)
cell14.region = +surf3 & -surf4 & -surf127 & +surf3 & +surf3 & -surf4 & -surf128 & +surf3 & +surf3 & -surf4 & -surf129

# Water
cell15 = openmc.Cell(cell_id=15, fill=mat3)
cell15.region = +surf3 & -surf4 & -surf130

# Water
cell16 = openmc.Cell(cell_id=16, fill=mat3)
cell16.region = +surf3 & -surf4 & -surf131 & +surf3 & +surf3 & -surf4 & -surf132 & +surf3 & +surf3 & -surf4 & -surf133

# Water
cell17 = openmc.Cell(cell_id=17, fill=mat3)
cell17.region = +surf3 & -surf4 & -surf134 & +surf3 & +surf3 & -surf4 & -surf135 & +surf3 & +surf3 & -surf4 & -surf136

# Water
cell18 = openmc.Cell(cell_id=18, fill=mat3)
cell18.region = +surf3 & -surf4 & -surf137 & +surf3 & +surf3 & -surf4 & -surf138 & +surf3 & +surf3 & -surf4 & -surf139

# Water
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = +surf3 & -surf4 & -surf140

# Water
cell20 = openmc.Cell(cell_id=20, fill=mat3)
cell20.region = +surf3 & -surf4 & -surf141 & +surf3 & +surf3 & -surf4 & -surf142 & +surf3 & +surf3 & -surf4 & -surf143

# Water
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = +surf3 & -surf4 & -surf144 & +surf3 & +surf3 & -surf4 & -surf145 & +surf3 & +surf3 & -surf4 & -surf146

# Water
cell22 = openmc.Cell(cell_id=22, fill=mat3)
cell22.region = +surf3 & -surf4 & -surf147 & +surf3 & +surf3 & -surf4 & -surf148 & +surf3 & +surf3 & -surf4 & -surf149

# Water
cell23 = openmc.Cell(cell_id=23, fill=mat3)
cell23.region = +surf3 & -surf4 & -surf150

# Water
cell24 = openmc.Cell(cell_id=24, fill=mat3)
cell24.region = +surf3 & -surf4 & -surf151 & +surf3 & +surf3 & -surf4 & -surf152 & +surf3 & +surf3 & -surf4 & -surf153

# Water
cell25 = openmc.Cell(cell_id=25, fill=mat3)
cell25.region = +surf3 & -surf4 & -surf154 & +surf3 & +surf3 & -surf4 & -surf155 & +surf3 & +surf3 & -surf4 & -surf156

# Water
cell26 = openmc.Cell(cell_id=26, fill=mat3)
cell26.region = +surf3 & -surf4 & -surf157 & +surf3 & +surf3 & -surf4 & -surf158 & +surf3 & +surf3 & -surf4 & -surf159

# Water
cell27 = openmc.Cell(cell_id=27, fill=mat3)
cell27.region = +surf3 & -surf4 & -surf160

# Water
cell28 = openmc.Cell(cell_id=28, fill=mat3)
cell28.region = +surf3 & -surf4 & -surf161 & +surf3 & +surf3 & -surf4 & -surf162 & +surf3 & +surf3 & -surf4 & -surf163

# Water
cell29 = openmc.Cell(cell_id=29, fill=mat3)
cell29.region = +surf3 & -surf4 & -surf164 & +surf3 & +surf3 & -surf4 & -surf165 & +surf3 & +surf3 & -surf4 & -surf166

# Water
cell30 = openmc.Cell(cell_id=30, fill=mat3)
cell30.region = +surf3 & -surf4 & -surf167 & +surf3 & +surf3 & -surf4 & -surf168 & +surf3 & +surf3 & -surf4 & -surf169

# Water
cell31 = openmc.Cell(cell_id=31, fill=mat3)
cell31.region = +surf3 & -surf4 & -surf170

# Water
cell32 = openmc.Cell(cell_id=32, fill=mat3)
cell32.region = +surf3 & -surf4 & -surf171 & +surf3 & +surf3 & -surf4 & -surf172 & +surf3 & +surf3 & -surf4 & -surf173

# Water
cell33 = openmc.Cell(cell_id=33, fill=mat3)
cell33.region = +surf3 & -surf4 & -surf174 & +surf3 & +surf3 & -surf4 & -surf175 & +surf3 & +surf3 & -surf4 & -surf176

# Water
cell34 = openmc.Cell(cell_id=34, fill=mat3)
cell34.region = +surf3 & -surf4 & -surf177 & +surf3 & +surf3 & -surf4 & -surf178 & +surf3 & +surf3 & -surf4 & -surf179

# Water
cell35 = openmc.Cell(cell_id=35, fill=mat3)
cell35.region = +surf3 & -surf4 & -surf180

# Water
cell36 = openmc.Cell(cell_id=36, fill=mat3)
cell36.region = +surf3 & -surf4 & -surf181 & +surf3 & +surf3 & -surf4 & -surf182 & +surf3 & +surf3 & -surf4 & -surf183

# Water
cell37 = openmc.Cell(cell_id=37, fill=mat3)
cell37.region = +surf3 & -surf4 & -surf184 & +surf3 & +surf3 & -surf4 & -surf185 & +surf3 & +surf3 & -surf4 & -surf186

# Water
cell38 = openmc.Cell(cell_id=38, fill=mat3)
cell38.region = +surf3 & -surf4 & -surf187 & +surf3 & +surf3 & -surf4 & -surf188 & +surf3 & +surf3 & -surf4 & -surf189

# Water
cell39 = openmc.Cell(cell_id=39, fill=mat3)
cell39.region = +surf3 & -surf4 & -surf190

# Water
cell40 = openmc.Cell(cell_id=40, fill=mat3)
cell40.region = +surf3 & -surf4 & -surf191 & +surf3 & +surf3 & -surf4 & -surf192 & +surf3 & +surf3 & -surf4 & -surf193

# Water
cell41 = openmc.Cell(cell_id=41, fill=mat3)
cell41.region = +surf3 & -surf4 & -surf194 & +surf3 & +surf3 & -surf4 & -surf195 & +surf3 & +surf3 & -surf4 & -surf196

# Water
cell42 = openmc.Cell(cell_id=42, fill=mat3)
cell42.region = +surf3 & -surf4 & -surf197 & +surf3 & +surf3 & -surf4 & -surf198 & +surf3 & +surf3 & -surf4 & -surf199

# Water
cell43 = openmc.Cell(cell_id=43, fill=mat3)
cell43.region = +surf3 & -surf4 & -surf200

# Water
cell44 = openmc.Cell(cell_id=44, fill=mat3)
cell44.region = +surf3 & +surf4 & -surf5 & -surf6

# Tank
cell45 = openmc.Cell(cell_id=45, fill=mat2)
cell45.region = +surf6 & -surf7

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45])
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
source.space = openmc.stats.Point((0.0, 2.71, 21.9))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
