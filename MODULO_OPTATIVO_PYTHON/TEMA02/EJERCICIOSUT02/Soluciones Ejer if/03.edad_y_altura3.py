edad = int (input("Dime la edad del usuario: "))
altura = float (input("Dime la altura del usuario: "))
'''
if 0 < edad < 120:
    print("edad ok")
else:
    print ("La edad no puede ser menor de 0 ni mayor de 120")
    edad= int(input("Dime de nuevo la edad: "))
    
if 0 < altura < 250:
    print ("altura ok")
else:
    print ("La altura no puede ser ni menor de 0 ni mayor de 250cms")
    altura = float(input("Dime de nuevo la altura: ")) 
    
print(f"Edad: {edad} años, Altura: {altura} cm") '''

print("="*30)

if (edad > 0 and edad < 120) and (0 < altura < 250):
    print("Edad OK!")
    print("Altura OK!")
else:
    edad= int(input("Dime de nuevo la edad: "))
    if not(edad > 0 and edad < 120):
        print("Edad incorrecta!")
    else:
        print('Edad Correcta!')
        
    altura = float(input("Dime de nuevo la altura: "))   
    if (0 > altura > 250):
        print("Altura incorrecta!")
    else:
        print('Altura Correcta!')

print(f"Edad: {edad} años, Altura: {altura} cm")