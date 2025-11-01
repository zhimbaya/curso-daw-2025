#pedir lados al usuario
while True:
    try:
        lado1 = float(input("Dime el la longitud del primer lado: "))
        lado2 = float(input("Dime la longitud del segundo lado: "))
        lado3 = float(input("Dime la longitud del tercer lado: "))
        if (lado1+lado2<=lado3) or (lado2+lado3<=lado1) or (lado1+lado3<=lado2):
            print("Con los datos que me has dado no se puede formar un triangulo")
            break
        elif lado1==lado2==lado3:
            print ("Se trata de un triángulo Equilatero")
        elif lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("Se trata de un triangulo Isósceles")
        elif lado1!=lado2 and lado2!=lado3 and lado1!=lado3:
            print("Se trata de un triángulo Escaleno")
        print('='*40)
    except ValueError:
        print('No es un nº correcto.')