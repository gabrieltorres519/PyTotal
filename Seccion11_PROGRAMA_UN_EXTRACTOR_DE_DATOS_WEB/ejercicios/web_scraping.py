import requests
import bs4


resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

soup = bs4.BeautifulSoup(resultado.text, 'html.parser')

print(len(soup.select('title')))
print(soup.select('title'))
print(soup.select('title')[0])
print(soup.select('title')[0].getText())
print(soup.select('p'))

parrafo_especial = soup.select('p')#[0].getText()
print('Resultado')
print(parrafo_especial)


resultado2  = requests.get("https://escueladirecta-blog.blogspot.com/2023/04/usa-python-para-modelar-simular-y.html")

soup2 = bs4.BeautifulSoup(resultado2.text, 'html.parser')

print('Resultado 2')
print(soup2.select('p')[3])

resultado3 = requests.get('https://escueladirecta-blog.blogspot.com/2024/07/copia-o-referencia.html')

soup3 = bs4.BeautifulSoup(resultado3.text, 'html.parser')

columna_lateral = soup3.select('.sidebar-container h3 a')  # Extraer de la class "sidebar-container" los elementos h3 y luego los elementos 'a' dentro de esos h3
                                                           # el '.' es el operador para indicar que es una clase, el espacio indica que se busca dentro de esa clase, 
                                                           # el h3 indica que se buscan los elementos h3 dentro de esa clase y luego el espacio y el 'a' indica que 
                                                           # se buscan los elementos 'a' dentro de esos h3
print('Resultado  3')
print(columna_lateral[2])



columna_lateral2 = soup3.select('.sidebar-container h3')

print('Resultado 3 - 2')

for h in columna_lateral2:
    print('\n')
    print(h)
    print('\n')

# Para, en lugar de por class, buscar por id, se utiliza el operador '#' en lugar del operador '.'


resultado4 = requests.get('https://escueladirecta-blog.blogspot.com/')

soup4 = bs4.BeautifulSoup(resultado4.text, 'html.parser')

# imagenes = soup4.select('.snippet-thumbnail-container')

imagenes = soup4.select('img')

print('Resultado 4')
print(len(imagenes)) #  Un elemento específico sería imagenes[0]['src']
for i in imagenes:
    print('\n')
    print(i['src']) 

img = imagenes[0]['src']

imagenExtraida = requests.get(img)

print(imagenExtraida.content)

f = open('imagenExtraida.jpg', 'wb') # 'wb' es el modo de escritura en binario, necesario para escribir archivos de imagen
f.write(imagenExtraida.content)
f.close()