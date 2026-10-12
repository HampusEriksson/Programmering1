item1 = "Diamond Sword"
item2 = "Diamond Pickaxe"
item3 = "Golden Apple"
item4 = "Ender Pearl"
item5 = "Bow"
item6 = "Shield"
item7 = "TNT"
item8 = "Enchanted Book"
item9 = "Compass"
item10 = "Cake"
item11 = ""
item12 = ""

# Print all items
print(
    f"Items: {item1}, {item2}, {item3}, {item4}, {item5}, {item6}, {item7}, {item8}, {item9}, {item10}"
)


# Skapa en lista - square brackets - option + 8

students = ["Albin", "Bea", "Calle", "Daniella", "Erik"]

print(students)
# Lägga till - append
new_student = input("Name of new student: ").capitalize()
students.append("Filippa")
# listans_namn.append(det som ska läggas till)
students.append(new_student)

# Ta bort med värde - remove
remove_student = input("Name of removed student: ").capitalize()
if remove_student in students:
    students.remove(remove_student)
else:
    print("The student is not in the list")
# Printa ut listor - använd * unpack
print(*students)

print(f"Alla elever i listan:")
print(*students)


# Index - börjar på 0
print(students[0])

# Index bakvänt - börjar på -1
print(students[-2])

# Slice
# [start:stop]
print(students[0:3])
# [början:stop]
print(students[:3])
# [start:slutet]
print(students[2:])
# [början:slutet:step]
print(students[::2])

# len() - antal element i listan
print(f"Amount of students: {len(students)}")
print(f"Letters in hampus: {len("hampus")}")

# Sortera

students.sort()
print(*students)
students.sort(key=lambda name: len(name))
print(*students)

# Loopa igenom listor
for student in students:
    print(f"{student} has {len(student)} letters in the name.")


# Lista som input

stuff = input("Skriv sakerna med mellanslag emellan").split(" ")
print(*stuff)
