# Al no ser de tipado estricto, Python permite ingresar a la misma variable
# valores de diferentes tipos. 

# Valor 1
mi_variable = 10
print(mi_variable)
print(type(mi_variable))
# Valor 2
mi_variable = "Hola"
print(mi_variable)
print(type(mi_variable))
# Valor 3
mi_variable = 3.14
print(mi_variable)
print(type(mi_variable))

# Hay otro proceso llamado castin o conversiones de tipos, que consiste en
# transformar un valor de un tipo a otro tipo.

#  Exiten la conversion implícita y la explícita.

# Un ejemplo de conversión implícita es cuando se realiza una operación
# matemática entre un entero y un flotante. Python convierte automáticamente
# el entero a flotante para realizar la operación.
entero = 5
flotante = 2.0
resultado = entero + flotante
print(resultado)
print(type(resultado))  

# Un ejemplo de conversión explícita es cuando se utiliza una función
# incorporada para convertir un valor de un tipo a otro.
# Convertir un entero a flotante
entero = 10
flotante = float(entero)
print(flotante)
print(type(flotante))
# Convertir un flotante a entero
flotante = 9.99
entero = int(flotante)
print(entero)
print(type(entero))

# Convertir un entero a cadena
entero = 100
cadena = str(entero)
print(cadena)
print(type(cadena))
# Convertir una cadena a entero
cadena = "250"
entero = int(cadena)
print(entero)
print(type(entero))
# Convertir una cadena a flotante
cadena = "3.1416"
flotante = float(cadena)
print(flotante)     
print(type(flotante))

#  Ejemplo de error de concatenación de diferentes tipos
edad = 25
nueva_edad = edad + 5
mensaje = "Tengo " + str(nueva_edad) + " años."
print(mensaje)  
# Sin la conversión explícita a cadena, el código anterior generaría un error.