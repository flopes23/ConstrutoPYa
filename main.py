import pytest

def print_hi(name):

    print(f'Holla, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def somar (num1, num2):
    return num1 + num2

def subtrair (num1, num2):
    return num1 - num2

def multiplicar (num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Divisao por zero'

# definicao dos testes unitarios

#teste funcao soma
def test_somar():

    # 1 - configura / prepara
    num1 = 8 #in
    num2 = 5 #in
    resultado_espeerado = 13 #out
    # 2 - executa
    resultado_atual = somar(num1, num2)
    #3 - Valida
    assert resultado_atual == resultado_espeerado


def test_soma_compact():
    assert somar(8, 3) == 11


def test_subitrai_compact():
    assert subtrair(8 , 3) == 5


if __name__ == '__main__':
    print_hi('ZeDasCove')

    resultado = somar(5,5)
    print(f'Resultado soma: {resultado}')

    resultado = subtrair(10,5)
    print(f'Resultado subtracao: {resultado}')

    resultado = multiplicar(2,4)
    print(f'Resultado multiplicacao: {resultado}')

    resultado = dividir (10,0)
    print(f'Resultado divisao: {resultado}')

