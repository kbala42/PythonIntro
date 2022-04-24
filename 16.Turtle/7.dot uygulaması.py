'''
---------------------------------------------------------tw:@tek_elo
Turtle 'da dot(nokta) uygulaması
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

# 5 kez tekrarlaması istediğimiz döngüde
#her adımda nokta komasını 20 px çizmesini sağlıyoruz
for i in range(5):
    kalem.dot()
    kalem.forward(20)

#Kalemi geriye 100 px gelerek başlangıç noktasına gelmesini sağlıyoruz
kalem.backward(100)

#Kalemin 180 dönmesini sağlıyoruz
kalem.left(180)

#Kalemi kaldırırak çizgi çizmesini sağlıyoruz
kalem.up()

# 5 kez tekrarlaması istediğimiz döngüde
#her adımda nokta koymasını ve 20 px hareket emesini sağlıyoruz
#20px çizmemesinin sebebi kalemin up() metodunu kullanmamız
for i in range(5):
    kalem.dot()
    kalem.forward(20)

turtle.done()