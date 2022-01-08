on_mesaj="Sayın "
mesaj_sonu=" nisan dönemi faturanız: "
abone_no=input("abone numaranız")
tuketim=input("tuketim miktarı")
tuketim_tutari=str(int(tuketim)*4.0)
mesaj=on_mesaj+abone_no+mesaj_sonu+tuketim_tutari+" tl dir."
print(mesaj)