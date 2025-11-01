#pedir por pantalla los 3 números
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))
if (numero1 > numero2 and numero1 > numero3):
    mayor = numero1
elif (numero2 > numero1 and numero2 > numero3):
    mayor = numero2
else: mayor = numero3
print (f"El mayor de los 3 números es: {mayor}")
    
