# Bibliotek (moduler) - färdig kod vi kan importera och använda
# Python har ett stort standardbibliotek med massor av moduler.
# Vi kan också installera externa bibliotek med pip (t.ex. pip install requests).

# --- Två sätt att importera ---

# Sätt 1: importera hela modulen - används med modulnamn.funktion()
# Importering gör vi längst upp i filen, enligt PEP8
import random

print(random.randint(1,100))
nummer = [1,2,3,4,5]
print(random.choice(nummer))

# Sätt 2: importera specifik funktion - används direkt utan modulnamn
from random import randint, choice
print(randint(1,100))

# importera allting med *
# Såhär ska vi inte göra!!!
from random import *
from math import *
print(randint(1,100))
nummer = [1,2,3,4,5]
print(choice(nummer))

# Tips: man kan ge modulen ett kortare alias med "as"
import random as r
print(r.randint(1,100))

# --- math - matematiska funktioner ---
import math
print(math.pi)
print(math.sqrt(9))
print(math.ceil(3.54))
print(math.floor(3.5213521))

# --- datetime - datum och tid ---
import datetime
print(datetime.datetime.now())

# --- time - mäta tid / pausa programmet ---
import time
start = time.time()

time.sleep(3)

stop = time.time()

print(f"Det har gått {stop - start} sekunder sedan du började.")

# --- os - interagera med operativsystemet ---
import os
print(os.getcwd())          # aktuell mapp
print(os.listdir("."))      # lista filer i mappen

# --- sys - systeminformation ---
import sys
print(sys.version)          # vilken Python-version
print(sys.platform)         # vilket OS
# sys.exit()                # avslutar programmet (kommenterad så koden körs klart)


