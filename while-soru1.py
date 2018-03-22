satisMiktari=500
birimSatisFiyati=20
ciro=5000
i=0
while True:
    ciro=(satisMiktari*birimSatisFiyati)+ciro
    satisMiktari=satisMiktari+200
    birimSatisFiyati=birimSatisFiyati+10
    i=i+1
    if (ciro>500000):
        print(i,"Ay kadar sonra 500000 TL'yi geçersiniz.")
        break
    
