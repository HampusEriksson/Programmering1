# Booleans
# En datatyp
# 2 möjliga värden
True
False

# Skriva ut boolean
print(7 > 5)

# if else - kontrollstruktur
age = int(input("Age: "))

# else
if age >= 16 and age < 95:
    print("Du får övningsköra.")
else:
    print("Du får inte övningsköra")

# elif
age = int(input("Age: "))

if age > 65:
    print("Priset är 100kr")
elif age > 25:
    print("Priset är 150kr")
elif age > 16:
    print("Priset är 120kr")
else:
    print("Priset är 50kr")


# .lower() (små bokstäver), .upper() (stora bokstäver)
# .capitalize() (första bokstaven stor, resten små)
svar1 = input("Vad är bästa ämnet?").lower()

if svar1 == "programmering":
    print("Rätt")
else:
    print("Fel")

if svar1 in ["programmering", "teknik", "matematik", "fysik"]:
    print("Rätt")
else:
    print("Fel")


tal = int(input("Tal: "))

if tal % 2 == 0:
    print("Jämnt")
elif tal % 2 != 0:
    print("Inte jämnt")
