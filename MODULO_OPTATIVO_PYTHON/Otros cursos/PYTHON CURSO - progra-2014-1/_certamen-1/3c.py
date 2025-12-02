ruta = raw_input('Ruta: ')

dx = 0
dy = 0
n = len(ruta)
for i in range(n):
    d = ruta[i]
    if d == 'n': dy += 1
    if d == 's': dy -= 1
    if d == 'e': dx += 1
    if d == 'o': dx -= 1

if dx > 0: x = 'e'
else:      x = 'o'

if dy > 0: y = 'n'
else:      y = 's'

opt = abs(dy) * y + abs(dx) * x
print 'Ruta optimizada:', opt

