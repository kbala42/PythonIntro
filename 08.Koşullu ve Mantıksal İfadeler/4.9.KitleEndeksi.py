boy = float(input("Boy: Örnek 1.73----:"))
kilo = float(input("Kilo: Örnek: 78.40----:"))
endeks = kilo/(boy**2)
if endeks<18.5:
    print("Zayıfsınız")
elif endeks > 18.5 and endeks <=25 :
    print("Normalsiniz")
elif endeks > 25 and endeks <=30:
    print("Kilolusunuz")
elif endeks > 30:
    print("Dikkat! obez")