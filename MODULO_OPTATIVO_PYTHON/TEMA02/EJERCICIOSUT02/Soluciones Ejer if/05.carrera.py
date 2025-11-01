import random

# Solicitar largo de la pista con validación
while True:
    try:
        largo_pista = int(input("Introduce el largo de la pista (entre 200 y 800 metros) [Enter]: ") or "250")
        if 200 <= largo_pista <= 800:
            break
        else:
            print("❌ El largo debe estar entre 200 y 800.")
    except ValueError:
        print("❌ Por favor, introduce un número válido.")

# Solicitar nombres de los competidores
atleta1 = input("Nombre del primer atleta [Enter]: ") or "Noah Lyles"
atleta2 = input("Nombre del segundo atleta [Enter]: ") or "Kishane Thompson"

# Inicializar posiciones
pos1 = 0
pos2 = 0

print("\n🏁 ¡Comienza la carrera!\n")

# Simular la carrera
while pos1 < largo_pista and pos2 < largo_pista:
    avance1 = random.randint(1, 10)
    avance2 = random.randint(1, 10)
    pos1 += avance1
    pos2 += avance2

    print(f"El atleta {atleta1} se encuentra en la posición: {pos1}")
    print(f"El atleta {atleta2} se encuentra en la posición: {pos2}")
    print("-" * 40)

# Determinar el resultado
print("\n🎉 ¡La carrera ha terminado!")
if pos1 >= largo_pista and pos2 >= largo_pista:
    print("¡Ha habido un empate!")
elif pos1 >= largo_pista:
    print(f"🏆 El atleta {atleta1} ha ganado la carrera.")
else:
    print(f"🏆 El atleta {atleta2} ha ganado la carrera.")