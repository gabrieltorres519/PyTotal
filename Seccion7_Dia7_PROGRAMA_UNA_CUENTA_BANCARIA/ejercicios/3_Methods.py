class Pajaro:
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    # Métodos de la clase
    def piar(self): # Self (obligatorio) hace referencia acada instancia o cada objeto de esa clase
        print('Pio')

    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')

piolin = Pajaro('amarillo','canario')

piolin.volar(50)
piolin.piar()