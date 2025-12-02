# Solucion usando while con variable bandera.
# Cuando se ingresa 'FIN', se setea la variable
# fin (se "sube la bandera") para que en la proxima iteracion
# la condicion no se cumpla.

x = float(raw_input('x: '))

suma = 0.0
potencia = 1.0

print 'Coeficientes:'
fin = False
while not fin:
    entrada = raw_input()
    if entrada == 'FIN':
        fin = True
    else:
        a = float(entrada)
        suma += a * potencia
        potencia *= x

print 'p(x) =', suma




