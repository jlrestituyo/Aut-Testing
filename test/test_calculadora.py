from pytest import mark
from test import calculadora as calc
import requests
from test import excel_util as eu

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

@mark.data
def test_read_data_from_excel():
    file_path = "./data/data.xlsx"
    sheet_name = "test1"
    data = eu.get_data(file = file_path , sheet = sheet_name)
    print("\n\n")
    print("DATA: ", data[0])


    if data[1] == "Librerias de Python":
        eu.write_data_to_excel(file_path, sheet_name, 2,3, "PASS")
    else:
        eu.write_data_to_excel(file_path, sheet_name, 2, 3, "FAILED")

