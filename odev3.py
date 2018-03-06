def ciroHesapla(satisMiktari,birimSatisFiyati):
    ciro=satisMiktari*birimSatisFiyati
    return ciro
    

def adamBasiCiroHesapla(ciro,toplamCalisan):
    adamCiro=ciro/toplamCalisan
    return adamCiro
    

toplamCalisan=25
satisMiktari=int(input("Satış Miktarını Giriniz:"))
birimSatisFiyati=int(input("Birim Satış Miktarını Giriniz:"))

print("Adambaşı Ciro:",adamBasiCiroHesapla(ciroHesapla(satisMiktari,birimSatisFiyati),toplamCalisan))
