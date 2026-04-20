<style>
  .ovning { page-break-inside: avoid; margin-bottom: 2em; }
  @media print { h2 { page-break-after: avoid; } }
</style>

# Felhantering övningar

<div class="ovning">

## Övning 1
### Kodsnutt
```python
ålder = 17
if ålder >= 18
    print("Du är myndig")
```

### Vad är fel och hur fixar man det?
____________________________________________________________

### Kryssa i vilken typ av error som uppstår
- [ ] TypeError
- [ ] KeyError
- [ ] SyntaxError
- [ ] IndentationError

</div>

<div class="ovning">

---

## Övning 2
### Kodsnutt
```python
def hälsa():
print("Hej! Välkommen.")

hälsa()
```

### Vad är fel och hur fixar man det?
____________________________________________________________

### Kryssa i vilken typ av error som uppstår
- [ ] NameError
- [ ] ZeroDivisionError
- [ ] IndentationError
- [ ] AttributeError

</div>

<div class="ovning">

---

## Övning 3
### Kodsnutt
```python
resultat = hastighet * tid
print(resultat)
```

### Vad är fel och hur fixar man det?
____________________________________________________________

### Kryssa i vilken typ av error som uppstår
- [ ] IndexError
- [ ] ValueError
- [ ] TypeError
- [ ] NameError

</div>

<div class="ovning">

---

## Övning 4
### Kodsnutt
```python
antal = 5
meddelande = "Det finns " + antal + " katter"
print(meddelande)
```

### Vad är fel och hur fixar man det?
____________________________________________________________

### Kryssa i vilken typ av error som uppstår
- [ ] ValueError
- [ ] TypeError
- [ ] KeyError
- [ ] IndentationError

</div>

<div class="ovning">

---

## Övning 5
### Kodsnutt
```python
x = int("tre")
print(x + 10)
```

### Vad är fel och hur fixar man det?
____________________________________________________________

### Kryssa i vilken typ av error som uppstår
- [ ] TypeError
- [ ] NameError
- [ ] ValueError
- [ ] ZeroDivisionError

</div>

<div class="ovning">

---

## Övning 6
### Kodsnutt
```python
frukter = ["äpple", "banan", "päron"]
print(frukter[5])
```

### Vad är fel och hur fixar man det?
____________________________________________________________

### Kryssa i vilken typ av error som uppstår
- [ ] SyntaxError
- [ ] TypeError
- [ ] IndexError
- [ ] KeyError

</div>

<div class="ovning">

---

## Övning 7
### Kodsnutt
```python
bil = {"märke": "Volvo", "år": 2022}
print(bil["färg"])
```

### Vad är fel och hur fixar man det?
____________________________________________________________

### Kryssa i vilken typ av error som uppstår
- [ ] NameError
- [ ] KeyError
- [ ] IndentationError
- [ ] AttributeError

</div>

<div class="ovning">

---

## Övning 8
### Kodsnutt
```python
tal = 42
resultat = tal.replace("4", "9")
print(resultat)
```

### Vad är fel och hur fixar man det?
____________________________________________________________

### Kryssa i vilken typ av error som uppstår
- [ ] KeyError
- [ ] ValueError
- [ ] IndexError
- [ ] AttributeError

</div>

<div class="ovning">

---

## Övning 9
### Kodsnutt
```python
poäng = 0
bonuspoäng = 50
resultat = bonuspoäng / poäng
print(resultat)
```

### Vad är fel och hur fixar man det?
____________________________________________________________

### Kryssa i vilken typ av error som uppstår
- [ ] TypeError
- [ ] NameError
- [ ] KeyError
- [ ] ZeroDivisionError

</div>

<div class="ovning">

---

## Övning 10
### Kodsnutt
```python
elever = ["Lena", "Kalle", "Maja"]
print(elever["1"])
```

### Vad är fel och hur fixar man det?
____________________________________________________________

