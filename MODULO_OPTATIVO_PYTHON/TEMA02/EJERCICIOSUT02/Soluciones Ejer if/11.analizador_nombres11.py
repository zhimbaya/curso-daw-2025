nombre = input("¿Cómo te llamas? ")

if nombre.startswith("A") or nombre.startswith("a"):
    print("🅰️ Tu nombre empieza por A, ¡como el abecedario!")
elif nombre.endswith("o"):
    print("😎 Tu nombre termina en 'o'. ¡Suena poderoso!")
elif len(nombre) < 4:
    print("😅 Nombre corto, pero fácil de recordar.")
else:
    print("😊 Encantado, " + nombre + ".")