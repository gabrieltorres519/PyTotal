texto = input("Ingrese un texto: ")

arrayLetrasAbecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

aparicionesLetra = []

for letraAbecedario in arrayLetrasAbecedario:
    aparicionesLetra.append(texto.count(letraAbecedario))

palabrasTotales = len(texto.split())

primeryUltimaLetra = texto[0], texto[-1]

inversoTexto = texto[::-1]

textoPyEncontrado = "python" in texto.lower()

print("Cantidad de apariciones de cada letra del abecedario:")
for i in range(len(arrayLetrasAbecedario)):
    print(f"{arrayLetrasAbecedario[i]}: {aparicionesLetra[i]}")
print(f"Cantidad total de palabras: {palabrasTotales}")
print(f"Primera letra: {primeryUltimaLetra[0]}, Última letra: {primeryUltimaLetra[1]}")
print(f"Texto invertido: {inversoTexto}")
print(f"¿El texto contiene la palabra 'python'? {'Sí' if textoPyEncontrado else 'No'}")


# Los 10 errores más comunes en Python.
# https://claude.ai/public/artifacts/cf53286d-97e3-4662-8812-cae227b60b46

