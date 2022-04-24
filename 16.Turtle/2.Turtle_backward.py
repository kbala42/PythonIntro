'''
---------------------------------------------------------tw:@tek_elo
turtle backward fonksiyonu bulunduğu konumdan
geriye çizim yapılmasını sağlayan fonksiyon
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

# kalemle geriye doğru 100 px çiziyoruz
kalem.backward(100)

# kalemi 90. derece sağa döndürüyoruz
kalem.right(90)

# kalemle geriye doğru 100 px çiziyoruz
kalem.backward(100)

turtle.done()