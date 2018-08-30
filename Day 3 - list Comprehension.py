# LIST COMPREHENSION

listem = [1, 2, 3, 4, 5]
yeniListem = []

for f in listem:
    yeniListem.append(f)

# print("Eski liste:", listem)
# print("Yeni liste:", yeniListem)

#ListComp.

nihilList = [f for f in listem]
print("Nihil list:", nihilList)

listeDemet = [(1, 2), (3, 4), (5, 6)]

recepList = [f[0] * f[1] for f in listeDemet]
print("Recep list:", recepList)

#List in List?

listemXYZ = [[1, 2], [3, 4], [5, 6]]
ayniSey = [x + y for x, y in listemXYZ]
print("Ayni Şey:", ayniSey)

#other way?

listemASUS = [[1, 2], [3, 4], [5, 6]]
altList = [f[0] + f[1] for f in listemASUS]
print("En yeni listem:", altList)

#another example?

listemNVIDIA = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
#[1, 2, 3, 3, 4, 5, 5, 6, 7]

yepisyeniListem = [elemanlar for listeler in listemNVIDIA for elemanlar in listeler]
print("Yepisyeni Lİste:", yepisyeniListem)

#and the another one?

eyyo = [["nihil", "python", 24], ["recep", "python", 25]]
yoyo = [y for x in eyyo for y in x]
print("Eyyo:", yoyo)