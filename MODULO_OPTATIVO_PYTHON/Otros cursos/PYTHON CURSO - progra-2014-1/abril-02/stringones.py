abreviado = raw_input()

original = ''
for i in range(len(abreviado) / 2):
    numero = int(abreviado[2 * i])
    letra = abreviado[2 * i + 1]
    original += numero * letra

print original
