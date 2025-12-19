"""
IEU-MET-FAST-021-1: FR0 experiment 4 (case 1 detailed model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Fuel and teflon
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 9.616200e-05)
mat1.add_nuclide("U235", 9.599100e-03)
mat1.add_nuclide("U238", 3.769900e-02)
mat1.add_element("C", 4.918000e-05)
mat1.add_element("F", 9.836200e-05)

# Natural uranium blocks
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 2.624000e-06)
mat2.add_nuclide("U235", 3.433700e-04)
mat2.add_nuclide("U238", 4.734500e-02)

# Natural uranium plus void
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U234", 2.599600e-06)
mat3.add_nuclide("U235", 3.401800e-04)
mat3.add_nuclide("U238", 4.690400e-02)

# SST frames & inner part end blocks
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 5.857800e-02)
mat4.add_element("Cr", 1.595100e-02)
mat4.add_element("Ni", 7.458200e-03)
mat4.add_element("Mn", 8.387000e-04)
mat4.add_element("Si", 8.202900e-04)

# SST outer part end blocks
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 4.761000e-02)
mat5.add_element("Cr", 1.296400e-02)
mat5.add_element("Ni", 6.061800e-03)
mat5.add_element("Mn", 6.816600e-04)
mat5.add_element("Si", 6.667000e-04)

# Steel
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 8.410900e-02)

# Aluminum
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Al", 6.030700e-02)

# Concrete
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Fe", 1.929500e-04)
mat8.add_nuclide("H1", 8.506500e-03)
mat8.add_element("C", 2.020400e-02)
mat8.add_nuclide("O16", 3.550800e-02)
mat8.add_element("F", 1.968400e-05)
mat8.add_element("Mg", 1.860600e-03)
mat8.add_element("Al", 5.559500e-04)
mat8.add_element("Si", 1.700400e-03)
mat8.add_element("K", 4.038500e-05)
mat8.add_element("Ca", 1.110400e-02)
mat8.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Concrete walls, floor and ceiling, inner
surf1 = openmc.model.RectangularParallelepiped(-425.285, 847.715, -380.0, 420.0, -150.75, 649.25)
# Concrete walls, floor and ceiling, outer
surf2 = openmc.model.RectangularParallelepiped(-572.285, 967.715, -530.0, 540.0, -210.75, 709.25, boundary_type="vacuum")
# Steel table
surf3 = openmc.model.RectangularParallelepiped(-77.285, 72.715, -71.0, 71.0, -77.75, -61.75)
# Steel LHS
surf4 = openmc.model.RectangularParallelepiped(-67.285, 62.715, -61.0, -59.4, -61.75, 61.75)
# Steel RHS
surf5 = openmc.model.RectangularParallelepiped(-67.285, 62.715, 59.4, 61.0, -61.75, 61.75)
# Steel top
surf6 = openmc.model.RectangularParallelepiped(-25.135, 25.135, -61.0, 61.0, 61.75, 63.15)
# Steel hat
surf7 = openmc.model.RectangularParallelepiped(-25.135, 25.135, -35.135, 35.135, 63.15, 64.55)
# Steel vertical plates
surf11 = openmc.model.RectangularParallelepiped(-7.285, 2.715, -26.18, -25.58, -61.75, 61.75)
surf12 = openmc.model.RectangularParallelepiped(-7.285, 2.715, 25.58, 26.18, -61.75, 61.75)
surf13 = openmc.model.RectangularParallelepiped(-26.18, -25.58, -25.58, -20.58, -61.75, 61.75)
surf14 = openmc.model.RectangularParallelepiped(-26.18, -25.58, 20.58, 25.58, -61.75, 61.75)
surf15 = openmc.model.RectangularParallelepiped(25.58, 26.18, -25.58, -20.58, -61.75, 61.75)
surf16 = openmc.model.RectangularParallelepiped(25.58, 26.18, 20.58, 25.58, -61.75, 61.75)
# Steel horizontal plates
surf21 = openmc.model.RectangularParallelepiped(-25.98, -25.58, -20.99, 20.99, -29.104, -25.104)
surf22 = openmc.model.RectangularParallelepiped(-25.98, -25.58, -20.99, 20.99, -2.404, 1.596)
surf23 = openmc.model.RectangularParallelepiped(-25.98, -25.58, -20.99, 20.99, 24.296, 28.296)
surf24 = openmc.model.RectangularParallelepiped(25.58, 25.98, -20.99, 20.99, -29.104, -25.104)
surf25 = openmc.model.RectangularParallelepiped(25.58, 25.98, -20.99, 20.99, -2.404, 1.596)
surf26 = openmc.model.RectangularParallelepiped(25.58, 25.98, -20.99, 20.99, 24.296, 28.296)
# Steel horizontal strips
surf31 = openmc.model.RectangularParallelepiped(-25.58, 25.58, -25.63, -25.58, -29.104, -23.104)
surf32 = openmc.model.RectangularParallelepiped(-25.58, 25.58, -25.63, -25.58, -3.404, 2.596)
surf33 = openmc.model.RectangularParallelepiped(-25.58, 25.58, -25.63, -25.58, 22.296, 28.296)
surf34 = openmc.model.RectangularParallelepiped(-25.58, 25.58, 25.58, 25.63, -29.104, -23.104)
surf35 = openmc.model.RectangularParallelepiped(-25.58, 25.58, 25.58, 25.63, -3.404, 2.596)
surf36 = openmc.model.RectangularParallelepiped(-25.58, 25.58, 25.58, 25.63, 22.296, 28.296)
# Steel reflector clamping structure
surf41 = openmc.model.RectangularParallelepiped(-16.07, -15.995, -16.07, 16.07, -29.104, 28.296)
surf42 = openmc.model.RectangularParallelepiped(-15.995, -6.93, 15.995, 16.07, -29.104, 28.296)
surf43 = openmc.model.RectangularParallelepiped(-6.93, -6.855, 15.995, 25.21, -29.104, 28.296)
surf44 = openmc.model.RectangularParallelepiped(-6.855, 2.285, 25.135, 25.21, -29.104, 28.296)
surf45 = openmc.model.RectangularParallelepiped(2.285, 2.36, 20.565, 25.21, -29.104, 28.296)
surf46 = openmc.model.RectangularParallelepiped(2.36, 6.855, 20.565, 20.64, -29.104, 28.296)
surf47 = openmc.model.RectangularParallelepiped(6.855, 6.93, 15.955, 20.64, -29.104, 28.296)
surf48 = openmc.model.RectangularParallelepiped(6.93, 15.995, 15.955, 16.07, -29.104, 28.296)
surf49 = openmc.model.RectangularParallelepiped(15.995, 16.07, -16.07, 16.07, -29.104, 28.296)
surf50 = openmc.model.RectangularParallelepiped(2.36, 15.995, -16.07, -15.995, -29.104, 28.296)
surf51 = openmc.model.RectangularParallelepiped(2.285, 2.36, -25.21, -15.995, -29.104, 28.296)
surf52 = openmc.model.RectangularParallelepiped(-6.855, 2.285, -25.21, -25.135, -29.104, 28.296)
surf53 = openmc.model.RectangularParallelepiped(-6.93, -6.855, -25.21, -15.995, -29.104, 28.296)
surf54 = openmc.model.RectangularParallelepiped(-15.995, -6.93, -16.09, -15.995, -29.104, 28.296)
# Aluminum large outer support tubes, inner
surf61 = openmc.ZCylinder(surface_id=61, x0=-12.0, y0=20.7, r=4.0)
surf62 = openmc.ZCylinder(surface_id=62, x0=-21.0, y0=16.0, r=4.0)
surf63 = openmc.ZCylinder(surface_id=63, x0=-21.0, y0=6.0, r=4.0)
surf64 = openmc.ZCylinder(surface_id=64, x0=-21.0, y0=-6.0, r=4.0)
surf65 = openmc.ZCylinder(surface_id=65, x0=-21.0, y0=-16.0, r=4.0)
surf66 = openmc.ZCylinder(surface_id=66, x0=-12.0, y0=-20.7, r=4.0)
surf67 = openmc.ZCylinder(surface_id=67, x0=12.0, y0=20.7, r=4.0)
surf68 = openmc.ZCylinder(surface_id=68, x0=21.0, y0=16.0, r=4.0)
surf69 = openmc.ZCylinder(surface_id=69, x0=21.0, y0=6.0, r=4.0)
surf70 = openmc.ZCylinder(surface_id=70, x0=21.0, y0=-6.0, r=4.0)
surf71 = openmc.ZCylinder(surface_id=71, x0=21.0, y0=-16.0, r=4.0)
surf72 = openmc.ZCylinder(surface_id=72, x0=12.0, y0=-20.7, r=4.0)
# Aluminum large outer support tubes, outer
surf81 = openmc.ZCylinder(surface_id=81, x0=-12.0, y0=20.7, r=4.5)
surf82 = openmc.ZCylinder(surface_id=82, x0=-21.0, y0=16.0, r=4.5)
surf83 = openmc.ZCylinder(surface_id=83, x0=-21.0, y0=6.0, r=4.5)
surf84 = openmc.ZCylinder(surface_id=84, x0=-21.0, y0=-6.0, r=4.5)
surf85 = openmc.ZCylinder(surface_id=85, x0=-21.0, y0=-16.0, r=4.5)
surf86 = openmc.ZCylinder(surface_id=86, x0=-12.0, y0=-20.7, r=4.5)
surf87 = openmc.ZCylinder(surface_id=87, x0=12.0, y0=20.7, r=4.5)
surf88 = openmc.ZCylinder(surface_id=88, x0=21.0, y0=16.0, r=4.5)
surf89 = openmc.ZCylinder(surface_id=89, x0=21.0, y0=6.0, r=4.5)
surf90 = openmc.ZCylinder(surface_id=90, x0=21.0, y0=-6.0, r=4.5)
surf91 = openmc.ZCylinder(surface_id=91, x0=21.0, y0=-16.0, r=4.5)
surf92 = openmc.ZCylinder(surface_id=92, x0=12.0, y0=-20.7, r=4.5)
# Aluminum plate and
surf100 = openmc.model.RectangularParallelepiped(-25.135, 25.135, -25.135, 25.135, -30.104, -29.104)
# cut-out
surf101 = openmc.model.RectangularParallelepiped(-15.995, 15.995, -15.995, 15.995, -30.999, -29.001)
# cut-out
surf102 = openmc.model.RectangularParallelepiped(-6.855, 2.285, -25.999, 25.999, -30.999, -29.001)
# cut-out
surf103 = openmc.model.RectangularParallelepiped(2.285, 6.855, 15.995, 20.565, -30.999, -29.001)
# Fuel or Nat-U
surf201 = openmc.model.RectangularParallelepiped(-2.15, 2.15, -2.15, 2.15, -17.204, 17.204)
# Nat-U
surf202 = openmc.model.RectangularParallelepiped(-2.15, 2.15, -2.15, 2.15, -30.104, 30.104)
# Inner void
surf203 = openmc.model.RectangularParallelepiped(-2.17, 2.17, -2.17, 2.17, -57.65, 58.05)
# Frame and inner end block
surf204 = openmc.model.RectangularParallelepiped(-2.25, 2.25, -2.25, 2.25, -59.95, 60.05)
# Outer void
surf205 = openmc.model.RectangularParallelepiped(-2.285, 2.285, -2.285, 2.285, -59.95, 60.05)
# SST outside end block
surf206 = openmc.model.RectangularParallelepiped(-2.285, 2.285, -2.285, 2.285, -61.75, 61.75)
# Small aluminum tube, inner
surf207 = openmc.ZCylinder(surface_id=207, r=1.7)
# Small aluminum tube, outer
surf208 = openmc.ZCylinder(surface_id=208, r=2.0)
# Partial element boundary
surf210 = openmc.XPlane(surface_id=210, x0=-0.716667)
# Array boundary
surf211 = openmc.model.RectangularParallelepiped(-6.855, 2.285, 15.995, 25.135, -61.75, 61.75)
# Array boundary
surf212 = openmc.model.RectangularParallelepiped(2.285, 6.855, 15.995, 20.565, -61.75, 61.75)
# Array boundary
surf213 = openmc.model.RectangularParallelepiped(-15.995, 15.995, -15.995, 15.995, -61.75, 61.75)
# Array boundary
surf214 = openmc.model.RectangularParallelepiped(-6.855, 2.285, -25.135, -15.995, -61.75, 61.75)
# Natural uranium rods
surf1001 = openmc.ZCylinder(surface_id=1001, x0=3.629, y0=21.95, r=1.265)
surf1002 = openmc.ZCylinder(surface_id=1002, x0=6.16, y0=21.95, r=1.265)
surf1003 = openmc.ZCylinder(surface_id=1003, x0=9.465, y0=22.1, r=1.265)
surf1004 = openmc.ZCylinder(surface_id=1004, x0=12.02, y0=22.1, r=1.265)
surf1005 = openmc.ZCylinder(surface_id=1005, x0=14.56, y0=22.1, r=1.265)
surf1006 = openmc.ZCylinder(surface_id=1006, x0=17.1, y0=22.1, r=1.265)
surf1007 = openmc.ZCylinder(surface_id=1007, x0=4.875, y0=24.16, r=1.265)
surf1008 = openmc.ZCylinder(surface_id=1008, x0=7.43, y0=24.16, r=1.265)
surf1009 = openmc.ZCylinder(surface_id=1009, x0=10.741, y0=24.3, r=1.265)
surf1010 = openmc.ZCylinder(surface_id=1010, x0=13.28, y0=24.3, r=1.265)
surf1011 = openmc.ZCylinder(surface_id=1011, x0=15.815, y0=24.3, r=1.265)
surf1012 = openmc.ZCylinder(surface_id=1012, x0=8.2, y0=17.34, r=1.265)
surf1013 = openmc.ZCylinder(surface_id=1013, x0=8.2, y0=19.871, r=1.265)
surf1014 = openmc.ZCylinder(surface_id=1014, x0=10.731, y0=17.34, r=1.265)
surf1015 = openmc.ZCylinder(surface_id=1015, x0=10.731, y0=19.875, r=1.265)
surf1016 = openmc.ZCylinder(surface_id=1016, x0=13.262, y0=19.875, r=1.265)
surf1017 = openmc.ZCylinder(surface_id=1017, x0=15.793, y0=19.875, r=1.265)
surf1018 = openmc.ZCylinder(surface_id=1018, x0=13.262, y0=17.34, r=1.265)
surf1019 = openmc.ZCylinder(surface_id=1019, x0=15.793, y0=17.34, r=1.265)
surf1020 = openmc.ZCylinder(surface_id=1020, x0=18.01, y0=18.63, r=1.265)
surf1021 = openmc.ZCylinder(surface_id=1021, x0=20.22, y0=19.94, r=1.265)
surf1022 = openmc.ZCylinder(surface_id=1022, x0=17.34, y0=15.331, r=1.265)
surf1023 = openmc.ZCylinder(surface_id=1023, x0=17.34, y0=12.8, r=1.265)
surf1024 = openmc.ZCylinder(surface_id=1024, x0=17.34, y0=10.269, r=1.265)
surf1025 = openmc.ZCylinder(surface_id=1025, x0=17.34, y0=7.739, r=1.265)
surf1026 = openmc.ZCylinder(surface_id=1026, x0=17.34, y0=5.208, r=1.265)
surf1027 = openmc.ZCylinder(surface_id=1027, x0=17.34, y0=2.678, r=1.265)
surf1028 = openmc.ZCylinder(surface_id=1028, x0=17.34, y0=0.148, r=1.265)
surf1029 = openmc.ZCylinder(surface_id=1029, x0=17.34, y0=-2.382, r=1.265)
surf1030 = openmc.ZCylinder(surface_id=1030, x0=17.34, y0=-4.913, r=1.265)
surf1031 = openmc.ZCylinder(surface_id=1031, x0=17.34, y0=-7.444, r=1.265)
surf1032 = openmc.ZCylinder(surface_id=1032, x0=17.34, y0=-9.975, r=1.265)
surf1033 = openmc.ZCylinder(surface_id=1033, x0=17.34, y0=-12.506, r=1.265)
surf1034 = openmc.ZCylinder(surface_id=1034, x0=17.34, y0=-15.037, r=1.265)
surf1035 = openmc.ZCylinder(surface_id=1035, x0=22.61, y0=-15.148, r=1.265)
surf1036 = openmc.ZCylinder(surface_id=1036, x0=3.63, y0=-17.34, r=1.265)
surf1037 = openmc.ZCylinder(surface_id=1037, x0=6.1605, y0=-17.34, r=1.265)
surf1038 = openmc.ZCylinder(surface_id=1038, x0=8.691, y0=-17.34, r=1.265)
surf1039 = openmc.ZCylinder(surface_id=1039, x0=11.222, y0=-17.34, r=1.265)
surf1040 = openmc.ZCylinder(surface_id=1040, x0=13.753, y0=-17.34, r=1.265)
surf1041 = openmc.ZCylinder(surface_id=1041, x0=16.284, y0=-17.34, r=1.265)
surf1042 = openmc.ZCylinder(surface_id=1042, x0=18.815, y0=-17.34, r=1.265)
surf1043 = openmc.ZCylinder(surface_id=1043, x0=21.346, y0=-17.34, r=1.265)
surf1044 = openmc.ZCylinder(surface_id=1044, x0=23.877, y0=-17.34, r=1.265)
surf1045 = openmc.ZCylinder(surface_id=1045, x0=4.895, y0=-19.532, r=1.265)
surf1046 = openmc.ZCylinder(surface_id=1046, x0=7.4255, y0=-19.532, r=1.265)
surf1047 = openmc.ZCylinder(surface_id=1047, x0=9.956, y0=-19.532, r=1.265)
surf1048 = openmc.ZCylinder(surface_id=1048, x0=12.4865, y0=-19.532, r=1.265)
surf1049 = openmc.ZCylinder(surface_id=1049, x0=15.017, y0=-19.532, r=1.265)
surf1050 = openmc.ZCylinder(surface_id=1050, x0=17.548, y0=-19.532, r=1.265)
surf1051 = openmc.ZCylinder(surface_id=1051, x0=20.079, y0=-19.532, r=1.265)
surf1052 = openmc.ZCylinder(surface_id=1052, x0=22.61, y0=-19.532, r=1.265)
surf1053 = openmc.ZCylinder(surface_id=1053, x0=3.63, y0=-21.724, r=1.265)
surf1054 = openmc.ZCylinder(surface_id=1054, x0=6.1605, y0=-21.724, r=1.265)
surf1055 = openmc.ZCylinder(surface_id=1055, x0=8.691, y0=-21.724, r=1.265)
surf1056 = openmc.ZCylinder(surface_id=1056, x0=11.222, y0=-21.724, r=1.265)
surf1057 = openmc.ZCylinder(surface_id=1057, x0=13.753, y0=-21.724, r=1.265)
surf1058 = openmc.ZCylinder(surface_id=1058, x0=16.284, y0=-21.724, r=1.265)
surf1059 = openmc.ZCylinder(surface_id=1059, x0=18.815, y0=-21.724, r=1.265)
surf1060 = openmc.ZCylinder(surface_id=1060, x0=4.895, y0=-23.93, r=1.265)
surf1061 = openmc.ZCylinder(surface_id=1061, x0=7.4255, y0=-23.93, r=1.265)
surf1062 = openmc.ZCylinder(surface_id=1062, x0=9.956, y0=-23.93, r=1.265)
surf1063 = openmc.ZCylinder(surface_id=1063, x0=12.4865, y0=-23.93, r=1.265)
surf1064 = openmc.ZCylinder(surface_id=1064, x0=15.017, y0=-23.93, r=1.265)
surf1065 = openmc.ZCylinder(surface_id=1065, x0=19.532, y0=16.596, r=1.265)
surf1066 = openmc.ZCylinder(surface_id=1066, x0=19.532, y0=14.065, r=1.265)
surf1067 = openmc.ZCylinder(surface_id=1067, x0=19.532, y0=11.5345, r=1.265)
surf1068 = openmc.ZCylinder(surface_id=1068, x0=19.532, y0=9.004, r=1.265)
surf1069 = openmc.ZCylinder(surface_id=1069, x0=19.532, y0=6.4738, r=1.265)
surf1070 = openmc.ZCylinder(surface_id=1070, x0=19.532, y0=3.9433, r=1.265)
surf1071 = openmc.ZCylinder(surface_id=1071, x0=19.532, y0=1.413, r=1.265)
surf1072 = openmc.ZCylinder(surface_id=1072, x0=19.532, y0=-1.117, r=1.265)
surf1073 = openmc.ZCylinder(surface_id=1073, x0=19.532, y0=-3.6475, r=1.265)
surf1074 = openmc.ZCylinder(surface_id=1074, x0=19.532, y0=-6.1785, r=1.265)
surf1075 = openmc.ZCylinder(surface_id=1075, x0=19.532, y0=-8.7095, r=1.265)
surf1076 = openmc.ZCylinder(surface_id=1076, x0=19.532, y0=-11.2405, r=1.265)
surf1077 = openmc.ZCylinder(surface_id=1077, x0=19.532, y0=-13.7715, r=1.265)
surf1078 = openmc.ZCylinder(surface_id=1078, x0=21.724, y0=17.862, r=1.265)
surf1079 = openmc.ZCylinder(surface_id=1079, x0=21.724, y0=15.331, r=1.265)
surf1080 = openmc.ZCylinder(surface_id=1080, x0=21.724, y0=12.8, r=1.265)
surf1081 = openmc.ZCylinder(surface_id=1081, x0=21.724, y0=10.269, r=1.265)
surf1082 = openmc.ZCylinder(surface_id=1082, x0=21.724, y0=7.739, r=1.265)
surf1083 = openmc.ZCylinder(surface_id=1083, x0=21.724, y0=5.208, r=1.265)
surf1084 = openmc.ZCylinder(surface_id=1084, x0=21.724, y0=2.678, r=1.265)
surf1085 = openmc.ZCylinder(surface_id=1085, x0=21.724, y0=0.148, r=1.265)
surf1086 = openmc.ZCylinder(surface_id=1086, x0=21.724, y0=-2.382, r=1.265)
surf1087 = openmc.ZCylinder(surface_id=1087, x0=21.724, y0=-4.913, r=1.265)
surf1088 = openmc.ZCylinder(surface_id=1088, x0=21.724, y0=-7.444, r=1.265)
surf1089 = openmc.ZCylinder(surface_id=1089, x0=21.724, y0=-9.975, r=1.265)
surf1090 = openmc.ZCylinder(surface_id=1090, x0=21.724, y0=-12.506, r=1.265)
surf1091 = openmc.ZCylinder(surface_id=1091, x0=23.93, y0=16.5947, r=1.265)
surf1092 = openmc.ZCylinder(surface_id=1092, x0=23.93, y0=14.0646, r=1.265)
surf1093 = openmc.ZCylinder(surface_id=1093, x0=23.93, y0=11.5345, r=1.265)
surf1094 = openmc.ZCylinder(surface_id=1094, x0=23.93, y0=9.004, r=1.265)
surf1095 = openmc.ZCylinder(surface_id=1095, x0=23.93, y0=6.4738, r=1.265)
surf1096 = openmc.ZCylinder(surface_id=1096, x0=23.93, y0=3.9433, r=1.265)
surf1097 = openmc.ZCylinder(surface_id=1097, x0=23.93, y0=1.413, r=1.265)
surf1098 = openmc.ZCylinder(surface_id=1098, x0=23.93, y0=-1.117, r=1.265)
surf1099 = openmc.ZCylinder(surface_id=1099, x0=23.93, y0=-3.6475, r=1.265)
surf1100 = openmc.ZCylinder(surface_id=1100, x0=23.93, y0=-6.1785, r=1.265)
surf1101 = openmc.ZCylinder(surface_id=1101, x0=23.93, y0=-8.7095, r=1.265)
surf1102 = openmc.ZCylinder(surface_id=1102, x0=23.93, y0=-11.2405, r=1.265)
surf1103 = openmc.ZCylinder(surface_id=1103, x0=-17.34, y0=15.231, r=1.265)
surf1104 = openmc.ZCylinder(surface_id=1104, x0=-17.34, y0=12.7, r=1.265)
surf1105 = openmc.ZCylinder(surface_id=1105, x0=-17.34, y0=10.169, r=1.265)
surf1106 = openmc.ZCylinder(surface_id=1106, x0=-17.34, y0=7.6385, r=1.265)
surf1107 = openmc.ZCylinder(surface_id=1107, x0=-17.34, y0=5.1081, r=1.265)
surf1108 = openmc.ZCylinder(surface_id=1108, x0=-17.34, y0=2.578, r=1.265)
surf1109 = openmc.ZCylinder(surface_id=1109, x0=-17.34, y0=0.048, r=1.265)
surf1110 = openmc.ZCylinder(surface_id=1110, x0=-17.34, y0=-2.482, r=1.265)
surf1111 = openmc.ZCylinder(surface_id=1111, x0=-17.34, y0=-5.013, r=1.265)
surf1112 = openmc.ZCylinder(surface_id=1112, x0=-17.34, y0=-7.544, r=1.265)
surf1113 = openmc.ZCylinder(surface_id=1113, x0=-17.34, y0=-10.075, r=1.265)
surf1114 = openmc.ZCylinder(surface_id=1114, x0=-17.34, y0=-12.606, r=1.265)
surf1115 = openmc.ZCylinder(surface_id=1115, x0=-17.34, y0=-15.137, r=1.265)
surf1116 = openmc.ZCylinder(surface_id=1116, x0=-19.532, y0=19.0251, r=1.265)
surf1117 = openmc.ZCylinder(surface_id=1117, x0=-19.532, y0=16.49505, r=1.265)
surf1118 = openmc.ZCylinder(surface_id=1118, x0=-19.532, y0=13.965, r=1.265)
surf1119 = openmc.ZCylinder(surface_id=1119, x0=-19.532, y0=11.4345, r=1.265)
surf1120 = openmc.ZCylinder(surface_id=1120, x0=-19.532, y0=8.904, r=1.265)
surf1121 = openmc.ZCylinder(surface_id=1121, x0=-19.532, y0=6.3738, r=1.265)
surf1122 = openmc.ZCylinder(surface_id=1122, x0=-19.532, y0=3.8433, r=1.265)
surf1123 = openmc.ZCylinder(surface_id=1123, x0=-19.532, y0=1.313, r=1.265)
surf1124 = openmc.ZCylinder(surface_id=1124, x0=-19.532, y0=-1.217, r=1.265)
surf1125 = openmc.ZCylinder(surface_id=1125, x0=-19.532, y0=-3.7475, r=1.265)
surf1126 = openmc.ZCylinder(surface_id=1126, x0=-19.532, y0=-6.2785, r=1.265)
surf1127 = openmc.ZCylinder(surface_id=1127, x0=-19.532, y0=-8.8095, r=1.265)
surf1128 = openmc.ZCylinder(surface_id=1128, x0=-19.532, y0=-11.3405, r=1.265)
surf1129 = openmc.ZCylinder(surface_id=1129, x0=-19.532, y0=-13.871, r=1.265)
surf1130 = openmc.ZCylinder(surface_id=1130, x0=-19.532, y0=-16.4015, r=1.265)
surf1131 = openmc.ZCylinder(surface_id=1131, x0=-19.532, y0=-18.932, r=1.265)
surf1132 = openmc.ZCylinder(surface_id=1132, x0=-21.724, y0=17.7611, r=1.265)
surf1133 = openmc.ZCylinder(surface_id=1133, x0=-21.724, y0=15.231, r=1.265)
surf1134 = openmc.ZCylinder(surface_id=1134, x0=-21.724, y0=12.7, r=1.265)
surf1135 = openmc.ZCylinder(surface_id=1135, x0=-21.724, y0=10.169, r=1.265)
surf1136 = openmc.ZCylinder(surface_id=1136, x0=-21.724, y0=7.6385, r=1.265)
surf1137 = openmc.ZCylinder(surface_id=1137, x0=-21.724, y0=5.1081, r=1.265)
surf1138 = openmc.ZCylinder(surface_id=1138, x0=-21.724, y0=2.578, r=1.265)
surf1139 = openmc.ZCylinder(surface_id=1139, x0=-21.724, y0=0.048, r=1.265)
surf1140 = openmc.ZCylinder(surface_id=1140, x0=-21.724, y0=-2.482, r=1.265)
surf1141 = openmc.ZCylinder(surface_id=1141, x0=-21.724, y0=-5.013, r=1.265)
surf1142 = openmc.ZCylinder(surface_id=1142, x0=-21.724, y0=-7.544, r=1.265)
surf1143 = openmc.ZCylinder(surface_id=1143, x0=-21.724, y0=-10.075, r=1.265)
surf1144 = openmc.ZCylinder(surface_id=1144, x0=-21.724, y0=-12.606, r=1.265)
surf1145 = openmc.ZCylinder(surface_id=1145, x0=-21.724, y0=-15.137, r=1.265)
surf1146 = openmc.ZCylinder(surface_id=1146, x0=-21.724, y0=-17.6675, r=1.265)
surf1147 = openmc.ZCylinder(surface_id=1147, x0=-21.724, y0=-20.198, r=1.265)
surf1148 = openmc.ZCylinder(surface_id=1148, x0=-23.93, y0=16.49461, r=1.265)
surf1149 = openmc.ZCylinder(surface_id=1149, x0=-23.93, y0=13.9646, r=1.265)
surf1150 = openmc.ZCylinder(surface_id=1150, x0=-23.93, y0=11.4345, r=1.265)
surf1151 = openmc.ZCylinder(surface_id=1151, x0=-23.93, y0=8.904, r=1.265)
surf1152 = openmc.ZCylinder(surface_id=1152, x0=-23.93, y0=6.3738, r=1.265)
surf1153 = openmc.ZCylinder(surface_id=1153, x0=-23.93, y0=3.8433, r=1.265)
surf1154 = openmc.ZCylinder(surface_id=1154, x0=-23.93, y0=1.313, r=1.265)
surf1155 = openmc.ZCylinder(surface_id=1155, x0=-23.93, y0=-1.217, r=1.265)
surf1156 = openmc.ZCylinder(surface_id=1156, x0=-23.93, y0=-3.7475, r=1.265)
surf1157 = openmc.ZCylinder(surface_id=1157, x0=-23.93, y0=-6.2785, r=1.265)
surf1158 = openmc.ZCylinder(surface_id=1158, x0=-23.93, y0=-8.8095, r=1.265)
surf1159 = openmc.ZCylinder(surface_id=1159, x0=-23.93, y0=-11.3405, r=1.265)
surf1160 = openmc.ZCylinder(surface_id=1160, x0=-23.93, y0=-13.8706, r=1.265)
surf1161 = openmc.ZCylinder(surface_id=1161, x0=-23.93, y0=-16.4007, r=1.265)
surf1162 = openmc.ZCylinder(surface_id=1162, x0=-8.2, y0=-17.34, r=1.265)
surf1163 = openmc.ZCylinder(surface_id=1163, x0=-10.731, y0=-17.34, r=1.265)
surf1164 = openmc.ZCylinder(surface_id=1164, x0=-13.262, y0=-17.34, r=1.265)
surf1165 = openmc.ZCylinder(surface_id=1165, x0=-15.793, y0=-17.34, r=1.265)
surf1166 = openmc.ZCylinder(surface_id=1166, x0=-9.465, y0=-19.532, r=1.265)
surf1167 = openmc.ZCylinder(surface_id=1167, x0=-11.996, y0=-19.532, r=1.265)
surf1168 = openmc.ZCylinder(surface_id=1168, x0=-14.5265, y0=-19.532, r=1.265)
surf1169 = openmc.ZCylinder(surface_id=1169, x0=-17.057, y0=-19.532, r=1.265)
surf1170 = openmc.ZCylinder(surface_id=1170, x0=-8.2, y0=-21.724, r=1.265)
surf1171 = openmc.ZCylinder(surface_id=1171, x0=-10.731, y0=-21.724, r=1.265)
surf1172 = openmc.ZCylinder(surface_id=1172, x0=-13.262, y0=-21.724, r=1.265)
surf1173 = openmc.ZCylinder(surface_id=1173, x0=-15.793, y0=-21.724, r=1.265)
surf1174 = openmc.ZCylinder(surface_id=1174, x0=-18.324, y0=-21.724, r=1.265)
surf1175 = openmc.ZCylinder(surface_id=1175, x0=-9.465, y0=-23.93, r=1.265)
surf1176 = openmc.ZCylinder(surface_id=1176, x0=-11.996, y0=-23.93, r=1.265)
surf1177 = openmc.ZCylinder(surface_id=1177, x0=-14.527, y0=-23.93, r=1.265)
surf1178 = openmc.ZCylinder(surface_id=1178, x0=-17.058, y0=-23.931, r=1.265)
surf1179 = openmc.ZCylinder(surface_id=1179, x0=-19.589, y0=-23.931, r=1.265)
surf1180 = openmc.ZCylinder(surface_id=1180, x0=-8.2, y0=17.37, r=1.265)
surf1181 = openmc.ZCylinder(surface_id=1181, x0=-10.731, y0=17.37, r=1.265)
surf1182 = openmc.ZCylinder(surface_id=1182, x0=-13.262, y0=17.37, r=1.265)
surf1183 = openmc.ZCylinder(surface_id=1183, x0=-15.793, y0=17.37, r=1.265)
surf1184 = openmc.ZCylinder(surface_id=1184, x0=-9.465, y0=19.562, r=1.265)
surf1185 = openmc.ZCylinder(surface_id=1185, x0=-11.996, y0=19.562, r=1.265)
surf1186 = openmc.ZCylinder(surface_id=1186, x0=-14.527, y0=19.562, r=1.265)
surf1187 = openmc.ZCylinder(surface_id=1187, x0=-17.058, y0=19.562, r=1.265)
surf1188 = openmc.ZCylinder(surface_id=1188, x0=-8.2, y0=21.754, r=1.265)
surf1189 = openmc.ZCylinder(surface_id=1189, x0=-10.731, y0=21.754, r=1.265)
surf1190 = openmc.ZCylinder(surface_id=1190, x0=-13.262, y0=21.754, r=1.265)
surf1191 = openmc.ZCylinder(surface_id=1191, x0=-15.793, y0=21.754, r=1.265)
surf1192 = openmc.ZCylinder(surface_id=1192, x0=-18.324, y0=21.754, r=1.265)
surf1193 = openmc.ZCylinder(surface_id=1193, x0=-20.855, y0=21.754, r=1.265)
surf1194 = openmc.ZCylinder(surface_id=1194, x0=-9.465, y0=23.96, r=1.265)
surf1195 = openmc.ZCylinder(surface_id=1195, x0=-11.996, y0=23.96, r=1.265)
surf1196 = openmc.ZCylinder(surface_id=1196, x0=-14.527, y0=23.96, r=1.265)
surf1197 = openmc.ZCylinder(surface_id=1197, x0=-17.058, y0=23.961, r=1.265)

# Z-plane surfaces for bounded cylinders
surf207_zmin = openmc.ZPlane(surface_id=2197, z0=-57.65)
surf207_zmax = openmc.ZPlane(surface_id=2198, z0=-30.104)
surf208_zmin = openmc.ZPlane(surface_id=2199, z0=-57.65)
surf208_zmax = openmc.ZPlane(surface_id=2200, z0=-30.104)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u31_cell0 = openmc.Cell(fill=mat2)
u31_cell0.region = -surf201 & -surf202
u31_cell1 = openmc.Cell(fill=mat2)
u31_cell1.region = +surf201 & -surf202
u31_cell2 = openmc.Cell()
u31_cell2.region = +surf202 & -surf203 & (-surf207 & +surf207_zmin & -surf207_zmax)
u31_cell3 = openmc.Cell(fill=mat7)
u31_cell3.region = +surf202 & -surf203 & (+surf207 | -surf207_zmin | +surf207_zmax) & (-surf208 & +surf208_zmin & -surf208_zmax)
u31_cell4 = openmc.Cell()
u31_cell4.region = +surf202 & -surf203 & (+surf208 | -surf208_zmin | +surf208_zmax)
u31_cell5 = openmc.Cell(fill=mat4)
u31_cell5.region = +surf203 & -surf204
u31_cell6 = openmc.Cell(fill=mat5)
u31_cell6.region = +surf204 & +surf205 & -surf206
universe31 = openmc.Universe(universe_id=31, cells=[u31_cell0, u31_cell1, u31_cell2, u31_cell3, u31_cell4, u31_cell5, u31_cell6])

u32_cell0 = openmc.Cell(fill=mat1)
u32_cell0.region = -surf201 & -surf202
u32_cell1 = openmc.Cell(fill=mat2)
u32_cell1.region = +surf201 & -surf202
u32_cell2 = openmc.Cell()
u32_cell2.region = +surf202 & -surf203 & (-surf207 & +surf207_zmin & -surf207_zmax)
u32_cell3 = openmc.Cell(fill=mat7)
u32_cell3.region = +surf202 & -surf203 & (+surf207 | -surf207_zmin | +surf207_zmax) & (-surf208 & +surf208_zmin & -surf208_zmax)
u32_cell4 = openmc.Cell()
u32_cell4.region = +surf202 & -surf203 & (+surf208 | -surf208_zmin | +surf208_zmax)
u32_cell5 = openmc.Cell(fill=mat4)
u32_cell5.region = +surf203 & -surf204
u32_cell6 = openmc.Cell(fill=mat5)
u32_cell6.region = +surf204 & +surf205 & -surf206
universe32 = openmc.Universe(universe_id=32, cells=[u32_cell0, u32_cell1, u32_cell2, u32_cell3, u32_cell4, u32_cell5, u32_cell6])

u41_cell0 = openmc.Cell(fill=mat1)
u41_cell0.region = -surf201 & -surf202 & +surf210
u41_cell1 = openmc.Cell(fill=mat3)
u41_cell1.region = -surf201 & -surf202 & -surf210
u41_cell2 = openmc.Cell(fill=mat2)
u41_cell2.region = +surf201 & -surf202
u41_cell3 = openmc.Cell()
u41_cell3.region = +surf202 & -surf203 & (-surf207 & +surf207_zmin & -surf207_zmax)
u41_cell4 = openmc.Cell(fill=mat7)
u41_cell4.region = +surf202 & -surf203 & (+surf207 | -surf207_zmin | +surf207_zmax) & (-surf208 & +surf208_zmin & -surf208_zmax)
u41_cell5 = openmc.Cell()
u41_cell5.region = +surf202 & -surf203 & (+surf208 | -surf208_zmin | +surf208_zmax)
u41_cell6 = openmc.Cell(fill=mat4)
u41_cell6.region = +surf203 & -surf204
u41_cell7 = openmc.Cell(fill=mat5)
u41_cell7.region = +surf204 & +surf205 & -surf206
universe41 = openmc.Universe(universe_id=41, cells=[u41_cell0, u41_cell1, u41_cell2, u41_cell3, u41_cell4, u41_cell5, u41_cell6, u41_cell7])

# Lattice 99: 7x11 array
lattice99 = openmc.RectLattice(lattice_id=99)
lattice99.lower_left = [-15.995, -25.135]
lattice99.pitch = [4.570000, 4.570000]
lattice99.universes = [
    [universe31, universe31, universe31, universe31, universe31, universe31, universe31],
    [universe31, universe31, universe31, universe31, universe31, universe31, universe31],
    [universe31, universe31, universe31, universe31, universe31, universe31, universe31],
    [universe32, universe32, universe32, universe32, universe31, universe31, universe31],
    [universe32, universe32, universe32, universe32, universe31, universe31, universe32],
    [universe32, universe32, universe32, universe32, universe32, universe31, universe32],
    [universe32, universe32, universe32, universe32, universe32, universe41, universe32],
    [universe32, universe32, universe32, universe32, universe32, universe32, universe32],
    [universe32, universe32, universe32, universe32, universe31, universe32, universe32],
    [universe32, universe32, universe32, universe32, universe31, universe32, universe32],
    [universe31, universe31, universe31, universe31, universe31, universe31, universe32],
]
universe99 = openmc.Universe(universe_id=99)
universe99.add_cell(openmc.Cell(fill=lattice99))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Cncrt
cell1 = openmc.Cell(cell_id=1, fill=mat8)
cell1.region = +surf1 & -surf2

# Steel
cell2 = openmc.Cell(cell_id=2, fill=mat6)
cell2.region = -surf3

# Steel
cell3 = openmc.Cell(cell_id=3, fill=mat6)
cell3.region = +surf3 & -surf4

# Steel
cell4 = openmc.Cell(cell_id=4, fill=mat6)
cell4.region = +surf3 & -surf5

# Steel
cell5 = openmc.Cell(cell_id=5, fill=mat6)
cell5.region = +surf4 & +surf5 & -surf6

# Steel
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf6 & -surf7

# Steel
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = +surf3 & -surf11

# Steel
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = +surf3 & -surf12

# Steel
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = +surf3 & -surf13

# Steel
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = +surf3 & -surf14

# Steel
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = +surf3 & -surf15

# Steel
cell12 = openmc.Cell(cell_id=12, fill=mat6)
cell12.region = +surf3 & -surf16

# Steel
cell13 = openmc.Cell(cell_id=13, fill=mat6)
cell13.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf21

# Steel
cell14 = openmc.Cell(cell_id=14, fill=mat6)
cell14.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf22

# Steel
cell15 = openmc.Cell(cell_id=15, fill=mat6)
cell15.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf23

# Steel
cell16 = openmc.Cell(cell_id=16, fill=mat6)
cell16.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf24

# Steel
cell17 = openmc.Cell(cell_id=17, fill=mat6)
cell17.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf25

# Steel
cell18 = openmc.Cell(cell_id=18, fill=mat6)
cell18.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf26

# Steel
cell19 = openmc.Cell(cell_id=19, fill=mat6)
cell19.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf31

# Steel
cell20 = openmc.Cell(cell_id=20, fill=mat6)
cell20.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf32

# Steel
cell21 = openmc.Cell(cell_id=21, fill=mat6)
cell21.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf33

# Steel
cell22 = openmc.Cell(cell_id=22, fill=mat6)
cell22.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf34

# Steel
cell23 = openmc.Cell(cell_id=23, fill=mat6)
cell23.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf35

# Steel
cell24 = openmc.Cell(cell_id=24, fill=mat6)
cell24.region = +surf3 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & -surf36

# Steel
cell25 = openmc.Cell(cell_id=25, fill=mat6)
cell25.region = +surf54 & -surf41 & +surf100

# Steel
cell26 = openmc.Cell(cell_id=26, fill=mat6)
cell26.region = +surf41 & -surf42 & +surf100

# Steel
cell27 = openmc.Cell(cell_id=27, fill=mat6)
cell27.region = +surf42 & -surf43 & +surf100

# Steel
cell28 = openmc.Cell(cell_id=28, fill=mat6)
cell28.region = +surf43 & -surf44 & +surf100

# Steel
cell29 = openmc.Cell(cell_id=29, fill=mat6)
cell29.region = +surf44 & -surf45 & +surf100

# Steel
cell30 = openmc.Cell(cell_id=30, fill=mat6)
cell30.region = +surf45 & -surf46 & +surf100

# Steel
cell31 = openmc.Cell(cell_id=31, fill=mat6)
cell31.region = +surf46 & -surf47 & +surf100

# Steel
cell32 = openmc.Cell(cell_id=32, fill=mat6)
cell32.region = +surf47 & -surf48 & +surf100

# Steel
cell33 = openmc.Cell(cell_id=33, fill=mat6)
cell33.region = +surf48 & -surf49 & +surf100

# Steel
cell34 = openmc.Cell(cell_id=34, fill=mat6)
cell34.region = +surf49 & -surf50 & +surf100

# Steel
cell35 = openmc.Cell(cell_id=35, fill=mat6)
cell35.region = +surf50 & -surf51 & +surf100

# Steel
cell36 = openmc.Cell(cell_id=36, fill=mat6)
cell36.region = +surf51 & -surf52 & +surf100

# Steel
cell37 = openmc.Cell(cell_id=37, fill=mat6)
cell37.region = +surf52 & -surf53 & +surf100

# Steel
cell38 = openmc.Cell(cell_id=38, fill=mat6)
cell38.region = +surf53 & -surf54 & +surf100

# Arry
cell39 = openmc.Cell(cell_id=39, fill=universe99)
cell39.region = +surf3 & -surf211

# Arry
cell40 = openmc.Cell(cell_id=40, fill=universe99)
cell40.region = +surf3 & +surf211 & -surf212

# Arry
cell41 = openmc.Cell(cell_id=41, fill=universe99)
cell41.region = +surf3 & +surf212 & -surf213

# Arry
cell42 = openmc.Cell(cell_id=42, fill=universe99)
cell42.region = +surf3 & +surf213 & -surf214

# Alum
cell43 = openmc.Cell(cell_id=43, fill=mat7)
cell43.region = +surf3 & +surf61 & -surf81

# Alum
cell44 = openmc.Cell(cell_id=44, fill=mat7)
cell44.region = +surf3 & +surf62 & -surf82

# Alum
cell45 = openmc.Cell(cell_id=45, fill=mat7)
cell45.region = +surf3 & +surf63 & -surf83

# Alum
cell46 = openmc.Cell(cell_id=46, fill=mat7)
cell46.region = +surf3 & +surf64 & -surf84

# Alum
cell47 = openmc.Cell(cell_id=47, fill=mat7)
cell47.region = +surf3 & +surf65 & -surf85

# Alum
cell48 = openmc.Cell(cell_id=48, fill=mat7)
cell48.region = +surf3 & +surf66 & -surf86

# Alum
cell49 = openmc.Cell(cell_id=49, fill=mat7)
cell49.region = +surf3 & +surf67 & -surf87

# Alum
cell50 = openmc.Cell(cell_id=50, fill=mat7)
cell50.region = +surf3 & +surf68 & -surf88

# Alum
cell51 = openmc.Cell(cell_id=51, fill=mat7)
cell51.region = +surf3 & +surf69 & -surf89

# Alum
cell52 = openmc.Cell(cell_id=52, fill=mat7)
cell52.region = +surf3 & +surf70 & -surf90

# Alum
cell53 = openmc.Cell(cell_id=53, fill=mat7)
cell53.region = +surf3 & +surf71 & -surf91

# Alum
cell54 = openmc.Cell(cell_id=54, fill=mat7)
cell54.region = +surf3 & +surf72 & -surf92

# Alum
cell55 = openmc.Cell(cell_id=55, fill=mat7)
cell55.region = -surf100 & +surf101 & +surf102 & +surf103

# NatU
cell56 = openmc.Cell(cell_id=56, fill=mat2)
cell56.region = +surf100 & -surf1001

# NatU
cell57 = openmc.Cell(cell_id=57, fill=mat2)
cell57.region = +surf100 & -surf1002

# NatU
cell58 = openmc.Cell(cell_id=58, fill=mat2)
cell58.region = +surf100 & -surf1003

# NatU
cell59 = openmc.Cell(cell_id=59, fill=mat2)
cell59.region = +surf100 & -surf1004

# NatU
cell60 = openmc.Cell(cell_id=60, fill=mat2)
cell60.region = +surf100 & -surf1005

# NatU
cell61 = openmc.Cell(cell_id=61, fill=mat2)
cell61.region = +surf100 & -surf1006

# NatU
cell62 = openmc.Cell(cell_id=62, fill=mat2)
cell62.region = +surf100 & -surf1007

# NatU
cell63 = openmc.Cell(cell_id=63, fill=mat2)
cell63.region = +surf100 & -surf1008

# NatU
cell64 = openmc.Cell(cell_id=64, fill=mat2)
cell64.region = +surf100 & -surf1009

# NatU
cell65 = openmc.Cell(cell_id=65, fill=mat2)
cell65.region = +surf100 & -surf1010

# NatU
cell66 = openmc.Cell(cell_id=66, fill=mat2)
cell66.region = +surf100 & -surf1011

# NatU
cell67 = openmc.Cell(cell_id=67, fill=mat2)
cell67.region = +surf100 & -surf1012

# NatU
cell68 = openmc.Cell(cell_id=68, fill=mat2)
cell68.region = +surf100 & -surf1013

# NatU
cell69 = openmc.Cell(cell_id=69, fill=mat2)
cell69.region = +surf100 & -surf1014

# NatU
cell70 = openmc.Cell(cell_id=70, fill=mat2)
cell70.region = +surf100 & -surf1015

# NatU
cell71 = openmc.Cell(cell_id=71, fill=mat2)
cell71.region = +surf100 & -surf1016

# NatU
cell72 = openmc.Cell(cell_id=72, fill=mat2)
cell72.region = +surf100 & -surf1017

# NatU
cell73 = openmc.Cell(cell_id=73, fill=mat2)
cell73.region = +surf100 & -surf1018

# NatU
cell74 = openmc.Cell(cell_id=74, fill=mat2)
cell74.region = +surf100 & -surf1019

# NatU
cell75 = openmc.Cell(cell_id=75, fill=mat2)
cell75.region = +surf100 & -surf1020

# NatU
cell76 = openmc.Cell(cell_id=76, fill=mat2)
cell76.region = +surf100 & -surf1021

# NatU
cell77 = openmc.Cell(cell_id=77, fill=mat2)
cell77.region = +surf100 & -surf1022

# NatU
cell78 = openmc.Cell(cell_id=78, fill=mat2)
cell78.region = +surf100 & -surf1023

# NatU
cell79 = openmc.Cell(cell_id=79, fill=mat2)
cell79.region = +surf100 & -surf1024

# NatU
cell80 = openmc.Cell(cell_id=80, fill=mat2)
cell80.region = +surf100 & -surf1025

# NatU
cell81 = openmc.Cell(cell_id=81, fill=mat2)
cell81.region = +surf100 & -surf1026

# NatU
cell82 = openmc.Cell(cell_id=82, fill=mat2)
cell82.region = +surf100 & -surf1027

# NatU
cell83 = openmc.Cell(cell_id=83, fill=mat2)
cell83.region = +surf100 & -surf1028

# NatU
cell84 = openmc.Cell(cell_id=84, fill=mat2)
cell84.region = +surf100 & -surf1029

# NatU
cell85 = openmc.Cell(cell_id=85, fill=mat2)
cell85.region = +surf100 & -surf1030

# NatU
cell86 = openmc.Cell(cell_id=86, fill=mat2)
cell86.region = +surf100 & -surf1031

# NatU
cell87 = openmc.Cell(cell_id=87, fill=mat2)
cell87.region = +surf100 & -surf1032

# NatU
cell88 = openmc.Cell(cell_id=88, fill=mat2)
cell88.region = +surf100 & -surf1033

# NatU
cell89 = openmc.Cell(cell_id=89, fill=mat2)
cell89.region = +surf100 & -surf1034

# NatU
cell90 = openmc.Cell(cell_id=90, fill=mat2)
cell90.region = +surf100 & -surf1035

# NatU
cell91 = openmc.Cell(cell_id=91, fill=mat2)
cell91.region = +surf100 & -surf1036

# NatU
cell92 = openmc.Cell(cell_id=92, fill=mat2)
cell92.region = +surf100 & -surf1037

# NatU
cell93 = openmc.Cell(cell_id=93, fill=mat2)
cell93.region = +surf100 & -surf1038

# NatU
cell94 = openmc.Cell(cell_id=94, fill=mat2)
cell94.region = +surf100 & -surf1039

# NatU
cell95 = openmc.Cell(cell_id=95, fill=mat2)
cell95.region = +surf100 & -surf1040

# NatU
cell96 = openmc.Cell(cell_id=96, fill=mat2)
cell96.region = +surf100 & -surf1041

# NatU
cell97 = openmc.Cell(cell_id=97, fill=mat2)
cell97.region = +surf100 & -surf1042

# NatU
cell98 = openmc.Cell(cell_id=98, fill=mat2)
cell98.region = +surf100 & -surf1043

# NatU
cell99 = openmc.Cell(cell_id=99, fill=mat2)
cell99.region = +surf100 & -surf1044

# NatU
cell100 = openmc.Cell(cell_id=100, fill=mat2)
cell100.region = +surf100 & -surf1045

# NatU
cell101 = openmc.Cell(cell_id=101, fill=mat2)
cell101.region = +surf100 & -surf1046

# NatU
cell102 = openmc.Cell(cell_id=102, fill=mat2)
cell102.region = +surf100 & -surf1047

# NatU
cell103 = openmc.Cell(cell_id=103, fill=mat2)
cell103.region = +surf100 & -surf1048

# NatU
cell104 = openmc.Cell(cell_id=104, fill=mat2)
cell104.region = +surf100 & -surf1049

# NatU
cell105 = openmc.Cell(cell_id=105, fill=mat2)
cell105.region = +surf100 & -surf1050

# NatU
cell106 = openmc.Cell(cell_id=106, fill=mat2)
cell106.region = +surf100 & -surf1051

# NatU
cell107 = openmc.Cell(cell_id=107, fill=mat2)
cell107.region = +surf100 & -surf1052

# NatU
cell108 = openmc.Cell(cell_id=108, fill=mat2)
cell108.region = +surf100 & -surf1053

# NatU
cell109 = openmc.Cell(cell_id=109, fill=mat2)
cell109.region = +surf100 & -surf1054

# NatU
cell110 = openmc.Cell(cell_id=110, fill=mat2)
cell110.region = +surf100 & -surf1055

# NatU
cell111 = openmc.Cell(cell_id=111, fill=mat2)
cell111.region = +surf100 & -surf1056

# NatU
cell112 = openmc.Cell(cell_id=112, fill=mat2)
cell112.region = +surf100 & -surf1057

# NatU
cell113 = openmc.Cell(cell_id=113, fill=mat2)
cell113.region = +surf100 & -surf1058

# NatU
cell114 = openmc.Cell(cell_id=114, fill=mat2)
cell114.region = +surf100 & -surf1059

# NatU
cell115 = openmc.Cell(cell_id=115, fill=mat2)
cell115.region = +surf100 & -surf1060

# NatU
cell116 = openmc.Cell(cell_id=116, fill=mat2)
cell116.region = +surf100 & -surf1061

# NatU
cell117 = openmc.Cell(cell_id=117, fill=mat2)
cell117.region = +surf100 & -surf1062

# NatU
cell118 = openmc.Cell(cell_id=118, fill=mat2)
cell118.region = +surf100 & -surf1063

# NatU
cell119 = openmc.Cell(cell_id=119, fill=mat2)
cell119.region = +surf100 & -surf1064

# NatU
cell120 = openmc.Cell(cell_id=120, fill=mat2)
cell120.region = +surf100 & -surf1065

# NatU
cell121 = openmc.Cell(cell_id=121, fill=mat2)
cell121.region = +surf100 & -surf1066

# NatU
cell122 = openmc.Cell(cell_id=122, fill=mat2)
cell122.region = +surf100 & -surf1067

# NatU
cell123 = openmc.Cell(cell_id=123, fill=mat2)
cell123.region = +surf100 & -surf1068

# NatU
cell124 = openmc.Cell(cell_id=124, fill=mat2)
cell124.region = +surf100 & -surf1069

# NatU
cell125 = openmc.Cell(cell_id=125, fill=mat2)
cell125.region = +surf100 & -surf1070

# NatU
cell126 = openmc.Cell(cell_id=126, fill=mat2)
cell126.region = +surf100 & -surf1071

# NatU
cell127 = openmc.Cell(cell_id=127, fill=mat2)
cell127.region = +surf100 & -surf1072

# NatU
cell128 = openmc.Cell(cell_id=128, fill=mat2)
cell128.region = +surf100 & -surf1073

# NatU
cell129 = openmc.Cell(cell_id=129, fill=mat2)
cell129.region = +surf100 & -surf1074

# NatU
cell130 = openmc.Cell(cell_id=130, fill=mat2)
cell130.region = +surf100 & -surf1075

# NatU
cell131 = openmc.Cell(cell_id=131, fill=mat2)
cell131.region = +surf100 & -surf1076

# NatU
cell132 = openmc.Cell(cell_id=132, fill=mat2)
cell132.region = +surf100 & -surf1077

# NatU
cell133 = openmc.Cell(cell_id=133, fill=mat2)
cell133.region = +surf100 & -surf1078

# NatU
cell134 = openmc.Cell(cell_id=134, fill=mat2)
cell134.region = +surf100 & -surf1079

# NatU
cell135 = openmc.Cell(cell_id=135, fill=mat2)
cell135.region = +surf100 & -surf1080

# NatU
cell136 = openmc.Cell(cell_id=136, fill=mat2)
cell136.region = +surf100 & -surf1081

# NatU
cell137 = openmc.Cell(cell_id=137, fill=mat2)
cell137.region = +surf100 & -surf1082

# NatU
cell138 = openmc.Cell(cell_id=138, fill=mat2)
cell138.region = +surf100 & -surf1083

# NatU
cell139 = openmc.Cell(cell_id=139, fill=mat2)
cell139.region = +surf100 & -surf1084

# NatU
cell140 = openmc.Cell(cell_id=140, fill=mat2)
cell140.region = +surf100 & -surf1085

# NatU
cell141 = openmc.Cell(cell_id=141, fill=mat2)
cell141.region = +surf100 & -surf1086

# NatU
cell142 = openmc.Cell(cell_id=142, fill=mat2)
cell142.region = +surf100 & -surf1087

# NatU
cell143 = openmc.Cell(cell_id=143, fill=mat2)
cell143.region = +surf100 & -surf1088

# NatU
cell144 = openmc.Cell(cell_id=144, fill=mat2)
cell144.region = +surf100 & -surf1089

# NatU
cell145 = openmc.Cell(cell_id=145, fill=mat2)
cell145.region = +surf100 & -surf1090

# NatU
cell146 = openmc.Cell(cell_id=146, fill=mat2)
cell146.region = +surf100 & -surf1091

# NatU
cell147 = openmc.Cell(cell_id=147, fill=mat2)
cell147.region = +surf100 & -surf1092

# NatU
cell148 = openmc.Cell(cell_id=148, fill=mat2)
cell148.region = +surf100 & -surf1093

# NatU
cell149 = openmc.Cell(cell_id=149, fill=mat2)
cell149.region = +surf100 & -surf1094

# NatU
cell150 = openmc.Cell(cell_id=150, fill=mat2)
cell150.region = +surf100 & -surf1095

# NatU
cell151 = openmc.Cell(cell_id=151, fill=mat2)
cell151.region = +surf100 & -surf1096

# NatU
cell152 = openmc.Cell(cell_id=152, fill=mat2)
cell152.region = +surf100 & -surf1097

# NatU
cell153 = openmc.Cell(cell_id=153, fill=mat2)
cell153.region = +surf100 & -surf1098

# NatU
cell154 = openmc.Cell(cell_id=154, fill=mat2)
cell154.region = +surf100 & -surf1099

# NatU
cell155 = openmc.Cell(cell_id=155, fill=mat2)
cell155.region = +surf100 & -surf1100

# NatU
cell156 = openmc.Cell(cell_id=156, fill=mat2)
cell156.region = +surf100 & -surf1101

# NatU
cell157 = openmc.Cell(cell_id=157, fill=mat2)
cell157.region = +surf100 & -surf1102

# NatU
cell158 = openmc.Cell(cell_id=158, fill=mat2)
cell158.region = +surf100 & -surf1103

# NatU
cell159 = openmc.Cell(cell_id=159, fill=mat2)
cell159.region = +surf100 & -surf1104

# NatU
cell160 = openmc.Cell(cell_id=160, fill=mat2)
cell160.region = +surf100 & -surf1105

# NatU
cell161 = openmc.Cell(cell_id=161, fill=mat2)
cell161.region = +surf100 & -surf1106

# NatU
cell162 = openmc.Cell(cell_id=162, fill=mat2)
cell162.region = +surf100 & -surf1107

# NatU
cell163 = openmc.Cell(cell_id=163, fill=mat2)
cell163.region = +surf100 & -surf1108

# NatU
cell164 = openmc.Cell(cell_id=164, fill=mat2)
cell164.region = +surf100 & -surf1109

# NatU
cell165 = openmc.Cell(cell_id=165, fill=mat2)
cell165.region = +surf100 & -surf1110

# NatU
cell166 = openmc.Cell(cell_id=166, fill=mat2)
cell166.region = +surf100 & -surf1111

# NatU
cell167 = openmc.Cell(cell_id=167, fill=mat2)
cell167.region = +surf100 & -surf1112

# NatU
cell168 = openmc.Cell(cell_id=168, fill=mat2)
cell168.region = +surf100 & -surf1113

# NatU
cell169 = openmc.Cell(cell_id=169, fill=mat2)
cell169.region = +surf100 & -surf1114

# NatU
cell170 = openmc.Cell(cell_id=170, fill=mat2)
cell170.region = +surf100 & -surf1115

# NatU
cell171 = openmc.Cell(cell_id=171, fill=mat2)
cell171.region = +surf100 & -surf1116

# NatU
cell172 = openmc.Cell(cell_id=172, fill=mat2)
cell172.region = +surf100 & -surf1117

# NatU
cell173 = openmc.Cell(cell_id=173, fill=mat2)
cell173.region = +surf100 & -surf1118

# NatU
cell174 = openmc.Cell(cell_id=174, fill=mat2)
cell174.region = +surf100 & -surf1119

# NatU
cell175 = openmc.Cell(cell_id=175, fill=mat2)
cell175.region = +surf100 & -surf1120

# NatU
cell176 = openmc.Cell(cell_id=176, fill=mat2)
cell176.region = +surf100 & -surf1121

# NatU
cell177 = openmc.Cell(cell_id=177, fill=mat2)
cell177.region = +surf100 & -surf1122

# NatU
cell178 = openmc.Cell(cell_id=178, fill=mat2)
cell178.region = +surf100 & -surf1123

# NatU
cell179 = openmc.Cell(cell_id=179, fill=mat2)
cell179.region = +surf100 & -surf1124

# NatU
cell180 = openmc.Cell(cell_id=180, fill=mat2)
cell180.region = +surf100 & -surf1125

# NatU
cell181 = openmc.Cell(cell_id=181, fill=mat2)
cell181.region = +surf100 & -surf1126

# NatU
cell182 = openmc.Cell(cell_id=182, fill=mat2)
cell182.region = +surf100 & -surf1127

# NatU
cell183 = openmc.Cell(cell_id=183, fill=mat2)
cell183.region = +surf100 & -surf1128

# NatU
cell184 = openmc.Cell(cell_id=184, fill=mat2)
cell184.region = +surf100 & -surf1129

# NatU
cell185 = openmc.Cell(cell_id=185, fill=mat2)
cell185.region = +surf100 & -surf1130

# NatU
cell186 = openmc.Cell(cell_id=186, fill=mat2)
cell186.region = +surf100 & -surf1131

# NatU
cell187 = openmc.Cell(cell_id=187, fill=mat2)
cell187.region = +surf100 & -surf1132

# NatU
cell188 = openmc.Cell(cell_id=188, fill=mat2)
cell188.region = +surf100 & -surf1133

# NatU
cell189 = openmc.Cell(cell_id=189, fill=mat2)
cell189.region = +surf100 & -surf1134

# NatU
cell190 = openmc.Cell(cell_id=190, fill=mat2)
cell190.region = +surf100 & -surf1135

# NatU
cell191 = openmc.Cell(cell_id=191, fill=mat2)
cell191.region = +surf100 & -surf1136

# NatU
cell192 = openmc.Cell(cell_id=192, fill=mat2)
cell192.region = +surf100 & -surf1137

# NatU
cell193 = openmc.Cell(cell_id=193, fill=mat2)
cell193.region = +surf100 & -surf1138

# NatU
cell194 = openmc.Cell(cell_id=194, fill=mat2)
cell194.region = +surf100 & -surf1139

# NatU
cell195 = openmc.Cell(cell_id=195, fill=mat2)
cell195.region = +surf100 & -surf1140

# NatU
cell196 = openmc.Cell(cell_id=196, fill=mat2)
cell196.region = +surf100 & -surf1141

# NatU
cell197 = openmc.Cell(cell_id=197, fill=mat2)
cell197.region = +surf100 & -surf1142

# NatU
cell198 = openmc.Cell(cell_id=198, fill=mat2)
cell198.region = +surf100 & -surf1143

# NatU
cell199 = openmc.Cell(cell_id=199, fill=mat2)
cell199.region = +surf100 & -surf1144

# NatU
cell200 = openmc.Cell(cell_id=200, fill=mat2)
cell200.region = +surf100 & -surf1145

# NatU
cell201 = openmc.Cell(cell_id=201, fill=mat2)
cell201.region = +surf100 & -surf1146

# NatU
cell202 = openmc.Cell(cell_id=202, fill=mat2)
cell202.region = +surf100 & -surf1147

# NatU
cell203 = openmc.Cell(cell_id=203, fill=mat2)
cell203.region = +surf100 & -surf1148

# NatU
cell204 = openmc.Cell(cell_id=204, fill=mat2)
cell204.region = +surf100 & -surf1149

# NatU
cell205 = openmc.Cell(cell_id=205, fill=mat2)
cell205.region = +surf100 & -surf1150

# NatU
cell206 = openmc.Cell(cell_id=206, fill=mat2)
cell206.region = +surf100 & -surf1151

# NatU
cell207 = openmc.Cell(cell_id=207, fill=mat2)
cell207.region = +surf100 & -surf1152

# NatU
cell208 = openmc.Cell(cell_id=208, fill=mat2)
cell208.region = +surf100 & -surf1153

# NatU
cell209 = openmc.Cell(cell_id=209, fill=mat2)
cell209.region = +surf100 & -surf1154

# NatU
cell210 = openmc.Cell(cell_id=210, fill=mat2)
cell210.region = +surf100 & -surf1155

# NatU
cell211 = openmc.Cell(cell_id=211, fill=mat2)
cell211.region = +surf100 & -surf1156

# NatU
cell212 = openmc.Cell(cell_id=212, fill=mat2)
cell212.region = +surf100 & -surf1157

# NatU
cell213 = openmc.Cell(cell_id=213, fill=mat2)
cell213.region = +surf100 & -surf1158

# NatU
cell214 = openmc.Cell(cell_id=214, fill=mat2)
cell214.region = +surf100 & -surf1159

# NatU
cell215 = openmc.Cell(cell_id=215, fill=mat2)
cell215.region = +surf100 & -surf1160

# NatU
cell216 = openmc.Cell(cell_id=216, fill=mat2)
cell216.region = +surf100 & -surf1161

# NatU
cell217 = openmc.Cell(cell_id=217, fill=mat2)
cell217.region = +surf100 & -surf1162 & +surf54

# NatU
cell218 = openmc.Cell(cell_id=218, fill=mat2)
cell218.region = +surf100 & -surf1163 & +surf54

# NatU
cell219 = openmc.Cell(cell_id=219, fill=mat2)
cell219.region = +surf100 & -surf1164 & +surf54

# NatU
cell220 = openmc.Cell(cell_id=220, fill=mat2)
cell220.region = +surf100 & -surf1165 & +surf54

# NatU
cell221 = openmc.Cell(cell_id=221, fill=mat2)
cell221.region = +surf100 & -surf1166

# NatU
cell222 = openmc.Cell(cell_id=222, fill=mat2)
cell222.region = +surf100 & -surf1167

# NatU
cell223 = openmc.Cell(cell_id=223, fill=mat2)
cell223.region = +surf100 & -surf1168

# NatU
cell224 = openmc.Cell(cell_id=224, fill=mat2)
cell224.region = +surf100 & -surf1169

# NatU
cell225 = openmc.Cell(cell_id=225, fill=mat2)
cell225.region = +surf100 & -surf1170

# NatU
cell226 = openmc.Cell(cell_id=226, fill=mat2)
cell226.region = +surf100 & -surf1171

# NatU
cell227 = openmc.Cell(cell_id=227, fill=mat2)
cell227.region = +surf100 & -surf1172

# NatU
cell228 = openmc.Cell(cell_id=228, fill=mat2)
cell228.region = +surf100 & -surf1173

# NatU
cell229 = openmc.Cell(cell_id=229, fill=mat2)
cell229.region = +surf100 & -surf1174

# NatU
cell230 = openmc.Cell(cell_id=230, fill=mat2)
cell230.region = +surf100 & -surf1175

# NatU
cell231 = openmc.Cell(cell_id=231, fill=mat2)
cell231.region = +surf100 & -surf1176

# NatU
cell232 = openmc.Cell(cell_id=232, fill=mat2)
cell232.region = +surf100 & -surf1177

# NatU
cell233 = openmc.Cell(cell_id=233, fill=mat2)
cell233.region = +surf100 & -surf1178

# NatU
cell234 = openmc.Cell(cell_id=234, fill=mat2)
cell234.region = +surf100 & -surf1179

# NatU
cell235 = openmc.Cell(cell_id=235, fill=mat2)
cell235.region = +surf100 & -surf1180

# NatU
cell236 = openmc.Cell(cell_id=236, fill=mat2)
cell236.region = +surf100 & -surf1181

# NatU
cell237 = openmc.Cell(cell_id=237, fill=mat2)
cell237.region = +surf100 & -surf1182

# NatU
cell238 = openmc.Cell(cell_id=238, fill=mat2)
cell238.region = +surf100 & -surf1183

# NatU
cell239 = openmc.Cell(cell_id=239, fill=mat2)
cell239.region = +surf100 & -surf1184

# NatU
cell240 = openmc.Cell(cell_id=240, fill=mat2)
cell240.region = +surf100 & -surf1185

# NatU
cell241 = openmc.Cell(cell_id=241, fill=mat2)
cell241.region = +surf100 & -surf1186

# NatU
cell242 = openmc.Cell(cell_id=242, fill=mat2)
cell242.region = +surf100 & -surf1187

# NatU
cell243 = openmc.Cell(cell_id=243, fill=mat2)
cell243.region = +surf100 & -surf1188

# NatU
cell244 = openmc.Cell(cell_id=244, fill=mat2)
cell244.region = +surf100 & -surf1189

# NatU
cell245 = openmc.Cell(cell_id=245, fill=mat2)
cell245.region = +surf100 & -surf1190

# NatU
cell246 = openmc.Cell(cell_id=246, fill=mat2)
cell246.region = +surf100 & -surf1191

# NatU
cell247 = openmc.Cell(cell_id=247, fill=mat2)
cell247.region = +surf100 & -surf1192

# NatU
cell248 = openmc.Cell(cell_id=248, fill=mat2)
cell248.region = +surf100 & -surf1193

# NatU
cell249 = openmc.Cell(cell_id=249, fill=mat2)
cell249.region = +surf100 & -surf1194

# NatU
cell250 = openmc.Cell(cell_id=250, fill=mat2)
cell250.region = +surf100 & -surf1195

# NatU
cell251 = openmc.Cell(cell_id=251, fill=mat2)
cell251.region = +surf100 & -surf1196

# NatU
cell252 = openmc.Cell(cell_id=252, fill=mat2)
cell252.region = +surf100 & -surf1197

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell55, cell56, cell57, cell58, cell59, cell60, cell61, cell62, cell63, cell64, cell65, cell66, cell67, cell68, cell69, cell70, cell71, cell72, cell73, cell74, cell75, cell76, cell77, cell78, cell79, cell80, cell81, cell82, cell83, cell84, cell85, cell86, cell87, cell88, cell89, cell90, cell91, cell92, cell93, cell94, cell95, cell96, cell97, cell98, cell99, cell100, cell101, cell102, cell103, cell104, cell105, cell106, cell107, cell108, cell109, cell110, cell111, cell112, cell113, cell114, cell115, cell116, cell117, cell118, cell119, cell120, cell121, cell122, cell123, cell124, cell125, cell126, cell127, cell128, cell129, cell130, cell131, cell132, cell133, cell134, cell135, cell136, cell137, cell138, cell139, cell140, cell141, cell142, cell143, cell144, cell145, cell146, cell147, cell148, cell149, cell150, cell151, cell152, cell153, cell154, cell155, cell156, cell157, cell158, cell159, cell160, cell161, cell162, cell163, cell164, cell165, cell166, cell167, cell168, cell169, cell170, cell171, cell172, cell173, cell174, cell175, cell176, cell177, cell178, cell179, cell180, cell181, cell182, cell183, cell184, cell185, cell186, cell187, cell188, cell189, cell190, cell191, cell192, cell193, cell194, cell195, cell196, cell197, cell198, cell199, cell200, cell201, cell202, cell203, cell204, cell205, cell206, cell207, cell208, cell209, cell210, cell211, cell212, cell213, cell214, cell215, cell216, cell217, cell218, cell219, cell220, cell221, cell222, cell223, cell224, cell225, cell226, cell227, cell228, cell229, cell230, cell231, cell232, cell233, cell234, cell235, cell236, cell237, cell238, cell239, cell240, cell241, cell242, cell243, cell244, cell245, cell246, cell247, cell248, cell249, cell250, cell251, cell252])
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
source.space = openmc.stats.Box((-10.14, -10.14, -1.0), (10.14, 10.14, 1.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
