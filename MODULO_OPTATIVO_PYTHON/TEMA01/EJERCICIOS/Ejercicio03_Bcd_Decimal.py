#Convertir Decimal a BCD en Python
def decimal_a_bcd(numero):
    bcd = ''
    for digito in str(numero):
        bcd += format(int(digito), '04b') + ' '
    return bcd.strip()

# Ejemplo
print(decimal_a_bcd(59))  # Salida: 0101 1001

#Convertir BCD a Decimal
def bcd_a_decimal(bcd):
    bcd = bcd.replace(' ', '')  # Elimina espacios
    decimal = ''
    for i in range(0, len(bcd), 4):
        grupo = bcd[i:i+4]
        decimal += str(int(grupo, 2))
    return int(decimal)

# Ejemplo
print(bcd_a_decimal('0101 1001'))  # Salida: 59