"""
LCT022-1: 1,969 U(10)O2 rods with 0.7 cm hexagonal pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(10)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.763600e-05)
mat1.add_nuclide("U235", 2.157700e-03)
mat1.add_nuclide("U236", 1.530000e-05)
mat1.add_nuclide("U238", 1.951000e-02)
mat1.add_nuclide("O16", 4.466100e-02)

# SST
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.889400e-02)
mat2.add_element("Cr", 1.646900e-02)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Si", 1.355100e-03)
mat2.add_element("Mn", 1.299000e-03)
mat2.add_element("C", 2.376600e-04)
mat2.add_element("Ti", 4.471300e-04)

# Al-alloy
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 1.498900e-04)
mat3.add_element("Si", 2.980400e-04)
mat3.add_element("Cu", 1.146000e-03)
mat3.add_element("Al", 5.711500e-02)
mat3.add_element("Mg", 1.033200e-03)
mat3.add_element("Mn", 1.828400e-04)
mat3.add_element("Ti", 3.496500e-05)
mat3.add_element("Zn", 7.680700e-05)
mat3.add_element("Ni", 2.852500e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.673600e-02)
mat4.add_nuclide("O16", 3.336800e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Void
surf1 = openmc.ZCylinder(surface_id=1, r=0.1)
# Clad - lower
surf2 = openmc.ZCylinder(surface_id=2, r=0.2)
# Clad - lower
surf3 = openmc.ZCylinder(surface_id=3, r=0.255)
# Fuel
surf4 = openmc.ZCylinder(surface_id=4, r=0.208)
# Void
surf5 = openmc.ZCylinder(surface_id=5, r=0.215)
# Void
surf6 = openmc.ZCylinder(surface_id=6, r=0.1)
# Clad - middle
surf7 = openmc.ZCylinder(surface_id=7, r=0.255)
# Clad - top
surf8 = openmc.ZCylinder(surface_id=8, r=0.187)
# Support plate
surf10 = openmc.ZCylinder(surface_id=10, r=99.9)
# Lattice plate hole - 1
surf11 = openmc.ZCylinder(surface_id=11, r=0.26)
# Lattice plate hole - 2
surf12 = openmc.ZCylinder(surface_id=12, x0=-0.35, y0=0.606218, r=0.26)
# Lattice plate hole - 3
surf13 = openmc.ZCylinder(surface_id=13, x0=-0.35, y0=-0.606218, r=0.26)
# Lattice plate hole - 4
surf14 = openmc.ZCylinder(surface_id=14, x0=0.35, y0=0.606218, r=0.26)
# Lattice plate hole - 5
surf15 = openmc.ZCylinder(surface_id=15, x0=0.35, y0=-0.606218, r=0.26)
# Lattice plate - lower
surf16 = openmc.ZCylinder(surface_id=16, r=99.9)
# Lattice plate - upper
surf17 = openmc.ZCylinder(surface_id=17, r=99.9)
surf21 = openmc.ZCylinder(surface_id=21, x0=-4.9, y0=15.761662, r=0.26)
surf22 = openmc.ZCylinder(surface_id=22, x0=4.9, y0=15.761662, r=0.26)
surf23 = openmc.ZCylinder(surface_id=23, x0=4.9, y0=-15.761662, r=0.26)
surf24 = openmc.ZCylinder(surface_id=24, x0=-4.9, y0=-15.761662, r=0.26)
surf25 = openmc.ZCylinder(surface_id=25, x0=-11.2, y0=12.124356, r=0.26)
surf26 = openmc.ZCylinder(surface_id=26, x0=11.2, y0=12.124356, r=0.26)
surf27 = openmc.ZCylinder(surface_id=27, x0=11.2, y0=-12.124356, r=0.26)
surf28 = openmc.ZCylinder(surface_id=28, x0=-11.2, y0=-12.124356, r=0.26)
surf29 = openmc.ZCylinder(surface_id=29, x0=-16.1, y0=3.639307, r=0.26)
surf30 = openmc.ZCylinder(surface_id=30, x0=16.1, y0=3.639307, r=0.26)
surf31 = openmc.ZCylinder(surface_id=31, x0=16.1, y0=-3.639307, r=0.26)
surf32 = openmc.ZCylinder(surface_id=32, x0=-16.1, y0=-3.639307, r=0.26)
# Prism 91: 12-sided polygon
surf91_0 = openmc.Plane(a=0.4999999577, b=-0.8660254282, c=0, d=16.4500000933)
surf91_1 = openmc.Plane(a=0.8660253990, b=-0.5000000083, c=0, d=16.3678803486)
surf91_2 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=16.4500000000)
surf91_3 = openmc.Plane(a=0.8660253990, b=0.5000000083, c=0, d=16.3678803486)
surf91_4 = openmc.Plane(a=0.4999999577, b=0.8660254282, c=0, d=16.4500000933)
surf91_5 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=16.3678800000)
surf91_6 = openmc.Plane(a=-0.4999999577, b=0.8660254282, c=0, d=16.4500000933)
surf91_7 = openmc.Plane(a=-0.8660253715, b=0.5000000559, c=0, d=16.3678805986)
surf91_8 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=16.4500000000)
surf91_9 = openmc.Plane(a=-0.8660253715, b=-0.5000000559, c=0, d=16.3678805986)
surf91_10 = openmc.Plane(a=-0.4999999577, b=-0.8660254282, c=0, d=16.4500000933)
surf91_11 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=16.3678800000)
# Boundary condition
surf99 = openmc.ZCylinder(surface_id=99, r=46.8)
surf101 = openmc.ZCylinder(surface_id=101, x0=-4.55, y0=16.367886, r=0.26)
surf102 = openmc.ZCylinder(surface_id=102, x0=-3.85, y0=16.367886, r=0.26)
surf103 = openmc.ZCylinder(surface_id=103, x0=-3.15, y0=16.367886, r=0.26)
surf104 = openmc.ZCylinder(surface_id=104, x0=-2.45, y0=16.367886, r=0.26)
surf105 = openmc.ZCylinder(surface_id=105, x0=-1.75, y0=16.367886, r=0.26)
surf106 = openmc.ZCylinder(surface_id=106, x0=-1.05, y0=16.367886, r=0.26)
surf107 = openmc.ZCylinder(surface_id=107, x0=-0.35, y0=16.367886, r=0.26)
surf108 = openmc.ZCylinder(surface_id=108, x0=0.35, y0=16.367886, r=0.26)
surf109 = openmc.ZCylinder(surface_id=109, x0=1.05, y0=16.367886, r=0.26)
surf110 = openmc.ZCylinder(surface_id=110, x0=1.75, y0=16.367886, r=0.26)
surf111 = openmc.ZCylinder(surface_id=111, x0=2.45, y0=16.367886, r=0.26)
surf112 = openmc.ZCylinder(surface_id=112, x0=3.15, y0=16.367886, r=0.26)
surf113 = openmc.ZCylinder(surface_id=113, x0=3.85, y0=16.367886, r=0.26)
surf114 = openmc.ZCylinder(surface_id=114, x0=4.55, y0=16.367886, r=0.26)
surf115 = openmc.ZCylinder(surface_id=115, x0=-5.6, y0=15.761668, r=0.26)
surf116 = openmc.ZCylinder(surface_id=116, x0=5.6, y0=15.761668, r=0.26)
surf117 = openmc.ZCylinder(surface_id=117, x0=-6.65, y0=15.155445, r=0.26)
surf118 = openmc.ZCylinder(surface_id=118, x0=6.65, y0=15.155445, r=0.26)
surf119 = openmc.ZCylinder(surface_id=119, x0=-7.7, y0=14.549232, r=0.26)
surf120 = openmc.ZCylinder(surface_id=120, x0=7.7, y0=14.549232, r=0.26)
surf121 = openmc.ZCylinder(surface_id=121, x0=-8.75, y0=13.943014, r=0.26)
surf122 = openmc.ZCylinder(surface_id=122, x0=8.75, y0=13.943014, r=0.26)
surf123 = openmc.ZCylinder(surface_id=123, x0=-9.8, y0=13.336796, r=0.26)
surf124 = openmc.ZCylinder(surface_id=124, x0=9.8, y0=13.336796, r=0.26)
surf125 = openmc.ZCylinder(surface_id=125, x0=-10.85, y0=12.730578, r=0.26)
surf126 = openmc.ZCylinder(surface_id=126, x0=10.85, y0=12.730578, r=0.26)
surf127 = openmc.ZCylinder(surface_id=127, x0=-11.9, y0=12.12436, r=0.26)
surf128 = openmc.ZCylinder(surface_id=128, x0=11.9, y0=12.12436, r=0.26)
surf129 = openmc.ZCylinder(surface_id=129, x0=-12.25, y0=11.518142, r=0.26)
surf130 = openmc.ZCylinder(surface_id=130, x0=12.25, y0=11.518142, r=0.26)
surf131 = openmc.ZCylinder(surface_id=131, x0=-12.6, y0=10.911924, r=0.26)
surf132 = openmc.ZCylinder(surface_id=132, x0=12.6, y0=10.911924, r=0.26)
surf133 = openmc.ZCylinder(surface_id=133, x0=-12.95, y0=10.305706, r=0.26)
surf134 = openmc.ZCylinder(surface_id=134, x0=12.95, y0=10.305706, r=0.26)
surf135 = openmc.ZCylinder(surface_id=135, x0=-13.3, y0=9.699488, r=0.26)
surf136 = openmc.ZCylinder(surface_id=136, x0=13.3, y0=9.699488, r=0.26)
surf137 = openmc.ZCylinder(surface_id=137, x0=-13.65, y0=9.09327, r=0.26)
surf138 = openmc.ZCylinder(surface_id=138, x0=13.65, y0=9.09327, r=0.26)
surf139 = openmc.ZCylinder(surface_id=139, x0=-14.0, y0=8.487052, r=0.26)
surf140 = openmc.ZCylinder(surface_id=140, x0=14.0, y0=8.487052, r=0.26)
surf141 = openmc.ZCylinder(surface_id=141, x0=-14.35, y0=7.880834, r=0.26)
surf142 = openmc.ZCylinder(surface_id=142, x0=14.35, y0=7.880834, r=0.26)
surf143 = openmc.ZCylinder(surface_id=143, x0=-14.7, y0=7.274616, r=0.26)
surf144 = openmc.ZCylinder(surface_id=144, x0=14.7, y0=7.274616, r=0.26)
surf145 = openmc.ZCylinder(surface_id=145, x0=-15.05, y0=6.668398, r=0.26)
surf146 = openmc.ZCylinder(surface_id=146, x0=15.05, y0=6.668398, r=0.26)
surf147 = openmc.ZCylinder(surface_id=147, x0=-15.4, y0=6.06218, r=0.26)
surf148 = openmc.ZCylinder(surface_id=148, x0=15.4, y0=6.06218, r=0.26)
surf149 = openmc.ZCylinder(surface_id=149, x0=-15.75, y0=5.455962, r=0.26)
surf150 = openmc.ZCylinder(surface_id=150, x0=15.75, y0=5.455962, r=0.26)
surf151 = openmc.ZCylinder(surface_id=151, x0=-16.1, y0=4.849744, r=0.26)
surf152 = openmc.ZCylinder(surface_id=152, x0=16.1, y0=4.849744, r=0.26)
surf153 = openmc.ZCylinder(surface_id=153, x0=-16.45, y0=4.243526, r=0.26)
surf154 = openmc.ZCylinder(surface_id=154, x0=16.45, y0=4.243526, r=0.26)
surf155 = openmc.ZCylinder(surface_id=155, x0=-16.45, y0=3.03109, r=0.26)
surf156 = openmc.ZCylinder(surface_id=156, x0=16.45, y0=3.03109, r=0.26)
surf157 = openmc.ZCylinder(surface_id=157, x0=-16.45, y0=1.818654, r=0.26)
surf158 = openmc.ZCylinder(surface_id=158, x0=16.45, y0=1.818654, r=0.26)
surf159 = openmc.ZCylinder(surface_id=159, x0=-16.45, y0=0.606218, r=0.26)
surf160 = openmc.ZCylinder(surface_id=160, x0=16.45, y0=0.606218, r=0.26)
surf201 = openmc.ZCylinder(surface_id=201, x0=-4.55, y0=-16.367886, r=0.26)
surf202 = openmc.ZCylinder(surface_id=202, x0=-3.85, y0=-16.367886, r=0.26)
surf203 = openmc.ZCylinder(surface_id=203, x0=-3.15, y0=-16.367886, r=0.26)
surf204 = openmc.ZCylinder(surface_id=204, x0=-2.45, y0=-16.367886, r=0.26)
surf205 = openmc.ZCylinder(surface_id=205, x0=-1.75, y0=-16.367886, r=0.26)
surf206 = openmc.ZCylinder(surface_id=206, x0=-1.05, y0=-16.367886, r=0.26)
surf207 = openmc.ZCylinder(surface_id=207, x0=-0.35, y0=-16.367886, r=0.26)
surf208 = openmc.ZCylinder(surface_id=208, x0=0.35, y0=-16.367886, r=0.26)
surf209 = openmc.ZCylinder(surface_id=209, x0=1.05, y0=-16.367886, r=0.26)
surf210 = openmc.ZCylinder(surface_id=210, x0=1.75, y0=-16.367886, r=0.26)
surf211 = openmc.ZCylinder(surface_id=211, x0=2.45, y0=-16.367886, r=0.26)
surf212 = openmc.ZCylinder(surface_id=212, x0=3.15, y0=-16.367886, r=0.26)
surf213 = openmc.ZCylinder(surface_id=213, x0=3.85, y0=-16.367886, r=0.26)
surf214 = openmc.ZCylinder(surface_id=214, x0=4.55, y0=-16.367886, r=0.26)
surf215 = openmc.ZCylinder(surface_id=215, x0=-5.6, y0=-15.761668, r=0.26)
surf216 = openmc.ZCylinder(surface_id=216, x0=5.6, y0=-15.761668, r=0.26)
surf217 = openmc.ZCylinder(surface_id=217, x0=-6.65, y0=-15.155445, r=0.26)
surf218 = openmc.ZCylinder(surface_id=218, x0=6.65, y0=-15.155445, r=0.26)
surf219 = openmc.ZCylinder(surface_id=219, x0=-7.7, y0=-14.549232, r=0.26)
surf220 = openmc.ZCylinder(surface_id=220, x0=7.7, y0=-14.549232, r=0.26)
surf221 = openmc.ZCylinder(surface_id=221, x0=-8.75, y0=-13.943014, r=0.26)
surf222 = openmc.ZCylinder(surface_id=222, x0=8.75, y0=-13.943014, r=0.26)
surf223 = openmc.ZCylinder(surface_id=223, x0=-9.8, y0=-13.336796, r=0.26)
surf224 = openmc.ZCylinder(surface_id=224, x0=9.8, y0=-13.336796, r=0.26)
surf225 = openmc.ZCylinder(surface_id=225, x0=-10.85, y0=-12.730578, r=0.26)
surf226 = openmc.ZCylinder(surface_id=226, x0=10.85, y0=-12.730578, r=0.26)
surf227 = openmc.ZCylinder(surface_id=227, x0=-11.9, y0=-12.12436, r=0.26)
surf228 = openmc.ZCylinder(surface_id=228, x0=11.9, y0=-12.12436, r=0.26)
surf229 = openmc.ZCylinder(surface_id=229, x0=-12.25, y0=-11.518142, r=0.26)
surf230 = openmc.ZCylinder(surface_id=230, x0=12.25, y0=-11.518142, r=0.26)
surf231 = openmc.ZCylinder(surface_id=231, x0=-12.6, y0=-10.911924, r=0.26)
surf232 = openmc.ZCylinder(surface_id=232, x0=12.6, y0=-10.911924, r=0.26)
surf233 = openmc.ZCylinder(surface_id=233, x0=-12.95, y0=-10.305706, r=0.26)
surf234 = openmc.ZCylinder(surface_id=234, x0=12.95, y0=-10.305706, r=0.26)
surf235 = openmc.ZCylinder(surface_id=235, x0=-13.3, y0=-9.699488, r=0.26)
surf236 = openmc.ZCylinder(surface_id=236, x0=13.3, y0=-9.699488, r=0.26)
surf237 = openmc.ZCylinder(surface_id=237, x0=-13.65, y0=-9.09327, r=0.26)
surf238 = openmc.ZCylinder(surface_id=238, x0=13.65, y0=-9.09327, r=0.26)
surf239 = openmc.ZCylinder(surface_id=239, x0=-14.0, y0=-8.487052, r=0.26)
surf240 = openmc.ZCylinder(surface_id=240, x0=14.0, y0=-8.487052, r=0.26)
surf241 = openmc.ZCylinder(surface_id=241, x0=-14.35, y0=-7.880834, r=0.26)
surf242 = openmc.ZCylinder(surface_id=242, x0=14.35, y0=-7.880834, r=0.26)
surf243 = openmc.ZCylinder(surface_id=243, x0=-14.7, y0=-7.274616, r=0.26)
surf244 = openmc.ZCylinder(surface_id=244, x0=14.7, y0=-7.274616, r=0.26)
surf245 = openmc.ZCylinder(surface_id=245, x0=-15.05, y0=-6.668398, r=0.26)
surf246 = openmc.ZCylinder(surface_id=246, x0=15.05, y0=-6.668398, r=0.26)
surf247 = openmc.ZCylinder(surface_id=247, x0=-15.4, y0=-6.06218, r=0.26)
surf248 = openmc.ZCylinder(surface_id=248, x0=15.4, y0=-6.06218, r=0.26)
surf249 = openmc.ZCylinder(surface_id=249, x0=-15.75, y0=-5.455962, r=0.26)
surf250 = openmc.ZCylinder(surface_id=250, x0=15.75, y0=-5.455962, r=0.26)
surf251 = openmc.ZCylinder(surface_id=251, x0=-16.1, y0=-4.849744, r=0.26)
surf252 = openmc.ZCylinder(surface_id=252, x0=16.1, y0=-4.849744, r=0.26)
surf253 = openmc.ZCylinder(surface_id=253, x0=-16.45, y0=-4.243526, r=0.26)
surf254 = openmc.ZCylinder(surface_id=254, x0=16.45, y0=-4.243526, r=0.26)
surf255 = openmc.ZCylinder(surface_id=255, x0=-16.45, y0=-3.03109, r=0.26)
surf256 = openmc.ZCylinder(surface_id=256, x0=16.45, y0=-3.03109, r=0.26)
surf257 = openmc.ZCylinder(surface_id=257, x0=-16.45, y0=-1.818654, r=0.26)
surf258 = openmc.ZCylinder(surface_id=258, x0=16.45, y0=-1.818654, r=0.26)
surf259 = openmc.ZCylinder(surface_id=259, x0=-16.45, y0=-0.606218, r=0.26)
surf260 = openmc.ZCylinder(surface_id=260, x0=16.45, y0=-0.606218, r=0.26)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=-0.8)
surf1_zmax = openmc.ZPlane(z0=0.0)
surf2_zmin = openmc.ZPlane(z0=-1.1)
surf2_zmax = openmc.ZPlane(z0=-0.1)
surf3_zmin = openmc.ZPlane(z0=-0.1)
surf3_zmax = openmc.ZPlane(z0=0.0)
surf4_zmin = openmc.ZPlane(z0=0.0)
surf4_zmax = openmc.ZPlane(z0=85.6)
surf5_zmin = openmc.ZPlane(z0=0.0)
surf5_zmax = openmc.ZPlane(z0=85.9)
surf6_zmin = openmc.ZPlane(z0=85.9)
surf6_zmax = openmc.ZPlane(z0=86.7)
surf7_zmin = openmc.ZPlane(z0=0.0)
surf7_zmax = openmc.ZPlane(z0=87.3)
surf8_zmin = openmc.ZPlane(z0=87.3)
surf8_zmax = openmc.ZPlane(z0=92.5)
surf10_zmin = openmc.ZPlane(z0=-2.3)
surf10_zmax = openmc.ZPlane(z0=-1.1)
surf16_zmin = openmc.ZPlane(z0=0.4)
surf16_zmax = openmc.ZPlane(z0=0.7)
surf17_zmin = openmc.ZPlane(z0=81.8)
surf17_zmax = openmc.ZPlane(z0=82.1)
surf99_zmin = openmc.ZPlane(z0=-20.0, boundary_type="vacuum")
surf99_zmax = openmc.ZPlane(z0=105.6, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell()
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell()
u1_cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell3 = openmc.Cell(fill=mat2)
u1_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell4 = openmc.Cell(fill=mat1)
u1_cell4.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell5 = openmc.Cell()
u1_cell5.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)
u1_cell6 = openmc.Cell()
u1_cell6.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell8 = openmc.Cell(fill=mat2)
u1_cell8.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax) & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & (-surf99 & +surf99_zmin & -surf99_zmax)
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & (-surf16 & +surf16_zmin & -surf16_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & (-surf17 & +surf17_zmin & -surf17_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

# Lattice 3: 47x27 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-16.45, -16.367886]
lattice3.pitch = [0.700000, 1.212436]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = (-surf91_0 & -surf91_1 & -surf91_2 & -surf91_3 & -surf91_4 & -surf91_5 & -surf91_6 & -surf91_7 & -surf91_8 & -surf91_9 & -surf91_10 & -surf91_11) & (-surf99 & +surf99_zmin & -surf99_zmax) & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26 & +surf27 & +surf28 & +surf29 & +surf30 & +surf31 & +surf32

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
source.space = openmc.stats.Point((0.0, 0.0, 42.8))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
