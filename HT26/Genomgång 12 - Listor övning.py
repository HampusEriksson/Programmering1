"""Genomgång av listor, meny och parallella listor."""

exempelval = 6

# BRA KODRADER ATT LYFTA
# Utdragen är kod från inlämningarna. Variabler har fått startvärden
# så att varje exempel står för sig självt.

# Kontrollerar att föremålet finns innan remove() körs

if exempelval == 1:
    lista = ["svärd", "sköld", "läk-dryck"]
    y = input("Vad vill du ta bort? ").lower()
    if y in lista:
        lista.remove(y)
    else:
        print("Detta finns inte")


# enumerate(..., start=1) ger numrering som börjar på 1, vilket är
# naturligt för användaren.
elif exempelval == 2:
    säck = ["tröja", "tärning", "bröd"]
    for index, sak in enumerate(säck, start=1):
        print(index, sak)


# Kontrollerar kapaciteten innan ett nytt föremål läggs till och visar
# ett meddelande när listan är full. >= hade även fångat en redan överskriden gräns.
elif exempelval == 3:
    lista = ["Pepsi", "Cola", "Fanta"]
    maxi = 5
    if len(lista) >= maxi:
        print("Listan är full")
    elif len(lista) < maxi:
        lista.append(input("Vad vill du lägga till i listan?"))


# Validerar texten innan int()-konvertering. Vid fel får användaren
# ett meddelande och loopen frågar igen.
elif exempelval == 4:
    while True:
        userchoice = input("Välj 1-4: ")
        if userchoice.isdigit() and userchoice in ["1", "2", "3", "4"]:
            userchoice = int(userchoice)
            break
        else:
            print("Fel input, skriv 1, 2, 3 eller 4.")


# Sparar föremålets index innan listan ändras och tar sedan bort priset
# från samma index, så de parallella listorna fortsätter att stämma.

elif exempelval == 5:
    skibidi = ["Toilet", "Kebabroll", "Afghanistan"]
    guldvarde = [30, 69420, 999999999999]
    radera_foremal = input("Radera nått")
    index = skibidi.index(radera_foremal)
    skibidi.remove(radera_foremal)
    guldvarde.pop(index)


# MISSTAG OCH LÄRDOMAR FRÅN INLÄMNINGARNA


# Skriv inte över listvariabeln i en for-loop.
# Efter loopen är föremål en sträng med sista föremålet, inte listan.
elif exempelval == 6:
    föremål = ["svärd", "sköld", "läl dryck"]
    for number, föremål in enumerate(föremål, start=1):
        print(f"{number}. {föremål}")

    print(len(föremål))


# Håll parallella listor synkroniserade.
# Här tas föremålet bort innan koden försöker hitta dess index.
elif exempelval == 7:
    Liam = ["svärd", "sköld"]
    Guldvärde = [100, 50]
    detmanvilltabort = "svärd"
    if detmanvilltabort in Liam:
        Liam.remove(detmanvilltabort)
        Guldvärde.pop(Liam.index(detmanvilltabort))


# Här tas föremålet bort och läggs till sist i stället för att bytas på plats.
elif exempelval == 8:
    lista = ["svärd", "sköld"]
    guldlista = [100, 50]
    byta_ut = "svärd"
    if byta_ut in lista:
        lista.remove(byta_ut)
        nytt_föremål = input("vad vill du lägga till?")
        lista.append(nytt_föremål)
        worth_byta = input("och vad är föremålet värt?")
        guldlista.append(worth_byta)


# input() ger text, även när användaren skriver siffror.
elif exempelval == 9:
    guld = [10, 20]
    g = guld.append(input("lägg till dess guldvärde"))
    if g.isdigit():
        g = int(g)
    else:
        print("måste vara tal")

elif exempelval == 12:
    val = "5."
    lista = ["svärd", "sköld"]
    if False:
        pass
    elif val == "5.":
        for i, z in enumerate(lista):
            print(f"{i} - {z}")
            nummer = int(input("Välj vilket nummer du vill ta bort: "))
