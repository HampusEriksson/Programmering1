# While True
password = "hej123"
while True:
    user_password = input("Password: ")
    if user_password == password:
        print("Du är inloggad")
        break
    else:
        print("Fel lösenord")

# While condition
count = 0
while count < 3:
    answer = int(input("Vad är 1+1?"))
    if answer == 2:
        print("Rätt")
        count += 1
    else:
        print("Fel")

# Continue
