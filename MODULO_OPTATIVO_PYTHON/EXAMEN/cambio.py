'''
Autor: Diego Simbaña
Fecha: 20/11/2025

Cajero de cambio: devuelve y desglosa el cambio en billetes y monedas de forma 
"ideal"; es decir, con el menor número de billetes y monedas posibles.

Pide un valor en euros y devuelve los billetes de 500, 200, 100, 50, 20, 10 y 5 
euros, y las monedas de 2€, 1€, 50c, 20c, 10c, 5c, 2c y 1c. Ejemplo:

Valor en €uros:  175,50

Cambio: 1 billete de 100€
  1 billete de 50€
  2 billetes de 20€
  1 billete de 5€
  1 moneda de 50c
'''
print('=====CAMBIO=====')
dinero = input('Introduce el dinero para el cambio: ') or '11.50'

euros = int(dinero.split('.')[0])
centimos = int(dinero.split('.')[1])

billetes = [500,200,100,50,20,10,5]
resto = euros
for i in range(len(billetes)):
    cuantia = resto//billetes[i]
    if cuantia > 0:
        if cuantia == 1:
            print(cuantia,'billete de ', billetes[i],'euro')
        else:
            print(cuantia,'billetes de ', billetes[i],'euros')
        resto = resto%billetes[i]

monedas = [200,100,50,20,10,5,2,1]
resto = (resto * 100) + centimos
for moneda in monedas:
    cuantia = resto//moneda
    if cuantia > 0:
        if moneda >= 100:
            if cuantia == 1:
                print('Una moneda de ', int(moneda/100),'euros')
            else:
                print(cuantia,'monedas de ', int(moneda/100),'euros')
                
        else:
            if cuantia == 1:
                print(cuantia,'moneda de ', moneda,'euro')
            else:
                print(cuantia,'monedas de ', moneda,'euros')
        resto = resto%moneda     