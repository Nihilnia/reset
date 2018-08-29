#Koşullu Durumlar:

#if - else:

#formul?

# if koşul:
#    yapılacak işlem/işlemler
# else:
#    yapılacak işlem/işlemler

# isim = "nihil"

# if isim == "Nihil":
#     print("Koşul sağlandığı için bu işlem bloğu (if) çalışmış oldu!")
# else:
#     print("Koşul sağlanamadığı için bu işlem bloğu (else) çalışmış oldu!")

girilenSayi = input("Bir sayı giriniz: ")

if int(girilenSayi) % 2 != 0:
    print("Girdiğiniz sayı: {} bir tek sayıdır!".format(girilenSayi))
else:
    print("Girdiğiniz sayı: {} bir çift sayıdır!".format(girilenSayi))