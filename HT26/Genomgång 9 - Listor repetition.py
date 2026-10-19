print()
print()

# Skapa en lista - square brackets - option + 8
food = ["kebab", "lakritspizza", "banancurry", "tacos"]

# Lägga till - append
# listans_namn.append(det som ska läggas till)
food.append("bend it like Bentley")
food.append(input("Vad vill du lägga till?").lower())

# Ta bort med värde - remove
food.remove("lakritspizza")

food_remove = input("Vad vill du ta bort?").lower()
if food_remove in food:
    food.remove(food_remove)
else:
    print("Den maten finns inte i listan")
# Printa ut listor - använd * unpack
print(*food, sep=", ")

score = 0
# Loopa igenom listor
for item in food:
    print(item)
    score += len(item)

# Loopa på index
for x in range(len(food)):
    print(food[x])

# Loopa med enumerate
for index, food_item in enumerate(food):
    print(f"{index} - {food_item}")

for i, letter in enumerate("pontus"):
    print(f"{i} - {letter}")
nr_remove = int(input("Vilket nummer vill du ta bort?"))
food.pop(nr_remove)
food.pop(3)

# len() - antal element i listan
print(f"Till slut så fanns det {len(food)} maträtter kvar i listan.")


# döp inte din lista till list
colors = ["blue", "red", "green"]
# kolla om input är en siffra
index = input("Vilket index vill du se?")
if index.isdigit():
    index = int(index)
else:
    print("Skriv en siffra tack.")
# hitta index i lista
color = input("Vilken färg vill du se index av?")

print(f"Den färgen har index {colors.index(color)}")

# ändra ordningen på två element
colors = ["blue", "red", "green"]
colors[0], colors[1] = colors[1], colors[0]

a, b = 1, 3
print(*colors)
