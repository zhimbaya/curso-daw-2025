anotaciones = raw_input('Anotaciones: ')
n = len(anotaciones)
puntos = 0
total = 0
periodo = 1
for i in range(n):
    a = anotaciones[i]
    if a == 'T':
        puntos += 3
    elif a == 'D':
        puntos += 2
    elif a == 'L':
        puntos += 1
    elif a == ' ':
        print puntos, 'puntos en el periodo', periodo
        total += puntos
        puntos = 0
        periodo += 1

# El ultimo periodo hay que tratarlo aparte
# despues del for, ya que es el unico que no
# esta terminado por un espacio en el string.
print puntos, 'puntos en el periodo', periodo
total += puntos

print 'Total:', total, 'puntos'


