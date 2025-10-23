'''
Comprobador de Palíndromos
En este ejercicio vas a crear un pequeño programa que determine si una palabra es un palíndromo, 
es decir, si se lee igual de izquierda a derecha que de derecha a izquierda 
(ejemplo: “radar”, “oso”, “reconocer”).
1. Pide una palabra al usuario.
2. Convierte la palabra a minúsculas para evitar errores con mayúsculas.
3. Compara la palabra original con su versión invertida y muestra true o false 
dependiendo de si es o no un palíndromo.
'''
palabra = input("Introduce una palabra: ").lower() or "reconocer"
lista = list(palabra)
lista.reverse()  # modifica la lista original
invertida = ''.join(lista)  # convierte la lista invertida en string
print(f"Es un palindromo, {palabra}?: ", "Sí" if palabra == invertida else "No")
print("=" *30)

palabra = input("Introduce una palabra: ").lower() or "radar"
palabra_invertida = palabra[::-1] #invertimos la palabra
print(f"Es un palindromo, {palabra}?: ","Si" if palabra == palabra_invertida else "No")