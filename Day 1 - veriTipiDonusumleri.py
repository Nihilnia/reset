#Veri Tipi Donusumleri

#Notlar:
# 1- Input ile alınan her değer string'tir.
# 2- Dönüştürülen değerin dönüşeceği değere uygun olması gerekir.

girilenDeger = input("Bir değer giriniz: ")
print("Girdiğiniz değer {}, ve tipi ise {}".format(girilenDeger, type(girilenDeger)))
girilenDeger = int(girilenDeger)
print("Girdiğiniz değer {2}, ve tipi ise {1}{2}{0}".format(girilenDeger, type(girilenDeger), "merhaba ben 2.index"))