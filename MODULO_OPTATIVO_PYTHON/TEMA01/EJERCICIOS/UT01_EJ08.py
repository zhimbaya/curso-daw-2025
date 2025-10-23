'''
8. Comparación de edades
Crea un programa que pida las edades de dos personas y muestre, con valores True o False, si:
1. La primera persona es mayor que la segunda.
2. La primera persona es menor que la segunda.
3. Ambas personas tienen la misma edad.
'''
print("=====Comprobacion de edades=====")
edad_p1 = abs(int(input("Dame tú edad: ") or "-22"))
edad_p2 = abs(int(input("Dame tú edad: ") or "3"))

print("Edad P1 mayor que P2: ",edad_p1 > edad_p2)
print("Edad P1 menor que P2: ",edad_p1 < edad_p2)
print("Misma edad?: ",edad_p1 == edad_p2)