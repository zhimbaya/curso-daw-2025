'''
**Autor:** Diego Simbaña
**Fecha:** 20/11/2025

Validador de DNIs.

Pide un DNI y comprueba que es correcto, será correcto si tiene 9 caracteres y
la letra es correcta.
Para calcular la letra se divide el número entre 23 y el resto indica la 
posición de la cadena de letras: "TRWAGMYFPDXBNJZSQVHLCKE"

Usar una función para validar el DNI y otra que te devuelva la letra del mismo.

PARA GENERAR LA DOCUMENTACIÓN:

python -m pydoc -w dni

python -m pip install pdoc

pdoc ejercicio.py -o docs

'''
print('=====VALIDAR DNI=====')

def letra(dni):
    '''función que busca la letra del número del DNI.'''
    numero = dni[0:8]
    posicion = int(numero)%23
    letra = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return letra[posicion] 


def validar_dni(dni):
    '''función que valida el DNI.'''
    if len(dni) == 8:
        dni = '0' + dni 
        
    if  (len(dni) == 9) and (dni[:8].isdecimal()) and letra(dni) == dni[8].upper() :
        return True

if __name__ == "__main__":
    dni = input('Introduce tu DNI: ') or '2562559z'
    while True:
        try:
            if validar_dni(dni):
                print('DNI Correcto, hasta pronto!')
                break
            else:
                print('No es correcto el DNI!')
                dni = input('Vuelve a introducir el DNI: ')
        except Exception as e:
            print('Ha ocurrido un error: ',e)
            dni = input('Volvemos...al principio del script, Vuelve a introducir el DNI: ')