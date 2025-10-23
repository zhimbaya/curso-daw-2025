'''
6. Comprobación de campos vacíos con booleanos
Crea un programa que pida tres datos al usuario:
1. Su nombre
2. Su correo electrónico
3. Su edad
Luego, convierte cada dato a booleano (bool()) y muestra si cada campo se ha 
rellenado o se ha dejado vacío. Finalmente, muestra si todos los campos están 
completos (True) o alguno falta (False).'''

print("======Datos del usuario=====")
nombre = input("Dame tú nombre: ") or ""
correo = input("Dame tu correo: ") or "micorreo@gmail.com"
edad = int(input("Dime tú edad: ") or "28")
print("="*30)
print("Campo nombre, rellenado" if bool(nombre) else "Campo nombre vacío")
print("Campo correo, rellenado" if bool(correo) else "Campo correo vacío")
print("Campo edad, rellenado" if bool(edad > 0) else "Campo edad vacío")
print("="*30)
print("Todo completo" if (bool(nombre) and bool(correo) and bool(edad)) else "Falta algún dato")