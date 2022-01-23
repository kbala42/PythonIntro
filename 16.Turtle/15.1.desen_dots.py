'''
---------------------------------------------------------tw:@tek_elo
Turtle noktalar (doys) uygulaması
--------------------------------------------------------------------
'''
import turtle

kalem = turtle.Turtle()

kalem.penup()

for y in range(4):
    for i in range(4):
        kalem.dot()
        kalem.forward(20)
    kalem.backward(80)
    kalem.right(90)
    kalem.forward(20)
    kalem.left(90)

turtle.done()