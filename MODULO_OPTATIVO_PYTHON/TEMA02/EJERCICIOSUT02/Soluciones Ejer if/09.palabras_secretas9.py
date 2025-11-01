palabra = input("Di la palabra secreta: ")

if palabra == "":
    print("⚠️ No has escrito nada.")
elif palabra.lower() in ("python", "serpiente", "programación"):
    print("🎉 ¡Has acertado la palabra secreta!")
else:
    print("❌ Esa no es la palabra secreta.")