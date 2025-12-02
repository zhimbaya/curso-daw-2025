#Bucle for en python
frase = input("Introduce una frase: ")
for car in frase:
    print(car, end ="")
print()

# Bucle que itera sobre una secuencia de números
for i in range(4,20,2):
    print(i, end=" ")
print()

for i in range(4):
    print(i, end="")
print()

for i in range(1, 5):
    for j in range (1, 11):
        print(f'{j} * {i} = {i*j}')
    print()

# Ejemplo para break y else
for i in range(1, 6):
    print(i)
    if i == 3:
        print("Me salgo del bucle")
        break
else:
    print("El bucle se completó sin interrupciones")
