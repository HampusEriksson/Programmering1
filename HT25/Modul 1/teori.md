## Introduktion till Python
Python är ett lättläst och kraftfullt programmeringsspråk som används för allt från små skript till större program och webbapplikationer. I Modul 1 har vi byggt upp grunderna: hur vi sparar information, skriver ut text, tar emot input från användaren och gör enkla beräkningar.

Det viktigaste i början är att förstå att programmering handlar om att:
- spara värden i variabler,
- arbeta med olika datatyper,
- skriva ut information,
- ta emot input från användaren,
- och använda operatorer för att beräkna eller jämföra värden.

---

## 1. Variabler
En variabel är ett namn som vi ger ett värde. Tanken är att vi kan använda namnet igen senare i programmet utan att behöva skriva värdet på nytt.

```python
namn = "Anna"
ålder = 17
pris = 19.90
```

Variabler fungerar ungefär som lådor:
- namn = etikett på lådan
- värdet = det som finns i lådan

### Regler för variabelnamn
- Får inte innehålla mellanslag
- Får inte börja med siffror
- Får inte innehålla specialtecken som `-` eller `?`
- Python skiljer mellan stora och små bokstäver

```python
namn = "Hampus"
Namn = "Anna"

print(namn)  # Hampus
print(Namn)  # Anna
```

Det är vanligt att använda underscore `_` i variabelnamn:

```python
mitt_namn = "Hampus"
min_ålder = 17
```

---

## 2. Datatyper
Varje variabel har en typ. Typen avgör vilket slags värde variabeln kan innehålla och vilka operationer vi kan göra med den.

### Vanliga datatyper i Modul 1

#### str – string / text
Textvärden skrivs oftast med citattecken.

```python
namn = "Hampus"
text = 'Hej!'
```

#### int – integer / heltal
Heltal utan decimaler.

```python
ålder = 16
antal = 42
```

#### float – decimaltal
Tal med decimaler.

```python
pris = 19.90
pi = 3.14159
```

### Exempel

```python
namn = "Anna"         # str
alder = 17            # int
pris = 19.90          # float
```

---

## 3. print() – skriva ut på skärmen
`print()` används för att visa text eller värden från variabler.

```python
print("Hej världen!")
```

```python
namn = "Hampus"
print(namn)
```

### Escape-sekvenser
Det finns specialtecken för att styra utskriften:

```python
print("Detta står på första raden\nDetta står på nästa rad")
print("Tabb\t mellan ord")
```

- `\n` = ny rad
- `\t` = tabulator

### Multiline-sträng
Det går att skriva text över flera rader med tre citattecken:

```python
print("""Det här är en text
på flera rader.""")
```

---

## 4. f-strings
När vi vill kombinera text och variabler använder vi oftast f-strings. Då skriver vi ett `f` före strängen och lägger variablerna i `{}`.

```python
namn = "Hampus"
ålder = 17
print(f"Hej {namn}! Du är {ålder} år gammal.")
```

Det gör koden lättläst och snygg.

### Exempel med beräkning i f-string

```python
x = 5
y = 3
print(f"Summan blir {x + y}")
```

---

## 5. input() – ta emot användardata
Med `input()` kan vi fråga användaren om något.

```python
namn = input("Vad heter du? ")
print(f"Hej {namn}!")
```

### Viktigt att veta
`input()` returnerar alltid text, alltså en `str`.

Om vi vill göra matematiska beräkningar med användarens svar måste vi först konvertera det.

---

## 6. Typkonvertering
När vi vill göra om en sträng till ett heltal eller decimaltal använder vi:

- `int()`
- `float()`
- `str()`

### Exempel

```python
svar = input("Hur många äpplen har du? ")
antal = int(svar)
print(f"Du har {antal} äpplen.")
```

```python
vikt = float(input("Skriv din vikt i kg: "))
print(f"Din vikt är {vikt} kg.")
```

```python
nummer = 5
text = str(nummer)
print(text)
```

### Vanlig fallgrop
Om användaren skriver text som inte är ett tal och vi använder `int()` eller `float()` får vi fel.

```python
ålder = int(input("Hur gammal är du? "))
```

Detta fungerar bara om användaren skriver ett tal, till exempel `17`.

---

## 7. Matematiska operatorer
I Python kan vi utföra beräkningar med operatorer.

### Grundläggande operatorer

```python
print(5 + 3)   # addition
print(10 - 4)  # subtraktion
print(6 * 2)   # multiplikation
print(8 / 2)   # division
```

### Exempel

```python
x = 27
y = 98

print(x + y)
print(x - y)
print(x * y)
print(x / y)
```

### Potenser
`**` betyder upphöjt i.

```python
print(3 ** 2)   # 9
print(5 ** 3)   # 125
```

### Kvadratrot
Man kan ta roten ur ett tal genom att höja till `0.5`:

```python
print(9 ** 0.5)   # 3.0
```

### Floor division
`//` ger heltalsdivision, alltså avrundar neråt.

```python
print(17 // 3)   # 5
```

### Modulo
`%` ger resten vid division.

```python
print(17 % 3)    # 2
print(10 % 2)    # 0
```

Det används ofta för att kolla om ett tal är jämnt eller udda:

```python
print(17 % 2)    # 1 -> udda
print(28 % 2)    # 0 -> jämnt
```

### Prioriteringsordning
Python räknar i en viss ordning:
1. parenteser
2. potenser
3. multiplikation/division/modulo
4. addition/subtraktion

```python
print(2 + 3 * 4)   # 14
print((2 + 3) * 4) # 20
```

---

## 8. Kommentarer
Kommentarer används för att förklara koden. Python ignorerar dem när programmet körs.

### Enradig kommentar
```python
# Detta är en kommentar
print("Hej")
```

### Flerlinjig kommentar
```python
"""
Detta är en kommentar
på flera rader.
"""
```

Kommentarer är viktiga för att göra koden lättare att förstå, både för dig själv och för andra.

---

## 9. Strängar och text
En sträng är text. I Python skrivs den med citattecken.

```python
"Hampus"
'Python'
"""Detta är flera rader"""
```

### Sätta citattecken i en sträng
```python
print('Han sa "Hej"')
print("Han sa 'Hej'")
```

### Konkatenering
Det går att lägga ihop strängar med `+`.

```python
fornamn = "Hampus"
efter_namn = "Eriksson"
print(fornamn + " " + efter_namn)
```

---

## 10. Vanliga begrepp att kunna

### Variabel
En variabel är ett namn som håller ett värde.

```python
x = 10
```

### Datatyp
Datatyp beskriver vilken sorts värde variabeln innehåller.

### Typkonvertering
Att ändra från en datatyp till en annan.

```python
int("5")
float("3.14")
str(42)
```

### Funktion
En funktion är ett återanvändbart block av kod.

```python
print("Detta är en funktion")
```

### Input
Används för att ta emot text från användaren.

```python
namn = input("Vad heter du? ")
```

---

## 11. Snabb repetitionsfråga
Du ska kunna svara på frågor som:
- Vad är en variabel?
- Vilka datatyper har vi använt?
- Vad gör `print()`?
- Vad gör `input()`?
- Hur konverterar du input till heltal?
- Vad skiljer `+`, `-`, `*`, `/`, `//`, `%`, `**` åt?
- Varför använder vi f-strings?
- Vad är en kommentar i Python?

Om du kan svara på dessa frågor har du förberett dig väl för Modul 1.
