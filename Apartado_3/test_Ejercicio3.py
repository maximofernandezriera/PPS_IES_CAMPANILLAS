'''
Crea una suite de tests mediante UnitTest que comprueben las 2 funciones que has desarrollado en el ejercicio 3 del libro de Jon Vadillo. 
Procura que los tests unitarios cubran lo mejor posible la aparición de comportamientos no deseados. 
Incluye los ficheros del código y un snapshot que muestre la ejecución correcta de los mismos.

'''

import unittest
from Ejercicio3 import *

# Debemos crear una clase que hereda de la clase TestCase
class ejecicio3Test(unittest.TestCase):

    lista = [6,14,11,3,2,1,15,19]

    # setUp se ejecuta siempre antes de ejecutar cada test
    def setUp(self):
        print("Empezando Test...")
    
    # tearDown se ejecuta siempre al finalizar cada test
    def tearDown(self):
        print("Test Ejecutado ...")
    
    # Cada test debe empezar por la palabra test_
    def test_estaEnRango_entrynumber(self):

        self.assertTrue(estaEnRango(5))
        self.assertFalse(estaEnRango(21))
        self.assertEqual(estaEnRango(3), True)        
    
    def test_estaEnRango_negative(self):
        
        self.assertFalse(estaEnRango(-1))

    def test_estaEnLista_entrynumber(self):

        self.assertTrue(estaEnLista(1,lista))
        self.assertFalse(estaEnLista(5,lista))
        self.assertEqual(estaEnLista(19,lista), True)

    def test_estaEnLista_negative(self):

        self.assertFalse(estaEnLista(-1,lista))

    def test_estaEnRango_isNotInt(self):
        
        self.assertFalse(estaEnRango("h"))
        self.assertFalse(estaEnRango("4i"))
    
    def test_estaEnLista_isNotInt(self):
        
        self.assertFalse(estaEnLista("hola_mundo",lista))
        self.assertFalse(estaEnLista("4i",lista))

# Llamamos a main para que se ejecute el Runner.
if __name__ == '__main__':
    unittest.main()