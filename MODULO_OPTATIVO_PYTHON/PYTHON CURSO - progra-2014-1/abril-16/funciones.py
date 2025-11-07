def sumar_palitos(x, y):
    return x + y

def restar_palitos(x, y):
    return (len(x) - len(y)) * 'i'


# Funcion auxiliar para ser usada en es_primo.
# No es necesaria, pero hace que la funcion siguiente
# sea mas legible.
def es_divisible(numero, divisor):
    return numero % divisor == 0

def es_primo(n):
    for d in range(2, n):
        if es_divisible(n, d):
            return False
    return True

def contar_primos_menores_que(m):
    c = 0
    for n in range(2, m):
        if es_primo(n):
            c += 1
    return c


def reflejar(n):
    r = 0
    while n > 0:
        r = 10 * r + n % 10
        n = n / 10
    return r

def es_palindromo(numero):
    return numero == reflejar(numero)

# es_palindromo tambien podria haber sido escrita asi:
#
#     def es_palindromo(numero):
#         if numero == reflejar(numero):
#             return True
#         else:
#             return False
#             
# pero es un poco redundante: si la comparacion es True se retorna True
# y si es False se retorna False. Es bueno acostumbrarse a retornar
# directamente el resultado de la comparacion.


# Ya que la funcion binomial(n, k) calcula tres factoriales,
# conviene definir antes la funcion factorial(m).
def factorial(m):
    f = 1
    for i in range(1, m + 1):
        f *= i
    return f

# ...aunque tambien la podriamos haber importado
# desde el modulo de funciones matematicas:
#
#     from math import factorial
#

def binomial(n, k):
    f_n  = factorial(n)
    f_nk = factorial(n - k)
    f_k  = factorial(k)
    return f_n / (f_nk * f_k)

