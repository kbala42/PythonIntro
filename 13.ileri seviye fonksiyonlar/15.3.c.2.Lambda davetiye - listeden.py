baslik='''.........ORTAOKULU
       Sayın '''
davet_metni='''
okumumuzda.............tarihinde.......saatinde bt sınıfında veli toplantısı yapılacaktır,
katılımınızı rica ederiz.
                                    BT Öğretmeni
                                      Nihat BAL
                                      '''
davet_et= lambda isim : baslik+isim+davet_metni

belge=open("davetliler.txt","r",encoding="utf-8")
for kisi in belge:
    print(100*"-")
    print(davet_et(kisi))