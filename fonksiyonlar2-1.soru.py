def katmaDegerCiro(toplamSatisMiktari,hammaddeMaliyeti,bakimOnarimMaliyeti,sevkiyatGiderleri,satinAlinanHizmetGiderleri):
    kDCiro=toplamSatisMiktari-(hammaddeMaliyeti+bakimOnarimMaliyeti+sevkiyatGiderleri+satinAlinanHizmetGiderleri)
    global katmaDegerCiro
    return kDCiro

toplamSatisMiktari=int(input("Toplam Satış Miktarınızı Giriniz:"))
hammaddeMaliyeti=int(input("Hammadde Maliyetini Giriniz:"))
bakimOnarimMaliyeti=int(input("Bakım Onarım Maliyetini Giriniz:"))
sevkiyatGiderleri=int(input("Sevkiyat Giderlerini Giriniz:"))
satinAlinanHizmetGiderleri=int(input("Satın Alınan Hizmet Giderlerini Giriniz:"))

ciro=katmaDegerCiro(toplamSatisMiktari,hammaddeMaliyeti,bakimOnarimMaliyeti,sevkiyatGiderleri,satinAlinanHizmetGiderleri)

if(ciro>1000):
    print("İşletme katma değer cirosu yüksek")
elif(500<=ciro<=999):
    print("İşletme katma değer cirosu düşük")
else:
    print("İşletme katma değer cirosu normal")
    
