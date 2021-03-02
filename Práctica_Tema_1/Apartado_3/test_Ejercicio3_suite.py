'''
Crea una suite de tests mediante UnitTest que comprueben las 2 funciones que has desarrollado en el ejercicio 3 del libro de Jon Vadillo. 
Procura que los tests unitarios cubran lo mejor posible la aparición de comportamientos no deseados. 
Incluye los ficheros del código y un snapshot que muestre la ejecución correcta de los mismos.

'''

import unittest
import test_Ejercicio3


def suite():
    suite = unittest.TestSuite()
    # Test de entrada de datos:

    suite.addTest(test_Ejercicio3.ejecicio3Test('test_estaEnRango_entrynumber'))
    suite.addTest(test_Ejercicio3.ejecicio3Test('test_estaEnLista_entrynumber'))

    # Test de entrada de datos negativos en la función estaEnLista:

    suite.addTest(test_Ejercicio3.ejecicio3Test('test_estaEnLista_negative'))

    # Test sobre entrada de datos tipo string:

    suite.addTest(test_Ejercicio3.ejecicio3Test('test_estaEnRango_isNotInt'))
    suite.addTest(test_Ejercicio3.ejecicio3Test('test_estaEnLista_isNotInt'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())