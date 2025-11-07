'''
Pedir una contraseña hasta que sea correcta. La contraseña será “python”. 
Nombre programa “contraseña.py”.
'''
p_verde = "\033[92m"
p_rojo = "\033[91m"
print('-----Login-----')
try:
    contrasena = input('Introduce la contraseña: ')
    while True:
        if contrasena == 'python':
            print(p_verde+"Felicidades, has acertado!",p_verde)
            break
        else:
            print(p_rojo+"La contraseña es erronea!"+p_rojo)
            contrasena = input('Introduce nuevamente la contraseña: ')
except KeyboardInterrupt:
    print("\n\033[93mPrograma interrumpido por el usuario.\033[0m")

except Exception as e:
    print(f"\033[91mHa ocurrido un error: {e}\033[0m")