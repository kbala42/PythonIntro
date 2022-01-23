'''
---------------------------------------------------------tw:@tek_elo
Turtle kare (square) uygulaması
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

kalem.pencolor("red")
kalem.pensize(3)

for i in range(4):
    kalem.forward(200)
    kalem.left(90)

turtle.done()