# Solucion usando operaciones de strings.

depto = raw_input('Departamento: ')

pos = depto[-1]   # tambien podria ser: pos = depto[len(depto) - 1]
if len(depto) == 4:
    piso = depto[0] + depto[1]
else:
    piso = depto[0]

# Partimos con el precio base, y lo modificamos
# solo para los departamentos "especiales"
precio = 245

if depto == '807':
    precio = 500
elif piso == '1':
    precio = 100
elif piso == '25':
    precio = 400
elif pos in '04':
    precio *= 0.83
elif pos in '37':
    precio *= 1.13

# Si no se cumple ninguna de las condiciones anteriores,
# estamos en un departamento comun, asi que el precio no cambia.
# Por lo tanto no ponemos else.

print int(precio)
