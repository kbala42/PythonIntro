def agacCiz(agacinYuksekligi, karakter='*'):
    b=agacinYuksekligi
    for i in range(1,agacinYuksekligi+1):
        print(b*' ',(2*i-1)*karakter)
        b-=1

agacYuksekligi=int(input("Ağacın yüksekliği kaç satır olsun? : "))
agacKarakteri=input("Ağaç için bir sembol veya karakter girin? : ")
if agacKarakteri!='' and agacYuksekligi>=1:
    agacCiz(agacYuksekligi, agacKarakteri[0])
elif agacKarakteri=='' and agacYuksekligi>=1:
    agacCiz(agacYuksekligi)
else:
    print('Hatalı giriş')