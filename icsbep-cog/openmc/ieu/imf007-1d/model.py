"""
IEU-MET-FAST-007 (Rev. 2): Big Ten Detailed Benchmark Model (translated)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Highly Enriched Uranium (93 wt.%)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.981400e-04)
mat1.add_nuclide("U235", 4.503400e-02)
mat1.add_nuclide("U236", 1.323600e-04)
mat1.add_nuclide("U238", 2.605600e-03)

# Intermediate Enriched Uranium (10 wt.%)
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 2.476100e-05)
mat2.add_nuclide("U235", 4.846100e-03)
mat2.add_nuclide("U236", 4.334800e-05)
mat2.add_nuclide("U238", 4.269500e-02)

# Natural Uranium
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U234", 2.651800e-06)
mat3.add_nuclide("U235", 3.470100e-04)
mat3.add_nuclide("U238", 4.784600e-02)

# Depleted Uranium
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U234", 2.867200e-07)
mat4.add_nuclide("U235", 1.005800e-04)
mat4.add_nuclide("U236", 1.146800e-06)
mat4.add_nuclide("U238", 4.767700e-02)

# Natural Uranium (P66)
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U234", 2.645800e-06)
mat5.add_nuclide("U235", 3.462300e-04)
mat5.add_nuclide("U238", 4.773800e-02)

# Steel 347
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 5.779800e-02)
mat6.add_element("Cr", 1.667800e-02)
mat6.add_element("Ni", 9.029600e-03)
mat6.add_element("Mn", 1.753900e-03)
mat6.add_element("Si", 1.715400e-03)
mat6.add_element("Nb", 5.185500e-04)

# Steel 304
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Fe", 5.930800e-02)
mat7.add_element("Cr", 1.760400e-02)
mat7.add_element("Ni", 7.593000e-03)
mat7.add_element("Mn", 1.753900e-03)
mat7.add_element("Si", 1.715400e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# top of C6, CV, CL, R5, R4, R3
surf1 = openmc.ZPlane(surface_id=1, z0=39.05250)
# top of C8, R6
surf2 = openmc.ZPlane(surface_id=2, z0=25.71750)
# top of P1, C7
surf3 = openmc.ZPlane(surface_id=3, z0=23.81250)
# top of P2
surf4 = openmc.ZPlane(surface_id=4, z0=16.66240)
# top of P3
surf5 = openmc.ZPlane(surface_id=5, z0=16.36268)
# top of P4
surf6 = openmc.ZPlane(surface_id=6, z0=13.66012)
# top of P5
surf7 = openmc.ZPlane(surface_id=7, z0=13.36040)
# top of P6
surf8 = openmc.ZPlane(surface_id=8, z0=10.65784)
# top of P7
surf9 = openmc.ZPlane(surface_id=9, z0=10.35812)
# top of P8
surf10 = openmc.ZPlane(surface_id=10, z0=7.65556)
# top of P9
surf11 = openmc.ZPlane(surface_id=11, z0=7.35584)
# top of P10
surf12 = openmc.ZPlane(surface_id=12, z0=4.65328)
# top of P11 and P12
surf13 = openmc.ZPlane(surface_id=13, z0=4.35356)
# top of C5
surf14 = openmc.ZPlane(surface_id=14, z0=4.35102)
# top of P13
surf15 = openmc.ZPlane(surface_id=15, z0=1.65100)
# top of P14 and C4
surf16 = openmc.ZPlane(surface_id=16, z0=1.35128)
# top of C3
surf17 = openmc.ZPlane(surface_id=17, z0=0.0)
# top of P15 and C2
surf18 = openmc.ZPlane(surface_id=18, z0=-1.35128)
# top of P16
surf19 = openmc.ZPlane(surface_id=19, z0=-1.35382)
# top of P17
surf20 = openmc.ZPlane(surface_id=20, z0=-1.65354)
# top of P18
surf21 = openmc.ZPlane(surface_id=21, z0=-3.15468)
# top of P19
surf22 = openmc.ZPlane(surface_id=22, z0=-3.15722)
# top of P20
surf23 = openmc.ZPlane(surface_id=23, z0=-4.35864)
# top of P21
surf24 = openmc.ZPlane(surface_id=24, z0=-4.65836)
# top of P22
surf25 = openmc.ZPlane(surface_id=25, z0=-6.15950)
# top of P23
surf26 = openmc.ZPlane(surface_id=26, z0=-6.16204)
# top of P24
surf27 = openmc.ZPlane(surface_id=27, z0=-7.36346)
# top of P25
surf28 = openmc.ZPlane(surface_id=28, z0=-7.66318)
# top of P26
surf29 = openmc.ZPlane(surface_id=29, z0=-9.16432)
# top of P27
surf30 = openmc.ZPlane(surface_id=30, z0=-9.16686)
# top of P28
surf31 = openmc.ZPlane(surface_id=31, z0=-10.36828)
# top of P29
surf32 = openmc.ZPlane(surface_id=32, z0=-10.66800)
# top of P30
surf33 = openmc.ZPlane(surface_id=33, z0=-12.16914)
# top of P31
surf34 = openmc.ZPlane(surface_id=34, z0=-12.17168)
# top of P32
surf35 = openmc.ZPlane(surface_id=35, z0=-13.37310)
# top of P33
surf36 = openmc.ZPlane(surface_id=36, z0=-13.67282)
# top of P34
surf37 = openmc.ZPlane(surface_id=37, z0=-15.17396)
# top of P35
surf38 = openmc.ZPlane(surface_id=38, z0=-15.17650)
# top of P36
surf39 = openmc.ZPlane(surface_id=39, z0=-16.37792)
# top of P37
surf40 = openmc.ZPlane(surface_id=40, z0=-16.67764)
# top of P38
surf41 = openmc.ZPlane(surface_id=41, z0=-18.17878)
# top of P39
surf42 = openmc.ZPlane(surface_id=42, z0=-18.18132)
# top of P40
surf43 = openmc.ZPlane(surface_id=43, z0=-19.38274)
# top of P41
surf44 = openmc.ZPlane(surface_id=44, z0=-19.68246)
# top of P42
surf45 = openmc.ZPlane(surface_id=45, z0=-21.18360)
# top of P43
surf46 = openmc.ZPlane(surface_id=46, z0=-21.18614)
# top of P44
surf47 = openmc.ZPlane(surface_id=47, z0=-22.38756)
# top of P45 and C1
surf48 = openmc.ZPlane(surface_id=48, z0=-22.39010)
# top of P46
surf49 = openmc.ZPlane(surface_id=49, z0=-22.68982)
# top of P47
surf50 = openmc.ZPlane(surface_id=50, z0=-24.19096)
# top of P48
surf51 = openmc.ZPlane(surface_id=51, z0=-24.19350)
# top of P49
surf52 = openmc.ZPlane(surface_id=52, z0=-25.39492)
# top of P50
surf53 = openmc.ZPlane(surface_id=53, z0=-25.69464)
# top of P51
surf54 = openmc.ZPlane(surface_id=54, z0=-27.19578)
# top of P52
surf55 = openmc.ZPlane(surface_id=55, z0=-27.19832)
# top of P53
surf56 = openmc.ZPlane(surface_id=56, z0=-28.39974)
# top of P54
surf57 = openmc.ZPlane(surface_id=57, z0=-28.69946)
# top of P55
surf58 = openmc.ZPlane(surface_id=58, z0=-30.20060)
# top of P56
surf59 = openmc.ZPlane(surface_id=59, z0=-30.20314)
# top of P57
surf60 = openmc.ZPlane(surface_id=60, z0=-31.40456)
# top of P58
surf61 = openmc.ZPlane(surface_id=61, z0=-31.70428)
# top of P59
surf62 = openmc.ZPlane(surface_id=62, z0=-33.20542)
# top of P60
surf63 = openmc.ZPlane(surface_id=63, z0=-33.20796)
# top of P61
surf64 = openmc.ZPlane(surface_id=64, z0=-34.40938)
# top of P62
surf65 = openmc.ZPlane(surface_id=65, z0=-34.70910)
# top of P63
surf66 = openmc.ZPlane(surface_id=66, z0=-36.21024)
# top of P64
surf67 = openmc.ZPlane(surface_id=67, z0=-36.21278)
# top of P65
surf68 = openmc.ZPlane(surface_id=68, z0=-37.41420)
# top of P66
surf69 = openmc.ZPlane(surface_id=69, z0=-37.71392)
# top of PR1
surf70 = openmc.ZPlane(surface_id=70, z0=-41.73361)
# bot of P66 and R2
surf71 = openmc.ZPlane(surface_id=71, z0=-42.22750)
# bot of R1, R2, and R3
surf72 = openmc.ZPlane(surface_id=72, z0=-57.46750)
# or of C6, ir of CV
surf100 = openmc.ZCylinder(surface_id=100, r=1.79451)
# or of CV, ir of CL
surf101 = openmc.ZCylinder(surface_id=101, r=1.8161)
# or of C1, ir of C7, C8, and R5
surf102 = openmc.ZCylinder(surface_id=102, r=1.905)
# or of C7, ir of C4, C5, P1-P11
surf103 = openmc.ZCylinder(surface_id=103, r=3.175)
# or of C*, ir of R6
surf104 = openmc.ZCylinder(surface_id=104, r=4.28625)
# or of C1,R1,R5,R6, ir of P45-P66, R2, R4
surf105 = openmc.ZCylinder(surface_id=105, r=7.62)
# or of C3 and C4, ir of P14
surf106 = openmc.ZCylinder(surface_id=106, r=11.1125)
# or of C2, C5,P11, ir of P12, P13, P15-P44
surf107 = openmc.ZCylinder(surface_id=107, r=12.7)
# or of R2, R4,and P1-P66 ir of R3
surf108 = openmc.ZCylinder(surface_id=108, r=26.67)
# or of R3
surf109 = openmc.ZCylinder(surface_id=109, r=41.91)
# o.r. rrod1
surf110 = openmc.ZCylinder(surface_id=110, x0=0.0, y0=-33.49752, r=4.43865)
# o.r. rv1
surf111 = openmc.ZCylinder(surface_id=111, x0=0.0, y0=-33.49752, r=4.52501)
# o.r. rl1
surf112 = openmc.ZCylinder(surface_id=112, x0=0.0, y0=-33.49752, r=4.60375)
# o.r. rrod2
surf113 = openmc.ZCylinder(surface_id=113, x0=-29.0097, y0=-16.74876, r=4.43865)
# o.r. rv2
surf114 = openmc.ZCylinder(surface_id=114, x0=-29.0097, y0=-16.74876, r=4.52501)
# o.r. rl2
surf115 = openmc.ZCylinder(surface_id=115, x0=-29.0097, y0=-16.74876, r=4.60375)
# o.r. rrod3
surf116 = openmc.ZCylinder(surface_id=116, x0=29.0097, y0=-16.74876, r=4.43865)
# o.r. rv3
surf117 = openmc.ZCylinder(surface_id=117, x0=29.0097, y0=-16.74876, r=4.52501)
# o.r. rl3
surf118 = openmc.ZCylinder(surface_id=118, x0=29.0097, y0=-16.74876, r=4.60375)
# o.r. rrod4
surf119 = openmc.ZCylinder(surface_id=119, x0=-29.0097, y0=16.74876, r=4.43865)
# o.r. rv4
surf120 = openmc.ZCylinder(surface_id=120, x0=-29.0097, y0=16.74876, r=4.52501)
# o.r. rl4
surf121 = openmc.ZCylinder(surface_id=121, x0=-29.0097, y0=16.74876, r=4.60375)
# o.r. rrod5
surf122 = openmc.ZCylinder(surface_id=122, x0=29.0097, y0=16.74876, r=4.43865)
# o.r. rv5
surf123 = openmc.ZCylinder(surface_id=123, x0=29.0097, y0=16.74876, r=4.52501)
# o.r. rl5
surf124 = openmc.ZCylinder(surface_id=124, x0=29.0097, y0=16.74876, r=4.60375)
# o.r. rrod6
surf125 = openmc.ZCylinder(surface_id=125, x0=0.0, y0=33.49752, r=4.43865)
# o.r. rv6
surf126 = openmc.ZCylinder(surface_id=126, x0=0.0, y0=33.49752, r=4.52501)
# o.r. rl6
surf127 = openmc.ZCylinder(surface_id=127, x0=0.0, y0=33.49752, r=4.60375)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# NatU
cell1 = openmc.Cell(cell_id=1, fill=mat3)
cell1.region = +surf103 & -surf108 & +surf4 & -surf3

# HEU
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf103 & -surf108 & +surf5 & -surf4

# NatU
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf103 & -surf108 & +surf6 & -surf5

# HEU
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = +surf103 & -surf108 & +surf7 & -surf6

# NatU
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf103 & -surf108 & +surf8 & -surf7

# HEU
cell6 = openmc.Cell(cell_id=6, fill=mat1)
cell6.region = +surf103 & -surf108 & +surf9 & -surf8

# NatU
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf103 & -surf108 & +surf10 & -surf9

# HEU
cell8 = openmc.Cell(cell_id=8, fill=mat1)
cell8.region = +surf103 & -surf108 & +surf11 & -surf10

# NatU
cell9 = openmc.Cell(cell_id=9, fill=mat3)
cell9.region = +surf103 & -surf108 & +surf12 & -surf11

# HEU
cell10 = openmc.Cell(cell_id=10, fill=mat1)
cell10.region = +surf103 & -surf108 & +surf13 & -surf12

# NatU
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = +surf107 & -surf108 & +surf15 & -surf13

# HEU
cell12 = openmc.Cell(cell_id=12, fill=mat1)
cell12.region = +surf107 & -surf108 & +surf16 & -surf15

# D38
cell13 = openmc.Cell(cell_id=13, fill=mat4)
cell13.region = +surf106 & -surf108 & +surf18 & -surf16

# HEU
cell14 = openmc.Cell(cell_id=14, fill=mat1)
cell14.region = +surf107 & -surf108 & +surf20 & -surf19

# NatU
cell15 = openmc.Cell(cell_id=15, fill=mat3)
cell15.region = +surf107 & -surf108 & +surf21 & -surf20

# NatU
cell16 = openmc.Cell(cell_id=16, fill=mat3)
cell16.region = +surf107 & -surf108 & +surf23 & -surf22

# HEU
cell17 = openmc.Cell(cell_id=17, fill=mat1)
cell17.region = +surf107 & -surf108 & +surf24 & -surf23

# NatU
cell18 = openmc.Cell(cell_id=18, fill=mat3)
cell18.region = +surf107 & -surf108 & +surf25 & -surf24

# NatU
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = +surf107 & -surf108 & +surf27 & -surf26

# HEU
cell20 = openmc.Cell(cell_id=20, fill=mat1)
cell20.region = +surf107 & -surf108 & +surf28 & -surf27

# NatU
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = +surf107 & -surf108 & +surf29 & -surf28

# NatU
cell22 = openmc.Cell(cell_id=22, fill=mat3)
cell22.region = +surf107 & -surf108 & +surf31 & -surf30

# HEU
cell23 = openmc.Cell(cell_id=23, fill=mat1)
cell23.region = +surf107 & -surf108 & +surf32 & -surf31

# NatU
cell24 = openmc.Cell(cell_id=24, fill=mat3)
cell24.region = +surf107 & -surf108 & +surf33 & -surf32

# NatU
cell25 = openmc.Cell(cell_id=25, fill=mat3)
cell25.region = +surf107 & -surf108 & +surf35 & -surf34

# HEU
cell26 = openmc.Cell(cell_id=26, fill=mat1)
cell26.region = +surf107 & -surf108 & +surf36 & -surf35

# NatU
cell27 = openmc.Cell(cell_id=27, fill=mat3)
cell27.region = +surf107 & -surf108 & +surf37 & -surf36

# NatU
cell28 = openmc.Cell(cell_id=28, fill=mat3)
cell28.region = +surf107 & -surf108 & +surf39 & -surf38

# HEU
cell29 = openmc.Cell(cell_id=29, fill=mat1)
cell29.region = +surf107 & -surf108 & +surf40 & -surf39

# NatU
cell30 = openmc.Cell(cell_id=30, fill=mat3)
cell30.region = +surf107 & -surf108 & +surf41 & -surf40

# NatU
cell31 = openmc.Cell(cell_id=31, fill=mat3)
cell31.region = +surf107 & -surf108 & +surf43 & -surf42

# HEU
cell32 = openmc.Cell(cell_id=32, fill=mat1)
cell32.region = +surf107 & -surf108 & +surf44 & -surf43

# NatU
cell33 = openmc.Cell(cell_id=33, fill=mat3)
cell33.region = +surf107 & -surf108 & +surf45 & -surf44

# NatU
cell34 = openmc.Cell(cell_id=34, fill=mat3)
cell34.region = +surf107 & -surf108 & +surf47 & -surf46

# HEU
cell35 = openmc.Cell(cell_id=35, fill=mat1)
cell35.region = +surf105 & -surf108 & +surf49 & -surf48

# NatU
cell36 = openmc.Cell(cell_id=36, fill=mat3)
cell36.region = +surf105 & -surf108 & +surf50 & -surf49

# NatU
cell37 = openmc.Cell(cell_id=37, fill=mat3)
cell37.region = +surf105 & -surf108 & +surf52 & -surf51

# HEU
cell38 = openmc.Cell(cell_id=38, fill=mat1)
cell38.region = +surf105 & -surf108 & +surf53 & -surf52

# NatU
cell39 = openmc.Cell(cell_id=39, fill=mat3)
cell39.region = +surf105 & -surf108 & +surf54 & -surf53

# NatU
cell40 = openmc.Cell(cell_id=40, fill=mat3)
cell40.region = +surf105 & -surf108 & +surf56 & -surf55

# HEU
cell41 = openmc.Cell(cell_id=41, fill=mat1)
cell41.region = +surf105 & -surf108 & +surf57 & -surf56

# NatU
cell42 = openmc.Cell(cell_id=42, fill=mat3)
cell42.region = +surf105 & -surf108 & +surf58 & -surf57

# NatU
cell43 = openmc.Cell(cell_id=43, fill=mat3)
cell43.region = +surf105 & -surf108 & +surf60 & -surf59

# HEU
cell44 = openmc.Cell(cell_id=44, fill=mat1)
cell44.region = +surf105 & -surf108 & +surf61 & -surf60

# NatU
cell45 = openmc.Cell(cell_id=45, fill=mat3)
cell45.region = +surf105 & -surf108 & +surf62 & -surf61

# NatU
cell46 = openmc.Cell(cell_id=46, fill=mat3)
cell46.region = +surf105 & -surf108 & +surf64 & -surf63

# HEU
cell47 = openmc.Cell(cell_id=47, fill=mat1)
cell47.region = +surf105 & -surf108 & +surf65 & -surf64

# NatU
cell48 = openmc.Cell(cell_id=48, fill=mat3)
cell48.region = +surf105 & -surf108 & +surf66 & -surf65

# NatU
cell49 = openmc.Cell(cell_id=49, fill=mat3)
cell49.region = +surf105 & -surf108 & +surf68 & -surf67

# HEU
cell50 = openmc.Cell(cell_id=50, fill=mat1)
cell50.region = +surf105 & -surf108 & +surf69 & -surf68

# NatUp6
cell51 = openmc.Cell(cell_id=51, fill=mat5)
cell51.region = +surf105 & -surf108 & +surf71 & -surf69

# SS304
cell52 = openmc.Cell(cell_id=52, fill=mat7)
cell52.region = +surf101 & -surf102 & +surf17 & -surf1

# U10
cell53 = openmc.Cell(cell_id=53, fill=mat2)
cell53.region = -surf105 & +surf70 & -surf48

# U10
cell54 = openmc.Cell(cell_id=54, fill=mat2)
cell54.region = -surf107 & +surf48 & -surf18

# U10
cell55 = openmc.Cell(cell_id=55, fill=mat2)
cell55.region = -surf106 & +surf18 & -surf17

# U10
cell56 = openmc.Cell(cell_id=56, fill=mat2)
cell56.region = +surf103 & -surf106 & +surf17 & -surf16

# U10
cell57 = openmc.Cell(cell_id=57, fill=mat2)
cell57.region = +surf103 & -surf107 & +surf16 & -surf14

# U10
cell58 = openmc.Cell(cell_id=58, fill=mat2)
cell58.region = -surf100 & +surf17 & -surf1

# U10
cell59 = openmc.Cell(cell_id=59, fill=mat2)
cell59.region = +surf102 & -surf103 & +surf17 & -surf3

# U10
cell60 = openmc.Cell(cell_id=60, fill=mat2)
cell60.region = +surf102 & -surf104 & +surf3 & -surf2

# D38
cell61 = openmc.Cell(cell_id=61, fill=mat4)
cell61.region = -surf105 & +surf72 & -surf70

# D38
cell62 = openmc.Cell(cell_id=62, fill=mat4)
cell62.region = +surf105 & -surf108 & +surf72 & -surf71

# D38
cell63 = openmc.Cell(cell_id=63, fill=mat4)
cell63.region = +surf108 & -surf109 & +surf72 & -surf1 & +surf112 & +surf115 & +surf118 & +surf121 & +surf124 & +surf127

# D38
cell64 = openmc.Cell(cell_id=64, fill=mat4)
cell64.region = +surf105 & -surf108 & +surf3 & -surf1

# D38
cell65 = openmc.Cell(cell_id=65, fill=mat4)
cell65.region = +surf102 & -surf105 & +surf2 & -surf1

# D38
cell66 = openmc.Cell(cell_id=66, fill=mat4)
cell66.region = +surf104 & -surf105 & +surf3 & -surf2

# D38
cell67 = openmc.Cell(cell_id=67, fill=mat4)
cell67.region = -surf110 & +surf72 & -surf1

# SS347
cell68 = openmc.Cell(cell_id=68, fill=mat6)
cell68.region = +surf111 & -surf112 & +surf72 & -surf1

# D38
cell69 = openmc.Cell(cell_id=69, fill=mat4)
cell69.region = -surf113 & +surf72 & -surf1

# SS347
cell70 = openmc.Cell(cell_id=70, fill=mat6)
cell70.region = +surf114 & -surf115 & +surf72 & -surf1

# D38
cell71 = openmc.Cell(cell_id=71, fill=mat4)
cell71.region = -surf116 & +surf72 & -surf1

# SS347
cell72 = openmc.Cell(cell_id=72, fill=mat6)
cell72.region = +surf117 & -surf118 & +surf72 & -surf1

# D38
cell73 = openmc.Cell(cell_id=73, fill=mat4)
cell73.region = -surf119 & +surf72 & -surf1

# SS347
cell74 = openmc.Cell(cell_id=74, fill=mat6)
cell74.region = +surf120 & -surf121 & +surf72 & -surf1

# D38
cell75 = openmc.Cell(cell_id=75, fill=mat4)
cell75.region = -surf122 & +surf72 & -surf1

# SS347
cell76 = openmc.Cell(cell_id=76, fill=mat6)
cell76.region = +surf123 & -surf124 & +surf72 & -surf1

# D38
cell77 = openmc.Cell(cell_id=77, fill=mat4)
cell77.region = -surf125 & +surf72 & -surf1

# SS347
cell78 = openmc.Cell(cell_id=78, fill=mat6)
cell78.region = +surf126 & -surf127 & +surf72 & -surf1

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell55, cell56, cell57, cell58, cell59, cell60, cell61, cell62, cell63, cell64, cell65, cell66, cell67, cell68, cell69, cell70, cell71, cell72, cell73, cell74, cell75, cell76, cell77, cell78])
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
source.space = openmc.stats.Box((-20.7, -20.7, -40.6), (20.7, 20.7, 33.3))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
