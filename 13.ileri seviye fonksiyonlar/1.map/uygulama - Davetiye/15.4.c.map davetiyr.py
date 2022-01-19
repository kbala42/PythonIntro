belge=open("yazdirlacak.txt","r",encoding="utf-8")
sonuc=map(lambda isim: ''' .........ORTAOKULU
       Sayın '''+isim+
'''
okumumuzda.............tarihinde.......saatinde bt sınıfında veli toplantısı yapılacaktır,
katılımınızı rica ederiz.
                                    BT Öğretmeni
                                      Nihat BAL
'''
,belge)

print(*sonuc)
belge.close()