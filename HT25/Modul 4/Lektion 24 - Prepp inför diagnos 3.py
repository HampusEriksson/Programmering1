# Vad är ett samlingsnamn för listor, tuples, dictionaries och sets?
# Är det samlingsnamnet en datatyp i sig själv i Python?
# Array, det är dock inte en datatyp i Python

# Vilka av de 4 datatyperna har index?
# listor, dictionaries har nycklar, tuples

# Vilka av de 4 datatyperna kan ändras (mutable)?
# lista, dictionaries, sets

# Hur lägger du till något till en lista? Hur tar du bort något?
my_list = [1,2,3,4,5,6]
# append lägger till
my_list.append(2)
# remove tar bort på värde
my_list.remove(2)
# pop tar bort på index
my_list.pop(0)

# Hur loopar du igenom en lista/tuple/set?
for x in my_list:
    print(x)

# Hur fungerar enumerate?
for index, x in enumerate(my_list):
    print(f"{index} : {x}")

# Hur loopar du igenom keys i ett dictionary? Hur loopar du igenom values? Hur loopar du igenom både och?
grades = {
    "matematik" : "C",
    "kemi" : "D",
    "engelska" : "B"
}

for k in grades.keys():
    print(k)
for v in grades.values():
    print(v)

for x,y in grades.items():
    print(f"{x} : {y}")

# Kan man blanda datatyper i en array?
the_list = [6, "anton", True, [1,2,3]]

# Varför skulle man vilja använda dictionaries eller tuples istället för listor?
# dictionaries snabbare att kolla om något finns, bättre struktur
# tuples - immutable, kan inte ändras

# Hur skriver du ut en lista utan [ ]?
my_list = [1,2,3,4,5,6]
print(*my_list)

# Vad är IndexError?
print(my_list[8])

# Hur kollar du om ett element finns i en lista?
if 7 in my_list:
    print("7 finns i listan")

# Hur byter du plats på två element i en lista?
my_list[1], my_list[4] = my_list[4], my_list[1]



