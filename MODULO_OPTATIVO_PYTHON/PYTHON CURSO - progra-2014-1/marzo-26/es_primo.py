n = int(raw_input('n: '))

# Determinar si n es primo o no
c = 0
for d in range(1, n + 1):
    if n % d == 0:
        c += 1
es_primo = c == 2

# Salida
if es_primo:
    print 'Primo'
else:
    print 'No primo'
