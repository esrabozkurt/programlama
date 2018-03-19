def ilkAltiAyGelir(yazilimGeliri,finansmanGeliri,urunSatisGeliri):
    ilkGelir=yazilimGeliri+finansmanGeliri+urunSatisGeliri
    global ilkAltiAyGelir 
    return ilkGelir


def ilkAltiAyGider(calisanMaaslari,kiraGideri,donanimMaliyeti):
    ilkGider=calisanMaaslari+kiraGideri+donanimMaliyeti
    global ilkAltiAyGider
    return ilkGider


def sonAltiAyGelir(yazilimGeliri,sponsorlukGeliri,eTicaretGeliri,urunSatisGeliri):
    sonGelir=yazilimGeliri+sponsorlukGeliri+eTicaretGeliri+urunSatisGeliri
    global sonAltiAyGelir
    return sonGelir

                 
def sonAltiAyGider(calisanMaaslari,kiraGideri,donanimMaliyeti):
    sonGider=calisanMaaslari-kiraGideri-donanimMaliyeti
    global sonAltiAyGider
    return sonGider

a=int(input("İlk 6 Aylık Yazılım Gelirinizi Giriniz:"))
b=int(input("İlk 6 Aylık Finansman Gelirinizi Giriniz:"))
c=int(input("İlk 6 Aylık Ürün Satış Gelirinizi Giriniz:"))
d=int(input("İlk 6 Aylık Çalışan Maaşlarını Giriniz:"))
e=int(input("İlk 6 Aylık Kira Giderlerinizi Giriniz:"))
f=int(input("İlk 6 Aylık Donanım Maliyetlerinizi Giriniz:"))

g=int(input("Son 6 Aylık Yazılım Gelirinizi Giriniz:"))
z=int(input("Son 6 Aylık Sponsorluk Gelirinizi Giriniz:"))
t=int(input("Son 6 Aylık E-Ticaret Gelirinizi Giriniz:"))
h=int(input("Son 6 Aylık Ürün Satış Gelirinizi Giriniz:"))
i=int(input("Son 6 Aylık Çalışan Maaşlarını Giriniz:"))
k=int(input("Son 6 Aylık Kira Giderlerinizi Giriniz:"))
p=int(input("Son 6 Aylık Bakım Maliyetlerinizi Giriniz:"))

x=ilkAltiAyGelir(a,b,c)
y=ilkAltiAyGider(d,e,f)
m=sonAltiAyGelir(g,z,t,h)
n=sonAltiAyGider(i,k,p)

kar1=x-y
kar2=m-n
fark=kar2-kar1


if (fark>1000):
    print("işletme çok karlı")
elif(1000<=fark<=5000):
    print("işletme karı normal")
else:
    print("işletme yeterince karda değil")

