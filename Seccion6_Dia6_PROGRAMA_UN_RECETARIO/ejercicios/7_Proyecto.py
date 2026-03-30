# Administrador de recetas

# Tomando como base la estructura de carpetas dentro de la carpeta "Recetas"

# 1) Saludo, bienvenida, ruta de acceso al directorio de recetas, informará el total de recetas en la carpeta
# 2) Pedir que elija una de las siguientes opciones:
#   a) Leer receta
#      1. Elegir categoria
#      2. Mostrar recetas disponibles en esa categoria
#      3. Elegir receta 
#      4. Leer receta (mostrar su contenido)
#   b) Crear receta
#      1. Elegir categoria
#      2. Crear nombre
#      3. Crear contenido 
#   c) Crear categoria
#      1. Nombre de la categoria
#      2. Crear categoria (carpeta)
#   d) Eliminar receta
#      1. Elegir categoria
#      2. Mostrar recetas disponibles en esa categoria
#      3. Elegir receta 
#      4. Eliminar receta (borrar el archivo)
#   e) Eliminar categoria
#      1. Elegir categoria
#      2. Eliminar categoria (borrar la carpeta)
#   f) Finalizar programa

# Consideraciones:
# - Cada que el usuario realice correctamente cada acción, el programa pedirá presionar alguna letra para
#   volver al inicio o menú hasta que elija finalizar programa
# - Cada que el usuario vuelva al menú inicial, se limpiará la pantalla para que no se acumule información

from os import system, name
import os
from pathlib import Path

# Funciones necesarias

def seleccionar_categoria(guiaFinal):

    print('Elige una categoria: \n')
    counter = 0
    for archivo in guiaFinal.glob("*"): # Para obtener solo las carpetas en la ruta, no todos los archivos dentro de ellas
        counter = counter + 1
        carpetas_ruta_completa = str(archivo) 
        retirar = str(archivo.parent) 
        print(f'{counter}: {carpetas_ruta_completa.removeprefix(retirar)}')
    
    seleccion_categoria = (input("\n: "))
    # Para asegurarse que el input sea un número entero y no otro tipo de caracter se puede hacer lo siguiente
    while not seleccion_categoria.isdigit():
        print('Seleccione una opción correcta...')
        seleccion_categoria = input("\n: ")
    seleccion_categoria = int(seleccion_categoria)

    listado_categorias = list(guiaFinal.glob("*"))

    print(f'La categoria seleccionada es: {listado_categorias[seleccion_categoria - 1].name}')

    path_categoria_seleccionada = listado_categorias[seleccion_categoria - 1]

    return path_categoria_seleccionada

def visualizar_recetas_categoria(guiaFinal,path_categoria_seleccionada_nombre):
    print('Recetas disponibles en esta categoria: \n')
    counter = 0
    for archivo in guiaFinal.glob(f"{path_categoria_seleccionada_nombre}/*"):
        counter = counter + 1
        print(f'{counter}: {archivo.name}')

    seleccion_receta = input("\n: ")

    while not seleccion_receta.isdigit():
        print('Seleccione una opción correcta...')
        seleccion_receta = input("\n: ")
    seleccion_receta = int(seleccion_receta)

    if seleccion_receta > counter or seleccion_receta < 1:
        print('Seleccione una opción correcta...')
        # continue

    receta_seleccionada = list(guiaFinal.glob(f"{path_categoria_seleccionada_nombre}/*"))[seleccion_receta - 1]
    print(f'\nContenido de la receta seleccionada: \n{receta_seleccionada.read_text()}')

    return receta_seleccionada

def limpiar_pantalla():
    if name == "nt":  # Windows
        system("cls")
    else:  # Unix/Linux/MacOS
        system("clear")

# Programa

continuar = 's'

limpiar_pantalla()

print('\nBienvenido al recetario \n')
base = Path.home()
guiaFinal = Path(base,"Documents","Cursos_Udemy",Path("Python_Total","Seccion6_Dia6_PROGRAMA_UN_RECETARIO","ejercicios","Recetas"))
    
