#Escribir los siguientes programas (sin usar condicionales, bucles ni estructuras)
# terminal
# python -m venv UT1
# pip install numpy

import math
import numpy as np

#Preguntará al usuario el radio en centímetros.
PI = 3.1415926535897932384626
radio_cm = float(input("Introduce el radio en cm: "))

#Conversión de unidades y cálculo del área
area_mm2 = math.pi * (radio_cm * 10) ** 2
area_cm2 = np.pi * radio_cm ** 2
area_m2 = PI * (radio_cm / 100) ** 2

#Presentará en pantalla:
#El área del círculo en mm2, cm2 y m2
print(f"El área del círculo es: {area_mm2:.2f} mm², {area_cm2:.2f} cm², {area_m2:.4f} m²")
