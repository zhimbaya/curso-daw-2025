'''
Pedir un texto y parar cuando el usuario escriba “salir”.
Nombre programa “salir.py”.'''
try:
    texto = input('Escribe un texto o "quit" para salir: ') or "Hola! como estas?"
    while True:
        if texto in ('quit','exit','bye','salir'):
            print('!Hasta pronto¡')
            break
            
        else:
            print('Has escrito: ',texto)
            texto = input('Escribe el texto nuevamente o "quit" para salir: ')
except Exception as e:
    print('Ha ocurrido un error:',e)