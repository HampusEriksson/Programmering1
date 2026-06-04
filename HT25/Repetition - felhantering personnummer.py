
manader = {
    1: "januari",
    2: "februari",
    3: "mars",
    4: "april",
    5: "maj",
    6: "juni",
    7: "juli",
    8: "augusti",
    9: "september",
    10: "oktober",
    11: "november",
    12: "december",
}

while True:
    pnr = input("Ange personnummer (YYMMDDXXXX)").strip()

    if len(pnr) != 10:
        print("Du ska skriva 10 tecken")
        continue

    # TODO 1 (live): Anvand isdigit har innan vi gar vidare.
    # Exempel: if not pnr.isdigit(): ... continue
    if not pnr.isdigit():
        print("Du ska bara skriva in siffror.")
        continue

    # TODO 2 (live): Lagg try/except runt blocket nedan.
    # Fanga minst: ValueError, IndexError, KeyError
    try:
        ar = int(pnr[0:2])
        manad = int(pnr[2:4])
        dag = int(pnr[4:6])

        manad_text = manader[manad]
    except KeyError:
        print("Månaden ska vara ett tal mellan 1 och 12")
        continue
  

    print("\n--- RAPPORT ---")
    print(f"Pnr: {pnr}")
    print(f"Fodd: {dag} {manad_text} -{ar}")
    break


print(f"Loopen avslutad med personnummer {pnr}")
