'''
La Universidad Tropical Filomena Santa Marta ha instaurado un nuevo reglamento de eval-
uaciones. Todas las asignaturas deben tener tres cert ́amenes y un examen. Las notas van
entre 0 y 10, con un decimal.
Despu ́es de los tres cert ́amenes, los alumnos con promedio menor que 3 reprueban y los con
promedio mayor o igual que 7 aprueban. El resto va al examen, en el que deben sacarse por
lo menos un 5 para aprobar.
Adem ́as, para reducir el trabajo de los profesores, se decidi ́o que los alumnos que se sacan
menos de un 2 en los dos primeros cert ́amenes est ́an autom ́aticamente reprobados. A su
vez, los que obtienen m ́as de un 9 en los dos primeros cert ́amenes est ́an autom ́aticamente
aprobados. En ambos casos, no deben rendir el tercer certamen.
Escriba un programa que pregunte a un estudiante las notas de las evaluaciones que rindi ́o,
y le diga si est ́a aprobado o reprobado.
'''
print('----- Universidad Tropical Filomena Santa Marta -----')
while True:
    try:
        while True:
            nota1 = float(input('Dime la nota de tu 1er certamen: ') or '1.5')
            if 0.0 <= nota1 <= 10.0:
                break
            else:
                print('Número fuera de rango')
        while True:
            nota2 = float(input('Dime la nota de tu 2do certamen: ') or '3.5')
            if 0.0 <= nota2 <= 10.0:
                break
            else:
                print('Número fuera de rango')
    except ValueError:
        print('Introduce una nota valida.')
                
        if nota1 <= 2.0 and nota2 <= 2.0:
            print('Automaticamente reprobados')
            print('No dan el tercer certamen')
            break
        elif nota1 >= 9.0 and nota2 >= 9.0:
            print('Automaticamente Aprobados')
            print('No dan el tercer certamen')
            break
        else:
            while True:
                nota3 = float(input('Dime la nota de tu 3er certamen: ') or '4.5')
                if 0.0 <= nota3 <= 10.0:
                    break
                else:
                    print('Número fuera de rango')
                    
            promedio = (nota1 + nota2 + nota3)/3.0
            if promedio < 3.0:
                print('Reprobados')
            elif promedio >=7.0:
                print('Aprobados')
            else:
                print('El promedio es: ', promedio)
                while True:
                    nota_examen = float(input('Dime la nota del examen: ') or '5.1')
                    if 0 <= nota_examen <= 10:
                        break
                    else:
                        print('Nota fuera de rango')
                if nota_examen >= 5.0:
                    print('Aprobado')
                else:
                    print('Suspenso')  
        break
    
