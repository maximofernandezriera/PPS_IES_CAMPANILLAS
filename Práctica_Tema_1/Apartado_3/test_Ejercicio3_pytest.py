import pytest
from Ejercicio3 import *

lista = [6,14,11,3,2,1,15,19]

def test_estaEnRango_entrynumber():

    assert estaEnRango(5)
    assert estaEnRango(21) == True
    assert estaEnRango(3)     

def test_estaEnRango_negative():
        
    assert estaEnRango(-1) == False

def test_estaEnLista_entrynumber():

    assert estaEnLista(1,lista)
    assert estaEnLista(5,lista) == False
    assert estaEnLista(19,lista)
    assert estaEnLista(21,lista) == False

def test_estaEnLista_negative():

    assert estaEnLista(-1,lista) == False

def test_estaEnRango_isNotInt():
        
    assert estaEnRango("h") == False
    assert estaEnRango("4i") == False
    
def test_estaEnLista_isNotInt():
        
    assert estaEnLista("hola_mundo",lista) == False
    assert estaEnLista("4i",lista) == False
