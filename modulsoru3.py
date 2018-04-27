begeniA=365000
begeniB=450000
begeniC=582000
yorumA=65000
yorumB=25000
yorumC=52000
paylasimA=870
paylasimB=380
paylasimC=1200
icerikA=500
icerikB=100
icerikC=650
takipciA=1125000
takipciB=1450000
takipciC=2000000
def oran1(begeniA,yorumA,paylasimA,icerikA,takipciA):
    global x
    x=(((begeniA+yorumA+paylasimA)/icerikA)/takipciA)*100
    return x

def oran2(begeniB,yorumB,paylasimB,icerikB,takipciB):
    global y
    y=(((begeniB+yorumB+paylasimB)/icerikB)/takipciB)*100
    return y

def oran3(begeniC,yorumC,paylasimC,icerikC,takipciC):
    global z
    z=(((begeniC+yorumC+paylasimC)/icerikC)/takipciC)*100
    return z

a=oran1(begeniA,yorumA,paylasimA,icerikA,takipciA)
b=oran2(begeniB,yorumB,paylasimB,icerikB,takipciB)
c=oran3(begeniC,yorumC,paylasimC,icerikC,takipciC)
