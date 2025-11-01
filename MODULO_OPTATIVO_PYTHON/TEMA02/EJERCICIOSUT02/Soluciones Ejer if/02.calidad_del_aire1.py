calidad_aire = float(input("Introduce el indice de calidad del aire: "))
if 0 <= calidad_aire <= 50:
    calidad = "Bueno"
elif calidad_aire <100:
    calidad = "Moderado"
elif calidad_aire < 150:
    calidad = "No es saludable para grupos sensibles"
elif calidad_aire < 200:
    calidad = "Insalubre"
elif calidad_aire < 300:
    calidad = "Muy Insalubre"
elif calidad_aire < 500:
    calidad = "Peligroso"
else:
    calidad = "Valor fuera de rango. El ICA debe estar entre 0 y 500"
print (f"La calidad del aire es: {calidad}")

    