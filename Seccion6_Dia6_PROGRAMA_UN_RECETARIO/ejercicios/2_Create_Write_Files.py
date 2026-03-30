#archivo = open('prueba.txt','r') # Con r solo se lee el archivo, con w el archivo se reescribe completamente, con a continua 
                                # al final de lo que el archivo ya tiene escrito

# Existen diferentes métodos para escribir los archivos 
archivo = open('prueba1.txt','w') # Escribir o resetear archivo
archivo.write("""Hola mundo
aquí estoy
cerando el texto\n""")

archivo.writelines(['Hola', 'mundo', 'aquí', 'estoy']) # Se envia una lista y se escribe todo el texto sin espacios

lista = ['Hola', 'mundo', 'aquí', 'estoy']

for palabra in lista:
    archivo.writelines(palabra + '\n')

archivo.close()

# Escribir en el archivo sin actualizarlo por completo, solo el texto nuevo

archivo_aux = open('prueba1.txt','a')

archivo_aux.write('Linea sin afectar lo escrito anteriormente en el archivo')

archivo_aux.close()