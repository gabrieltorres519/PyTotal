"""Saber en qué sistema operativo me encuentro"""

import os

print(os.getcwd())

"""Manejo de archivos"""

archivo = open('curso.txt','w')
archivo.write('Texto de prueba')
archivo.close()

print(os.listdir())

"""Movimientos dentro del sistema operativo"""

import shutil

#shutil.move('curso.txt','/home/gabrielle/Documents/Cursos_Udemy/Python_Total') # Mover  el archivo

# Los demás métodos de shutil funcionan y se llaman muy parecido a los comandos nativos de Linux

# Para evitar el uso del método de borrado de shutil y solo mandar archivos a la papelera se instala
# -> pip install send2trash
# import send2trash

# send2trash.send2trash('curso.txt')

ruta = '/home/gabrielle/Documents/Cursos_Udemy/Python_Total/Seccion9_Dia9_PROGRAMA_UN_BUSCADOR_DE_NUMEROS_DE_SERIE/ejercicios'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'\nEn la carpeta: {carpeta}')
    print(f'Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t {sub}')
    print(f'Los archivos son: ')
    for arch in archivo:
        if arch.startswith('2015'):
            print(f'\t {arch}\n')

