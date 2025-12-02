ruta = raw_input('Ruta: ')

desp_vertical = 0
desp_horizontal = 0
for i in range(len(ruta)):
    if ruta[i] == 'n':
        desp_vertical += 1
    elif ruta[i] == 's':
        desp_vertical -= 1
    elif ruta[i] == 'e':
        desp_horizontal += 1
    elif ruta[i] == 'o':
        desp_horizontal -= 1

if desp_vertical > 0:
    dir_vertical = 'n'
else:
    dir_vertical = 's'

if desp_horizontal > 0:
    dir_horizontal ='e'
else:
    dir_horizontal = 'o'

ruta_vertical   = abs(desp_vertical)   * dir_vertical
ruta_horizontal = abs(desp_horizontal) * dir_horizontal

print 'Ruta optimizada:', ruta_vertical + ruta_horizontal

