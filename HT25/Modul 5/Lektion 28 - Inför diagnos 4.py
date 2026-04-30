# Funktion
# Gör något eventuellt baserat på indata (variabel)

def f(x):
    return 3*x

# Parameter - det vi skickar in till funktionen
# Default - c är 0 OM c inte skickas in
def add(a,b,c=0):
    return a+b+c

add(1,2,3) # 6
add(7,5) #12

def hi():
    print("Hi there.")

print(hi())