# Funktioner

def hello():
    print("Hello")

hello()























# Parametrar, skicka in data till funktionen
def hello_name(name):
    print(f"Hello {name}. Welcome to the program.")


hello_name("Roni")

hello_name("Olof")
















def sub(a, b, c=0):
    print(a-b-c)

sub(5, 2)
sub(10,3,2)

import random
def omar(a,b):
    return (a+b + random.randint(1,10))

age1 = int(input("What is your age?"))
age2 = int(input("What is your age?"))
svar = omar(age1, age2)
print(f"Ditt magiska tal är {svar}.")


def pythagoras(a,b):
    return (a**2 + b**2)**(1/2)

katet1 = 3
katet2 = 4
hypotenusan = pythagoras(katet1, katet2)







def meme_generator(name):
    return ("Sigma Kirk " + name).upper() + "!!!!"

username = input("What is your name?")
username = meme_generator(username)
print(username)

