'''
---------------------------------------------------------tw:@tek_elo
Turtle shape, penup ve goto metotları
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

#kalem şekillerinden turtle imlecini çıkartıyoruz
kalem.shape("turtle")
# 100px ileri çizim yapıyoruz
kalem.forward(100)

#Kalemi kaldırıyoruz
kalem.penup()

#kalemi 0, 100 noktasına taşıyoruz
kalem.goto(0,100)

# 5 kez tekrarlaması istediğimiz döngüde
#her adımda nokta komasını 20 px çizmesini sağlıyoruz
for i in range(5):
    kalem.dot()
    kalem.forward(20)

turtle.done()