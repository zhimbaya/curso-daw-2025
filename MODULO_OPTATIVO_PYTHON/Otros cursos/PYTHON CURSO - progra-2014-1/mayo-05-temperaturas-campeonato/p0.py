# Ejecute este programa para ver
# las respuestas del ejercicio cero.

print '==== P1 ===='
d = {'x': 'y', 'y': 'z'}
print d['y']

print '==== P2 ===='
a = 'x'
d = {a: 'm', 'a': a}
print d['a']

print '==== P3 ===='
x = []
d = {1: 3, 5: 2, 6: 4}
for k in d:
    x.append(d[k])
print max(x)

print '==== P4 ===='
d = {}
for x in range(10):
    d[x * x] = x
print d[4]

print '==== P5 ===='
capitales = {
  'Chile': 'Santiago',
  'Peru':  'Lima',
  'Bolivia': 'La Paz',
}
for pais in capitales:
    print capitales[pais]

print '==== P6 ===='
d = {1: 'un', 2: 'dos'}
d[3] = 'tres'
d[1] = 'uno'
d[10] = 'diez'
print len(d)

print '==== P7 ===='
print len({
  11: ['a', 'bcd'],
  1: ['ef', 'ghij', 'k'],
  111: ['l'],
}[1][1][1])

print '==== P8 ===='
d = {'a': 'b', 'b': 'c',
     'c': 'a', 'f': 'e'}
a = ['d', 'e', 'a']
for c in d:
    if c in a:
        print d[c]

