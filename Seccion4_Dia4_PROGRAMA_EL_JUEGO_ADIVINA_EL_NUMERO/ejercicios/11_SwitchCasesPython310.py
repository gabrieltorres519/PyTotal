serie = "Toradora"

match serie:
    case "Game of Thrones":
        print("Winter is coming")
    case "Breaking Bad":
        print("I am the one who knocks")
    case "Stranger Things":
        print("Friends don't lie")
    case _:
        print("Unknown series")

# Pero python da más posibilidades que un simple switch, 
# también podemos usarlo para comparar con varias opciones a la vez:

cliente = {
    "nombre": "Juan",
    "edad": 30,
    "ocupacion": "Ingeniero"
}

pelicula = {
    "titulo": "Inception",
    "ficha_tecnica": {
        "protagonista": "Leonardo DiCaprio",
        "director": "Christopher Nolan",
    }
}

elementos = [cliente, pelicula, 'libro', 7]

for e in elementos:
    match e:
        case {"nombre": nombre, "edad": edad, "ocupacion": ocupacion}:
            print(f"Es una persona: {nombre}, {edad} años, {ocupacion}")
        case {"titulo": titulo, "ficha_tecnica": {"protagonista": protagonista, "director": director}}:
            print(f"Es una película: {titulo}, Protagonista: {protagonista}, Director: {director}")
        case _:
            print("Elemento desconocido")
