import turtle

t = turtle.Turtle()
t.pensize(4)

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
t.pencolor("black")
t.fillcolor("#F8C471")

go(174.95, 79.12) 
t.begin_fill()
t.seth(92.22)
t.circle(166.67, 172.02)
t.end_fill()

go(282.64, -19.81) 
t.begin_fill()
t.seth(98.73)
t.circle(77.11, 43.92)
t.seth(142.65)
t.circle(517.78, 10.25)
t.seth(155.31)
t.circle(427.02, 45.83)
t.seth(205.68)
t.circle(827.76, 5.76)
t.seth(211.45)
t.circle(119.59, 39.36)
t.seth(261.99)
t.circle(87.85, 68.82)
t.seth(325.22)
t.circle(417.55, 70.47)
t.seth(38.54)
t.circle(100.14, 51.49)
t.end_fill()

t.fillcolor("#C0392B")

go(146.08, 91.13) 
t.begin_fill()
t.seth(140.88)
t.circle(228.05, 75.35)
t.seth(17.61)
t.circle(-427.02, 38.1)
t.end_fill()

t.fillcolor("#F5CBA7")

go(136.72, 23.81) 
t.begin_fill()
t.seth(129.53)
t.circle(175.80, 97.43)
t.seth(273.9)
t.circle(945.89, 10.66)
t.seth(284.56)
t.circle(79.53, 34.38)
t.seth(318.94)
t.circle(172.93, 27.87)
t.seth(346.8)
t.circle(31.03, 30.48)
t.seth(17.29)
t.circle(201.46, 24.61)
t.seth(41.9)
t.circle(47.84, 30.6)
t.seth(72.5)
t.circle(720.90, 14.51)
t.end_fill()

go(121.73, -89.41) 
t.begin_fill()
t.seth(256.74)
t.circle(-882.26, 5.02)
t.seth(359.52)
t.circle(38.60, 47.13)
t.seth(46.65)
t.circle(57.22, 57.88)
t.seth(112.74)
t.circle(16.16, 90)
t.end_fill()

go(-109.76, -96.27) 
t.begin_fill()
t.seth(131.34)
t.circle(20.21, 47.29)
t.seth(195.36)
t.circle(20.88, 90)
t.seth(280.18)
t.circle(57.46, 43.42)
t.seth(317.26)
t.circle(42.06, 39.35)
t.seth(112.41)
t.circle(-319.81, 12.34)
t.end_fill()

t.fillcolor("black")

go(34.13, -42.54) 
t.begin_fill()
t.seth(111.13)
t.circle(422.83, 18.83)
t.seth(263.15)
t.circle(316.64, 20.79)
t.seth(122.35)
t.circle(-173.14, 38.35)
t.seth(242.15)
t.circle(283.75, 28.21)
t.seth(133.87)
t.circle(34.06, 24.9)
t.seth(270)
t.forward(35.66)
t.seth(157.77)
t.circle(-20.24, 52.93)
t.seth(275.5)
t.circle(204.38, 10.83)
t.seth(139.2)
t.circle(-70.44, 8.4)
t.seth(287)
t.circle(-118.09, 9.17)
t.seth(126.45)
t.circle(264.43, 10.28)
t.seth(221.59)
t.circle(-78.11, 23.94)
t.seth(60.7)
t.circle(138.61, 23.31)
t.seth(202.81)
t.circle(-60.36, 33.4)
t.seth(44.33)
t.circle(148.38, 29.19)
t.seth(54.15)
t.circle(-267.44, 5.03)
t.seth(49.96)
t.circle(-175.80, 97.43)
t.seth(311.72)
t.circle(-101.56, 25.25)
t.seth(289.67)
t.circle(95.96, 29.45)
t.seth(195.88)
t.circle(-50.36, 31.76)
t.seth(278.06)
t.circle(174.76, 13.06)
t.seth(169.64)
t.circle(-46.47, 33.62)
t.seth(242.84)
t.circle(-127.09, 22.07)
t.seth(76.93)
t.circle(207.52, 13.22)
t.seth(253.577)
t.circle(-23.15, 36.99)
t.seth(82.95)
t.circle(145.57, 21.16)
t.seth(254.66)
t.circle(-72, 21.75)
t.seth(93.3)
t.circle(218.19, 30.03)
t.seth(277.47)
t.circle(-444.77, 8.97)
t.seth(125.89)
t.circle(-234.11, 15.63)
t.seth(283.73)
t.circle(-240.73, 21.45)
t.end_fill()

