#solicitar el año por pantalla
año = int(input("Dime el año y te diré si es bisiesto: ") or '2000')
# un año es bisiesto si es divisible por 4 y además 
# (no es divisible por 100 o sí es divisible por 400)."
if (año % 4 == 0 and año % 100 != 0) or (año % 100 == 0 and año % 400 == 0): #mas precisa y entendible
    # o también podemos preguntar acortando:
    print (f"El año {año} es bisiesto")
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
# el año es bisiesto si es múltiplo de 4 y, además,no es múltiplo de 100 o sí es múltiplo de 400.”
    print (f"El año {año} es bisiesto")
else: print(F"El año {año} no es bisiesto")
