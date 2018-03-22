#uretim=200
#defo>uretim*20/100 firmaya uyarı
#defo<uretim*20/100 toplam defolu ürün sayısını ve kaç günlük defolu ürün saysını

uretim=200
i=0
toplamDefo=0
while True:
    defo=int(input("Defolu ürün sayısını giriniz:"))
    defoluUrun=uretim*20/100
    if(defo>defoluUrun):
        print("Defolu ürün sayınız günlük üretimin %20'sinden fazla!")
        break
    else:
        toplamDefo=toplamDefo+defo
        i=i+1
        print(i,"Günlük defolu ürün",toplamDefo)
        
