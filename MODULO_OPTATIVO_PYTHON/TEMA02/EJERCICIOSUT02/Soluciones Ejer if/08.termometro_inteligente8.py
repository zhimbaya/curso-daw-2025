# Termómetro inteligente
temp = float(input("Introduce la temperatura en °C: "))
hora = int(input("Introduce la hora actual (0–23): "))

if temp < 0:
    if hora < 6 or hora > 20:
        print("🌙 Noche helada, mejor quedarse en casa.")
    else:
        print("❄️ Frío de día, abrígate bien.")
elif temp < 16:
    if hora < 6 or hora > 20:
        print("🌃 Noche fresca, lleva algo de abrigo.")
    else:
        print("🌬️ Hace fresco, ponte una chaqueta.")
elif temp < 26:
    if hora < 6 or hora > 20:
        print("🌜 Noche templada, ideal para pasear.")
    else:
        print("😊 Temperatura perfecta para salir.")
elif temp < 36:
    if hora < 6 or hora > 20:
        print("🌡️ Noche calurosa, duerme con la ventana abierta.")
    else:
        print("🥵 Hace calor, bebe agua y busca sombra.")
else:
    if hora < 6 or hora > 20:
        print("💦 Noche tropical, hidrátate bien.")
    else:
        print("🔥 ¡Mucho calor! Evita salir al sol.")