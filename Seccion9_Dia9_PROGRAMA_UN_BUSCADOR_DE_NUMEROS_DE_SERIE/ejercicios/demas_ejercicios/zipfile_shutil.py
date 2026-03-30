import zipfile
import shutil


"""Comprimier archivos en carpeta"""
mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')

mi_zip.write('texto1.txt')
mi_zip.write('texto2.txt')
mi_zip.write('texto3.txt')

mi_zip.close()


"""Extraer los archivos (descomprimir)"""
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')

zip_abierto.extractall()

# zip_abierto.extract('texto1.txt') # Si queremos extraer un archivo en concreto, lo indicamos entre paréntesis




"""Shutil para comprimir el contenido de carpetas completas"""
carpeta_origen = '/home/gabrielle/Documents/Cursos_Udemy/Python_Total/Seccion9_Dia9_PROGRAMA_UN_BUSCADOR_DE_NUMEROS_DE_SERIE/ejercicios/demas_ejercicios/carpeta_origen'

archivo_destino = '/home/gabrielle/Documents/Cursos_Udemy/Python_Total/Seccion9_Dia9_PROGRAMA_UN_BUSCADOR_DE_NUMEROS_DE_SERIE/ejercicios/demas_ejercicios/carpeta_comprimida.zip'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

"""Descomprimir con shutil"""
shutil.unpack_archive(archivo_destino, 'carpeta_descomprimida', 'zip')