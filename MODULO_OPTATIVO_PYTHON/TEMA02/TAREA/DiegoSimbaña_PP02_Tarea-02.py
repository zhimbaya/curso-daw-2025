'''Escenario: Una tienda online necesita un programa en Python para gestionar pedidos.
•	Lista de productos: ["Camiseta", "Pantalón", "Zapatillas", "Chaqueta"]
•	Precios: [15, 25, 50, 40]
Requisitos:
1,2,3,4,5
Preguntas de análisis:
•	¿Cómo aplicaste las estructuras de selección, repetición y control de excepciones? -> Tal como se muestra en el código
•	¿Qué ocurriría si no se usara try-except? -> Lanzaría un error
•	¿Cómo refuerza este ejercicio la relación entre teoría y práctica? -> lo refuerza mucho, en análisis y comprensión
'''

productos = ["Camiseta", "Pantalón", "Zapatillas", "Chaqueta"]
precios = [15, 25, 50, 40]
precio = 0

print('='*40)
print('BIENVENIDOS A MI TIENDA ONLINE')
print('='*40)

#4.	Usar un bucle while que permita seguir comprando hasta que el usuario escriba "salir".
while True:
    #1.	Mostrar un menú con los productos y precios.
    print('Lista de productos y precios:')
    for i in range(len(productos)):
        print(f'\tOpción {i+1}: {productos[i]} \t-> {precios[i]}€')
    print('Opción 5. Salir ')
    
    #5.	Incluir manejo de errores con try-except.
    try:
        #2.	Permitir al usuario seleccionar varios productos y calcular el total.
        opcion = int(input("Selecciona una opción: ") or "2")
        
        if(opcion == 5):
            print('='*40)
            #3.	Aplicar un 10% de descuento si el total supera los 100 €.
            if(precio > 100):
                descuento = precio * 0.10
                precio -= descuento
                print(f'Precio Total con Descuento: {precio:.2f}€')
            else:
                print(f'Precio Total sin Descuento: {precio:.2f}€')
                
            print('Hasta pronto!')
            break
        elif opcion in (1,2,3,4):
            #precio += precios[opcion - 1] #todo se puede reducir a una linea
            if(opcion==1):
                precio += precios[opcion - 1]
            elif opcion == 2:
                precio += precios[opcion - 1]
            elif opcion == 3:
                precio += precios[opcion - 1]
            elif opcion == 4:
                precio += precios[opcion - 1]
            else:
                pass
            print(f'Suma Total: {precio:.2f}€')
            print('='*40)
        
        else:
            print("⚠️ Opción no válida. Intentalo de nuevo.")
            
    except ValueError:
        print("❌ Error: Debes ingresar un número válido.")
        continue
    finally:
        print("🔁 Volviendo al menú principal...")    