'''
7. Comprobación de números positivos con booleanos
Crea un programa que pida tres números enteros y determine si al menos dos de ellos son positivos. Para ello:
1. Convierte cada número a booleano (bool()) para saber si es verdadero (positivo o distinto de 0) o falso 
(cero o negativo).
2. Muestra el valor booleano de cada número.
3. Muestra si al menos dos de ellos son positivos usando operadores lógicos (and, or).'''

n1 = int (input("Dame un número: ") or "1")
n2 = int (input("Dame un número: ") or "1")
n3 = int (input("Dame un número: ") or "-2")

n1_espositivo = bool(n1 > 0)
n2_espositivo = bool(n2 > 0)
n3_espositivo = bool(n3 > 0)

print(f"{n1} , es positivo?:", n1_espositivo)
print(f"{n2} , es positivo?:", n2_espositivo)
print(f"{n3} , es positivo?:", n3_espositivo)


al_menos = (n1_espositivo and n2_espositivo) or (n1_espositivo and n3_espositivo) or (n2_espositivo and n3_espositivo)
print("Al menos dos positivos?: ", "Si" if al_menos else "No")
