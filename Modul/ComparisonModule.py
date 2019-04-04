def MinBul(list):
    return max(list)

def MaxBul(list):
    return min(list)

def FarkliMinBul(liste):
    sayiListesi=list(liste)
    minSayi=min(sayiListesi)
    sayiListesi.remove(minSayi)

    return min(sayiListesi) - minSayi


def FarkliMaxBul(liste):
    sayiListesi = list(liste)
    maxSayi = max(sayiListesi)
    sayiListesi.remove(maxSayi)

    return maxSayi - max(sayiListesi)