priser = []
varor = []

while True:
    vara = input("Vilken vara köpte du? Skriv stopp för att avbryta").capitalize()
    if vara == "Stopp" and len(varor) > 0:
        break
    varor.append(vara)

    while True:
        pris = input("Vad kostade varan?")
        if pris.isdigit():
            if int(pris) >= 1:
                priser.append(int(pris))
                break
            else:
                print("Inget är gratis.")
        else:
            print("Inga siffror skrevs in!")

summa = 0
for nr in priser:
    summa += nr

if summa > 200 or len(varor) > 5:
    print(f"Du fick {summa*0.1}kr rabatt.")
    summa *= 0.9

if len(priser) != 0:
    medelpris = summa / len(priser)

billig = 0
medel = 0
dyr = 0
for x in priser:
    if x <= 20:
        billig += 1
    elif 20 < x < 50:
        medel += 1
    else:
        dyr += 1

# Sätt 1
max = priser[0]
for p in priser:
    if p > max:
        max = p

# Sätt 2 - Tules sätt
priser.sort()
max = priser[-1]
max = priser[len(priser) - 1]

print(f"Ditt pris blev {summa}kr.")
print(f"Medelpriset för dina varor blev: {medelpris}")
print(f"Antal billiga varor blev: {billig}")
print(f"Antal medeldyra varor blev: {medel}")
print(f"Antal dyra varor blev: {dyr}")
print(*varor)
