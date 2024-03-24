def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero")
    return a / b

import pytest
from calculadora import adicao, subtracao, multiplicacao, divisao

def interface_calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada: ")

    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida!")
        return

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '4' and num2 == 0:
        print("Erro: Divisão por zero!")
        return

    if escolha == '1':
        resultado = adicao(num1, num2)
    elif escolha == '2':
        resultado = subtracao(num1, num2)
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
    elif escolha == '4':
        resultado = divisao(num1, num2)

    print("Resultado:", resultado)

if __name__ == "__main__":
    interface_calculadora()
