'''
Casting (cambiar el tipo de dato de una variable a otro tipo compatible) y operadores con 
texto y números
En este ejercicio vas a practicar cómo Python trata de forma diferente los números y las 
cadenas de texto.
1. Pide al usuario un número escrito como texto, por ejemplo "25".
2. Pide otro número entero real, por ejemplo 5.
3. Convierte el primer valor (el texto) a número con int(), para poder hacer operaciones 
matemáticas.
4. Muestra en un solo print() dos resultados:
○ 🔹 La suma numérica de ambos valores.
○ 🔹 La repetición del texto, multiplicando la cadena por el número.
'''

num_texto = input("Dame un número: ") or "25"
num_int = int(input("Dame otro número: ") or "5")

texto_a_num = int(num_texto)

print("La suma es: ", texto_a_num + num_int ,"\nRepetición del texto: ",num_texto * num_int)