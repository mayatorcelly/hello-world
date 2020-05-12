# Juego Tenis in Python

import turtle

#ventana
wn = turtle.Screen()
wn.title('Tenis by @Torcelly')
wn.bgcolor('green')
wn.setup(width=800, height=600)
wn.tracer(0)

#puntuacion
puntuacion1 = 0
puntuacion2 = 0


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
pelota.shape('circle')
pelota.color('yellow')
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.3
pelota.dy = 0.3

#linea divisoria
division = turtle.Turtle()
division.color('white')
division.goto(0, 400)
division.goto(0, -400)

# marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(2, 240)
pen.write('Jugador 1: 0     Jugador 2: 0', align = 'center', font=('courier', 18, 'normal'))

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
        puntuacion1 += 1
        pen.clear()
        pen.write('Jugador 1: {}     Jugador 2: {}'.format(puntuacion1, puntuacion2), align = 'center', font=('courier', 18, 'normal'))

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntuacion2 += 1
        pen.clear()
        pen.write('Jugador 1: {}     Jugador 2: {}'.format(puntuacion1, puntuacion2), align = 'center', font=('courier', 18, 'normal'))

    # golpeo raquetas y pelota
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < Jugador_2.ycor()) + 50
            and pelota.ycor() > Jugador_2.ycor() - 50):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < Jugador_1.ycor()) + 50
            and pelota.ycor() > Jugador_1.ycor() - 50):
        pelota.dx *= -1
