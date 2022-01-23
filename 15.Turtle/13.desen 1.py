'''
---------------------------------------------------------tw:@tek_elo
Turtle desen (pattern) uygulaması - 1
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

kalem.color("green")

for i in range (6):
    for j in range (6):
        kalem.forward(50)
        kalem.left(60) # iç döngü
    kalem.left(60)# dış döngü

turtle.done()