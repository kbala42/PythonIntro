'''
---------------------------------------------------------tw:@tek_elo
Turtle çokgen (polygon) uygulaması
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

kalem.pencolor("red")
kalem.pensize(3)

kenar_sayısı=int(input(" çizmek istediğiniz çokgenin kenar sayısını giriniz: "))

for i in range(kenar_sayısı):
    kalem.forward(50)
    kalem.left(360/kenar_sayısı)

turtle.done()