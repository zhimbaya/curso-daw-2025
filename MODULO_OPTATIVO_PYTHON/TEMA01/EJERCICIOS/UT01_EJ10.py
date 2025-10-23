'''
10.Ejercicio: Mostrar una tabla con nombres y edades usando caracteres de escape
Crea un programa en Python que muestre una pequeña tabla con los nombres y edades de dos personas. 
El texto debe aparecer alineado en columnas, utilizando los caracteres especiales de escape:
● \t → para insertar tabulaciones (espacios amplios entre columnas).
● \n → para insertar saltos de línea.
'''

p1_nombre = "diego"
p2_nombre = "armando"
p1_edad = 24
p2_edad = 40

print("==========TABLA==========")
print("| Nombre \t| Edad \t|")
print("-"*25)
print(f"| {p1_nombre} \t| {p1_edad} \t|")
print(f"| {p2_nombre} \t| {p2_edad} \t|")
print("="*25)


