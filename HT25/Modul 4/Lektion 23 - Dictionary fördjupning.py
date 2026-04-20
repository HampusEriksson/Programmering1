# Skapa dictionary
# Key-value pair
# Lägg till key-value pair - kolla först om den finns!
# Ändra value - kolla först om den finns!
# Ändra value med update - kolla först om den finns!
# Ta bort - del
# Ta bort - pop
# .keys()
# .values()
# .items()


# Exempel 1: Dictionary utan nästlad dictionary
elev = {
	"namn": "Maja",
	"klass": "TE25",
	"ålder": 17,
	"aktiv": True,
}
# Skriva ut från dictionary
print(elev["namn"])
print(elev["ålder"])
elev["längd"] = 150
print(elev["längd"])

for k in elev.keys():
    print(k)
for v in elev.values():
    print(v)







# Exempel 2: Dictionary med nästlad dictionary
skola = {
	"namn": "IT-Gymnasiet",
	"adress": {
		"gata": "Exempelvägen 12",
		"stad": "Göteborg",
	},
	"lärare": {
		"python": "Anders",
		"webb": "Beata",
	},
	"antal_elever": 420,
}
print(skola["antal_elever"])
print(skola["adress"]["stad"])
print(skola["lärare"]["webb"])

# bitcoin exempel

btc = {
    "value" : 70000,
    "value_2020" : 20000,
    "value_2015": 1000
}
