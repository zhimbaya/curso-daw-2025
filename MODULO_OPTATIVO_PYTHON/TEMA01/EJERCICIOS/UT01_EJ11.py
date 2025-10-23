'''
11. Combinación alterna de letras (cadenas de 5 caracteres)
Crea un programa que trabaje con dos textos de exactamente 5 caracteres 
cada uno (recuerda: el espacio también cuenta como un carácter).
El programa debe hacer lo siguiente:
1. Imprimir las dos cadenas separadas por una barra vertical (|).
2. Crear una nueva cadena combinada tomando letras alternas:
○ 1ª letra de la primera cadena
○ 2ª letra de la segunda cadena
○ 3ª letra de la primera cadena
○ 4ª letra de la segunda cadena
3. Mostrar la nueva palabra en mayúsculas.
4. Imprimir todas las cadenas (las dos originales y la nueva) separadas por puntos (.).
'''
cadena_texto1 = "HolaH"
cadena_texto2 = "bienb"
print(cadena_texto1 +" | "+ cadena_texto2)
print(cadena_texto1,cadena_texto2 , sep=" | ")

combinada = cadena_texto1[0] + cadena_texto2[1] + cadena_texto1[2] + cadena_texto2[3] + cadena_texto1[4]
print (combinada)
print("Combinada en mayúsculas:", combinada.upper())
print(cadena_texto1 + "." + cadena_texto2 + "." + combinada)
print(cadena_texto1, cadena_texto2, combinada, sep=".")