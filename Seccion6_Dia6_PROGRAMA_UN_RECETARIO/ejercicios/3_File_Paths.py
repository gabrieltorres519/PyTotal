# Para evitar problemas con los paths y sus diferentes formas (windows, linux y macos)
# se utiliza el objeto path del módulo pathlib en la librería os

# Los métodos para cambiar de directorio no arrojan nada, solo cambian el CWD para el código
import os

ruta = os.getcwd() # Get Current Working Directory

print('---Directorio actual de trabajo---')

archivo_cwd = open('prueba1.txt') 

print(archivo_cwd.read())

archivo_cwd.close()

ruta2 = os.chdir('/home/gabrielle/Documents') # Para cambiar el directorio de trabajo para este archivo python
# A partir de este momento en el código, cualquier archivo se buscará en la carpeta Documents

print('\n---Cambiando el directorio de trabajo---')

archivo_fuera = open('PruebaCursoPyhton.txt')
print(archivo_fuera.read())

archivo_fuera.close()

# Regresando al directorio actual de trabajo

print('\n...Regresando al directorio original...')

ruta_original = os.chdir(ruta) 

archivo_cwd = open('prueba1.txt') 

print(archivo_cwd.read())

print(ruta_original)

archivo_cwd.close()

# Creación de directorios para archivos

#rutaCrearDirectorio = os.makedirs('/home/gabrielle/Documents/Cursos_Udemy/Python_Total/Seccion6_Dia6_PROGRAMA_UN_RECETARIO/ejercicios/creado_con_python')
# La carpeta solo se puede crear una vez, posteriores ejecuciones del programa darán error



# Trabajar con rutas del sistema de archivos

ruta_global = '/home/gabrielle/Documents/Cursos_Udemy/Python_Total/Seccion6_Dia6_PROGRAMA_UN_RECETARIO/ejercicios/prueba1.txt'

# Para obtener el nombre del archivo en la ruta
elemento = os.path.basename(ruta_global)
print(f'El archivo es {elemento}')

# Para obtener toda la ruta global anterior al archivo
ruta_anterior = os.path.dirname(ruta_global)
print(f'La ruta antes de él es {ruta_anterior}')

# Para tener la ruta global y el archivo en una tupla
print('En tupla')
ruta_anterior = os.path.split(ruta_global)
print(ruta_anterior)

# Para eliminar un directorio o carpeta
#os.rmdir('/home/gabrielle/Documents/Cursos_Udemy/Python_Total/Seccion6_Dia6_PROGRAMA_UN_RECETARIO/ejercicios/creado_con_python')


# Trabajar con rutas independientemente del sistema operativo

from pathlib import Path

carpeta = Path('/home/gabrielle/Documents') # Aunque la ruta es mac/linux, gracias a path, windows encontrará el archivo

archivo = carpeta / 'PruebaCursoPyhton.txt'

mi_archivo = open(archivo)

print(mi_archivo.read())

