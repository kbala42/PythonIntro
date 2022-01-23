'''
---------------------------------------------------------tw:@tek_elo
Turtle altıgen (hexagon) uygulaması
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

kalem.pencolor("blue")
kalem.pensize(3)

for i in range(6):
    kalem.forward(100)
    kalem.left(60)
turtle.done()