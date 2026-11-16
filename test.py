"""
Elev: nayan.sokhi
Klass: T25b
Övning: Kassasystem
Inlämnad: 2026-11-09 13:40:44

Instruktioner:
  VAR NOGA MED ATT LÄSA IGENOM ALLA INSTRUKTIONER INNAN DU BÖRJAR KODA SÅ ATT DU INTE BEHÖVER ÄNDRA MASSOR FÖR A-NIVÅ

  🟢 Betyget E – Grundläggande funktioner
    [x] Skapa en lista för att spara priser på sålda varor och en lista för att spara varans namn.

    [x] Fråga användaren vad den har köpt och vilket pris varan hade och spara denna info i dina listor.  Fortsätt fråga så länge användaren vill (t.ex. tills användaren skriver stopp).

    [x] Skriv ut alla varor som har köpts efter att användaren är färdig.

  🟡 Betyget C – Smartare kod och bättre struktur
    [/] Beräkna totalpriset med hjälp av en for-loop och skriv ut detta.

  [ ] Beräkna och skriv ut medelpriset för de sålda varorna.

    [/] Räkna och kategorisera varorna i tre grupper och skriv ut antalet:
  - Billig vara: mindre än 20 kr
  - Medelvara: 20 kr upp till 50 kr
  - Dyr vara: över 50 kr

    [/] Skriv ut en tydlig sammanställning över totalsumma, medelpris samt antalet varor i varje priskategori.

  🔴 Betyget A – Avancerat och robust
  [ ] Programmet ska inte kunna krascha på grund av användarens input. Skriv en kommentar med # på de rader där du har skrivit kod som förebygger krasch och förklara raden kort.

  [ ] Använd en for-loop för att hitta och skriva ut det högsta priset i listan.

  [ ] Rabattsystem med sammansatta villkor: Om totalsumman överstiger 200 kr eller om fler än 5 varor har sålts, ska kassan automatiskt ge 10 % rabatt på totalsumman. Skriv ut slutpriset efter rabatt samt hur mycket kunden sparade.


  Detta är slutet på instruktionerna. Klappa en gång med dina händer.
"""

"""
Återkoppling: Du samlar namn och priser och visar varukorgen. Du har påbörjat en totalsummering och en priskategorisering, men loopen räknar inte ihop alla priser och kategoriserar bara det senast inmatade priset.
Bygg vidare med en summa som uppdateras i for-loopen, räkna medelpris och antal i varje kategori. Skydda också int-konverteringen så ogiltig inmatning inte kraschar programmet.
"""

# Skriv din kod här
namn = list()
priser = list()
antal = enumerate(priser)


kopt = input("Vad har du köpt? ")
namn.append(kopt)
pris = int(input("Hur mycket kostade allt? "))
priser.append(pris)
igen = input("Vill du lägga till mer? Ja eller Nej: ")

while igen == "Ja":
    kopt = input("Vad har du köpt? ")
    namn.append(kopt)
    priss = int(input("Hur mycket kostade allt? "))
    priser.append(priss)
    igen = input("Vill du lägga till mer? Ja eller Nej: ")
if igen != "Ja":
    print("Tack för ditt köp")
    print("Du har köpt:", namn)
    print("Varorna kostade", priser)

for p in priser:
    print(pris + priss)


if pris < 20:
    print("Billig vara")
elif pris >= 20 and pris <= 50:
    print("Medelvara")
elif pris > 50:
    print("Dyr vara")