for archivo in guiaFinal.glob("*"): # Para obtener solo las carpetas en la ruta, no todos los archivos dentro de ellas
    carpetas_ruta_completa = str(archivo) 
    retirar = str(archivo.parent) 
    print(carpetas_ruta_completa.removeprefix(retirar))

contador = 0 
    
for archivo in guiaFinal.glob('**/*.txt'):
    contador = contador + 1
    
print(f'\nHay {contador} recetas en este recetario \n')

while continuar == 's':

    print('Seleccione una de las siguentes opciones: \n')

    print("""   
    a) Leer receta
    b) Crear receta
    c) Crear categoria
    d) Eliminar receta
    e) Eliminar categoria
    f) Finalizar programa
    """)

    seleccion = input(": ")

    limpiar_pantalla()

    if seleccion == 'f':
        print('Programa finalizado...')


    if seleccion.lower() == 'f':
        
        continuar = 'n'

    elif seleccion in 'abcde':
        
        match seleccion:
        
            case 'a':

                limpiar_pantalla()

                print('Leer receta')

                path_categoria_seleccionada = seleccionar_categoria(guiaFinal)

                print(f'La categoria seleccionada es: {path_categoria_seleccionada.name}')

                path_categoria_seleccionada_nombre = Path(path_categoria_seleccionada).name

                visualizar_recetas_categoria(guiaFinal,path_categoria_seleccionada_nombre)

                
            case 'b':

                limpiar_pantalla()

                print('Crear receta')

                path_categoria_seleccionada = seleccionar_categoria(guiaFinal)
                categoria_seleccionada = path_categoria_seleccionada.name
                ruta_categoria = path_categoria_seleccionada

                print(f'La ruta de la categoria es: {ruta_categoria}')

                print(f'La categoria seleccionada fue: {categoria_seleccionada}')

                nombre_receta = input('Ingrese el nombre de la receta a crear: ')

                ruta_completa_archivo  = Path(ruta_categoria,str(f'{nombre_receta}.txt'))

                archivo = open(ruta_completa_archivo,'w')

                contenido = input('Ingrese el contenido de la receta: ')

                archivo.write(str(contenido))

                archivo.close()

                lectura = open(f'{ruta_completa_archivo}')

                print(lectura.read())

            case 'c':

                limpiar_pantalla()

                print('Crear categoria')

                nombre = input('Ingrese el nombre de la nueva categoría: ')
                bandera = False
                for carpeta in guiaFinal.glob('*'):
                    if str(carpeta.name).lower() == str(nombre).lower():
                        print('La categoría que intenta crear ya existe...')
                        bandera = True

                if bandera == False:
                    print(str(nombre))
                    ruta_nueva_categoria = Path(guiaFinal,str(nombre))
                    os.makedirs(ruta_nueva_categoria)
                    print(f'La categoria {nombre} ha sido creada exitosamente...')

            case 'd':

                limpiar_pantalla()

                print('Eliminar receta')

                path_categoria_seleccionada = seleccionar_categoria(guiaFinal)
                
                path_categoria_seleccionada_nombre = path_categoria_seleccionada.name
                ruta_categoria = path_categoria_seleccionada

                print(f'La ruta de la categoria es: {ruta_categoria}')

                print(f'La categoria seleccionada fue: {path_categoria_seleccionada_nombre}')

                # nombre_receta = input('Ingrese el nombre de la receta a eliminar: ')

                receta_seleccionada = visualizar_recetas_categoria(guiaFinal,path_categoria_seleccionada_nombre)

                print(receta_seleccionada)

                os.remove(receta_seleccionada)

            case 'e':

                limpiar_pantalla()

                print('Eliminar categoria')

                path_categoria_seleccionada = seleccionar_categoria(guiaFinal)

                categoria_seleccionada = path_categoria_seleccionada.name
                ruta_categoria = path_categoria_seleccionada

                print(f'Categoría a eliminar {categoria_seleccionada}')

                os.rmdir(Path(path_categoria_seleccionada))
                print("Categoria eliminada exitosamente...")
                

            case _:

                print('Seleccione una opción correcta...')

    elif seleccion not in 'abcde':

        pass

    