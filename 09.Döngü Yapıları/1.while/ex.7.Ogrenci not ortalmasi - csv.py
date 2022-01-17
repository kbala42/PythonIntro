print('--------------------------------------------------------------tw:@tek_elo')
print('Excel dosyasından alınan öğrenci dikte bilgilerinin\n'
      'ortalamalarını ekrana yazdırma')
print('------------------------------------------------------------------------')
print()

# modülü kod içine aktarıyoruz
import xlrd

# Dosyanın konumunu beliliyoruz
location="dikte-kontrol.xls"

# Workbook (çalışma kitabını) açıyoruz
wb = xlrd.open_workbook_xls(location)


# Excel çalışma sayfasını alıyoruz.
sheet = wb.sheet_by_index(0)  # 0. indisli çalışma alıyoruz

# Toplam kullanılan satır ve sütun sayılarını bulalım
satirSayisi = sheet.nrows
sutunSayisi = sheet.ncols
print('toplam satır sayısı:', satirSayisi)
print('toplam sütun sayısı:', sutunSayisi)

# while ile öğrencilerin olduğu satırlarda döngüye girelim
#   ➡ Öğrenci adını alalım ✅
#   ➡ Diktelerin olduğu sütunlarda döngüye girelim
#       ➡ Kontrol edilen dikte sayısını bulalım
#       ➡ Dikte kontrollerinde başarılı kelime sayısını toplayalım
#       ➡ Dikte ortalamasını hesaplayıp öğrenci adıyla ekrana yazdıralım

# adlar 3. satırdan itibaren yer aldığı için 3 atıoruz
satir = 3

# o anki okunan satır değeri, toplam satır sayısından küçük olduğu sürece bloğu çalıştırıyoruz
while satir < satir_sayisi:

    # addeğerini çalışma sayfası içinden, o anki okunan satır değeri ve 0. sütundan alıyoruz
    ad = cs.cell_value(satir, 0)

    # girişlerin sayısını tutan değişkeni tanımlıyoruz. Boş girişleri göz önünde tutmak için.
    dikte_sayisi = 0

    # giriş yapılan sayıların toplamını tutan değişkeni tanımlıyoruz. Boş girişleri göz önünde tutmak için.
    dikte_toplami = 0

    for sutun in range(1, 6):
        dikte = sheet.cell_value(satir, sutun)

        # if dikte:  # boş değer False, tek karakter bile True anlamına gelir
        if dikte != "":
            dikte_sayisi += 1
            dikte_toplami += int(dikte)

    ortalama = round(dikte_toplami / dikte_sayisi, 2)
    print(f"{ad}: {ortalama}")

    satir += 1