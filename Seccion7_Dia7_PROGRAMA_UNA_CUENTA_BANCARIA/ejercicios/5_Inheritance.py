# Para cumplir con la filosofia DRY en programación (Don't Repeat Yourself) se hace uso la herencia
# de características en las clases, así una clase Animal más general, podría tener atributos y 
# métodos para clases relacionadas más particulares, como Conejo o Gato

class Animal:
    def nacer(self):
        print('Este animal ha nacido...')

class Pajaro(Animal):
    pass

piolin = Pajaro()

piolin.nacer()

# -------------------------------------------------------------------------------------------------

class Planta:

    def __init__(self,altura,color):
        self.altura = altura
        self.color = color

    def crecer(self):
        print('La planta está creciendo...')

class Rosa(Planta):
    pass

mi_rosa = Rosa(27,'roja')

mi_rosa.crecer()

print(mi_rosa.altura)
print(mi_rosa.color)

# -------------------------------------------------------------------------------------------------

