donenVarliklar=128000
duranVarliklar=183000
kisaVadeliYabanciKaynak=102000
uzunVadeliYabanciKaynak=150000
ozKaynak=59000
def aktif(donenVarliklar,duranVarliklar):
    global aktifToplamTutar
    aktifToplamTutar=donenVarliklar+duranVarliklar
    return aktifToplamTutar
def pasif(kisaVadeliYabanciKaynak,uzunVadeliYabanciKaynak,ozKaynak):
    global pasifToplam
    pasifToplam=kisaVadeliYabanciKaynak+uzunVadeliYabanciKaynak+ozKaynak
    return pasifToplam
x=aktif(donenVarliklar,duranVarliklar)
y=pasif(kisaVadeliYabanciKaynak,uzunVadeliYabanciKaynak,ozKaynak)

