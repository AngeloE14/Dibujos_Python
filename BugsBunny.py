import turtle
t = turtle.Turtle()
t.pensize(7)
t.shape("turtle")

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def arco(direc, radio, ang):
    t.seth(direc)
    t.circle(radio, ang)

def linea(direc, longitud):
    t.seth(direc)
    t.forward(longitud)
    
t.fillcolor("OrangeRed")
go(181.85, -28.19)
t.begin_fill()
arco(90, 181.85, 360)
t.end_fill()

t.pensize(3)
t.fillcolor("DarkGray")
go(45.58, 77.09)
t.begin_fill()
arco(104.41, 153.54, 51.76)
arco(156.17, -178.95, 28.78)
arco(239.18, 24, 52.68)
arco(291.86, 175.21, 38.83)
arco(330.69, -194.67, 26.54)
arco(53.7, -35.25, 32.37)
t.end_fill()

t.fillcolor("#ffccbc")
go(35.09, 74.1)
t.begin_fill()
arco(104.99, 133.63, 47.08)
arco(152.07, -415.54, 9.71)
arco(298.73, 168.78, 29.41)
arco(328.14, -262.37, 19.6)
t.end_fill()

go(-106.05, 212.79)
arco(302.62, 69.16, 19.21)

t.fillcolor("DarkGray")
go(128.42, -15.2)
t.begin_fill()
arco(117.6, -371.2, 6.82)
arco(110.78, 315.61, 8.2)
arco(74.76, 161.41, 57.14)
arco(131.9, -169.78, 29.47)
arco(232.8, 47.89, 39.82)
arco(272.62, 172.39, 28.92)
arco(301.53, -500.42, 10.3)
arco(148.12, 43.64, 38.19)
arco(351.23, -32.95, 44.42)
arco(144.34, 35.76, 56.29)
arco(0.57, -35.71, 41.72)
arco(173.77, 36.48, 41.87)
arco(5.75, -113.12, 11.5)
arco(202.11, 72.88, 26.3)
arco(121.97, 20.72, 36.4)
arco(158.37, 4.99, 101.21)
arco(259.58, 49.75, 24.81)
arco(284.39, -70.27, 50.75)
arco(349.27, -43.76, 29.87)
arco(329.11, 41.42, 55.33)
arco(24.44, -127.89, 32.58)
t.end_fill()

t.fillcolor("#ffccbc")
go(83.75, 89.96)
t.begin_fill()
arco(80.3, 126.24, 49.51)
arco(129.81, -327.74, 11.57)
arco(274.72, 158.98, 29.15)
arco(303.87, -292.5, 17.65)
t.end_fill()

t.fillcolor("DarkGray")
go(94.56, -100.53)
t.begin_fill()
arco(233.56, -52.7, 32.79)
arco(200.77, -29.86, 24.96)
arco(271.89, 186.9, 3.75)
arco(158.15, 31.25, 25.41)
arco(183.56, 23.84, 57.7)
arco(241.26, 69.21, 56.53)
arco(8.01, 181.85, 8.19)
arco(305.39, 253.3, 24.26)
arco(329.65, 11.47, 111.67)
arco(81.32, 235.3, 33.42)
arco(114.74, 26.7, 84.27)
arco(97.63, -67.69, 15.26)
t.end_fill()

go(-25.56, -208.23)
t.begin_fill()
arco(112.45, 935.38, 6)
arco(213.04, -56.22, 27.39)
arco(297.16, -353.16, 12.03)
arco(338.69, 181.85, 13.23)
t.end_fill()

t.pensize(7)
t.fillcolor("White")
go(99.88, -180.15)
t.begin_fill()
arco(213.32, -181.85, 7.11)
t.pensize(3)
arco(320.43, 188.94, 11.44)
arco(106.1, 252.05, 7.79)
t.end_fill()

