'''
---------------------------------------------------------tw:@tek_elo
Turtle kullandığımız kalemin renginin ve kalınlığını belirlenmesi
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

# Kalemin rengini kırmızı olarak belirledik
kalem.pencolor("red")
# Kalemin kalınlığını 3px olarak belirledik
kalem.pensize(3)

kalem.forward(100)
kalem.left(90)

kalem.color("#ACE515")
kalem.pensize(8)
kalem.forward(100)

kalem.left(90)

kalem.pencolor("yellow")
kalem.pensize(6)
kalem.forward(100)

kalem.left(90)
kalem.color("#2259C1")
kalem.pensize(1)
kalem.forward(100)

kalem.left (90)

turtle.done()