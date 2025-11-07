m = int(raw_input('m: '))
print 'Los primos menores que', m, 'son:'
for n in range(m):

    # Determinar si n es primo o no
    c = 0
    for d in range(1, n + 1):
        if n % d == 0:
            c += 1
    es_primo = c == 2

    # Salida
    if es_primo:
        print n,