go(62.3, -174.86)
t.begin_fill()
arco(81.45, -65.19, 15.26)
arco(66.18, 146.94, 13.02)
arco(79.2, 27.63, 22.33)
arco(28.08, 52.7, 25.48)
arco(23.73, 187.85, 11.67)
arco(35.4, 43.39, 29.29)
arco(291.2, 5.47, 23.16)
arco(314.36, 3.55, 134.34)
arco(88.7, 22.67, 33.28)
arco(317.07, 34.89, 11.45)
arco(328.52, 2.4, 121.02)
arco(89.53, 32.08, 35.33)
arco(327.19, 48.43, 13.57)
arco(340.75, 1.81, 139.87)
arco(120.62, 43.57, 40.78)
arco(161.4, 99.45, 45.61)
arco(207.01, -47.76, 63.56)
arco(143.46, 28.33, 66.33)
arco(209.78, 35.57, 25.54)
arco(235.32, 2.11, 135.44)
arco(10.76, 15.17, 29.59)
arco(218.54, 24.5, 44.83)
arco(263.37, 2.51, 130.22)
arco(33.59, 9.36, 42.18)
arco(251.95, 28.46, 44.14)
arco(296.09, 1.32, 121.1)
arco(57.19, 18.56, 25.99)
arco(308.43, 142.84, 14.8)
arco(323.22, -5052.05, 0.45)
arco(295.45, 29.55, 46.15)
arco(276.11, -174.96, 5.69)
arco(229.16, 48.28, 27.6)
arco(306.84, 233.7, 5.28)
t.end_fill()

go(62.16, -175.18)
t.begin_fill()
arco(72.11, 12.88, 117.99)
arco(190.1, 12.93, 18.75)
arco(208.85, 26.98, 67.41)
arco(276.26, 19.54, 33.19)
arco(309.45, 14.31, 73.61)
arco(137.46, -24.38, 32.3)
arco(105.16, -14.96, 76.63)
arco(28.53, -8.31, 86.84)
t.end_fill()

go(43.67, -159.95)
t.begin_fill()
arco(208.85, 26.98, 67.41)
arco(276.26, 19.54, 33.19)
arco(309.45, 14.31, 73.61)
arco(197.17, -169.96, 25.03)
arco(56.06, -114.53, 41.5)
t.end_fill()

go(-55.42, -101.74)
t.begin_fill()
arco(78.64, 12.72, 87.64)
arco(166.6, 43.14, 75.75)
arco(242.34, 12.63, 92.59)
arco(334.93, 27.82, 30.75)
arco(5.68, 56.35, 27.33)
arco(33.01, 28.1, 45.63)
t.end_fill()

t.fillcolor("Orange")
go(-58.09, -44.04)
t.begin_fill()
arco(117.03, 71.07, 14.79)
arco(113.3, 70.23, 30.57)
arco(126.12, 65.81, 32.21)
arco(130.18, 67.25, 26.55)
arco(234.29, -6.71, 92.54)
arco(313.42, -9.02, 62.04)
arco(251.38, -4.83, 118.72)
arco(297.29, -35.79, 10.76)
arco(286.54, -9.96, 38.63)
arco(278.53, 22.75, 40.41)
arco(286.37, 153.76, 22.34)
arco(277.4, 64.73, 30.42)
arco(307.82, 30.61, 93.22)
arco(41.04, 35.13, 75.99)
t.end_fill()

t.fillcolor("White")
go(-64.78, -33.38)
t.begin_fill()
arco(107.68, -81.65, 13.67)
arco(94.01, -192.08, 11.83)
arco(82.17, 4.19, 115.99)
arco(198.16, 19.1, 45.63)
arco(243.79, 62.62, 20.44)
arco(322.19, -70.23, 28.89)
arco(311.82, -71.07, 4.63)
t.end_fill()

go(-77.22, -92.6)
t.begin_fill()
arco(197.48, -30.61, 69.66)
arco(127.82, -64.73, 17.35)
arco(31.98, 39.39, 53.11)
arco(85.09, 42.97, 9.82)
arco(93.64, 7.37, 139.39)
arco(233.03, -96.51, 13.1)
arco(65.66, 50.25, 54.01)
arco(119.67, 5.82, 126.65)
arco(246.32, 1154.42, 1.26)
arco(128.48, 72.01, 35.42)
arco(163.9, 14.52, 42.88)
arco(206.78, 3.99, 109.99)
arco(316.77, -259.42, 12.76)
arco(246.96, 25.12, 13.6)
arco(260.55, 12.38, 105.37)
arco(253.12, 13.29, 61.65)
arco(314.77, 141.64, 5.06)
arco(319.84, 141.89, 17.97)
arco(337.81, 17.6, 86.82)
arco(64.64, 13.98, 35.41)
t.end_fill()

go(81.53, -16.58)
t.begin_fill()
arco(72.05, 66.9, 58.72)
arco(229.88, 53.52, 40.34)
arco(270.22, 105.37, 20.31)
arco(26.01, -99.45, 11.6)
t.end_fill()

