import requests
import bs4


# Multiples páginas
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# for i in range(1, 51):
#     print(url_base.format(i))

resultado = requests.get(url_base.format(1))
soup = bs4.BeautifulSoup(resultado.text, 'html.parser')

print(len(soup.select('.product_pod'))) #  Extrae los elementos con la clase 'product_pod' que contienen la información de cada libro    

libros = soup.select('.product_pod')

ejemplo_libro = libros[0].select('a')[1]['title'] # Extrae el elemento 'a' dentro del elemento 'h3' que contiene el título del libro
print(ejemplo_libro)





#  Condiciones de extracción [solo titulos de libros con 4 o más estrellas]

titulos_rating_alto  = []

    # Iterar páginas
for pagina in range(1, 51):

    # Crear soup en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    soup =  bs4.BeautifulSoup(resultado.text, 'html.parser')

    # Seleccionar datos de los libros
    libros = soup.select('.product_pod')

    # iterar en los libros

    for libro in libros:
        
        # Verificar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            
            # Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # Agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)


    # Ver los libros encontrados

for t in titulos_rating_alto:
    print(t)
