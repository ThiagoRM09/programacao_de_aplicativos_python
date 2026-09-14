# Estruturas de Repetição

# While Loop

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

# For Loop
print("")

for numero in range(10, 0, -1):
    print(numero)

# Array
print("")

nomes = ["Ana", "Betina", "Carol"]

for nome in nomes:
    print(nome)

# Break, Continue and Pass
print("")

#Break
print("-- Break --")
for numero in range(1, 11):

    if numero == 6:
        break
    print(numero)

#Continue
print("-- Continue --")
for numero in range(1, 11):

    if numero == 6:
        continue
    print(numero)

#Pass
print("-- Pass --")
for numero in range(1, 11):

    if numero == 6:
        pass
    print(numero)