go(17.89, -24.39)
t.begin_fill()
arco(65.09, 81.22, 51.14)
arco(232.25, 34.71, 32.55)
arco(264.81, 259.63, 10.39)
arco(323.13, 56.88, 9.45)
t.end_fill()

go(11.45, 271.53)
arco(277.8, 75.76, 19.72)
go(86.52, 32.88)
arco(90, 71.07, 31.33)
arco(123.61, 7.37, 82.93)
arco(206.53, 14.82, 51.42)
go(81.41, 78.26)
arco(76.4, 148.57, 4.6)
go(75.76, 74.4)
arco(90.93, 88.57, 16.27)
go(63.78, 78.26)
arco(149.1, 24.19, 26.58)
go(68.56, 47.71)
arco(132.18, 25.85, 18.07)
go(28.9, 55.12)
arco(101.03, 23.25, 19.51)
go(17.08, 45.71)
arco(114.48, 18.94, 15.65)
go(44.02, -13.42)
arco(138.57, 10.59, 62.65)
go(44.56, -17.29)
arco(145.95, 18.35, 51.11)
go(-18.98, -26.02)
arco(215.22, 29.15, 8.78)
go(-21.93, -39.36)
arco(234.97, 44.98, 4.15)
go(-17.08, -55.7)
arco(88.45, 12.41, 28.03)
go(-6.86, -43.23)
arco(314.38, 16.42, 54.71)
go(8.46, -38.98)
arco(243.91, 13.39, 113.76)
arco(357.67, 25.46, 23.08)
arco(170.26, -12.84, 50.85)
go(35.16, -91.06)
arco(285.32, 67.14, 12.85)
go(68.43, -42.81)
arco(162.89, 27.34, 30.86)
go(94.56, -100.53)
arco(51.3, 72.67, 8)
go(105.94, -46.36)
arco(14.35, 32.9, 21.91)
go(137.49, -58.25)
arco(291.73, 19.22, 23.82)
go(138.82, -42.38)
arco(299.38, 48.54, 13.79)
go(144.23, -31.75)
arco(320.7, 57.44, 6.1)
go(40.72, -105.02)
arco(298.17, 31.84, 30.79)
arco(328.97, 19.74, 52.23)
arco(21.2, 59.38, 30.1)
go(58.04, -147.72)
arco(71.67, 23.29, 24.94)
go(99.88, -180.15)
arco(111.99, 34.35, 31.72)
go(111.59, -212.33)
arco(334.76, 399.85, 2.86)
go(94.56, -118.5)
arco(204.05, 26.74, 29.72)
arco(233.77, 57.4, 20.54)
go(62.16, -175.18)
arco(317.22, 635.74, 2.19)
go(-152.59, -18.08)
arco(244.65, 207.72, 8)
go(-130.13, -39.73)
arco(231.61, -95.8, 10.66)
arco(219.93, 30.18, 29.48)
go(-127.39, -68.51)
arco(16.12, 26.2, 17.65)

t.fillcolor("Black")
go(24, 0)
t.begin_fill()
arco(103.93, 5.67, 44.13)
arco(148.05, 2.61, 94.01)
arco(242.06, 18.33, 50.67)
arco(292.74, 3.79, 66.43)
arco(71.81, 81.22, 11.25)
t.end_fill()

go(80.24, 2.28)
t.begin_fill()
arco(123.35, 3.15, 113.82)
arco(237.17, 15.42, 65.66)
arco(302.83, 2.85, 109.63)
arco(52.46, 14.61, 70.89)
t.end_fill()

t.fillcolor("#11b525")
go(-76.19, -67.91)
t.begin_fill()
arco(196.45, 10.95, 38.03)
arco(298.1, -164.65, 16.26)
arco(281.83, -328.84, 8.08)
arco(222.32, 67.98, 49.96)
arco(272.29, 6.34, 104.76)
arco(259.57, 30.16, 35.87)
arco(295.45, 9.2, 58.37)
arco(265.27, 20.51, 66.25)
arco(253.36, 31.82, 37.03)
arco(290.39, 8.71, 117.03)
arco(47.43, 35.49, 34.84)
arco(310.09, 7.85, 125.39)
arco(75.48, 34.84, 34.88)
arco(327.21, 22.13, 19.86)
arco(347.07, 6.22, 106.54)
arco(93.6, 39.4, 32.28)
arco(315.54, 6.43, 120.59)
arco(76.13, 39.63, 34.92)
arco(111.05, 70.11, 36.17)
arco(110.03, 261.51, 17.37)
arco(111.29, 146.31, 9.56)
t.end_fill()

