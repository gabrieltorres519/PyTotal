# Instancias de path independientes del sistema operativo

from pathlib import Path

base = Path.home()
guia = Path("Barcelona","Sagrada_Familia.txt")
guia_completa = Path(base, "Barcelona", "Sagrada_Familia.txt")
# También admite otros objetos path
guia_completa2 = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
print(base)
print(guia)
print(guia_completa)
print(guia_completa2)

# Para sustituir el nombre del archivo, se puede usar with_name
guia3 = guia_completa2.with_name("La_pedrera.txt")

print(guia3)

# Para obtener la carpeta padre del archivo, se puede usar parent una vez, o varias veces para subir más niveles
print(guia3.parent)


# Para obtener todos los archivos en diferentes carpetas, se puede usar glob
guiaFinal = Path(base,"Documents","Cursos_Udemy",Path("Python_Total","Seccion6_Dia6_PROGRAMA_UN_RECETARIO","ejercicios","Europa"))

print("\n Inspeccionando archivos en la carpeta con ciclo for: \n")

for archivo in guiaFinal.glob("*.txt"):
    print(archivo)

print("\n Inspeccionando archivos en las subcarpetas con ciclo for: \n")

for archivo in guiaFinal.glob("**/*.txt"):
    print(archivo)


# Ejemplo de uso de relative_to para obtener la ruta relativa entre dos objetos path
ruta1 = Path("/home/usuario/Documentos/Curso_Python")
ruta2 = Path("/home/usuario/Documentos/Curso_Python/Seccion6_Dia6_PROGRAMA_UN_RECETARIO/ejercicios/Europa/Barcelona/Sagrada_Familia.txt")
ruta_relativa = ruta2.relative_to(ruta1)
print("\n Ruta relativa entre ruta1 y ruta2: \n")
print(ruta_relativa)



