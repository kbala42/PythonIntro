'''
---------------------------------------------------------tw:@tek_elo
Turtle kareler (squares) uygulaması
--------------------------------------------------------------------
'''
import turtle

kalem = turtle.Turtle()

kalem.color("blue")

for k in range(5,106,25):
    print(k)
    for i in range(4):
        kalem.forward(k)
        kalem.left(90)

turtle.done()