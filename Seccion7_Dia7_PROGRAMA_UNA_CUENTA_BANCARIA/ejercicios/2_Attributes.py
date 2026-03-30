class ClaseEjemplo:

    # Método constructor
    def __init__(self, mi_parametro):
        self.atributo = mi_parametro
    
mi_ClaseEjemplo = ClaseEjemplo('negro') # Siempre agregarlos parámetros requeridos en la definición de la clase

print(mi_ClaseEjemplo.atributo)

# palabra = 'hola'

# Lo  primero en llamarse después de instanciar un objeto
# es el constructor de la clase


class Pajaro:

    alas = True

    def __init__(self,color,especie):
        self.color =  color
        self.especie = especie


mi_pajaro = Pajaro('Negro','Tucan')

print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')

# 

print(Pajaro.alas)

print(mi_pajaro.alas)

