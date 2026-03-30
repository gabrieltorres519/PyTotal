# Las clases que se definen sin constructor ni parámetros son las más simples 
# almomento de crear instancias de las mismas (instanciarlas o crear objetos de la clase)  

class Personaje:
    pass

harry_potter = Personaje()

print(harry_potter)
print(type(harry_potter))

class Dinosaurio:
    pass

velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio = Dinosaurio()
print(velociraptor)
print(tiranosaurio_rex)
print(braquiosaurio)


class PlataformaStreaming:
    pass

netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()