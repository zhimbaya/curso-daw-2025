estado = int(input("Introduce el número de error: "))
match estado:
    case 401 | 403 | 404:
        print("Acceso no permitido")

mes = int(input("Introduce el número del día de la semana (1-lunes, 7-domingo):"))
match mes:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Error. El número debe estar entre 1 y 7 ")