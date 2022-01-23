'''
---------------------------------------------------------tw:@tek_elo
Kullanıcıdan aldığımız uzunluk ve dönüş açısına bağlı olarak
çizim yapan program
--------------------------------------------------------------------
'''
import turtle

kalem=turtle.Turtle()

# kullanıcıdan çizim uzunluğunu alıyoruz
uzunluk=int(input("çizgi uzunluğunu giriniz: "))

# kullanıcıdan dönüş açısını alıyoruz
donusAcisi=int(input("dönüş açısını giriniz: "))
#Kullanıcıdan aldığımız uzunluğa göre çiziyoruz
kalem.forward(uzunluk)
#Kullanıcıdan aldığımız açıya göre kalemi döndürüyoruz
kalem.right(donusAcisi)
#Kullanıcıdan aldığımız uzunluğa göre çiziyoruz
kalem.forward(uzunluk)

turtle.done()