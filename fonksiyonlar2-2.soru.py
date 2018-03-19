def hesap2016(calisilanSure=170,toplamMusteriSayisi=50):
    hesap1=calisilanSure/toplamMusteriSayisi
    global hesap2016
    return hesap1
k=hesap2016(calisilanSure=170,toplamMusteriSayisi=50)
print("2016 Yılı Müşterilerle Çalışma Süresi:",k)

def hesap2017(calisilanSure=220,toplamMusteriSayisi=70):
    hesap2=(calisilanSure/toplamMusteriSayisi)
    global hesap2017
    return hesap2
t=hesap2017(calisilanSure=220,toplamMusteriSayisi=70)
print("2017 Yılı Müşterilerle Çalışma Süresi:",t)

def fark(k,t):
    farkhesap=k-t
    global fark
    return farkhesap
a=fark(k,t)
print("2017-2016 Yılları Müşterilerle Çalışma Süreleri Arasındaki Fark:",a)

