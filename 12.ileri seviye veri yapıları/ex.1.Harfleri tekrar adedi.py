'''
---------------------------------------------------------tw:@tek_elo
Metinde geçen karakterlerin adedini bulan programı yazınız
--------------------------------------------------------------------
'''

metin = "Metindegeçenkarakterlerinadedin"

# karakterlerin adedini bulmak için boş sözlük oluşturuyoruz
tekrarAdedi = dict()

#metni tek tek tarıyoruz
for karakter in metin:
    if (karakter in tekrarAdedi):# frekans içinde ki karakter varsa bir arttır
        tekrarAdedi[karakter] += 1
    else: #harf daha nce geçmiyorsa adedini 1 yap
        tekrarAdedi[karakter] = 1
for i, j in tekrarAdedi.items():# harfleri ve tekrar sayılarını yazdırıyoruz
    print(i, ":", j)