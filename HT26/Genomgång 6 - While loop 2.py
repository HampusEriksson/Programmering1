# While loop

# Inloggning
# Continue
# not in
# Alternativ 1
antal = 0
while antal < 3:

    namn = input("Name: ")
    if namn not in ["Hampus", "Lasse", "Biman", "Pelle"]:
        print("Fel namn")
        antal += 1
        continue  # Loopen startar om
    # Detta körs bara om man har skrivit ett av namnen
    print("Välkommen till programmet.")
    # Här är allt hemligt material som bara Hampus kan se
    break

# Alternativ 2
antal = 0
logged_in = False
while antal < 3:

    namn = input("Name: ")
    if namn in ["Hampus", "Lasse", "Biman", "Pelle"]:
        logged_in = True
        break
    else:
        print("Fel namn")
        antal += 1

# Detta körs bara om man har skrivit ett av namnen
if logged_in == True:
    print("Välkommen till programmet.")
    # Här är allt hemligt material som bara Hampus kan se
