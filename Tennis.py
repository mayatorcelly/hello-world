# Tennis game in Python



import turtle

wn = turtle.Screen()
wn.title('Tennis by @Torcelly')
wn.bgcolor('green')
wn.setup(width=800, height=600)
wn.tracer(0)

#Puntuacion
puntuacion_1 = 0
puntuacion_2 = 0

# Jugador 1
Jugador_1 = turtle.Turtle()
Jugador_1.speed(0)
Jugador_1.shape('square')
Jugador_1.color('white')
Jugador_1.shapesize(stretch_wid=5, stretch_len=1)
Jugador_1.penup()
Jugador_1.goto(-350, 0)

# Jugador 2
Jugador_2 = turtle.Turtle()
Jugador_2.speed(0)
Jugador_2.shape('square')
Jugador_2.color('black')
Jugador_2.shapesize(stretch_wid=5, stretch_len=1)
Jugador_2.penup()
Jugador_2.goto(350, 0)

# pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape('square')
pelota.color('white')
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.1
pelota.dy = 0.1

# lapiz
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0 Player B: 0'), align= 'center', font=('Courier', 24, 'normal')

#Funcion
def Jugador_1_arriba():
    y = Jugador_1.ycor()
    y += 20
    Jugador_1.sety(y)

def Jugador_1_abajo():
    y = Jugador_1.ycor()
    y -= 20
    Jugador_1.sety(y)

def Jugador_2_arriba():
    y = Jugador_2.ycor()
    y += 20
    Jugador_2.sety(y)

def Jugador_2_abajo():
    y = Jugador_2.ycor()
    y -= 20
    Jugador_2.sety(y)

# teclado
wn.listen()
wn.onkeypress(Jugador_1_arriba, 'w')
wn.onkeypress(Jugador_1_abajo, 's')
wn.onkeypress(Jugador_2_arriba, 'p')
wn.onkeypress(Jugador_2_abajo, 'l')


# loop principal
while True:
    wn.update()


    # pelotear
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #fuera
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntuacion_1 += 1

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntuacion_2 *= 1

    # golpeo raquetas y pelota
    
    if (pelota.xcor() > 340 and (pelota.xcor() < 350) and (pelota.ycor() < Jugador_2.ycor() + 40 and pelota.ycor() > Jugador_2.ycor() -40)
       pelota.setx(-340) 
       pelota.dx *= -1

    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < Jugador_1.ycor() + 40 and pelota.ycor() > Jugador_1.ycor() -40)
       pelota.setx(-340) 
       pelota.dx *= -1

