# DEMETLER (TUPLES)
# "değiştirilemezler"

# formul?
ornekDemet = ("nihil", 24, 16.7)

#cagırma?

print(int(ornekDemet[1] + ornekDemet[2]))

#Metodları?

#count()
print("Recep geçiyor mu?", ornekDemet.count("recep"))
print("Nihil geçiyor mu?", ornekDemet.count("NihiL".lower())) #nihil

#index()
print("24 integeri hangi indexte?:", ornekDemet.index(24))