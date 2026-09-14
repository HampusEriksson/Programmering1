import random

# computer_choice kommer vara antingen sten, sax eller påse
computer_choice = random.choice(["sten", "sax", "påse"])

# skriv din kod här
user_choice = input("Sten, sax eller påse?")

if user_choice == computer_choice:
    print("Tie")
elif user_choice == "sax" and computer_choice == "påse":
    print("You win!")
elif user_choice == "sten" and computer_choice == "sax":
    print("You win!")
elif user_choice == "påse" and computer_choice == "sten":
    print("You win!")
else:
    print("You lose.")
