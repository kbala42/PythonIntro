'''
---------------------------------------------------------tw:@tek_elo
turtle modülü python altında grafiksel çizimler
yapabilmemiz sağlayan bir modüldür
--------------------------------------------------------------------
'''
import turtle
#Çizim yaparken kullanacağımız kalem adında nesne üretiyoruz
kalem=turtle.Turtle()

# Başlangıç noktasından ileri doğru 100px çizmesini sağlıyoruz
kalem.forward(100)

#kalemi son noktadan 90 derece dönmesini sağlıyoruz
kalem.lt(90)

# son bulunduğumuz noktadan 100px hareket ettiriyoruz
kalem.forward(100)

#olay döngüsünün yapılmasını sağlayan fonksiyon
turtle.done()