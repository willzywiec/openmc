"""
SMF008-1: Np-237 sphere surrounded by HEU shells (detailed model)
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
mat7.add_element("Al", 5.923800e-02)

# Other aluminum parts
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 6.037600e-02)

# HEU shell #21
mat21 = openmc.Material(material_id=21)
mat21.set_density("sum")
mat21.add_nuclide("U234", 4.896100e-04)
mat21.add_nuclide("U235", 4.452700e-02)
mat21.add_nuclide("U236", 2.236900e-04)
mat21.add_nuclide("U238", 2.524800e-03)

# HEU shell #22
mat22 = openmc.Material(material_id=22)
mat22.set_density("sum")
mat22.add_nuclide("U234", 4.894600e-04)
mat22.add_nuclide("U235", 4.451300e-02)
mat22.add_nuclide("U236", 2.236200e-04)
mat22.add_nuclide("U238", 2.524000e-03)

# HEU shell #23
mat23 = openmc.Material(material_id=23)
mat23.set_density("sum")
mat23.add_nuclide("U234", 4.892300e-04)
mat23.add_nuclide("U235", 4.449300e-02)
mat23.add_nuclide("U236", 2.235200e-04)
mat23.add_nuclide("U238", 2.522800e-03)

# HEU shell #24
mat24 = openmc.Material(material_id=24)
mat24.set_density("sum")
mat24.add_nuclide("U234", 4.905200e-04)
mat24.add_nuclide("U235", 4.460900e-02)
mat24.add_nuclide("U236", 2.241000e-04)
mat24.add_nuclide("U238", 2.529500e-03)

# HEU shell #25
mat25 = openmc.Material(material_id=25)
mat25.set_density("sum")
mat25.add_nuclide("U234", 4.853400e-04)
mat25.add_nuclide("U235", 4.413900e-02)
mat25.add_nuclide("U236", 2.217400e-04)
mat25.add_nuclide("U238", 2.502800e-03)

# HEU shell #26
mat26 = openmc.Material(material_id=26)
mat26.set_density("sum")
mat26.add_nuclide("U234", 4.880300e-04)
mat26.add_nuclide("U235", 4.438300e-02)
mat26.add_nuclide("U236", 2.229700e-04)
mat26.add_nuclide("U238", 2.516600e-03)

# HEU shell #27
mat27 = openmc.Material(material_id=27)
mat27.set_density("sum")
mat27.add_nuclide("U234", 4.875300e-04)
mat27.add_nuclide("U235", 4.433800e-02)
mat27.add_nuclide("U236", 2.227400e-04)
mat27.add_nuclide("U238", 2.514100e-03)

# HEU shell #28
mat28 = openmc.Material(material_id=28)
mat28.set_density("sum")
mat28.add_nuclide("U234", 4.891900e-04)
mat28.add_nuclide("U235", 4.448900e-02)
mat28.add_nuclide("U236", 2.235000e-04)
mat28.add_nuclide("U238", 2.522600e-03)

# HEU shell #29
mat29 = openmc.Material(material_id=29)
mat29.set_density("sum")
mat29.add_nuclide("U234", 4.862500e-04)
mat29.add_nuclide("U235", 4.422100e-02)
mat29.add_nuclide("U236", 2.221500e-04)
mat29.add_nuclide("U238", 2.507500e-03)

# HEU shell #30
mat30 = openmc.Material(material_id=30)
mat30.set_density("sum")
mat30.add_nuclide("U234", 4.860700e-04)
mat30.add_nuclide("U235", 4.420500e-02)
mat30.add_nuclide("U236", 2.220700e-04)
mat30.add_nuclide("U238", 2.506500e-03)

# HEU shell #31
mat31 = openmc.Material(material_id=31)
mat31.set_density("sum")
mat31.add_nuclide("U234", 4.884600e-04)
mat31.add_nuclide("U235", 4.442200e-02)
mat31.add_nuclide("U236", 2.231600e-04)
mat31.add_nuclide("U238", 2.518900e-03)

# HEU shell #32
mat32 = openmc.Material(material_id=32)
mat32.set_density("sum")
mat32.add_nuclide("U234", 4.876600e-04)
mat32.add_nuclide("U235", 4.434900e-02)
mat32.add_nuclide("U236", 2.228000e-04)
mat32.add_nuclide("U238", 2.514700e-03)

# HEU shell #33
mat33 = openmc.Material(material_id=33)
mat33.set_density("sum")
mat33.add_nuclide("U234", 4.876100e-04)
mat33.add_nuclide("U235", 4.434500e-02)
mat33.add_nuclide("U236", 2.227800e-04)
mat33.add_nuclide("U238", 2.514500e-03)

# HEU shell #34
mat34 = openmc.Material(material_id=34)
mat34.set_density("sum")
mat34.add_nuclide("U234", 4.873900e-04)
mat34.add_nuclide("U235", 4.432500e-02)
mat34.add_nuclide("U236", 2.226800e-04)
mat34.add_nuclide("U238", 2.513400e-03)

# HEU shell #35
mat35 = openmc.Material(material_id=35)
mat35.set_density("sum")
mat35.add_nuclide("U234", 4.886300e-04)
mat35.add_nuclide("U235", 4.443800e-02)
mat35.add_nuclide("U236", 2.232400e-04)
mat35.add_nuclide("U238", 2.519700e-03)

# HEU shell #36
mat36 = openmc.Material(material_id=36)
mat36.set_density("sum")
mat36.add_nuclide("U234", 4.895300e-04)
mat36.add_nuclide("U235", 4.451900e-02)
mat36.add_nuclide("U236", 2.236500e-04)
mat36.add_nuclide("U238", 2.524400e-03)

# HEU shell #37
mat37 = openmc.Material(material_id=37)
mat37.set_density("sum")
mat37.add_nuclide("U234", 4.974600e-04)
mat37.add_nuclide("U235", 4.524100e-02)
mat37.add_nuclide("U236", 2.272800e-04)
mat37.add_nuclide("U238", 2.565300e-03)

# HEU shell #38
mat38 = openmc.Material(material_id=38)
mat38.set_density("sum")
mat38.add_nuclide("U234", 4.797800e-04)
mat38.add_nuclide("U235", 4.363300e-02)
mat38.add_nuclide("U236", 2.192000e-04)
mat38.add_nuclide("U238", 2.474100e-03)

# HEU shell #39
mat39 = openmc.Material(material_id=39)
mat39.set_density("sum")
mat39.add_nuclide("U234", 4.892900e-04)
mat39.add_nuclide("U235", 4.449700e-02)
mat39.add_nuclide("U236", 2.235400e-04)
mat39.add_nuclide("U238", 2.523100e-03)

# HEU shell #40
mat40 = openmc.Material(material_id=40)
mat40.set_density("sum")
mat40.add_nuclide("U234", 4.879300e-04)
mat40.add_nuclide("U235", 4.437400e-02)
mat40.add_nuclide("U236", 2.229200e-04)
mat40.add_nuclide("U238", 2.516100e-03)

# HEU shell #41
mat41 = openmc.Material(material_id=41)
mat41.set_density("sum")
mat41.add_nuclide("U234", 4.882300e-04)
mat41.add_nuclide("U235", 4.440100e-02)
mat41.add_nuclide("U236", 2.230600e-04)
mat41.add_nuclide("U238", 2.517700e-03)

# HEU shell #42
mat42 = openmc.Material(material_id=42)
mat42.set_density("sum")
mat42.add_nuclide("U234", 4.881800e-04)
mat42.add_nuclide("U235", 4.439700e-02)
mat42.add_nuclide("U236", 2.230400e-04)
mat42.add_nuclide("U238", 2.517400e-03)

# HEU shell #43
mat43 = openmc.Material(material_id=43)
mat43.set_density("sum")
mat43.add_nuclide("U234", 4.888900e-04)
mat43.add_nuclide("U235", 4.446100e-02)
mat43.add_nuclide("U236", 2.233600e-04)
mat43.add_nuclide("U238", 2.521100e-03)

# HEU shell #44
mat44 = openmc.Material(material_id=44)
mat44.set_density("sum")
mat44.add_nuclide("U234", 4.888700e-04)
mat44.add_nuclide("U235", 4.445900e-02)
mat44.add_nuclide("U236", 2.233500e-04)
mat44.add_nuclide("U238", 2.521000e-03)

# HEU shell #45
mat45 = openmc.Material(material_id=45)
mat45.set_density("sum")
mat45.add_nuclide("U234", 4.885000e-04)
mat45.add_nuclide("U235", 4.442600e-02)
mat45.add_nuclide("U236", 2.231800e-04)
mat45.add_nuclide("U238", 2.519100e-03)

# HEU shell #46
mat46 = openmc.Material(material_id=46)
mat46.set_density("sum")
mat46.add_nuclide("U234", 4.885600e-04)
mat46.add_nuclide("U235", 4.443100e-02)
mat46.add_nuclide("U236", 2.232100e-04)
mat46.add_nuclide("U238", 2.519400e-03)

# HEU shell #47
mat47 = openmc.Material(material_id=47)
mat47.set_density("sum")
mat47.add_nuclide("U234", 4.894600e-04)
mat47.add_nuclide("U235", 4.451400e-02)
mat47.add_nuclide("U236", 2.236200e-04)
mat47.add_nuclide("U238", 2.524000e-03)

# HEU shell #48
mat48 = openmc.Material(material_id=48)
mat48.set_density("sum")
mat48.add_nuclide("U234", 4.904300e-04)
mat48.add_nuclide("U235", 4.460100e-02)
mat48.add_nuclide("U236", 2.240600e-04)
mat48.add_nuclide("U238", 2.529000e-03)

# HEU shell #49
mat49 = openmc.Material(material_id=49)
mat49.set_density("sum")
mat49.add_nuclide("U234", 4.883000e-04)
mat49.add_nuclide("U235", 4.440800e-02)
mat49.add_nuclide("U236", 2.230900e-04)
mat49.add_nuclide("U238", 2.518100e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat21, mat22, mat23, mat24, mat25, mat26, mat27, mat28, mat29, mat30, mat31, mat32, mat33, mat34, mat35, mat36, mat37, mat38, mat39, mat40, mat41, mat42, mat43, mat44, mat45, mat46, mat47, mat48, mat49])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Al mounting plate
surf1 = openmc.model.RectangularParallelepiped(-15.24, 15.24, -15.24, 15.24, -28.2575, -27.6225)
# SS304 lower base
surf2 = openmc.model.RectangularParallelepiped(-13.335, 13.335, -7.62, 7.62, -27.6225, -26.3525)
# SS304 middle base
surf3 = openmc.model.RectangularParallelepiped(-9.8425, 9.8425, -8.255, 8.255, -26.3525, -17.78)
# SS304 table
surf4 = openmc.model.RectangularParallelepiped(-12.7, 12.7, -7.62, 7.62, -17.78, -15.24)
# Al mounting tube: spherical contour
surf5 = openmc.Sphere(surface_id=5, x0=10.0, y0=tr, z0=0, r=0)
# Al mounting tube: large hole
surf6 = openmc.ZCylinder(surface_id=6, r=5.08)
# Al mounting tube: small hole
surf7 = openmc.ZCylinder(surface_id=7, r=0.35179)
# Al mounting tube: upper portion
surf8 = openmc.ZCylinder(surface_id=8, r=7.62)
# Al mounting tube: lower portion
surf9 = openmc.ZCylinder(surface_id=9, r=7.62)
# Al shell: top; Al spacer: bottom
surf10 = openmc.ZPlane(surface_id=10, z0=-0.3175)
# Al shell: inner
surf11 = openmc.Sphere(surface_id=11, x0=4.83108, y0=tr, z0=0, r=0)
# Al shell: outer
surf12 = openmc.Sphere(surface_id=12, x0=4.99872, y0=tr, z0=0, r=0)
# Al stem
surf13 = openmc.ZCylinder(surface_id=13, r=0.3302)
# SS304 alignment rod: upper
surf14 = openmc.ZCylinder(surface_id=14, r=0.17526)
# SS304 alignment rod: lower
surf15 = openmc.ZCylinder(surface_id=15, r=0.3175)
# Al spacer: inner
surf17 = openmc.ZCylinder(surface_id=17, r=4.81838)
# Al spacer: outer
surf18 = openmc.ZCylinder(surface_id=18, r=10.0)
# Al spacer: top
surf19 = openmc.ZPlane(surface_id=19, z0=0.0)
# Np sphere
surf21 = openmc.Sphere(surface_id=21, x0=4.14909, y0=tr, z0=0, r=0)
# W shield: inner
surf22 = openmc.Sphere(surface_id=22, x0=4.16814, y0=tr, z0=0, r=0)
# W shield: outer
surf23 = openmc.Sphere(surface_id=23, x0=4.42722, y0=tr, z0=0, r=0)
# Inner Ni cladding: inner
surf24 = openmc.Sphere(surface_id=24, x0=4.4323, y0=tr, z0=0, r=0)
# Inner Ni cladding: outer
surf25 = openmc.Sphere(surface_id=25, x0=4.6228, y0=tr, z0=0, r=0)
# Outer Ni cladding: inner
surf26 = openmc.Sphere(surface_id=26, x0=4.62788, y0=tr, z0=0, r=0)
# Outer Ni cladding: outer
surf27 = openmc.Sphere(surface_id=27, x0=4.81838, y0=tr, z0=0, r=0)
# Hole in Al support plate, collar and mounting flange
surf31 = openmc.ZCylinder(surface_id=31, r=10.4775)
# Al support plate
surf32 = openmc.model.RectangularParallelepiped(-31.75, 31.75, -27.305, 27.305, -2.54, -1.27)
# Al support collar
surf33 = openmc.ZCylinder(surface_id=33, r=16.51)
# Hole in SS301 membrane
surf34 = openmc.ZCylinder(surface_id=34, r=4.9149)
# SS301 membrane
surf35 = openmc.ZCylinder(surface_id=35, r=13.335)
# Al moutning flange
surf36 = openmc.ZCylinder(surface_id=36, r=13.335)
# Al veritical bracket: left
surf41 = openmc.model.RectangularParallelepiped(-15.6591, -14.3891, -2.54, 2.54, 0.0, 13.97)
# Al veritical bracket: right
surf42 = openmc.model.RectangularParallelepiped(14.3891, 15.6591, -2.54, 2.54, 0.0, 13.97)
# Al horizontal bracket: top
surf43 = openmc.model.RectangularParallelepiped(-15.6591, 15.6591, -2.54, 2.54, 13.97, 15.24)
# Square hole in Al top plate
surf45 = openmc.model.RectangularParallelepiped(-22.098, 22.098, -22.098, 22.098, -49.995, 49.995)
# Al top plate
surf46 = openmc.model.RectangularParallelepiped(-57.15, 57.15, -57.15, 57.15, -10.16, -7.62)
# Al shell: bottom
surf50 = openmc.ZPlane(surface_id=50, z0=0.08128)
# Al shell: inner
surf51 = openmc.Sphere(surface_id=51, x0=4.83108, y0=tr, z0=0, r=0)
# Al shell: outer
surf52 = openmc.Sphere(surface_id=52, x0=4.99872, y0=tr, z0=0, r=0)
# Al stem
surf53 = openmc.ZCylinder(surface_id=53, r=0.3302)
# SS304 mounting rod: lower
surf54 = openmc.ZCylinder(surface_id=54, r=0.17526)
# SS304 mounting rod: upper
surf55 = openmc.ZCylinder(surface_id=55, r=0.3175)
# Central z-hole in all HEU shells
surf200 = openmc.ZCylinder(surface_id=200, r=0.35687)
# HEU shell no. 21: inner
surf211 = openmc.Sphere(surface_id=211, x0=5.017, y0=tr, z0=0, r=0)
# HEU shell no. 21: outer
surf212 = openmc.Sphere(surface_id=212, x0=5.337, y0=tr, z0=0, r=0)
# HEU shell no. 21: x-hole
surf213 = openmc.XCylinder(surface_id=213, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 21: y-hole
surf214 = openmc.YCylinder(surface_id=214, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 22: inner
surf221 = openmc.Sphere(surface_id=221, x0=5.013, y0=tr, z0=0, r=0)
# HEU shell no. 22: outer
surf222 = openmc.Sphere(surface_id=222, x0=5.336, y0=tr, z0=0, r=0)
# HEU shell no. 22: x-hole
surf223 = openmc.XCylinder(surface_id=223, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 22: y-hole
surf224 = openmc.YCylinder(surface_id=224, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 23: inner
surf231 = openmc.Sphere(surface_id=231, x0=5.346, y0=tr, z0=0, r=0)
# HEU shell no. 23: outer
surf232 = openmc.Sphere(surface_id=232, x0=5.669, y0=tr, z0=0, r=0)
# HEU shell no. 23: x-hole
surf233 = openmc.XCylinder(surface_id=233, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 23: y-hole
surf234 = openmc.YCylinder(surface_id=234, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 24: inner
surf241 = openmc.Sphere(surface_id=241, x0=5.346, y0=tr, z0=0, r=0)
# HEU shell no. 24: outer
surf242 = openmc.Sphere(surface_id=242, x0=5.669, y0=tr, z0=0, r=0)
# HEU shell no. 24: x-hole
surf243 = openmc.XCylinder(surface_id=243, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 24: y-hole
surf244 = openmc.YCylinder(surface_id=244, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 25: inner
surf251 = openmc.Sphere(surface_id=251, x0=5.679, y0=tr, z0=0, r=0)
# HEU shell no. 25: outer
surf252 = openmc.Sphere(surface_id=252, x0=6.003, y0=tr, z0=0, r=0)
# HEU shell no. 25: x-hole
surf253 = openmc.XCylinder(surface_id=253, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 25: y-hole
surf254 = openmc.YCylinder(surface_id=254, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 26: inner
surf261 = openmc.Sphere(surface_id=261, x0=5.679, y0=tr, z0=0, r=0)
# HEU shell no. 26: outer
surf262 = openmc.Sphere(surface_id=262, x0=6.001, y0=tr, z0=0, r=0)
# HEU shell no. 26: x-hole
surf263 = openmc.XCylinder(surface_id=263, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 26: y-hole
surf264 = openmc.YCylinder(surface_id=264, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 27: inner
surf271 = openmc.Sphere(surface_id=271, x0=6.011, y0=tr, z0=0, r=0)
# HEU shell no. 27: outer
surf272 = openmc.Sphere(surface_id=272, x0=6.335, y0=tr, z0=0, r=0)
# HEU shell no. 27: x-hole
surf273 = openmc.XCylinder(surface_id=273, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 27: y-hole
surf274 = openmc.YCylinder(surface_id=274, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 28: inner
surf281 = openmc.Sphere(surface_id=281, x0=6.012, y0=tr, z0=0, r=0)
# HEU shell no. 28: outer
surf282 = openmc.Sphere(surface_id=282, x0=6.334, y0=tr, z0=0, r=0)
# HEU shell no. 28: x-hole
surf283 = openmc.XCylinder(surface_id=283, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 28: y-hole
surf284 = openmc.YCylinder(surface_id=284, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 29: inner
surf291 = openmc.Sphere(surface_id=291, x0=6.345, y0=tr, z0=0, r=0)
# HEU shell no. 29: outer
surf292 = openmc.Sphere(surface_id=292, x0=6.671, y0=tr, z0=0, r=0)
# HEU shell no. 29: x-hole
surf293 = openmc.XCylinder(surface_id=293, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 29: y-hole
surf294 = openmc.YCylinder(surface_id=294, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 30: inner
surf301 = openmc.Sphere(surface_id=301, x0=6.344, y0=tr, z0=0, r=0)
# HEU shell no. 30: outer
surf302 = openmc.Sphere(surface_id=302, x0=6.670, y0=tr, z0=0, r=0)
# HEU shell no. 30: x-hole
surf303 = openmc.XCylinder(surface_id=303, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 30: y-hole
surf304 = openmc.YCylinder(surface_id=304, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 31: inner
surf311 = openmc.Sphere(surface_id=311, x0=6.678, y0=tr, z0=0, r=0)
# HEU shell no. 31: outer
surf312 = openmc.Sphere(surface_id=312, x0=7.002, y0=tr, z0=0, r=0)
# HEU shell no. 31: x-hole
surf313 = openmc.XCylinder(surface_id=313, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 31: y-hole
surf314 = openmc.YCylinder(surface_id=314, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 32: inner
surf321 = openmc.Sphere(surface_id=321, x0=6.679, y0=tr, z0=0, r=0)
# HEU shell no. 32: outer
surf322 = openmc.Sphere(surface_id=322, x0=7.003, y0=tr, z0=0, r=0)
# HEU shell no. 32: x-hole
surf323 = openmc.XCylinder(surface_id=323, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 32: y-hole
surf324 = openmc.YCylinder(surface_id=324, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 33: inner
surf331 = openmc.Sphere(surface_id=331, x0=7.006, y0=tr, z0=0, r=0)
# HEU shell no. 33: outer
surf332 = openmc.Sphere(surface_id=332, x0=7.330, y0=tr, z0=0, r=0)
# HEU shell no. 33: x-hole
surf333 = openmc.XCylinder(surface_id=333, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 33: y-hole
surf334 = openmc.YCylinder(surface_id=334, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 34: inner
surf341 = openmc.Sphere(surface_id=341, x0=7.010, y0=tr, z0=0, r=0)
# HEU shell no. 34: outer
surf342 = openmc.Sphere(surface_id=342, x0=7.334, y0=tr, z0=0, r=0)
# HEU shell no. 34: x-hole
surf343 = openmc.XCylinder(surface_id=343, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 34: y-hole
surf344 = openmc.YCylinder(surface_id=344, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 35: inner
surf351 = openmc.Sphere(surface_id=351, x0=7.342, y0=tr, z0=0, r=0)
# HEU shell no. 35: outer
surf352 = openmc.Sphere(surface_id=352, x0=7.666, y0=tr, z0=0, r=0)
# HEU shell no. 35: x-hole
surf353 = openmc.XCylinder(surface_id=353, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 35: y-hole
surf354 = openmc.YCylinder(surface_id=354, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 36: inner
surf361 = openmc.Sphere(surface_id=361, x0=7.343, y0=tr, z0=0, r=0)
# HEU shell no. 36: outer
surf362 = openmc.Sphere(surface_id=362, x0=7.666, y0=tr, z0=0, r=0)
# HEU shell no. 36: x-hole
surf363 = openmc.XCylinder(surface_id=363, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 36: y-hole
surf364 = openmc.YCylinder(surface_id=364, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 37: inner
surf371 = openmc.Sphere(surface_id=371, x0=7.682, y0=tr, z0=0, r=0)
# HEU shell no. 37: outer
surf372 = openmc.Sphere(surface_id=372, x0=8.003, y0=tr, z0=0, r=0)
# HEU shell no. 37: x-hole
surf373 = openmc.XCylinder(surface_id=373, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 37: y-hole
surf374 = openmc.YCylinder(surface_id=374, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 38: inner
surf381 = openmc.Sphere(surface_id=381, x0=7.671, y0=tr, z0=0, r=0)
# HEU shell no. 38: outer
surf382 = openmc.Sphere(surface_id=382, x0=8.003, y0=tr, z0=0, r=0)
# HEU shell no. 38: x-hole
surf383 = openmc.XCylinder(surface_id=383, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 38: y-hole
surf384 = openmc.YCylinder(surface_id=384, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 39: inner
surf391 = openmc.Sphere(surface_id=391, x0=8.013, y0=tr, z0=0, r=0)
# HEU shell no. 39: outer
surf392 = openmc.Sphere(surface_id=392, x0=8.336, y0=tr, z0=0, r=0)
# HEU shell no. 39: x-hole
surf393 = openmc.XCylinder(surface_id=393, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 39: y-hole
surf394 = openmc.YCylinder(surface_id=394, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 40: inner
surf401 = openmc.Sphere(surface_id=401, x0=8.007, y0=tr, z0=0, r=0)
# HEU shell no. 40: outer
surf402 = openmc.Sphere(surface_id=402, x0=8.329, y0=tr, z0=0, r=0)
# HEU shell no. 40: x-hole
surf403 = openmc.XCylinder(surface_id=403, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 40: y-hole
surf404 = openmc.YCylinder(surface_id=404, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 41: inner
surf411 = openmc.Sphere(surface_id=411, x0=8.346, y0=tr, z0=0, r=0)
# HEU shell no. 41: outer
surf412 = openmc.Sphere(surface_id=412, x0=8.668, y0=tr, z0=0, r=0)
# HEU shell no. 41: x-hole
surf413 = openmc.XCylinder(surface_id=413, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 41: y-hole
surf414 = openmc.YCylinder(surface_id=414, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 42: inner
surf421 = openmc.Sphere(surface_id=421, x0=8.344, y0=tr, z0=0, r=0)
# HEU shell no. 42: outer
surf422 = openmc.Sphere(surface_id=422, x0=8.668, y0=tr, z0=0, r=0)
# HEU shell no. 42: x-hole
surf423 = openmc.XCylinder(surface_id=423, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 42: y-hole
surf424 = openmc.YCylinder(surface_id=424, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 43: inner
surf431 = openmc.Sphere(surface_id=431, x0=8.678, y0=tr, z0=0, r=0)
# HEU shell no. 43: outer
surf432 = openmc.Sphere(surface_id=432, x0=9.000, y0=tr, z0=0, r=0)
# HEU shell no. 43: x-hole
surf433 = openmc.XCylinder(surface_id=433, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 43: y-hole
surf434 = openmc.YCylinder(surface_id=434, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 44: inner
surf441 = openmc.Sphere(surface_id=441, x0=8.676, y0=tr, z0=0, r=0)
# HEU shell no. 44: outer
surf442 = openmc.Sphere(surface_id=442, x0=8.999, y0=tr, z0=0, r=0)
# HEU shell no. 44: x-hole
surf443 = openmc.XCylinder(surface_id=443, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 44: y-hole
surf444 = openmc.YCylinder(surface_id=444, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 45: inner
surf451 = openmc.Sphere(surface_id=451, x0=9.009, y0=tr, z0=0, r=0)
# HEU shell no. 45: outer
surf452 = openmc.Sphere(surface_id=452, x0=9.333, y0=tr, z0=0, r=0)
# HEU shell no. 45: x-hole
surf453 = openmc.XCylinder(surface_id=453, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 45: y-hole
surf454 = openmc.YCylinder(surface_id=454, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 46: inner
surf461 = openmc.Sphere(surface_id=461, x0=9.010, y0=tr, z0=0, r=0)
# HEU shell no. 46: outer
surf462 = openmc.Sphere(surface_id=462, x0=9.333, y0=tr, z0=0, r=0)
# HEU shell no. 46: x-hole
surf463 = openmc.XCylinder(surface_id=463, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 46: y-hole
surf464 = openmc.YCylinder(surface_id=464, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 47: inner
surf471 = openmc.Sphere(surface_id=471, x0=9.342, y0=tr, z0=0, r=0)
# HEU shell no. 47: outer
surf472 = openmc.Sphere(surface_id=472, x0=9.667, y0=tr, z0=0, r=0)
# HEU shell no. 47: x-hole
surf473 = openmc.XCylinder(surface_id=473, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 47: y-hole
surf474 = openmc.YCylinder(surface_id=474, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 48: inner
surf481 = openmc.Sphere(surface_id=481, x0=9.343, y0=tr, z0=0, r=0)
# HEU shell no. 48: outer
surf482 = openmc.Sphere(surface_id=482, x0=9.668, y0=tr, z0=0, r=0)
# HEU shell no. 48: x-hole
surf483 = openmc.XCylinder(surface_id=483, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 48: y-hole
surf484 = openmc.YCylinder(surface_id=484, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 49: inner
surf491 = openmc.Sphere(surface_id=491, x0=9.677, y0=tr, z0=0, r=0)
# HEU shell no. 49: outer
surf492 = openmc.Sphere(surface_id=492, x0=10.000, y0=tr, z0=0, r=0)
# HEU shell no. 49: x-hole
surf493 = openmc.XCylinder(surface_id=493, x0=0.0, y0=0.0, r=0.15875)
# HEU shell no. 49: y-hole
surf494 = openmc.YCylinder(surface_id=494, x0=0.0, y0=0.0, r=0.15875)

# Z-plane surfaces for bounded cylinders
surf6_zmin = openmc.ZPlane(surface_id=1494, z0=-10.4775)
surf6_zmax = openmc.ZPlane(surface_id=1495, z0=-7.9375)
surf7_zmin = openmc.ZPlane(surface_id=1496, z0=-15.24)
surf7_zmax = openmc.ZPlane(surface_id=1497, z0=-10.4775)
surf8_zmin = openmc.ZPlane(surface_id=1498, z0=-10.4775)
surf8_zmax = openmc.ZPlane(surface_id=1499, z0=-7.9375)
surf9_zmin = openmc.ZPlane(surface_id=1500, z0=-15.24)
surf9_zmax = openmc.ZPlane(surface_id=1501, z0=-10.4775)
surf13_zmin = openmc.ZPlane(surface_id=1502, z0=-7.3025)
surf13_zmax = openmc.ZPlane(surface_id=1503, z0=-1.0)
surf14_zmin = openmc.ZPlane(surface_id=1504, z0=-7.3025)
surf14_zmax = openmc.ZPlane(surface_id=1505, z0=-6.0325)
surf15_zmin = openmc.ZPlane(surface_id=1506, z0=-15.24)
surf15_zmax = openmc.ZPlane(surface_id=1507, z0=-7.3025)
surf33_zmin = openmc.ZPlane(surface_id=1508, z0=-1.27)
surf33_zmax = openmc.ZPlane(surface_id=1509, z0=0.0)
surf35_zmin = openmc.ZPlane(surface_id=1510, z0=0.0)
surf35_zmax = openmc.ZPlane(surface_id=1511, z0=0.08128)
surf36_zmin = openmc.ZPlane(surface_id=1512, z0=0.08128)
surf36_zmax = openmc.ZPlane(surface_id=1513, z0=1.35128)
surf53_zmin = openmc.ZPlane(surface_id=1514, z0=1.0)
surf53_zmax = openmc.ZPlane(surface_id=1515, z0=7.06628)
surf54_zmin = openmc.ZPlane(surface_id=1516, z0=5.79628)
surf54_zmax = openmc.ZPlane(surface_id=1517, z0=7.06628)
surf55_zmin = openmc.ZPlane(surface_id=1518, z0=7.06628)
surf55_zmax = openmc.ZPlane(surface_id=1519, z0=15.95628)

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
cell4.region = +surf3 & -surf4 & (+surf15 | -surf15_zmin | +surf15_zmax)

# Al
cell5 = openmc.Cell(cell_id=5, fill=mat8)
cell5.region = +surf5 & (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# Al
cell6 = openmc.Cell(cell_id=6, fill=mat8)
cell6.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax) & (-surf9 & +surf9_zmin & -surf9_zmax)

# Al
cell7 = openmc.Cell(cell_id=7, fill=mat8)
cell7.region = -surf10 & +surf11 & -surf12

# Al
cell8 = openmc.Cell(cell_id=8, fill=mat8)
cell8.region = +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (+surf15 | -surf15_zmin | +surf15_zmax)

# SS304
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = (-surf14 & +surf14_zmin & -surf14_zmax)

# SS304
cell10 = openmc.Cell(cell_id=10, fill=mat5)
cell10.region = (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)

# Al
cell11 = openmc.Cell(cell_id=11, fill=mat7)
cell11.region = +surf10 & +surf17 & -surf18 & -surf19

# Np
cell12 = openmc.Cell(cell_id=12, fill=mat1)
cell12.region = -surf21

# W
cell13 = openmc.Cell(cell_id=13, fill=mat2)
cell13.region = +surf22 & -surf23

# Ni
cell14 = openmc.Cell(cell_id=14, fill=mat3)
cell14.region = +surf24 & -surf25

# Ni
cell15 = openmc.Cell(cell_id=15, fill=mat3)
cell15.region = +surf26 & -surf27

# Al
cell16 = openmc.Cell(cell_id=16, fill=mat8)
cell16.region = +surf31 & -surf32

# Al
cell17 = openmc.Cell(cell_id=17, fill=mat8)
cell17.region = +surf31 & +surf32 & (-surf33 & +surf33_zmin & -surf33_zmax)

# SS301
cell18 = openmc.Cell(cell_id=18, fill=mat6)
cell18.region = (+surf33 | -surf33_zmin | +surf33_zmax) & +surf34 & (-surf35 & +surf35_zmin & -surf35_zmax)

# Al
cell19 = openmc.Cell(cell_id=19, fill=mat8)
cell19.region = +surf31 & (+surf35 | -surf35_zmin | +surf35_zmax) & (-surf36 & +surf36_zmin & -surf36_zmax)

# Al
cell20 = openmc.Cell(cell_id=20, fill=mat8)
cell20.region = (+surf33 | -surf33_zmin | +surf33_zmax) & -surf41

# Al
cell21 = openmc.Cell(cell_id=21, fill=mat8)
cell21.region = (+surf33 | -surf33_zmin | +surf33_zmax) & -surf42

# Al
cell22 = openmc.Cell(cell_id=22, fill=mat8)
cell22.region = +surf41 & +surf42 & -surf43 & (+surf55 | -surf55_zmin | +surf55_zmax)

# Al
cell23 = openmc.Cell(cell_id=23, fill=mat8)
cell23.region = +surf45 & -surf46

# Al
cell24 = openmc.Cell(cell_id=24, fill=mat8)
cell24.region = +surf50 & +surf51 & -surf52

# Al
cell25 = openmc.Cell(cell_id=25, fill=mat8)
cell25.region = +surf50 & +surf52 & (-surf53 & +surf53_zmin & -surf53_zmax) & (+surf54 | -surf54_zmin | +surf54_zmax) & (+surf55 | -surf55_zmin | +surf55_zmax)

# SS304
cell26 = openmc.Cell(cell_id=26, fill=mat5)
cell26.region = (-surf54 & +surf54_zmin & -surf54_zmax)

# SS304
cell27 = openmc.Cell(cell_id=27, fill=mat5)
cell27.region = (+surf54 | -surf54_zmin | +surf54_zmax) & (-surf55 & +surf55_zmin & -surf55_zmax)

# HEU
cell28 = openmc.Cell(cell_id=28, fill=mat21)
cell28.region = -surf10 & +surf200 & +surf211 & -surf212 & +surf213 & +surf214

# HEU
cell29 = openmc.Cell(cell_id=29, fill=mat23)
cell29.region = -surf10 & +surf200 & +surf231 & -surf232 & +surf233 & +surf234

# HEU
cell30 = openmc.Cell(cell_id=30, fill=mat25)
cell30.region = -surf10 & +surf200 & +surf251 & -surf252 & +surf253 & +surf254

# HEU
cell31 = openmc.Cell(cell_id=31, fill=mat27)
cell31.region = -surf10 & +surf200 & +surf271 & -surf272 & +surf273 & +surf274

# HEU
cell32 = openmc.Cell(cell_id=32, fill=mat29)
cell32.region = -surf10 & +surf200 & +surf291 & -surf292 & +surf293 & +surf294

# HEU
cell33 = openmc.Cell(cell_id=33, fill=mat31)
cell33.region = -surf10 & +surf200 & +surf311 & -surf312 & +surf313 & +surf314

# HEU
cell34 = openmc.Cell(cell_id=34, fill=mat33)
cell34.region = -surf10 & +surf200 & +surf331 & -surf332 & +surf333 & +surf334

# HEU
cell35 = openmc.Cell(cell_id=35, fill=mat35)
cell35.region = -surf10 & +surf200 & +surf351 & -surf352 & +surf353 & +surf354

# HEU
cell36 = openmc.Cell(cell_id=36, fill=mat37)
cell36.region = -surf10 & +surf200 & +surf371 & -surf372 & +surf373 & +surf374

# HEU
cell37 = openmc.Cell(cell_id=37, fill=mat39)
cell37.region = -surf10 & +surf200 & +surf391 & -surf392 & +surf393 & +surf394

# HEU
cell38 = openmc.Cell(cell_id=38, fill=mat41)
cell38.region = -surf10 & +surf200 & +surf411 & -surf412 & +surf413 & +surf414

# HEU
cell39 = openmc.Cell(cell_id=39, fill=mat43)
cell39.region = -surf10 & +surf200 & +surf431 & -surf432 & +surf433 & +surf434

# HEU
cell40 = openmc.Cell(cell_id=40, fill=mat45)
cell40.region = -surf10 & +surf200 & +surf451 & -surf452 & +surf453 & +surf454

# HEU
cell41 = openmc.Cell(cell_id=41, fill=mat47)
cell41.region = -surf10 & +surf200 & +surf471 & -surf472 & +surf473 & +surf474

# HEU
cell42 = openmc.Cell(cell_id=42, fill=mat49)
cell42.region = -surf10 & +surf200 & +surf491 & -surf492 & +surf493 & +surf494

# HEU
cell43 = openmc.Cell(cell_id=43, fill=mat22)
cell43.region = +surf50 & +surf200 & +surf221 & -surf222 & +surf223 & +surf224

# HEU
cell44 = openmc.Cell(cell_id=44, fill=mat24)
cell44.region = +surf50 & +surf200 & +surf241 & -surf242 & +surf243 & +surf244

# HEU
cell45 = openmc.Cell(cell_id=45, fill=mat26)
cell45.region = +surf50 & +surf200 & +surf261 & -surf262 & +surf263 & +surf264

# HEU
cell46 = openmc.Cell(cell_id=46, fill=mat28)
cell46.region = +surf50 & +surf200 & +surf281 & -surf282 & +surf283 & +surf284

# HEU
cell47 = openmc.Cell(cell_id=47, fill=mat30)
cell47.region = +surf50 & +surf200 & +surf301 & -surf302 & +surf303 & +surf304

# HEU
cell48 = openmc.Cell(cell_id=48, fill=mat32)
cell48.region = +surf50 & +surf200 & +surf321 & -surf322 & +surf323 & +surf324

# HEU
cell49 = openmc.Cell(cell_id=49, fill=mat34)
cell49.region = +surf50 & +surf200 & +surf341 & -surf342 & +surf343 & +surf344

# HEU
cell50 = openmc.Cell(cell_id=50, fill=mat36)
cell50.region = +surf50 & +surf200 & +surf361 & -surf362 & +surf363 & +surf364

# HEU
cell51 = openmc.Cell(cell_id=51, fill=mat38)
cell51.region = +surf50 & +surf200 & +surf381 & -surf382 & +surf383 & +surf384

# HEU
cell52 = openmc.Cell(cell_id=52, fill=mat40)
cell52.region = +surf50 & +surf200 & +surf401 & -surf402 & +surf403 & +surf404

# HEU
cell53 = openmc.Cell(cell_id=53, fill=mat42)
cell53.region = +surf50 & +surf200 & +surf421 & -surf422 & +surf423 & +surf424

# HEU
cell54 = openmc.Cell(cell_id=54, fill=mat44)
cell54.region = +surf50 & +surf200 & +surf441 & -surf442 & +surf443 & +surf444

# HEU
cell55 = openmc.Cell(cell_id=55, fill=mat46)
cell55.region = +surf50 & +surf200 & +surf461 & -surf462 & +surf463 & +surf464

# HEU
cell56 = openmc.Cell(cell_id=56, fill=mat48)
cell56.region = +surf50 & +surf200 & +surf481 & -surf482 & +surf483 & +surf484

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell55, cell56])
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
source.space = openmc.stats.Point((0.0, 0.0, -0.3175))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
