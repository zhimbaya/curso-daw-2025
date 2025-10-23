'''Escenario:
Una empresa necesita un programa en Python para calcular el salario semanal de sus empleados. El programa debe:
•	Solicitar el nombre del trabajador, las horas trabajadas y el precio por hora.
'''
print("==========SALARIO SEMANAL==========")
#Se solicita el nombre del trabajador
nombre_trabajador = input("Introduce tu nombre: ") or "Diego"
#Se solicita las horas trabajadas
horas_trabajadas= abs(float(input("Introduce las horas: ") or "39.5"))
#Precio por hora
precio_hora = abs(float(input("Cuál es el precio por hora: ") or "20.4"))

'''
•	Calcular el salario normal (hasta 40 horas) y las horas extra (se pagan al 150%).
'''
#Calculo del salario normal
salario_normal = horas_trabajadas * precio_hora
#Calculo de las horas extra
horas_extra = horas_trabajadas - 40
#Calculo del salario + horas extra
salario_extra = (40 * precio_hora) + (horas_extra * (precio_hora * 1.5))
'''
•	Mostrar un reporte con el nombre del trabajador y su salario total.
'''
print("="*35)
print("Nombre del trabajador: ",nombre_trabajador.lower())
#Se muestra por pantalla dependiendo del número de horas
total = salario_normal if horas_trabajadas <= 40 else salario_extra
print(f"Salario total: {total:.2f} €")
print("="*35)
'''
Problemas detectados en el prototipo actual del código:
•	Uso de variables con nombres poco claros (x, y, z).
•	Un error de indentación provoca un IndentationError.
•	Se han usado valores fijos en lugar de variables para las horas y precios.
•	No hay comentarios explicativos.
Preguntas a resolver:
1.	Identifica los errores estructurales y de estilo en el prototipo.
2.	Propón un código corregido, comentado y bien estructurado.
3.	Explica por qué tu solución es más clara y robusta que la inicial.
4.	Reflexiona sobre la importancia de los operadores y conversiones de tipo en este caso.
Extensión orientativa: 2–3 páginas.
'''