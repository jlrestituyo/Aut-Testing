from pytest import mark
from test import calculadora as calc
import requests

@mark.ui
def test_suma():
    resultado = calc.suma(4,6)
    assert resultado == 10

@mark.parametrize("num1", [3,5,6,9])
@mark.parametrize("num2", [1,3,4,5])

@mark.suma
def test_suma2(num1, num2):
    resultado_esperado = num1 + num2
    assert calc.suma(num1, num2) == resultado_esperado


def test_resta():
    assert calc.resta(5,1) == 4

def test_multiplicacion():
    assert calc.multiplicacion(4,6) == 24

def test_division():
    assert calc.division(100, 10 ) == 10

def test_potenciacion():
    assert calc.potencia(3,2) == 9

@mark.api
def test_provincias():
    url = "http://provinciasrd.raydelto.org/provincias/5"
    response = requests.get(url).json()
    claves = response.keys()
    assert 1 == 1
