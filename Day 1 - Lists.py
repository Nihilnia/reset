#Listeler

#formul

# listeAdi = list()
# listeAdi = []
# listeAdi = ["elemenlar", "elemanlar"]

listem = ["okan", "recep", 1994]
print("Eski hali: ")
print(*listem)

#eleman Ekleme!

listem.append("reset 1.Gun")
print("Yeni hali: ")
print(listem)


#parcalama

print("Parcalanmıs hali: ")
print(*listem[:2])

#reverse
print("Tersten: ")
print(listem[::-1])


#ayrıntı!

adam = "Recep"
yeniListem = list(adam)
print("Recep listesi: ")
print(yeniListem)


#TEMEL LISTE METODLARI VE ISLEMLER
enYeniListe = ["1", "2", "3", "4" ,"5"]
ilkEleman = int(enYeniListe[0])
sonEleman = int(enYeniListe[-1])
print("Başındaki elemanı {} ve sonundaki elemanı {} toplarsak, sonuc = {}".format(ilkEleman, sonEleman, ilkEleman + sonEleman))

#eleman degistirme
enYeniListe[0] = "17"
ilkEleman = int(enYeniListe[0])
print("değiştirmeyi uyguladıktan sonra:")
print("Başındaki elemanı {} ve sonundaki elemanı {} toplarsak, sonuc = {}".format(ilkEleman, sonEleman, ilkEleman + sonEleman))

#Listeden eleman cıkarma - pop()
print("Listenin ilk hali:", enYeniListe)
enYeniListe.pop()
print("Listenin ikinci hali:", enYeniListe)
enYeniListe.pop(2)
print("Listenin ikinci hali:", enYeniListe) #17, 2, 4


#Listeyi sıralama - sort()
xListem = [2, 5, 3, 19, 1000, 0]
print("X listem, sırasız hali: ", xListem)
xListem.sort()
print("X listem, sıralı hali: ", xListem)

yListem = ["2", "5", "3", "19", "1000", "0"]
print("Y listem, sırasız hali: ", yListem)
yListem.sort()
print("Y listem, sıralı hali: ", yListem)

alfabetikListe = ["c", "a", "b", "d"]
print("Alfabetik listemin sırasız hali:", alfabetikListe)
alfabetikListe.sort()
print("Alfabetik listemin sıralı hali:", alfabetikListe)
