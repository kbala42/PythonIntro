'''
---------------------------------------------------------tw:@tek_elo
 Kullanıcı girişlerini test eden program
 veri girişlerinden herhangi biri boş girilmişse programı sonladırılır.
 Eğer bütün veriler tam olarak girilmişse yeni veri girilmesi sağlanır.
--------------------------------------------------------------------
'''
while True:
    ad= input("adınızı girin: ")
    soyad= input("soyadınızı girin: ")
    yas= input("yaşınızı girin: ")
    if not ad:
        break
    if not soyad:
        break
    if not yas:
        break
    try:
        print('adınız:',ad,'soyadınız:','yaşınız:',yas)
    except ValueError:
        print("veri girişi yapmadınız")
        continue
    except ZeroDivisionError:
        print("Sıfır girilirse")
        continue