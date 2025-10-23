'''
13. Ejercicio: Manipulación de dos cadenas
Crea un programa que pida dos cadenas de texto al usuario y realice diferentes operaciones con ellas.
1. Muestra cuántas letras tiene cada una.
2. Crea una nueva cadena que esté formada por:
○ desde la 3ª letra de la primera palabra hasta el final,
○ seguida de la primera mitad de la segunda palabra.
3. Muestra la nueva cadena resultante en mayúsculas.
4. Finalmente, imprime todas las cadenas separadas por un guion (-) en una sola línea.'''

texto1 = input("Introduce una cadena de texto: ") or "Hola"
texto2 = input("Introduce otra cadena de texto: ") or "Bienvenidos"

print(f"Nº de letras,{texto1}: ",len(texto1))
print(f"Nº de letras,{texto2}: ",len(texto2))

posicion = int(len(texto2)/2)
nueva_palabra = (texto1[2:])+texto2[posicion:]

print(nueva_palabra)
print(texto1,texto2,nueva_palabra,nueva_palabra.upper(),sep="_")
