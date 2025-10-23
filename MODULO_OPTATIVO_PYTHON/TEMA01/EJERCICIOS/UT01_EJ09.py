'''
9. Cálculo del IMC (sin if)
Crea un programa que calcule el Índice de Masa Corporal (IMC) a partir del peso (kg) y la altura (m) de una persona.
1. Pide el peso y la altura al usuario.
2. Calcula el IMC con la fórmula:
3. Muestra el valor del IMC con dos decimales.
4. Imprime tres expresiones booleanas (True o False) indicando si el IMC es:
○ Bajo peso → menor que 18.5
○ Peso normal → entre 18.5 y 24.9
○ Sobrepeso → mayor o igual a 25
'''
print("=====Cálculo del IMC=====")
peso_kg = float(input("Introduce tu peso en Kg: ") or "30.5")
print(peso_kg)
altura_metro = float(input("Introduce tu altura en metros: ") or "1.75")
print(altura_metro ** 2)
imc = peso_kg / (altura_metro ** 2)
print ("El IMC es: ", round(imc,2))
print (f"El IMC es: {imc:.2f}")

print("Bajo peso (< 18.5)?:", imc < 18.5)
print("Peso normal (18.5 - 24.9)?:", 18.5 <= imc <= 24.9)
print("Sobrepeso (≥ 25)?:", imc >= 25)

print("Bajo" if imc < 18.5 else "Normal" if 18.5 <= imc <= 24.9 else "Sobrepeso" if imc >= 25 else "Nada")
