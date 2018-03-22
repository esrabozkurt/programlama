i=0
girilen=""
while(girilen!='0'):
    girilen=int(input('Bir sayı Giriniz. Çıkmak için 0:'))
    if(girilen==0):
        print('Çıkış yaptınız.')
        break 
    else:
       i=i+girilen%3
       print("Sayıların 3'e bölümünden kalanlar toplamı:",i)
