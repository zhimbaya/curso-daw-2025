#Preguntará al usuario un número en base decimal
n_decimal = int(input("Introduce un número decimal: "))

#Conversión de tipos
#int (cadena , base)
n_binario = bin(n_decimal)[2:] #muestra el dato desde la posición 2
n_octal = oct(int(n_binario,2))[2:]
n_hexadecimal = hex(int(n_octal,8))[2:]


'''
Presentará en pantalla:
El número en base binaria
El número en base hexadecimal
'''
print(f"El número en base binaria: {n_binario}")
print(f"El número en base octal: {n_octal}")
print(f"El número en base hexadecimal: {n_hexadecimal.upper()}")
print(int(n_hexadecimal,16))

