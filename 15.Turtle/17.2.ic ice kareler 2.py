'''
---------------------------------------------------------tw:@tek_elo
Turtle Dışa doğru açılan kareler uygulaması
--------------------------------------------------------------------
'''

import turtle  # Inside_Out

tuval = turtle.Screen()

tuval.bgcolor("Blue")

kalem = turtle.Turtle()
kalem.color("white")


def kareCiz(size):
    for i in range(4):
        kalem.fd(size)
        kalem.left(90)
        size = size + 5

x=10
for i in range(5):
    kareCiz(x)
    x+=40

turtle.done()
