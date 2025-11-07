ruta = raw_input('Ruta: ')

norte = 0
sur = 0
este = 0
oeste = 0
for i in range(len(ruta)):
    if ruta[i] == 'n':
        norte += 1
    elif ruta[i] == 's':
        sur += 1
    elif ruta[i] == 'e':
        este += 1
    elif ruta[i] == 'o':
        oeste += 1

if sur > norte:
    ruta_vertical = (sur - norte) * 's'
else:
    ruta_vertical = (norte - sur) * 'n'

if oeste > este:
    ruta_horizontal = (oeste - este) * 'o'
else:
    ruta_horizontal = (este - oeste) * 'e'

print 'Ruta optimizada:', ruta_vertical + ruta_horizontal

