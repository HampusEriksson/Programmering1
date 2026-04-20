# Felhantering - Koppling till betygskriterier
# E -Utför felsökning av enkla syntaxfel.
# C - utför på ett systematiskt sätt felsökning av syntaxfel, körtidsfel och programmeringslogiska fel.
# A - utför på ett systematiskt och effektivt sätt felsökning av syntaxfel, körtidsfel och programmeringslogiska fel.

# ============================================
# E - Utför felsökning av enkla syntaxfel
# ============================================
# ENKLA SYNTAXFEL: Fel i kodens struktur som förhindrar att programmet körs överhuvudtaget

# SyntaxError - fel i syntaxen, t.ex. saknade parenteser eller felaktiga indragningar
print("hej


# IndentationError - fel indrag, Python kräver rätt antal mellanslag eller tabbar i block
def hej():
print("hej")


# ============================================
# C - Utför på ett systematiskt sätt felsökning av syntaxfel, körtidsfel och programmeringslogiska fel
# ============================================
# KÖRTIDSFEL (Runtime Errors): Programmet startar men kraschar när det körs

# NameError - du använder ett namn på en variabel eller funktion som inte finns
poäng = 10
print(poang)


# TypeError - operationen fungerar inte med de datatyper du använder
print("5" + 5)


# ValueError - rätt datatyp används, men värdet är ogiltigt
tal = int("hej")


# IndexError - du försöker hämta en position i en lista som inte finns
siffror = [10, 20, 30]
print(siffror[5])


# KeyError - du försöker hämta en nyckel i en dictionary som inte finns
person = {"namn": "Ali"}
print(person["ålder"])


# AttributeError - objektet saknar metoden eller attributet du försöker använda
namn = "Anna"
namn.append("!")


# ZeroDivisionError - du kan inte dividera med noll
print(10 / 0)


# ============================================
# A - Utför på ett systematiskt och effektivt sätt felsökning
# ============================================
# FELSÖKNING: Läs felmeddelandet, hitta raden, förstå problemet, fixa det

# -------- EXEMPEL 1: Körtidsfel --------
# Exempel: Vi bygger en funktion som beräknar medelvärde
def beräkna_medelvärde(siffror):
    summa = 0
    for tal in siffror:
        summa += tal
    return summa / len(siffror)  # ← Här kraschar det om listan är tom!

# Testa den:
resultat = beräkna_medelvärde([])  



# -------- EXEMPEL 2: Programmeringslogiska fel --------
# Fel som inte kraschar men ger FEL resultat!

# Funktion som är tänkt att räkna summan av tal i en lista
def räkna_summa_fel(tal_lista):
    summa = 1 
    for tal in tal_lista:
        summa += tal
    return summa

resultat_fel = räkna_summa_fel([5, 10, 15]) 
print(f"Summa av [5, 10, 15]: {resultat_fel}") 

