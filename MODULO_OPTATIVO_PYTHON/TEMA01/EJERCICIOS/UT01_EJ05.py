'''
5. Casting con valores booleanos
Crea un programa que pida al usuario tres valores diferentes:
1. Un texto
2. Un número entero
3. Un número decimal
Después convierte cada uno a tipo booleano (bool()) y muestra si su valor es Verdadero (True) o Falso (False).'''

texto = input("Introduce un texto: ") or ""
entero = int(input("Introduce un nº entero: ") or "-1")
decimal = float(input("Introduce un nº decimal: ") or "-12.0")

print ("Verdadero" if bool(texto) else "Falso")
print ("Verdadero" if bool(entero > 0) else "Falso")
print ("Verdadero" if bool(decimal) else "Falso")
