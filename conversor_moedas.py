def real_para_dolar(valor):
    taxa = 0.20
    return valor * taxa

def dolar_para_real(valor):
    taxa = 5.0
    return valor * taxa

def real_para_euro(valor):
    taxa = 0.18
    return valor * taxa

def euro_para_real(valor):
    taxa = 5.43
    return valor * taxa

def interface_conversor_moedas():
    print("Selecione a conversão de moeda:")
    print("1. Real para Dólar")
    print("2. Dólar para Real")
    print("3. Real para Euro")
    print("4. Euro para Real")

    escolha = input("Digite o número da conversão desejada: ")

    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida!")
        return

    valor = float(input("Digite o valor a ser convertido: "))

    if escolha == '1':
        resultado = real_para_dolar(valor)
        print("Resultado:", resultado)
    elif escolha == '2':
        resultado = dolar_para_real(valor)
        print("Resultado:", resultado)
    elif escolha == '3':
        resultado = real_para_euro(valor)
        print("Resultado:", resultado)
    elif escolha == '4':
        resultado = euro_para_real(valor)
        print("Resultado:", resultado)

if __name__ == "__main__":
    interface_conversor_moedas()

import pytest
from conversor_moedas import real_para_dolar, dolar_para_real, real_para_euro, euro_para_real

def test_real_para_dolar():
    assert real_para_dolar(100) == 20

def test_dolar_para_real():
    assert dolar_para_real(10) == 50

def test_real_para_euro():
    assert real_para_euro(100) == 18

def test_euro_para_real():
    assert euro_para_real(10) == 54.3
