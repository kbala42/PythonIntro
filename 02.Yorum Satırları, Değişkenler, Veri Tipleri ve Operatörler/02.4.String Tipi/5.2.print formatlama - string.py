print('-----------------------------------------------')
print('String tiplerinde değişkenler için aşağıdaki\n'
      'şekillerde formatlama yapılabilir')
print('-----------------------------------------------')
metin1="Merhaba"
metin2="Python"
metin3="Dili"
print("{} {} {}".format(metin1,metin2,metin3))
print()

print('-----------------------------------------------')
print('format fonksiyonu içinde indis numarası\n'
      'verilerek daha esnek bir formatlama yapılabilir')
print('-----------------------------------------------')
print("{1} {2} {0}".format(metin1,metin2,metin3))
print()

print('------------------------------------------------------')
print('format fonksiyonu bir belirteç olarak belirtilmek\n'
      'suretiyle direkt eklenmesi düşünülen yerde yazılabilir')
print('------------------------------------------------------')
print(f"{metin2} {metin3} {metin1}")
