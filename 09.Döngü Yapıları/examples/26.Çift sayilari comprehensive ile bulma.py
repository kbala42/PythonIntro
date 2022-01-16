print('''
-----------------------------------------------------------------------------tw:@tek_elo
list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayılardan\n
bir liste oluşturma
----------------------------------------------------------------------------------------''')
liste = [x for x in range(1,101) if x % 2 == 0]
print(liste)