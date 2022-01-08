yasi=int(input('Lütfen yaşınızı giriniz: '))
bolum='Bilgisayar'
yabanciDil=True
if (yasi>=18 and yasi<35 and bolum=='Bilgisayar' and yabanciDil==True):
    #Aşağıdaki kodun çalışması için yukarıdaki 3 şartın da sağlanması gerekir.
    print('Mülakata katılabilirsiniz.')
else:
    print('Şartlarınız tutmuyor.')