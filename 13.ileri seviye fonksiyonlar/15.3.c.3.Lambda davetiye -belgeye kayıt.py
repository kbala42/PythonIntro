baslik='''              .........ORTAOKULU
       Sayın '''
davet_metni='''
okumumuzda.............tarihinde.......saatinde bt sınıfında veli toplantısı yapılacaktır,
katılımınızı rica ederiz.
                                    BT Öğretmeni
                                      Nihat BAL
                                      '''
davet_et= lambda isim : baslik+isim+davet_metni

belge=open("davetliler.txt","r",encoding="utf-8")
hepsi=""
for kisi in belge:
    print(100*"-")
    hepsi=hepsi+"\n"+davet_et(kisi)
    print(davet_et(kisi))
belge.close()

belge=open("yazdirlacak.txt","w",encoding="utf-8")
belge.write(hepsi)

