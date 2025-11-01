numero = int(input("Dime un número: ") or "42")

if numero % 3 == 0 and numero % 7 == 0:
    print (f"{numero} es un número normal")
elif numero % 3 == 0 or numero % 7 == 0:
    print (f"{numero} es un número raro")
else: 
    print(f"{numero} no es multiplo ni de 3 ni de 7")   
print("="*40) 
#o puede ser también así:
#el número es múltiplo de 3 o de 7, pero no múltiplo de ambos al mismo tiempo
# Debe cumplirse la primera condición, y además no cumplirse la segunda”.
if (numero % 3 == 0 or numero % 7 == 0) and not (numero % 3 == 0 and numero % 7 == 0):
    print("Este número es RARO 😜 (solo múltiplo de 3 o de 7)")
else:
    print("Este número es normal 😐")
    
print("="*40)
    
if numero % 3 == 0 or numero % 7 == 0:
    print (f"{numero} es número es raro 😜")
elif numero % 3 == 0 and numero % 7 == 0:
    print (f"{numero} es un número normal")
elif not(numero % 3 == 0 and numero % 7 == 0):
    print (f"{numero} es un número no múltiplo ni de 3 ni de 7.") 
else: 
    print("No es un número valido")  

