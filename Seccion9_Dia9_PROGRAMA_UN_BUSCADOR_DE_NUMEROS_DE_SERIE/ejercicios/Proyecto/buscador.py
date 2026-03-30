import os, re, time, math
from datetime import datetime
from pathlib import Path

def programa():

    ruta = '/home/gabrielle/Documents/Cursos_Udemy/Python_Total/Seccion9_Dia9_PROGRAMA_UN_BUSCADOR_DE_NUMEROS_DE_SERIE/ejercicios/Proyecto/Mi_Gran_Directorio'
    misarchivos = []
    nos_serie = []
    fecha = datetime.now()

    for carpeta, subcarpeta, archivo in os.walk(ruta):
        # print(f'En la carpeta: {carpeta}\n')
        # print('Las subcarpetas son: \n')
        for sub in subcarpeta:
            # print(f'\t {carpeta+sub}')
            # print('Los archivos son: \n')
            ruta_con_archivos = Path(carpeta,sub)
            for archivo in ruta_con_archivos.glob("*.txt"):
                # print(f'{archivo}\n\n')
                mi_archivo = open(f'{archivo}')
                contenido = str(mi_archivo.read())
                # print(contenido)
                patron = re.compile(r'N([a-z]{3})-(\d{5})') # Ejemplo de patrón para un número de serie: N seguido de 3 letras y 5 dígitos
                busqueda = re.search(patron,contenido)
                if busqueda == None:
                    pass
                else:
                    # print('¡Archivo con número de serie encontrado!\n')
                    misarchivos.append(str(archivo.name))
                    # print(busqueda.group())
                    nos_serie.append(str(busqueda.group()))
                # buscar = re.search(patron,contenido) # Devolverá "None" si no cumple los requisitos del patrón
                mi_archivo.close()

    # print(misarchivos)
    # print(nos_serie)
    # print(fecha.date())
    # print(len(nos_serie))
    print(f"""
        ----------------------------------------------------
        Fecha de búsqueda: {fecha.date()}
    """)
    print('\tARCHIVO           NRO. SERIE\n')
    i=0
    for elemento in nos_serie:
        print(f"""\t-------	         ----------\n\t{misarchivos[i]}    {nos_serie[i]}
        """)
        i+=1
    print(f"""

        Números encontrados: {len(nos_serie)}
    """)

inicio1 = time.time()
programa()
final1 = time.time()
# print(final1-inicio1)

tiempo = math.ceil((final1-inicio1)*10000) / 10000 # El ciclo for es más rápido en esta prueba

print(f'        Duración de la búsqueda: {tiempo} segundos\n        ----------------------------------------------------')


