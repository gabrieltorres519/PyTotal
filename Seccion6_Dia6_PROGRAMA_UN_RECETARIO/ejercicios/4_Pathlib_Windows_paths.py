from pathlib import Path, PureWindowsPath



carpeta = Path('/home/gabrielle/Documents/Cursos_Udemy/Python_Total/Seccion6_Dia6_PROGRAMA_UN_RECETARIO/ejercicios')

if not carpeta.exists():
    print('La carpeta no existe')
else:
    print('Genial!, existe la carpeta')
    ruta_windows = PureWindowsPath(carpeta)
    print(ruta_windows)

