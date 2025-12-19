"""
PMF017-2: LLNL Pu Array Phase II - MHE - 4x4x4 - 6kg - case 202
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.601000e-02)
mat1.add_nuclide("Pu240", 2.923600e-03)
mat1.add_nuclide("Pu241", 2.243300e-04)
mat1.add_nuclide("Pu242", 4.856600e-06)
mat1.add_element("Al", 2.179500e-06)
mat1.add_element("Ag", 1.090300e-07)
mat1.add_element("B", 1.087900e-06)
mat1.add_element("C", 1.762600e-04)
mat1.add_element("Ca", 2.934600e-05)
mat1.add_element("Cu", 9.254100e-07)
mat1.add_element("Cr", 4.523900e-06)
mat1.add_element("Fe", 7.370900e-06)
mat1.add_element("Mg", 9.678000e-06)
mat1.add_element("Mn", 1.070400e-06)
mat1.add_element("Na", 5.115800e-07)
mat1.add_element("Ni", 1.002000e-05)
mat1.add_element("Pb", 5.676200e-08)
mat1.add_element("Si", 6.281400e-06)
mat1.add_element("Sn", 1.981800e-07)
mat1.add_element("Ti", 1.228200e-06)

# Aluminum
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.179500e-02)
mat2.add_element("Cu", 1.493800e-03)
mat2.add_element("Fe", 8.094000e-05)
mat2.add_element("Mg", 1.239900e-05)
mat2.add_element("Mn", 8.227900e-05)
mat2.add_element("Si", 1.073000e-04)
mat2.add_element("Ti", 1.888200e-05)
mat2.add_element("Zn", 2.304600e-05)

# Aluminum
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.596300e-02)
mat3.add_element("Cr", 3.149700e-05)
mat3.add_element("Cu", 1.121100e-03)
mat3.add_element("Fe", 1.462200e-04)
mat3.add_element("Mg", 1.010700e-03)
mat3.add_element("Mn", 1.788600e-04)
mat3.add_element("Si", 2.915600e-04)
mat3.add_element("Zn", 6.262300e-05)

# Aluminum
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 5.840200e-02)
mat4.add_element("Cu", 6.444200e-05)
mat4.add_element("Fe", 2.053100e-04)
mat4.add_element("Mg", 7.076400e-04)
mat4.add_element("Mn", 3.727000e-04)
mat4.add_element("Si", 1.749700e-04)
mat4.add_element("Zn", 6.263400e-05)

# Aluminum
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 5.827400e-02)
mat5.add_element("Cr", 6.254200e-05)
mat5.add_element("Cu", 6.396800e-05)
mat5.add_element("Fe", 2.038000e-04)
mat5.add_element("Mg", 6.689800e-04)
mat5.add_element("Mn", 4.439500e-05)
mat5.add_element("Si", 3.473600e-04)
mat5.add_element("Ti", 5.093900e-05)
mat5.add_element("Zn", 6.217400e-05)

# Aluminum
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Al", 3.599700e-02)
mat6.add_element("Cr", 3.863300e-05)
mat6.add_element("Cu", 3.951400e-05)
mat6.add_element("Fe", 1.258900e-04)
mat6.add_element("Mg", 4.132500e-04)
mat6.add_element("Mn", 2.742300e-05)
mat6.add_element("Si", 2.145700e-04)
mat6.add_element("Ti", 3.146600e-05)
mat6.add_element("Zn", 3.840600e-05)

# Aluminum
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Al", 4.476600e-02)
mat7.add_element("Cr", 4.804500e-05)
mat7.add_element("Cu", 4.914000e-05)
mat7.add_element("Fe", 1.565600e-04)
mat7.add_element("Mg", 5.139100e-04)
mat7.add_element("Mn", 3.410400e-05)
mat7.add_element("Si", 2.668400e-04)
mat7.add_element("Ti", 3.913100e-05)
mat7.add_element("Zn", 4.776200e-05)

# Aluminum
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 5.700200e-02)
mat8.add_element("Cr", 3.208200e-05)
mat8.add_element("Cu", 1.141900e-03)
mat8.add_element("Fe", 1.493500e-04)
mat8.add_element("Mg", 1.029500e-03)
mat8.add_element("Mn", 1.821800e-04)
mat8.add_element("Si", 2.969700e-04)
mat8.add_element("Zn", 6.378600e-05)

# Aluminum
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Al", 1.724900e-02)
mat9.add_element("Cr", 1.851200e-05)
mat9.add_element("Cu", 1.893500e-05)
mat9.add_element("Fe", 6.032600e-05)
mat9.add_element("Mg", 1.980200e-04)
mat9.add_element("Mn", 1.314100e-05)
mat9.add_element("Si", 1.028200e-04)
mat9.add_element("Ti", 1.507800e-05)
mat9.add_element("Zn", 1.840300e-05)

# Iron (steel)
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("Fe", 8.450600e-02)
mat10.add_element("C", 3.168700e-04)
mat10.add_element("Mn", 3.204100e-04)
mat10.add_element("P", 2.303900e-05)
mat10.add_element("S", 3.709800e-05)
mat10.add_element("Si", 1.693900e-05)
mat10.add_element("Sn", 1.202500e-04)

# Homogenized
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_element("Al", 3.201600e-03)
mat11.add_element("C", 2.092900e-04)
mat11.add_element("Cu", 2.550100e-02)
mat11.add_element("Cr", 5.959600e-04)
mat11.add_element("Fe", 1.090600e-02)
mat11.add_element("Mg", 5.782300e-05)
mat11.add_element("Mn", 5.237800e-05)
mat11.add_element("Mo", 8.343300e-05)
mat11.add_element("Pb", 6.385500e-07)
mat11.add_element("S", 8.253700e-06)
mat11.add_element("Si", 2.168900e-04)
mat11.add_element("Sn", 1.706700e-04)
mat11.add_element("V", 6.103500e-05)
mat11.add_element("Zn", 1.617700e-02)

# Concrete
mat12 = openmc.Material(material_id=12)
mat12.set_density("sum")
mat12.add_element("Al", 7.350000e-04)
mat12.add_element("C", 3.814400e-03)
mat12.add_element("Ca", 1.158800e-02)
mat12.add_element("Fe", 1.968000e-04)
mat12.add_nuclide("H1", 1.486800e-02)
mat12.add_element("Mg", 5.870000e-04)
mat12.add_element("Na", 3.040000e-04)
mat12.add_nuclide("O16", 4.151900e-02)
mat12.add_element("Si", 6.037000e-03)
mat12.add_s_alpha_beta("c_H_in_H2O")

# Moderator
mat13 = openmc.Material(material_id=13)
mat13.set_density("sum")
mat13.add_element("Al", 1.043900e-07)
mat13.add_element("B", 8.684200e-08)
mat13.add_element("C", 2.388700e-02)
mat13.add_element("Ca", 2.342500e-07)
mat13.add_element("Cu", 4.432300e-09)
mat13.add_element("Cr", 3.611200e-08)
mat13.add_element("Fe", 4.202800e-07)
mat13.add_element("Mg", 1.158800e-07)
mat13.add_nuclide("H1", 2.924900e-02)
mat13.add_element("Mn", 8.544600e-09)
mat13.add_element("Mo", 1.957200e-09)
mat13.add_element("Na", 8.167500e-07)
mat13.add_element("Ni", 3.198800e-08)
mat13.add_nuclide("O16", 2.036400e-02)
mat13.add_element("Pb", 1.812400e-09)
mat13.add_element("Si", 6.685600e-08)
mat13.add_element("Sn", 1.582000e-09)
mat13.add_element("Ti", 9.800100e-09)
mat13.add_element("Zn", 7.179900e-09)
mat13.add_element("N", 2.116100e-02)
mat13.add_element("K", 4.802500e-06)
mat13.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11, mat12, mat13])

# ==============================================================================
# Geometry
# ==============================================================================

# Table top
surf1 = openmc.model.RectangularParallelepiped(-106.5, 106.5, -106.5, 106.5, -2.382, 0.0)
# Frame
surf2 = openmc.model.RectangularParallelepiped(-106.5, 106.5, -106.5, 106.5, -12.542, -2.3819999999999997)
# Concrete, inner
surf3 = openmc.model.RectangularParallelepiped(-457.2, 457.2, -457.2, 457.2, -360.342, 554.058)
# Concrete, outer
surf4 = openmc.model.RectangularParallelepiped(-609.6, 609.6, -609.6, 609.6, -451.78200000000004, 615.013, boundary_type="vacuum")
surf10 = openmc.model.RectangularParallelepiped(96.34, 106.5, -106.5, 106.5, 206.195, 216.35500000000002)
surf11 = openmc.model.RectangularParallelepiped(51.425000000000004, 151.415, -499.95, 499.95, 206.83, 215.72)
surf12 = openmc.XPlane(surface_id=12, x0=101.1025)
surf13 = openmc.XPlane(surface_id=13, x0=101.7375)
surf15 = openmc.model.RectangularParallelepiped(-106.5, -96.34, -106.5, 106.5, 206.195, 216.35500000000002)
surf16 = openmc.model.RectangularParallelepiped(-151.415, -51.425000000000004, -499.95, 499.95, 206.83, 215.72)
surf17 = openmc.XPlane(surface_id=17, x0=-101.7375)
surf18 = openmc.XPlane(surface_id=18, x0=-101.1025)
# 1st, inner
surf20 = openmc.model.RectangularParallelepiped(-49.95, 49.95, -36.2035, -27.5165, 217.0915, 220.69850000000002)
# 1st, outer
surf21 = openmc.model.RectangularParallelepiped(-42.48, 42.48, -36.94, -26.78, 216.35500000000002, 221.435)
# 2nd, inner
surf22 = openmc.model.RectangularParallelepiped(-49.95, 49.95, -14.9635, -6.2764999999999995, 217.0915, 220.69850000000002)
# 2nd, outer
surf23 = openmc.model.RectangularParallelepiped(-42.48, 42.48, -15.7, -5.539999999999999, 216.35500000000002, 221.435)
# 3rd, inner
surf24 = openmc.model.RectangularParallelepiped(-49.95, 49.95, 6.2764999999999995, 14.9635, 217.0915, 220.69850000000002)
# 3rd, outer
surf25 = openmc.model.RectangularParallelepiped(-42.48, 42.48, 5.539999999999999, 15.7, 216.35500000000002, 221.435)
# 4th, inner
surf26 = openmc.model.RectangularParallelepiped(-49.95, 49.95, 27.5165, 36.2035, 217.0915, 220.69850000000002)
# 4th, outer
surf27 = openmc.model.RectangularParallelepiped(-42.48, 42.48, 26.78, 36.94, 216.35500000000002, 221.435)
# Hole
surf30 = openmc.ZCylinder(surface_id=30, r=1.4986)
# Bottom heat sink
surf31 = openmc.ZCylinder(surface_id=31, r=3.2995)
# Fe can lid
surf32 = openmc.ZCylinder(surface_id=32, r=3.2995)
# Pu
surf33 = openmc.ZCylinder(surface_id=33, r=3.2625)
# Al can wall
surf34 = openmc.ZCylinder(surface_id=34, r=3.2995)
# Al can bottom
surf35 = openmc.ZCylinder(surface_id=35, r=3.2995)
# Al middle heat sink
surf36 = openmc.ZCylinder(surface_id=36, r=3.2995)
# Fe can lid
surf37 = openmc.ZCylinder(surface_id=37, r=3.2995)
# Pu
surf38 = openmc.ZCylinder(surface_id=38, r=3.2625)
# Al can wall
surf39 = openmc.ZCylinder(surface_id=39, r=3.2995)
# Al bottom
surf40 = openmc.ZCylinder(surface_id=40, r=3.2995)
# Al top heat sink
surf41 = openmc.ZCylinder(surface_id=41, r=3.2995)
# Al tube, outer
surf50 = openmc.ZCylinder(surface_id=50, r=3.607)
# Bottom homogenized shoe
surf51 = openmc.ZPlane(surface_id=51, z0=4.922)
# Lower support tube
surf52 = openmc.ZPlane(surface_id=52, z0=25.083)
# ditto
surf53 = openmc.ZCylinder(surface_id=53, r=2.8672)
# Al tube, inner
surf54 = openmc.ZCylinder(surface_id=54, r=3.429)
# Hole
surf60 = openmc.ZCylinder(surface_id=60, r=3.123)
# Bottom spacer
surf61 = openmc.ZCylinder(surface_id=61, r=3.3338)
# MHE
surf62 = openmc.ZCylinder(surface_id=62, r=3.3975)
# 6 kg part
surf63 = openmc.ZCylinder(surface_id=63, r=3.2995)
# MHE
surf64 = openmc.ZCylinder(surface_id=64, r=3.3975)
# Inner spacer
surf65 = openmc.ZCylinder(surface_id=65, r=3.3338)
# MHE
surf66 = openmc.ZCylinder(surface_id=66, r=3.3975)
# 6 kg part
surf67 = openmc.ZCylinder(surface_id=67, r=3.2995)
# MHE
surf68 = openmc.ZCylinder(surface_id=68, r=3.3975)
# Inner spacer
surf69 = openmc.ZCylinder(surface_id=69, r=3.3338)
# MHE
surf70 = openmc.ZCylinder(surface_id=70, r=3.3975)
# 6 kg part
surf71 = openmc.ZCylinder(surface_id=71, r=3.2995)
# MHE
surf72 = openmc.ZCylinder(surface_id=72, r=3.3975)
# Inner spacer
surf73 = openmc.ZCylinder(surface_id=73, r=3.3338)
# MHE
surf74 = openmc.ZCylinder(surface_id=74, r=3.3975)
# 6 kg part
surf75 = openmc.ZCylinder(surface_id=75, r=3.2995)
# MHE
surf76 = openmc.ZCylinder(surface_id=76, r=3.3975)
# MHE, inner
surf80 = openmc.ZCylinder(surface_id=80, r=3.8141)
# MHE, ring 1
surf81 = openmc.ZCylinder(surface_id=81, r=6.3628)
# MHE, ring 2
surf82 = openmc.ZCylinder(surface_id=82, r=6.3628)
# MHE, ring 3
surf83 = openmc.ZCylinder(surface_id=83, r=6.3628)
# MHE, ring 4
surf84 = openmc.ZCylinder(surface_id=84, r=6.3628)
surf101 = openmc.ZCylinder(surface_id=101, x0=-31.86, y0=-31.86, r=6.3628)
surf102 = openmc.ZCylinder(surface_id=102, x0=-31.86, y0=-10.62, r=6.3628)
surf103 = openmc.ZCylinder(surface_id=103, x0=-31.86, y0=10.62, r=6.3628)
surf104 = openmc.ZCylinder(surface_id=104, x0=-31.86, y0=31.86, r=6.3628)
surf105 = openmc.ZCylinder(surface_id=105, x0=-10.62, y0=-31.86, r=6.3628)
surf106 = openmc.ZCylinder(surface_id=106, x0=-10.62, y0=-10.62, r=6.3628)
surf107 = openmc.ZCylinder(surface_id=107, x0=-10.62, y0=10.62, r=6.3628)
surf108 = openmc.ZCylinder(surface_id=108, x0=-10.62, y0=31.86, r=6.3628)
surf109 = openmc.ZCylinder(surface_id=109, x0=10.62, y0=-31.86, r=6.3628)
surf110 = openmc.ZCylinder(surface_id=110, x0=10.62, y0=-10.62, r=6.3628)
surf111 = openmc.ZCylinder(surface_id=111, x0=10.62, y0=10.62, r=6.3628)
surf112 = openmc.ZCylinder(surface_id=112, x0=10.62, y0=31.86, r=6.3628)
surf113 = openmc.ZCylinder(surface_id=113, x0=31.86, y0=-31.86, r=6.3628)
surf114 = openmc.ZCylinder(surface_id=114, x0=31.86, y0=-10.62, r=6.3628)
surf115 = openmc.ZCylinder(surface_id=115, x0=31.86, y0=10.62, r=6.3628)
surf116 = openmc.ZCylinder(surface_id=116, x0=31.86, y0=31.86, r=6.3628)

# Z-plane surfaces for bounded cylinders
surf31_zmin = openmc.ZPlane(surface_id=1116, z0=0.33092)
surf31_zmax = openmc.ZPlane(surface_id=1117, z0=0.635)
surf32_zmin = openmc.ZPlane(surface_id=1118, z0=0.635)
surf32_zmax = openmc.ZPlane(surface_id=1119, z0=0.656)
surf33_zmin = openmc.ZPlane(surface_id=1120, z0=0.656)
surf33_zmax = openmc.ZPlane(surface_id=1121, z0=5.289)
surf34_zmin = openmc.ZPlane(surface_id=1122, z0=0.656)
surf34_zmax = openmc.ZPlane(surface_id=1123, z0=5.289)
surf35_zmin = openmc.ZPlane(surface_id=1124, z0=5.289)
surf35_zmax = openmc.ZPlane(surface_id=1125, z0=5.376)
surf36_zmin = openmc.ZPlane(surface_id=1126, z0=5.376)
surf36_zmax = openmc.ZPlane(surface_id=1127, z0=5.7316)
surf37_zmin = openmc.ZPlane(surface_id=1128, z0=5.7316)
surf37_zmax = openmc.ZPlane(surface_id=1129, z0=5.7526)
surf38_zmin = openmc.ZPlane(surface_id=1130, z0=5.7526)
surf38_zmax = openmc.ZPlane(surface_id=1131, z0=10.3856)
surf39_zmin = openmc.ZPlane(surface_id=1132, z0=5.7526)
surf39_zmax = openmc.ZPlane(surface_id=1133, z0=10.3856)
surf40_zmin = openmc.ZPlane(surface_id=1134, z0=10.3856)
surf40_zmax = openmc.ZPlane(surface_id=1135, z0=10.4726)
surf41_zmin = openmc.ZPlane(surface_id=1136, z0=10.4726)
surf41_zmax = openmc.ZPlane(surface_id=1137, z0=10.9516)
surf50_zmin = openmc.ZPlane(surface_id=1138, z0=0.0)
surf50_zmax = openmc.ZPlane(surface_id=1139, z0=208.417)
surf61_zmin = openmc.ZPlane(surface_id=1140, z0=25.083)
surf61_zmax = openmc.ZPlane(surface_id=1141, z0=71.2455)
surf62_zmin = openmc.ZPlane(surface_id=1142, z0=71.2455)
surf62_zmax = openmc.ZPlane(surface_id=1143, z0=73.7942)
surf63_zmin = openmc.ZPlane(surface_id=1144, z0=73.7942)
surf63_zmax = openmc.ZPlane(surface_id=1145, z0=84.7458)
surf64_zmin = openmc.ZPlane(surface_id=1146, z0=84.7458)
surf64_zmax = openmc.ZPlane(surface_id=1147, z0=87.2945)
surf65_zmin = openmc.ZPlane(surface_id=1148, z0=87.2945)
surf65_zmax = openmc.ZPlane(surface_id=1149, z0=97.0655)
surf66_zmin = openmc.ZPlane(surface_id=1150, z0=97.0655)
surf66_zmax = openmc.ZPlane(surface_id=1151, z0=99.6142)
surf67_zmin = openmc.ZPlane(surface_id=1152, z0=99.6142)
surf67_zmax = openmc.ZPlane(surface_id=1153, z0=110.5658)
surf68_zmin = openmc.ZPlane(surface_id=1154, z0=110.5658)
surf68_zmax = openmc.ZPlane(surface_id=1155, z0=113.1145)
surf69_zmin = openmc.ZPlane(surface_id=1156, z0=113.1145)
surf69_zmax = openmc.ZPlane(surface_id=1157, z0=122.8855)
surf70_zmin = openmc.ZPlane(surface_id=1158, z0=122.8855)
surf70_zmax = openmc.ZPlane(surface_id=1159, z0=125.4342)
surf71_zmin = openmc.ZPlane(surface_id=1160, z0=125.4342)
surf71_zmax = openmc.ZPlane(surface_id=1161, z0=136.3858)
surf72_zmin = openmc.ZPlane(surface_id=1162, z0=136.3858)
surf72_zmax = openmc.ZPlane(surface_id=1163, z0=138.9345)
surf73_zmin = openmc.ZPlane(surface_id=1164, z0=138.9345)
surf73_zmax = openmc.ZPlane(surface_id=1165, z0=148.7055)
surf74_zmin = openmc.ZPlane(surface_id=1166, z0=148.7055)
surf74_zmax = openmc.ZPlane(surface_id=1167, z0=151.2542)
surf75_zmin = openmc.ZPlane(surface_id=1168, z0=151.2542)
surf75_zmax = openmc.ZPlane(surface_id=1169, z0=162.2058)
surf76_zmin = openmc.ZPlane(surface_id=1170, z0=162.2058)
surf76_zmax = openmc.ZPlane(surface_id=1171, z0=164.7545)
surf81_zmin = openmc.ZPlane(surface_id=1172, z0=71.2455)
surf81_zmax = openmc.ZPlane(surface_id=1173, z0=87.2945)
surf82_zmin = openmc.ZPlane(surface_id=1174, z0=97.0655)
surf82_zmax = openmc.ZPlane(surface_id=1175, z0=113.1145)
surf83_zmin = openmc.ZPlane(surface_id=1176, z0=122.8855)
surf83_zmax = openmc.ZPlane(surface_id=1177, z0=138.9345)
surf84_zmin = openmc.ZPlane(surface_id=1178, z0=148.7055)
surf84_zmax = openmc.ZPlane(surface_id=1179, z0=164.7545)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat5)
u1_cell0.region = (-surf31 & +surf31_zmin & -surf31_zmax)
u1_cell1 = openmc.Cell(fill=mat10)
u1_cell1.region = (+surf31 | -surf31_zmin | +surf31_zmax) & (-surf32 & +surf32_zmin & -surf32_zmax)
u1_cell2 = openmc.Cell(fill=mat1)
u1_cell2.region = (+surf32 | -surf32_zmin | +surf32_zmax) & (-surf33 & +surf33_zmin & -surf33_zmax)
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = (+surf32 | -surf32_zmin | +surf32_zmax) & (+surf33 | -surf33_zmin | +surf33_zmax) & (-surf34 & +surf34_zmin & -surf34_zmax)
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = (+surf33 | -surf33_zmin | +surf33_zmax) & (+surf34 | -surf34_zmin | +surf34_zmax) & (-surf35 & +surf35_zmin & -surf35_zmax)
u1_cell5 = openmc.Cell(fill=mat6)
u1_cell5.region = +surf30 & (+surf35 | -surf35_zmin | +surf35_zmax) & (-surf36 & +surf36_zmin & -surf36_zmax)
u1_cell6 = openmc.Cell(fill=mat10)
u1_cell6.region = (+surf36 | -surf36_zmin | +surf36_zmax) & (-surf37 & +surf37_zmin & -surf37_zmax)
u1_cell7 = openmc.Cell(fill=mat1)
u1_cell7.region = (+surf37 | -surf37_zmin | +surf37_zmax) & (-surf38 & +surf38_zmin & -surf38_zmax)
u1_cell8 = openmc.Cell(fill=mat4)
u1_cell8.region = (+surf37 | -surf37_zmin | +surf37_zmax) & (+surf38 | -surf38_zmin | +surf38_zmax) & (-surf39 & +surf39_zmin & -surf39_zmax)
u1_cell9 = openmc.Cell(fill=mat4)
u1_cell9.region = (+surf38 | -surf38_zmin | +surf38_zmax) & (+surf39 | -surf39_zmin | +surf39_zmax) & (-surf40 & +surf40_zmin & -surf40_zmax)
u1_cell10 = openmc.Cell(fill=mat7)
u1_cell10.region = +surf30 & (+surf40 | -surf40_zmin | +surf40_zmax) & (-surf41 & +surf41_zmin & -surf41_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10])

u2_cell0 = openmc.Cell(fill=mat11)
u2_cell0.region = (-surf50 & +surf50_zmin & -surf50_zmax) & -surf51
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = (-surf50 & +surf50_zmin & -surf50_zmax) & +surf51 & -surf52 & +surf53
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = (-surf50 & +surf50_zmin & -surf50_zmax) & +surf52 & +surf54
u2_cell3 = openmc.Cell(fill=mat5)
u2_cell3.region = +surf52 & +surf60 & (-surf61 & +surf61_zmin & -surf61_zmax)
u2_cell4 = openmc.Cell(fill=mat13)
u2_cell4.region = (+surf61 | -surf61_zmin | +surf61_zmax) & (-surf62 & +surf62_zmin & -surf62_zmax)
u2_cell5 = openmc.Cell(fill=mat13)
u2_cell5.region = (+surf63 | -surf63_zmin | +surf63_zmax) & (-surf64 & +surf64_zmin & -surf64_zmax)
u2_cell6 = openmc.Cell(fill=mat5)
u2_cell6.region = +surf60 & (+surf64 | -surf64_zmin | +surf64_zmax) & (-surf65 & +surf65_zmin & -surf65_zmax)
u2_cell7 = openmc.Cell(fill=mat13)
u2_cell7.region = (+surf65 | -surf65_zmin | +surf65_zmax) & (-surf66 & +surf66_zmin & -surf66_zmax)
u2_cell8 = openmc.Cell(fill=mat13)
u2_cell8.region = (+surf67 | -surf67_zmin | +surf67_zmax) & (-surf68 & +surf68_zmin & -surf68_zmax)
u2_cell9 = openmc.Cell(fill=mat5)
u2_cell9.region = +surf60 & (+surf68 | -surf68_zmin | +surf68_zmax) & (-surf69 & +surf69_zmin & -surf69_zmax)
u2_cell10 = openmc.Cell(fill=mat13)
u2_cell10.region = (+surf69 | -surf69_zmin | +surf69_zmax) & (-surf70 & +surf70_zmin & -surf70_zmax)
u2_cell11 = openmc.Cell(fill=mat13)
u2_cell11.region = (+surf71 | -surf71_zmin | +surf71_zmax) & (-surf72 & +surf72_zmin & -surf72_zmax)
u2_cell12 = openmc.Cell(fill=mat5)
u2_cell12.region = +surf60 & (+surf72 | -surf72_zmin | +surf72_zmax) & (-surf73 & +surf73_zmin & -surf73_zmax)
u2_cell13 = openmc.Cell(fill=mat13)
u2_cell13.region = (+surf73 | -surf73_zmin | +surf73_zmax) & (-surf74 & +surf74_zmin & -surf74_zmax)
u2_cell14 = openmc.Cell(fill=mat13)
u2_cell14.region = (+surf75 | -surf75_zmin | +surf75_zmax) & (-surf76 & +surf76_zmin & -surf76_zmax)
u2_cell15 = openmc.Cell(fill=mat13)
u2_cell15.region = +surf80 & (-surf81 & +surf81_zmin & -surf81_zmax)
u2_cell16 = openmc.Cell(fill=mat13)
u2_cell16.region = +surf80 & (-surf82 & +surf82_zmin & -surf82_zmax)
u2_cell17 = openmc.Cell(fill=mat13)
u2_cell17.region = +surf80 & (-surf83 & +surf83_zmin & -surf83_zmax)
u2_cell18 = openmc.Cell(fill=mat13)
u2_cell18.region = +surf80 & (-surf84 & +surf84_zmin & -surf84_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8, u2_cell9, u2_cell10, u2_cell11, u2_cell12, u2_cell13, u2_cell14, u2_cell15, u2_cell16, u2_cell17, u2_cell18])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Tube
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.translation = (-31.86, -31.86, 0.0)
cell1.region = -surf101

# Tube
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.translation = (-31.86, -10.62, 0.0)
cell2.region = -surf102

# Tube
cell3 = openmc.Cell(cell_id=3, fill=universe2)
cell3.translation = (-31.86, 10.62, 0.0)
cell3.region = -surf103

# Tube
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.translation = (-31.86, 31.86, 0.0)
cell4.region = -surf104

# Tube
cell5 = openmc.Cell(cell_id=5, fill=universe2)
cell5.translation = (-10.62, -31.86, 0.0)
cell5.region = -surf105

# Tube
cell6 = openmc.Cell(cell_id=6, fill=universe2)
cell6.translation = (-10.62, -10.62, 0.0)
cell6.region = -surf106

# Tube
cell7 = openmc.Cell(cell_id=7, fill=universe2)
cell7.translation = (-10.62, 10.62, 0.0)
cell7.region = -surf107

# Tube
cell8 = openmc.Cell(cell_id=8, fill=universe2)
cell8.translation = (-10.62, 31.86, 0.0)
cell8.region = -surf108

# Tube
cell9 = openmc.Cell(cell_id=9, fill=universe2)
cell9.translation = (10.62, -31.86, 0.0)
cell9.region = -surf109

# Tube
cell10 = openmc.Cell(cell_id=10, fill=universe2)
cell10.translation = (10.62, -10.62, 0.0)
cell10.region = -surf110

# Tube
cell11 = openmc.Cell(cell_id=11, fill=universe2)
cell11.translation = (10.62, 10.62, 0.0)
cell11.region = -surf111

# Tube
cell12 = openmc.Cell(cell_id=12, fill=universe2)
cell12.translation = (10.62, 31.86, 0.0)
cell12.region = -surf112

# Tube
cell13 = openmc.Cell(cell_id=13, fill=universe2)
cell13.translation = (31.86, -31.86, 0.0)
cell13.region = -surf113

# Tube
cell14 = openmc.Cell(cell_id=14, fill=universe2)
cell14.translation = (31.86, -10.62, 0.0)
cell14.region = -surf114

# Tube
cell15 = openmc.Cell(cell_id=15, fill=universe2)
cell15.translation = (31.86, 10.62, 0.0)
cell15.region = -surf115

# Tube
cell16 = openmc.Cell(cell_id=16, fill=universe2)
cell16.translation = (31.86, 31.86, 0.0)
cell16.region = -surf116

# I-beam
cell17 = openmc.Cell(cell_id=17, fill=mat8)
cell17.region = -surf10 & +surf11

# I-beam
cell18 = openmc.Cell(cell_id=18, fill=mat8)
cell18.region = -surf10 & -surf11 & +surf12 & -surf13

# I-beam
cell19 = openmc.Cell(cell_id=19, fill=mat8)
cell19.region = -surf15 & +surf16

# I-beam
cell20 = openmc.Cell(cell_id=20, fill=mat8)
cell20.region = -surf15 & -surf16 & +surf17 & -surf18

# O-beam
cell21 = openmc.Cell(cell_id=21, fill=mat8)
cell21.region = +surf20 & -surf21

# O-beam
cell22 = openmc.Cell(cell_id=22, fill=mat8)
cell22.region = +surf22 & -surf23

# O-beam
cell23 = openmc.Cell(cell_id=23, fill=mat8)
cell23.region = +surf24 & -surf25

# O-beam
cell24 = openmc.Cell(cell_id=24, fill=mat8)
cell24.region = +surf26 & -surf27

# Table
cell25 = openmc.Cell(cell_id=25, fill=mat2)
cell25.region = -surf1

# Frame
cell26 = openmc.Cell(cell_id=26, fill=mat9)
cell26.region = +surf1 & -surf2

# Cncrt
cell27 = openmc.Cell(cell_id=27, fill=mat12)
cell27.region = +surf3 & -surf4

# THS
cell39 = openmc.Cell(cell_id=39, fill=mat7)
cell39.region = +surf30 & (+surf40 | -surf40_zmin | +surf40_zmax) & (-surf41 & +surf41_zmin & -surf41_zmax)

# MHE
cell59 = openmc.Cell(cell_id=59, fill=mat13)
cell59.region = +surf80 & (-surf84 & +surf84_zmin & -surf84_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell39, cell59])
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
source.space = openmc.stats.Box((-32.86, -32.86, 75.7667), (32.86, 32.86, 160.3233))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
