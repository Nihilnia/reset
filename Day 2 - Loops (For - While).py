# Döngüler

# in - öperatörü

# isim = "recep"

# if "e" in isim:
#     print("Evet ismin içinde 'e' harfi geçiyor.")

# # For Döngüsü:
# benimListem = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# tekSayilar = []
# ciftSayilar = []
# for sayi in benimListem: #listenin içindeki her elemanı bok olarak adlandırdık.
#     if sayi % 2 == 1:
#         tekSayilar.append(sayi)
#     else:
#         ciftSayilar.append(sayi)

# print("Çift Sayilar:", ciftSayilar)
# print("Tek Sayilar:", tekSayilar)

#ikinci Yöntem:
# benimListem = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ciftSayilar = []
# for sayilar in benimListem:
#     if sayilar % 2 == 0:
#         ciftSayilar.append(sayilar)
#     else:
#         print(sayilar, end = " ")
# print("\n", *ciftSayilar)


# isim = "okan"

# for harfler in isim:
#     print(harfler)



listem = [12, 123, (12, "recep", "emine", "gökçe")]
for f in listem:
    print(f)
    if isinstance(f, tuple):
        for demetIcindekiElemanlar in f:
            print("Demet içindeki elemanlar: ")
            print(demetIcindekiElemanlar)


# basit = "sdçlkıfhskdljfhks"
# for f in  basit:
#     for x in f:
#         for y in x:
#             for z in y:
#                 for amk in z:
#                     for yeterAmk in amk:
#                         print(yeterAmk)