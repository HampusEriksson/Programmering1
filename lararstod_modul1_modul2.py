# 1: Variabler och datatyper (str, int, float, bool)
# variabel = värde
# citattecken -> text (string)
name = "Hampus"
# int -> heltal
age = 32

# 2: print
print("Welcome to the program")
print("The creator is named:", name)

# 3: input() och typkonvertering med int()/float()
your_name = input("What's your name? ")
print("Hello", your_name)

your_age = int(input("How old are you? "))

# 4: Enkel matte med variabler (+, -, *, /)
print("You and", name, "are", age + your_age, "years old.")
print("You and", name, "are", age - your_age, "years apart.")

# 6: Modul 2-koppling - if/else med alder >= 18
guess = int(input("How old do you think Hampus is? "))
if (guess == age):
    print("Correct, you are the master of equation systems.")
else:
    print("F in math 2b!!")