t.fillcolor("white")

go(97.44, -114.79) 
t.begin_fill()
t.seth(197.41)
t.circle(-374.02, 28.96)
t.seth(268.81)
t.circle(71.12, 70.58)
t.seth(339.38)
t.circle(132.11, 43.8)
t.seth(23.18)
t.circle(70.83, 75.18)
t.end_fill()

t.fillcolor("black")
t.pensize(3)

# Dientes
go(93.18, -153.11)
t.seth(182.07)
t.forward(87.09)

go(84.32, -136.40)
t.seth(255.98)
t.forward(25.30)

go(-16.73, -156.26)
t.seth(187.85)
t.circle(-182.55, 21.09)

go(-66.02, -162.18)
t.seth(112.43)
t.forward(22.88)

# Nariz
go(-5.88, -58.98)
t.seth(284.03)
t.circle(-109.74, 23.22)

go(-5.88, -111.51)
t.seth(282.57)
t.circle(12.33, 54.92)

go(15.09, -115.73)
t.seth(239.41)
t.circle(-7.26, 36.87)

go(99.97, -40.25)
t.seth(135)
t.circle(46.38, 90)

go(-30.28, -40.25)
t.seth(154.96)
t.circle(62.16, 59.47)

go(58.55, -64.03)
t.seth(194.9)
t.circle(47.54, 27.66)

go(-31.43, -74.96)
t.seth(128.94)
t.circle(27.14, 56.03)

go(93.18, -80.91) 
t.begin_fill()
t.seth(131.11)
t.circle(36.24, 100.54)
t.seth(28.32)
t.circle(-61.51, 53.88)
t.end_fill()

go(-31.43, -82.25) 
t.begin_fill()
t.seth(124.18)
t.circle(31.66, 122.28)
t.seth(45.9)
t.circle(-42.62, 81.17)
t.end_fill()

go(96.30, -90.24)
t.seth(212.84)
t.circle(-54.42, 49.82)

go(90.28, -100.03)
t.seth(118.87)
t.forward(9.16)

go(69.10, -105.67)
t.seth(105.79)
t.forward(11.82)

go(-107.54, -117.05)
t.seth(121.52)
t.circle(61.64, 16.99)
t.seth(142.04)
t.circle(9.43, 90)

go(-107.54, -120.34)
t.seth(137.19)
t.circle(3.54, 180)
t.seth(308.1)
t.circle(50.62, 18.18)

go(-116.19, -120.53)
t.seth(211.59)
t.circle(9.31, 90)
t.seth(309.02)
t.circle(49.62, 32.91)

go(137.61, -101.92)
t.seth(114.19)
t.circle(6.90, 141.97)

go(105.16, -153.11)
t.seth(9.34)
t.circle(29.91, 90)

go(109.05, -141.04)
t.seth(35.7)
t.circle(48.17, 18.46)
t.seth(61.58)
t.circle(9.65, 90)

go(-149.12, -118.08)
t.seth(160.22)
t.circle(-148.71, 23.43)

go(-219.17, -62.41)
t.seth(135)
t.circle(-44.13, 90)

go(-176.48, 41.5)
t.seth(34.6)
t.circle(-330.54, 17.91)

go(85.14, 86.03)
t.seth(346.06)
t.circle(-257.06, 23.19)

go(221.06, 4.39)
t.seth(312.22)
t.circle(-47.29, 90)

go(204.36, -86.53)
t.seth(222.53)
t.circle(-151.58, 23.44)

t.hideturtle()
turtle.done()