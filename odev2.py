def ekipmanKullanilabilirlikOrani(planlanmisUretimSuresi,plansizDurus):
    kullanilabilirlik=(planlanmisUretimSuresi-plansizDurus)/planlanmisUretimSuresi
    return kullanilabilirlik

def kaliteOraniDegerleri(saglamUrunMiktari,toplamUretimMiktari):
    kalite=(saglamUrunMiktari/toplamUretimMiktari)
    return kalite

def performansOrani(standartCevrimZamani,uretimMiktari,planlanmisUretimSuresi,plansizDurus):
    performans=(standartCevrimZamani*uretimMiktari)/(planlanmisUretimSuresi-plansizDurus)
    return performans

def ekipmanEtkililikOrani(kullanilabilirlik,performans,kalite):
    oOE=(kullanilabilirlik*performans*kalite)
    return oOE

planlanmisUretimSuresi=int(input("Planlanmış Üretim Süresini Giriniz:"))
plansizDurus=int(input("Plansız Duruş Süresini Griniz:"))
saglamUrunMiktari=int(input("Sağlam Ürün Miktarını Giriniz:"))
toplamUretimMiktari=int(input("Toplam Üretim Miktarını Giriniz:"))
standartCevrimZamani=int(input("Standart Çevrim Zamanını Giriniz:"))
uretimMiktari=int(input("Üretim Miktarını Giriniz:"))
print("EKO:%",ekipmanKullanilabilirlikOrani(planlanmisUretimSuresi,plansizDurus))
print("KOD:%",kaliteOraniDegerleri(saglamUrunMiktari,toplamUretimMiktari))
print("PO:%",performansOrani(standartCevrimZamani,uretimMiktari,planlanmisUretimSuresi,plansizDurus))


print("ekipmanEtkililikOrani:%",ekipmanEtkililikOrani(ekipmanKullanilabilirlikOrani(planlanmisUretimSuresi,plansizDurus),performansOrani(standartCevrimZamani,uretimMiktari,planlanmisUretimSuresi,plansizDurus),kaliteOraniDegerleri(saglamUrunMiktari,toplamUretimMiktari)))


