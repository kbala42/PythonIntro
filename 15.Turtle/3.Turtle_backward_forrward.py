'''
---------------------------------------------------------tw:@tek_elo
turtle fonksiyon hareketlerinde noktalı ve eksi sayılar kullanabiliriz
eksi sayılar geriye doğru hareketi temsil eder.
--------------------------------------------------------------------
'''
import turtle
kalem=turtle.Turtle()

kalem.forward(-100.5)
kalem.right(90)

kalem.forward(-100.5)
kalem.backward(-100.6)
kalem.right(90)

kalem.backward(-100.6)
kalem.left(45)

kalem.forward(100)
turtle.done()