import turtle
mp=turtle.Turtle()
turtle.bgcolor("pink")
mp.speed(10)
mp.color('purple')
mp.pensize(14)
mp.penup()
mp.left(180)
mp.forward(300)
mp.right(90)
mp.forward(100)
mp.left(90)
mp.left(120)
mp.pendown()
mp.circle(25,140)
mp.forward(140)
mp.right(160)
mp.forward(40)
mp.circle(40,160)
mp.forward(40)
mp.right(160)
mp.forward(140)
mp.circle(25,155)
mp.forward(140)
mp.right(155)
mp.forward(140)
mp.circle(25,170)
mp.forward(100)
mp.circle(-40,250)
mp.forward(55)
mp.left(120)
mp.forward(100)
mp.circle(25,120)
mp.forward(80)
mp.right(160)
mp.forward(80)
mp.circle(25,160)
mp.forward(140)
mp.right(155)
mp.forward(140)
mp.circle(25,160)
mp.forward(30)
mp.left(50)
mp.penup()
mp.forward(40)
mp.left(45)
mp.pendown()
mp.forward(90)
mp.penup()
mp.forward(220)
mp.pendown()
mp.forward(90)
mp.penup()
mp.forward(300)
mp.left(90)
mp.forward(330)
mp.left(180)
mp.pendown()
mp.forward(140)
mp.right(50)
mp.forward(50)
mp.circle(-45,200)
mp.forward(88)
mp.left(70)
mp.forward(140)
mp.left(70)
mp.circle(25,90)
mp.forward(140)
mp.right(140)
mp.forward(140)
mp.circle(25,160)
mp.forward(110)
mp.left(180)
mp.forward(70)
mp.circle(60,180)
mp.forward(70)
mp.left(180)
mp.forward(100)
mp.circle(25,180)
mp.forward(200)
mp.left(180)
mp.forward(200)
mp.circle(25,165)
mp.forward(130)
mp.right(150)
mp.forward(130)
mp.circle(25,130)
mp.left(40)
mp.penup()
mp.forward(70)
mp.left(85)
mp.pendown()
mp.forward(110)
mp.penup()
mp.forward(270)
mp.pendown()
mp.forward(100)
mp.penup()
mp.right(90)
mp.forward(360)
mp.right(90)
mp.forward(515)
mp.pendown()
colores=["deep pink","dark violet","deep pink","dark violet"]
for i in range(8):
    mp.pensize(5)
    mp.color(colores[i%4])
    mp.left(70)
    mp.forward(50)
    mp.right(140)
    mp.right(135)
    mp.penup()
    mp.forward(1)
    mp.pendown()
    mp.left(70)
mp.penup()
mp.right(50)
mp.forward(450)
mp.pendown()
mp.color("black")
mp.pensize(9)
mp.speed(10)
mp.left(60)
mp.circle(-60,70)
mp.right(35)
mp.circle(-60,65)
mp.left(60)
mp.circle(-100,90)
mp.circle(-200,90)
mp.circle(-100,90)
mp.left(60)
mp.circle(-60,65)
mp.right(35)
mp.circle(-60,70)
mp.left(83)
mp.circle(-200,37)
mp.penup()
mp.right(35)
mp.forward(110)
mp.left(65)
mp.pendown()
mp.circle(-200,25)
mp.left(180)
mp.circle(200,25)
mp.penup()
mp.left(80)
mp.forward(30)
mp.left(90)
mp.pendown()
mp.circle(-200,25)
mp.left(180)
mp.circle(200,25)
mp.penup()
mp.left(80)
mp.forward(30)
mp.left(90)
mp.pendown()
mp.circle(-200,25)
mp.left(180)
mp.circle(200,25)
mp.right(3)
mp.penup()
mp.forward(270)
mp.pendown()
mp.left(7)
mp.circle(200,25)
mp.left(180)
mp.circle(-200,25)
mp.right(80)
mp.penup()
mp.forward(30)
mp.right(90)
mp.pendown()
mp.circle(200,25)
mp.left(180)
mp.circle(-200,25)
mp.right(80)
mp.penup()
mp.forward(30)
mp.right(90)
mp.pendown()
mp.circle(200,25)
mp.left(180)
mp.circle(-200,25)
mp.left(30)
mp.penup()
mp.forward(40)
mp.pendown()
mp.fillcolor("black")
mp.begin_fill()
mp.left(90)
mp.circle(-17)
mp.end_fill()
mp.right(137)
mp.penup()
mp.forward(182)
mp.pendown()
mp.fillcolor("black")
mp.begin_fill()
mp.circle(17)
mp.end_fill()
mp.left(180)
mp.penup()
mp.forward(70)
mp.pendown()
mp.right(37)
mp.pensize(5)
mp.fillcolor("yellow")
mp.begin_fill()
mp.circle(25,90)
mp.circle(12.5,90)
mp.circle(25,90)
mp.circle(12.5,90)
mp.end_fill()
mp.right(30)
mp.penup()
mp.forward(125)
mp.pendown()
col=["DarkMagenta", "HotPink2"]
for i in range(15):
    mp.color(col[i%2])
    mp.pensize(11)
    mp.circle(50,90)
    mp.left(90)
    mp.circle(40,50)
mp.penup()
mp.forward(1000000)