### Kryssa i vilken typ av error som uppstår
- [ ] IndexError
- [ ] NameError
- [ ] TypeError
- [ ] KeyError
</div>

<div class="ovning">

---

## Övning 11
### Kodsnutt
```python
def räkna_rätt(tal):
    resultat = 0
    for i in range(tal):
        resultat = resultat + i
    return resultat

print(räkna_rätt(5))  # Förväntat: 10 (0+1+2+3+4)
```

### Vad är fel och hur fixar man det?
____________________________________________________________

</div>

<div class="ovning">

---

## Övning 12
### Kodsnutt
```python
def hitta_största(lista):
    största = lista[0]
    for tal in lista:
        if tal > största:
            storsta = tal
    return största

print(hitta_största([3, 7, 2, 9, 1]))  # Förväntat: 9
```

### Vad är fel och hur fixar man det?
____________________________________________________________

</div>

<div class="ovning">

---

## Övning 13
### Kodsnutt
```python
räkna = 1
while räkna <= 5:
    print(räkna)
    räkna -= 1

print("Klar!")
```

### Vad är fel och hur fixar man det?
____________________________________________________________

</div>

<div class="ovning">

---

## Övning 14
### Kodsnutt
```python
def beräkna_rabatt(pris, rabatt_procent):
    rabatt = pris * rabatt_procent
    slutpris = pris - rabatt
    return slutpris

print(beräkna_rabatt(100, 0.2))  # 20% rabatt på 100 kr - förväntat: 80
```

### Vad är fel och hur fixar man det?
____________________________________________________________

</div>

---
<div class="ovning">

## Facit

1. SyntaxError – saknar `:` efter `if`-villkoret. Fix: Lägg till `:`
2. IndentationError – `print` saknar indrag inuti funktionen. Fix: Dra in `print` med 4 mellanslag
3. NameError – `hastighet` och `tid` är inte definierade. Fix: Definiera variablerna innan
4. TypeError – kan inte konkatenera `str` och `int`. Fix: Konvertera: `str(antal)`
5. ValueError – `"tre"` kan inte omvandlas till `int`. Fix: Använd `int("3")` eller hålla isär datatyper
6. IndexError – index 5 finns inte i en lista med 3 element. Fix: Använd `frukter[2]` eller kontrollera längden
7. KeyError – nyckeln `"färg"` finns inte i dictionaryn. Fix: Kontrollera vilka nycklar som finns eller lägga till `"färg"`
8. AttributeError – `int` har ingen metod `replace`. Fix: Konvertera först: `str(tal).replace(...)`
9. ZeroDivisionError – division med noll. Fix: Kontrollera att nämnaren inte är 0 innan division
10. TypeError – listindex måste vara `int`, inte `str`. Fix: Använd `elever[1]` istället för `elever["1"]`

11. **Fel:** Resultatet blir 9 istället för 10. Range(5) är 0,1,2,3,4 och summan blir 0+1+2+3+4=10, men här räknas bara 1+2+3+4=10... faktiskt blir det rätt! Men många elever förväntar sig 15 (0+1+2+3+4+5). **Ingen bugg här** – det är en bra övning för att visa att `range(n)` går till n-1.

12. **Fungerar korrekt** – hittar största värdet. Men den kraschar om listan är tom! Förbättring: Lägg till kontroll för tom lista: `if len(lista) == 0: return None` eller liknande.

13. **Fel:** Loopen blir oändlig! `räkna` minskar (`räkna = räkna - 1`), så villkoret `räkna <= 5` blir aldrig falskt. Fix: Ändra till `räkna = räkna + 1` för att räknaren ska öka.

14. **Ingen bugg** – Beräkningen fungerar korrekt. `rabatt_procent` används som decimaltal (0.2), så `100 * 0.2 = 20` vilket ger `100 - 20 = 80`. Det är rätt sätt att räkna procent. En bra övning för att visa att procent som decimaler fungerar direkt.
</div>