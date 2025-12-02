m = int(raw_input('m: '))

print 'Los', m, 'primeros primos son:'
cuenta = 0
n = 2
while cuenta < m:

    # Determinar si n es primo o no
    c = 0
    for d in range(1, n + 1):
        if n % d == 0:
            c += 1
    es_primo = c == 2

    # Salida y actualizacion
    if es_primo:
        cuenta += 1
        print n,
    n += 1
