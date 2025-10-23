'''
Contraseña con vocales y números
Crea un programa que pida una contraseña y compruebe si cumple tres condiciones básicas:
1. Tiene una longitud de al menos 8 caracteres.
2. Contiene al menos una vocal (a, e, i, o, u, en minúscula o mayúscula).
3. Contiene al menos un número (0–9).
El programa debe mostrar si cada condición se cumple y, al final, indicar si la contraseña es segura o débil. 
Pista: puedes usar el operador in para comprobar si una letra o número está dentro de la cadena.'''

contrasena = input("Introduce una contraseña: ") or "Mipcssxxx0"
caracteres = len(contrasena)

print("Tú contraseña tiene más de 8 caracteres?: ","Si" if caracteres >= 8 else "No")
vocales = "aeiouAEIOU" #any() al menos hay una vocal
print("Tú contraseña contiene al menos una vocal?: ","Si" if any(letra in vocales for letra in contrasena) else "No")
numeros = "0123456789"
print("Tú contraseña contiene al menos un nº?: ","Si" if any(numero in numeros for numero in contrasena) else "No")
print("="*40)

texto = input("Introduce una contraseña: ") or "xxxx"
caracteres = len(texto)
print("Tú contraseña tiene más de 8 caracteres?: ","Si" if caracteres >= 8 else "No")
contiene_vocal = (
    "a" in texto or "e" in texto or "i" in texto or "o" in texto or "u" in texto or
    "A" in texto or "E" in texto or "I" in texto or "O" in texto or "U" in texto
)
print("Tú contraseña contiene al menos una vocal?: ","Si" if contiene_vocal else "No")
contiene_numero = (
    "0" in texto or "1" in texto or "2" in texto or
    "3" in texto or "4" in texto or "5" in texto or
    "6" in texto or "7" in texto or "8" in texto or
    "9" in texto
)
print("Tú contraseña contiene al menos un nº?: ","Si" if contiene_numero else "No")