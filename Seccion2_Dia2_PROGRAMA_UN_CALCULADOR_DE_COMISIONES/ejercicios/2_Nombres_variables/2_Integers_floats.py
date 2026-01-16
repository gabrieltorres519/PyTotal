mi_numero = 1
print(mi_numero)
print(type(mi_numero))

mi_numero = 5 + 2.5
print(mi_numero)
print(type(mi_numero))  

# No se pueden hacer operaciones con datos obtenidos por input() sin convertirlos
numero1 = input("Dime un número: ")
numero2 = input("Dime otro número: ")
print("La suma es: " + str(int(numero1) + int(numero2)))
# Solución alternativa
print("La suma es: " + str(float(numero1) + float(numero2)))
# Conversión explícita de tipos
numero1 = int(numero1)
numero2 = int(numero2)
print("La suma es: " + str(numero1 + numero2))
# Conversión implícita de tipos
print("La suma es: " + str(numero1 + 2.5))
# Ejemplo de conversión implícita
mi_numero = 7
print(mi_numero + 3.5)  # Aquí 7 se convierte implíc


