'''
---------------------------------------------------------tw:@tek_elo
Turtle ucgen (triangle) uygulaması
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

kalem.pencolor("blue")
kalem.pensize(3)

for i in range(3):
    kalem.forward(200)
    kalem.left(120)

turtle.done()