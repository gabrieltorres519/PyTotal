import re

# Los caracteres especiales en las expresiones regulares son:
# /d: Coincide con cualquier dígito (equivalente a [0-9])
# /D: Coincide con cualquier carácter que no sea un dígito (equivalente a [^0-9])
# /w: Coincide con cualquier carácter alfanumérico (equivalente a [a-zA-Z0-9_])
# /W: Coincide con cualquier carácter que no sea alfanumérico (equivalente a [^a-zA-Z0-9_])
# /s: Coincide con cualquier espacio en blanco (equivalente a [ \t\n\r\f\v])
# /S: Coincide con cualquier carácter que no sea un espacio en blanco (equivalente a [^ \t\n\r\f\v])
# .: Coincide con cualquier carácter excepto el salto de línea
# ^: Coincide con el inicio de una cadena
# $: Coincide con el final de una cadena
# *: Coincide con cero o más repeticiones del patrón anterior
# +: Coincide con una o más repeticiones del patrón anterior
# ?: Coincide con cero o una repetición del patrón anterior


# {n}: Coincide con exactamente n repeticiones del patrón anterior
# {n,}: Coincide con n o más repeticiones del patrón anterior
# {n,m}: Coincide con entre n y m repeticiones del patrón anterior
# []: Define un conjunto de caracteres a coincidir
# (): Agrupa patrones para aplicar operadores a todo el grupo
# |: Operador OR para combinar patrones
# \: Escapa un carácter especial para que se trate como un carácter literal



#----------------------Ejemplos simples---------------------------------------

texto = 'En algún lugar de la Mancha de cuyo nombre no quiero acordarme'

patron = 'Mancha'

busqueda = re.search(patron,texto)

print(busqueda)

print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

busqueda = re.findall('de',texto)

print(busqueda)
print(len(busqueda))

for hallazgo in re.finditer('de',texto):
    print(hallazgo.span()) # Imprimir la ubicación de cada coincidencia (inicio y fin en el string)



#----------------------Ejemplos con patrones más complejos--------------------

texto = 'llama al 567-525-5678 ya mismo' 

patron = r'\d\d\d-\d\d\d-\d\d\d\d'

patron2 = r'\d{3}-\d{3}-\d{4}'

resultado = re.search(patron,texto)

print(resultado)

resultado2 = re.search(patron2,texto)

print(resultado2)
print(resultado2.group())




patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado3 = re.search(patron3,texto)

print(resultado3)
print(resultado3.group(2)) # Indice comienza en 1 para esta agrupación


#------------------------------Inserción de clave y validación-------------------------------------

clave = input('Clave iniciando con una letra seguido de 7 caracteres: ')

patron = r'\D{1}\w{7}' # Primer dato no sea un dígito (solo letras) y 7 letras o números más, por fuerza

chequear = re.search(patron,clave)

print(chequear)

#-------------------------------Más ejemplos---------------------------------------------------

texto = "No atendemos los lunes por la tarde"

buscar = re.search(r'lunes|martes',texto)

print(buscar)

buscar = re.search(r'....demos....',texto) # Se almacenarán tantos caracteres como puntos antes y después (en caso de encontrase demos)

print(buscar)

# Para buscar si no hay un dígito al incio de la cadena
buscar = re.search(r'^\D',texto)

print(buscar)


# Para buscar si no hay un dígito al final de la cadena
buscar = re.search(r'\D$',texto)

print(buscar)


# Obtener en una lista todos los caracteres  que  no sean espacios vacios
buscar = re.findall(r'[^\s]',texto)

print(buscar)


# Obtener en una lista todos los caracteres  que  no sean espacios vacios
buscar = re.findall(r'[^\s]+',texto) # El signo + hace que se agrupen los caracteres no vacíos en palabras completas, en lugar de caracteres individuales

print(buscar)

email = input('Ingrese su correo electrónico: ')

patron = re.compile(r'(\w{2,})@(\w{2,})\.com(\.{0,1})(\w{0,})')

buscar = re.search(patron,email) # Devolverá "None" si no cumple los requisitos del patrón
print(buscar)