t.fillcolor("FireBrick")
go(105.94, -46.36)
t.begin_fill()
arco(188.71, -63.42, 26.66)
arco(162.05, 24.77, 57.78)
arco(219.83, -34.84, 41.42)
arco(296.06, -2975.34, 0.89)
arco(295.17, 13.82, 105.61)
arco(40.78, 59.13, 26.26)
arco(67.04, -207.27, 10.89)
t.end_fill()

t.fillcolor("LightSalmon")
go(93.11, -68.28)
t.begin_fill()
arco(166.6, 15.37, 46.14)
arco(162.85, 17.44, 57.24)
arco(220.09, 45.47, 36.77)
arco(295.17, 13.82, 105.61)
arco(40.78, 59.13, 26.26)
arco(67.04, -207.27, 3.86)
t.end_fill()

t.fillcolor("Salmon")
go(37.84, -30.82)
t.begin_fill()
arco(41.47, 2.48, 124.62)
arco(166.09, 50.54, 20.21)
arco(186.3, 3.57, 104.97)
arco(291.27, 20.51, 34.22)
arco(22.6, 51.04, 18.87)
t.end_fill()

go(81.24, -70.3)
arco(217.35, 24.18, 42.07)

t.fillcolor("White")
go(45.33, -53.53)
t.begin_fill()
arco(204.35, -34.84, 25.94)
arco(200.75, -25.46, 21.6)
arco(289.88, 90.99, 16.05)
arco(358.74, 37.88, 17.91)
linea(47.82, 6.5)
arco(99.78, -603.23, 2)
t.end_fill()

go(28.47, -57.14)
arco(289.06, 65.67, 14.86)
go(-158.75, 15.78)
arco(309.85, 6.79, 48.5)
arco(358.35, 5.47, 86.92)
arco(85.26, 19.72, 25.71)
arco(354.13, 18.48, 17.57)
arco(11.69, 3.78, 92.75)
arco(104.45, 23.55, 24.03)
go(-151.03, 7.98)
arco(265.44, 58.29, 5.87)
go(-131.73, 22.36)
arco(185.16, 18.39, 61.93)
go(-120.39, 22.36)
arco(164.81, 21.06, 18.18)
go(-110.42, 2.99)
arco(176.24, 20.82, 54.12)
go(-91.53, 0)
arco(149.52, 62.61, 11.89)
go(-93.07, -22.81)
arco(186.95, 23.6, 23.27)
go(-68.44, -28.94)
arco(143.58, 35.79, 31.69)
go(-64.16, -65.93)
arco(170, 19.98, 97.06)

t.pensize(2)
go(13.45, -30.28)
arco(162.14, 446.01, 12.82)
go(11.88, -38.07)
arco(164.17, 221.13, 28.14)
go(9.53, -44.17)
arco(174.3, 232.28, 26.39)
go(38.85, -38.07)
arco(19.42, -239.95, 32.11)
go(40.85, -41.86)
arco(11.12, -229.87, 33.74)
go(38.85, -46.76)
arco(1.37, -236.33, 29.95)

t.pensize(3)
go(-34.56, -260.29)
arco(293.44, 20.36, 26.08)
go(-53.37, -263.86)
arco(345.06, 21.84, 11.75)
go(-20.6, -238.5)
arco(294.29, 14.19, 26.93)
go(-59.19, -229.51)
arco(264.61, 22.25, 50.28)
arco(314.89, 7.25, 59.81)
arco(14.7, 19.6, 35.62)
go(-64.04, -244.14)
arco(4.89, 8.35, 54.06)
go(-9.31, -219.62)
arco(125.25, 47.23, 18.63)
go(-64.72, -199.98)
arco(229.18, 38.33, 34.06)
go(-34.06, -183.14)
arco(150.1, 28.12, 70.32)
go(-16.39, -174.6)
arco(142.44, 22.56, 79.18)
go(-27.53, -159.08)
arco(287.99, -51.19, 13.04)
go(-55.81, -114.02)
arco(294.05, -185.42, 16.7)
go(-65.48, -89.81)
arco(290.35, -291.66, 18.03)
go(-59.82, -161.74)
arco(278.08, -130.71, 8.65)

t.hideturtle()
turtle.done()