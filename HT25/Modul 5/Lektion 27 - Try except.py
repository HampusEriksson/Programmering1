"""Exempel på try/except i Python."""

# try except
while True:
	try:
		age = int(input("What is your age?"))
		break

	except ValueError:
		print("Du skrev inte in ett tal")

print(age)

# isdigit
while True:
	age = input("What is your age?")

	if age.isdigit():
		age = int(age)
		break
	else:
		print("Du skrev inte in ett tal")






















# Exempel 1: Fånga ValueError
try:
	tal = int(input("Skriv ett heltal: "))
	print("Du skrev:", tal)
except ValueError:
	print("Fel: du måste skriva ett heltal.")


# Exempel 2: Fånga ZeroDivisionError
try:
	a = int(input("Skriv täljare: "))
	b = int(input("Skriv nämnare: "))
	print("Svar:", a / b)
except ZeroDivisionError:
	print("Fel: du kan inte dividera med noll.")
except ValueError:
	print("Fel: skriv bara siffror.")



# Exempel 3: else och finally
try:
	namn = input("Skriv ditt namn: ")
	if len(namn) < 2:
		raise ValueError("Namnet är för kort.")
except ValueError as fel:
	print("Fel:", fel)
else:
	print("Hej", namn)
finally:
	print("Detta körs alltid, även om fel uppstår.")


# Exempel 4: Fånga alla fel (generellt)

try:
	lista = ["a", "b", "c"]
	index = int(input("Välj index 0-2: "))
	print("Du valde:", lista[index])
except Exception as fel:
	print("Något gick fel:", fel)


