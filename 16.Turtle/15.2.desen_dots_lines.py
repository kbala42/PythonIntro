'''
---------------------------------------------------------tw:@tek_elo
Turtle noktalar (doys) uygulaması - 2
--------------------------------------------------------------------
'''
import turtle

kalem = turtle.Turtle()

for y in range(4):
    kalem.down()
    kalem.dot()
    for i in range(4):
        kalem.forward(20)
        kalem.dot()
    kalem.up()
    kalem.backward(80)
    kalem.right(90)
    kalem.forward(20)
    kalem.left(90)

turtle.done()