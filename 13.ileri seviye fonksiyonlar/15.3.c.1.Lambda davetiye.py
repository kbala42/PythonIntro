baslik='''.........ORTAOKULU
       Sayın '''
davet_metni='''
okumumuzda.............tarihinde.......saatinde bt sınıfında veli toplantısı yapılacaktır,
katılımınızı rica ederiz.
                                    BT Öğretmeni
                                      Nihat BAL
                                      '''
davet_et= lambda isim : baslik+isim+davet_metni

kisi=input("davetli ismi")
print(davet_et(kisi))