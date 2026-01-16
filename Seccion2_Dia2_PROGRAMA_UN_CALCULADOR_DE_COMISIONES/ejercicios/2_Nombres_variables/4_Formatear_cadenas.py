# Para poder mostrar los valores podríamos valernos del casteo a cadena, sin embargo 
# existe una forma más elegante de hacerlo utilizando f-strings (formatted strings).

color_auto  = "rojo"
matricula = 266254

print("El auto es de color " + color_auto + " y su matrícula es " + str(matricula) + ".")  # Forma tradicional
print(f"El auto es de color {color_auto} y su matrícula es {matricula}.")  # Forma con f-strings, también llamada interpolación de cadenas

# Tambien con la función format()
print("El auto es de color {} y su matrícula es {}.".format(color_auto, matricula))