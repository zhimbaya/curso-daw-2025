emocion = input("¿Cómo te sientes hoy? (feliz, triste, enfadado, sorprendido): ")
#puedes pegar directamente el emoji o poner su código

if emocion.lower() == "feliz":
    print("😊 Me alegro mucho.")
    print("\U0001F60A Me alegro mucho")
elif emocion.lower() == "triste":
    print("\U0001F622 😢 Ánimo, mañana será mejor.")
elif emocion.lower() == "enfadado":
    print("\U0001F621 Respira hondo... cuenta hasta 10.")
elif emocion.lower() == "sorprendido":
    print("😲 ¡Vaya! No me lo esperaba.")
else:
    print("🤔 No entiendo esa emoción, pero espero que estés bien.")