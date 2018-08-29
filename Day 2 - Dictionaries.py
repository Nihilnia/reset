#Sozlukler - Dictionaries

#formul?
# key -> value
ornekSozluk = {"anahtar": "deger"}
print(ornekSozluk["anahtar"]) #deger - olarak yazdıracak

okanSozlugu = {"isim": "nihil", "yas": 24}
recepSozlugu = {"isim": "cesard", "yas": 24}

#erisim?

print("""
Okan sözlüğündeki ilk anahtarın değeri:     {}
Recep sözlüğündeki ilk anahtarın değeri:    {}""".format(okanSozlugu["isim"], recepSozlugu["isim"]))

#deger eklemek?
recepSozlugu["esininAdi"] = "Emine"
recepSozlugu["cocugununAdi"] = "Gökçe başkan"

print(recepSozlugu)

#Değiştirmek?
recepSozlugu["isim"] = "Recep"
print(recepSozlugu)

#Deger silmek? - del
print("Silmeden önceki hali:", okanSozlugu)
del okanSozlugu["yas"]
print("Sildikten sonraki hali:", okanSozlugu)



#İÇ içe sözlükler?

xSozluk = {
"icecekler": {"favori içeceğim": "iceTea", "ikinci favorim": "cay"},
"yemekler": {"fav yemeğim": "pizza", "ikinci fav yemeğim": 0}}

print("Okan'ın favori iceceği: {}, favori yemeği: {}".format(xSozluk["icecekler"]["favori içeceğim"], xSozluk["yemekler"]["fav yemeğim"]))


#Temel sözlük metodları:

#keys() - Anahtarlar
print("recepSozlugu anahtarları: ")
print(recepSozlugu.keys())

#values() - Değerler
print("recepSozlugu Değerleri")
print(recepSozlugu.values())

#items() - Eşyalar - Hem anahtarlar, hem değerler
print("recepSozlugu Hem anahtarları hem değerleri")
print(recepSozlugu.items())


print("Okan sözlüğünün eski hali: ")
print(okanSozlugu.items())
girilenIsim = input("Lütfen bir isim giriniz: ")
okanSozlugu["yeniKisi"] = girilenIsim

print("Okan sözlüğünün yeni hali: ")
print(okanSozlugu.items())