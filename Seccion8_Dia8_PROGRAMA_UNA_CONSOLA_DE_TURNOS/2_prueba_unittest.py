# Biblioteca incorporada con Python (a diferencia de la biblioteca externa Pylint)

import unittest
import cambia_texto_paraUnittest

# Heredando todos los métodos de testeo de unittest
class ProbarCambiaTexto(unittest.TestCase):

    # Es necesario nombar a los casos de prueba con test al inicio como en test_nombre
    def test_mayusculas(self):
        palabra = 'Buen día'
        resultado = cambia_texto_paraUnittest.todo_mayusculas(palabra)
        self.assertEqual(resultado,'BUEN DÍA')

# Ya que python no maneja un main global como otros lenguajes
if __name__ == '__main__':
    unittest.main()