
import re

def validar_telefone(numero):
    padrao = r'^\([1-9]{2}\) [2-9][0-9]{3,4}-[0-9]{4}$'

    if re.match(padrao, numero):
        return True
    else:
        return False

from validar_telefone import validar_telefone

def test_validar_telefone_valido():
    assert validar_telefone("(11) 91234-5678") == True
    assert validar_telefone("(99) 98765-4321") == True
    assert validar_telefone("(21) 1234-5678") == True


def test_validar_telefone_invalido():
    assert validar_telefone("(11) 1234-5678") == False  # Número sem o nono dígito
    assert validar_telefone("(12) 123456789") == False  # Número sem hífen
    assert validar_telefone("(99) 12345-6789") == False  # DDD inválido
    assert validar_telefone("(11) 1234-567") == False  # Número incompleto
