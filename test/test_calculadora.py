from pytest import mark
from test import calculadora as calc

@mark.ui
def test_suma():
    resultado = calc.suma(4,6)
    assert resultado == 10

@mark.ui
def test_suma2():
    assert calc.suma(-3,-2) == -5

def test_resta():
    assert calc.resta(5,1) == 4

def test_multiplicacion():
    assert calc.multiplicacion(4,6) == 24

def test_division():
    assert calc.division(100, 10 ) == 10

def test_potenciacion():
    assert calc.potencia(3,2) == 9