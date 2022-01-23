'''
---------------------------------------------------------tw:@tek_elo
Turtle desen (pattern) uygulaması - 2
--------------------------------------------------------------------
'''
import turtle

def desenCiz (kenarUzunlugu=50,icKenar=3,turSayisi=3):

    if(turSayisi <3 or icKenar<3):
        print("hatalı veri girdiniz")
    else:
        kalem=turtle.Turtle()
        for i in range (turSayisi):
            for j in range (icKenar):
                kalem.forward(kenarUzunlugu)
                kalem.left(360/icKenar)
            kalem.left(360/turSayisi)

desenCiz()

desenCiz(60,4,5)

desenCiz(70,6,10)

turtle.done()