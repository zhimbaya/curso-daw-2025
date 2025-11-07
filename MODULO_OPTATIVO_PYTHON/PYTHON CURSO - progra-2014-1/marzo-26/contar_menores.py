m = int(raw_input('m: '))
cuenta = 0
for n in range(m):

    # Determinar si n es primo o no
    c = 0
    for d in range(1, n + 1):
        if n % d == 0:
            c += 1
    es_primo = c == 2

    # Llevar la cuenta
    if es_primo:
        cuenta += 1

# Salida
print 'Hay', cuenta, 'primos menores que', m
