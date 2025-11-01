'''
Elabora un programa interactivo en Python que integre:
1.	Una estructura condicional (if-elif-else).
2.	Un bucle de repetición (for o while).
3.	Una estructura de salto (break o continue).
4.	Manejo de excepciones (try-except).
⚠️ El trabajo debe ser original, de autoría propia y 🚫 sin uso de herramientas de IA.

'''
print("🔢 Bienvenido Grado Superior de DAW - Módulo de Python")

while True:
    try:
        print("\nSelecciona una opción para saber acerca del tema: ")
        print('''
            1. Identificación de los elementos de un programa informático.
            2. Uso de estructuras de control.
            3. Funciones. Definición de funciones definidas por el programador. Recursividad.
            4. Cadenas de caracteres. Listas. Tuplas y Diccionarios.
            5. Lectura y escritura de información.
            6. Programación orientada a objetos. Encapsulación, herencia y polimorfismo.
            ''')
        print("7. Salir")

        opcion = int(input("Selecciona una opción (1-7): "))

        if opcion == 7:
            print("👋 ¡Gracias por usar la calculadora!")
            break
        elif opcion in [1, 2, 3, 4, 5, 6]:
                if opcion == 1:
                    informacion = '''
                    🔹 Comandos y conceptos clave:
                        •  print() → salida por consola
                        •  # comentario → documentación interna
                        •  input() → entrada de datos
                        •  type() → tipo de dato
                        •  id() → identificador de objeto
                        •  help() → documentación integrada
                        •  dir() → atributos y métodos disponibles
                    '''
                elif opcion == 2:
                    informacion = '''
                    🔹 Comandos y estructuras:
                        •  if, elif, else → decisiones condicionales
                        •  for → bucle sobre secuencias
                        •  while → bucle con condición
                        •  break → salir del bucle
                        •  continue → saltar a la siguiente iteración
                        •  pass → instrucción nula
                        '''
                elif opcion == 3:
                    informacion = '''
                    🔹 Comandos y estructuras:
                        •  def nombre_funcion(): → definición de función
                        •  return → devolver resultado
                        •  *args, **kwargs → argumentos variables
                        •  lambda → funciones anónimas
                        •  Recursividad → función que se llama a sí misma
                    '''
                elif opcion == 4:
                    informacion = '''
                    🔹 Comandos y métodos comunes:
                        •  Cadenas: .upper(), .lower(), .split(), .replace(), len()
                        •  Listas: .append(), .remove(), .sort(), .pop(), len()
                        •  Tuplas: tuple(), acceso por índice
                        •  Diccionarios: .get(), .keys(), .values(), .items(), del
                    '''
                elif opcion == 5:
                    informacion = '''
                    🔹 Comandos clave:
                        •  open() → abrir archivo
                        •  read(), readlines() → leer contenido
                        •  write() → escribir en archivo
                        •  with open(...) as f: → gestión segura de archivos
                        •  json → lectura/escritura de datos estructurados
                    '''
                elif opcion == 6:
                    informacion = '''
                    🔹 Comandos y estructuras:
                        •  class → definición de clase
                        •  __init__() → constructor
                        •  self → referencia al objeto
                        •  Herencia: class Hija(Padre):
                        •  Encapsulación: atributos privados __atributo
                        •  Polimorfismo: redefinición de métodos
                    '''
                print(f"✅ El resultado de la opcion - {opcion} es: {informacion}")
        else:
            print("⚠️ Opción no válida. Intentalo de nuevo.")
    except ValueError:
        print("❌ Error: Debes ingresar un número válido.")
        continue