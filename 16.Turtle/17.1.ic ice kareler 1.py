'''
---------------------------------------------------------tw:@tek_elo
Turtle İçe doğru kapanan kareler çizme uygulaması
--------------------------------------------------------------------
'''
import turtle   

tuval = turtle.Screen()

# Arka plan rengi atama
tuval.bgcolor("blue")

tuval.title("Turtle")

kalem = turtle.Turtle()
kalem.color("white")


def kareCiz(size):
    for i in range(4):
        kalem.fd(size)
        kalem.left(90)
        size = size - 5

x=200
for i in range(5):
    kareCiz(x)
    x-=40

turtle.done()
