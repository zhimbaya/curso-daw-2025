def interpretar_geojson(linea):
    # quitar el salto de linea y las llaves
    linea = linea.strip()[1:-1]
    datos = linea.split(',')

    sismo = {}
    for dato in datos:
        llave, valor = dato.split(':', 1)

        # convertir el valor al tipo apropiado
        if llave == 'mag' or llave == 'dept':
            valor = float(valor)
        elif llave == 'tsunami':
            valor = int(valor)
        elif llave == 'date':
            valor = tuple(map(int, valor.split('-')))

        sismo[llave] = valor

    return sismo


def mayor_sismo(nombre_archivo):
    mayor_magnitud = 0.0
    mayor_sismo = None

    archivo = open(nombre_archivo)
    for linea in archivo:
        sismo = interpretar_geojson(linea)
        if sismo['mag'] > mayor_magnitud:
            mayor_magnitud = sismo['mag']
            mayor_sismo = (sismo['mag'], sismo['place'], sismo['date'])
    archivo.close()

    return mayor_sismo


def mostrar_registro(nombre_archivo, mag):
    archivo = open(nombre_archivo)
    plantilla = '{} <-> {} <-> {} <> {}-{}'
    for linea in archivo:
        sismo = interpretar_geojson(linea)
        if sismo['mag'] >= mag:
            print plantilla.format(sismo['place'].upper(),
                                   sismo['mag'],
                                   sismo['dept'],
                                   '-'.join(map(str, sismo['date'])),
                                   sismo['time'])
    archivo.close()


print interpretar_geojson('{mag:5.8,place:Salvador,dept:23.0,tsunami:0,date:2014-03-17,time:06:11:08}')
print
print mayor_sismo('registro.geojson')
print
mostrar_registro('registro.geojson', 4.4)
