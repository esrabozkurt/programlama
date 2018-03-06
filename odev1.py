finansmanGelir=int(input("Finansman Gelir Miktarını Giriniz:"))
pazarGelir=int(input("Pazar Gelir Miktarını Giriniz:"))
kiraGelir=int(input("Kira Gelir Miktarını Giriniz:"))
ucret=int(input("Ücret Miktarını Giriniz:"))
finansmanGider=int(input("Finansman Gider Miktarını Giriniz:"))
pazarGider=int(input("Pazar Gider Miktarını Giriniz:"))
kiraGider=int(input("Kira Gider Miktarını Giriniz:"))
muhasebeGider=int(input("Muhasebe Gider Miktarını Giriniz:"))
Gelir=finansmanGelir+pazarGelir+kiraGelir
Gider=ucret+finansmanGider+pazarGider+kiraGider+muhasebeGider
kar=Gelir-Gider
if kar>1000:
    print("Karlı",kar)
else:
    print("Karlı Değil",kar)
