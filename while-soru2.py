stokMiktari=10000
i=0
while True:
    stokMiktari=stokMiktari-500
    stokMiktari=stokMiktari+100
    i=i+1
    if(stokMiktari==0):
        print(i,". ayda stoklarınız sıfırlanır.")
        break
