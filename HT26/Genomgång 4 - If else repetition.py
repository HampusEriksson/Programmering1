"""
Biljettpriser
18-25 : 100kr
25 - 65 : 150 kr
65+ : 50kr
18-: 50kr
"""

age = int(input("Age: "))
# if age >= 18 and age <= 25:
if 18 <= age <= 25:
    print("Pris 100kr")
elif age > 25 and age < 65:
    print("Pris 150kr")
else:
    print("Pris 50kr")

# Nästlad if
member = input("Är du member? ").lower()
if 18 <= age <= 25:
    if member == "ja":
        print("Pris 80kr")
    else:
        print("Pris 100kr")
elif age > 25 and age < 65:
    if member == "ja":
        print("Pris 130kr")
    else:
        print("Pris 150kr")
else:
    print("Pris 50kr")
