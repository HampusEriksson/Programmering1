# For-loop
# Repetera kod ett visst antal gånger
for _ in range(17):
    print("Hejsan")

# loopvariabel
for i in range(10):
    print(i)

# Start, stop
for x in range(13, 37):
    print(x)

# Start, stop, step
for tal in range(45, 78, 3):
    print(tal)

user_tal = int(input("Vilken gångertabell vill du se? "))
for z in range(1, 11):
    print(f"{user_tal} * {z} = {user_tal*z}")

# Loopa igenom string
# En string är en iterable
namn = input("Name: ")

for bokstav in namn:
    print(bokstav)

# len() ger dig längden av en sträng eller lista
print(f"Ditt namn är {len(namn)} bokstäver långt.")
