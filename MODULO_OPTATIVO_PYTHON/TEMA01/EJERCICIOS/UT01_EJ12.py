'''
12. Combinación e inversión de cadenas
Partiendo de dos cadenas de texto introducidas por el usuario, crea un programa que:
1. Imprima las cadenas separadas por un guion bajo (_).
2. Tome las 3 primeras letras de la primera palabra.
3. Tome las 3 últimas letras de la segunda palabra.
4. Una ambas partes para formar una nueva cadena.
5. Muestre la cadena resultante invertida (al revés).
6. Finalmente, muestra todas las cadenas (las originales y la nueva) separadas por una coma.
'''
texto1 = input("Introduce una cadena de texto: ") or "Hola"
texto2 = input("Introduce otra cadena de texto: ") or "Bienvenidos"

print("Separadas por _: ",texto1,texto2, sep="_")
print("3 primeras letras: ",texto1[:3])
print("3 últimas letras: ",texto2[-3:])
nueva_cadena = texto1[:3]+texto2[3:]
print("Nueva cadena: ",nueva_cadena )
invertida = nueva_cadena[::-1]
print("Nueva cadena: ", invertida)
print(texto1,texto2,nueva_cadena,invertida,sep=",")