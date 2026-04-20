import random

# Parametrar - det som skickas in till funktionen
# Datatyper på parametrar
# docstring - beskrivning av funktionen
import random

def remove_random_element(the_list : list):
    """Tar bort ett slumpmässigt element från en lista."""
    if isinstance(the_list, list):
        the_list.remove(random.choice(the_list))
    else:
        print("The parameter is not a list.")

bananas= ["Yellow banana", "Long banana", "kokbanan", "Skalad banan"]
remove_random_element(bananas)
print(bananas)


# default värden på parametrar
def greet(name="world"):
    """Hälsar på någon, eller världen om inget namn anges."""
    print(f"Hej {name}!")

greet("Maja")
greet("Najib")
greet()

# def g(x,y):
#     return x*y

# Lambda
# variabelnamn = lambda parameter1, parameter2 : returdata
g = lambda x,y : x * y
""" Samma sak som
def f(x):
    return 3*x + 2
"""
f = lambda x : 3*x + 2

print(f(3))

print(g(5,10))

# lambda i sortering
# sortera list av tuples
students = [("Erik", 15), ("Adam", 17), ("Berit", 13), ("Carl", 20), ("David", 10)]

print(*students)
# Sorterar default på index [0]
students.sort()
print(*students)

# Om vi vill sortera på andra index, använd lambda-funktion
students.sort(key=lambda x: x[1])
print(*students)

# sortera på längden av namnet
students.sort(key=lambda x: len(x[0]))
print(students)

# args och kwargs
def calculate_total_score(*scores):
    print(scores)
    """Tar emot ett valfritt antal delpoang och returnerar totalen."""
    return sum(scores)

def create_student_profile(**student_info):
    """Tar emot elevinformation som nyckelord och skriver ut en elevprofil."""
    print("Elevprofil")
    for key, value in student_info.items():
        print(f"{key}: {value}")

total_score = calculate_total_score(12, 18, 20, 15, 5235,41512,521,521)
print(f"Total poang pa prov och uppgifter: {total_score}")

create_student_profile(
    namn="Maja",
    klass="TE25",
    favoritamne="Programmering",
    narvaro="96%",
    stad = "stockholm"
)