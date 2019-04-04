import Modul.ComparisonModule as compModule

sayilar=[]
while True:
    try:
       sayi=input("Lütfen sayi girin. Sayi girişini durdurmak için s ye basın. Programdan çıkmak için q'ya basın")

       if sayi=="s":
           break
       elif sayi== "q":
            print("Sayı girişi durduruldu.")
            print("Maksimum Değer: {}".format(compModule.MaxBul(sayilar)))
            print("Minimum Değer: {}".format(compModule.MinBul(sayilar)))

            print("2 Maksimum Değer arasındaki fark: {}".format(compModule.FarkliMaxBul(sayilar)))
            print("2 Minimum Değer arasındaki fark: {}".format(compModule.FarkliMinBul(sayilar)))
       else:
           sayilar.append(int(sayi))

    except:
      print("HATA! Lütfen geçerli bir değer girin!")

