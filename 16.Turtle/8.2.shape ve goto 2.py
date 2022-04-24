'''
---------------------------------------------------------tw:@tek_elo
Turtle imleç uygulaması
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

#kalem şekillerinden turtle imlecini çıkartıyoruz
kalem.shape("turtle")

# 4 kez tekrarlaması istediğimiz döngüde
#iki nokta rası 20 px çizgi
#daha sonra ki nokta arası boşluk
#olan bir örüntü çiziyoruz
for i in range(4):
    kalem.up()
    kalem.forward(20)
    kalem.dot()
    kalem.down()
    kalem.forward(20)
    kalem.dot()
turtle.done()