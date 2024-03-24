def verificar_senha_segura(senha):
    if len(senha) < 8:
        return False
    
    if not any(c.isupper() for c in senha):
        return False
    
    if not any(c.islower() for c in senha):
        return False
    
    caracteres_especiais = "!@#$%^&*()-_+=[]{}|;:,.<>?/~"
    if not any(c in caracteres_especiais for c in senha):
        return False
    
    return True


import pytest
from verificador_senha import verificar_senha_segura

def test_senha_curta():
    assert not verificar_senha_segura("Abcd1!")

def test_senha_sem_maiuscula():
    assert not verificar_senha_segura("abcdefgh1!")

def test_senha_sem_minuscula():
    assert not verificar_senha_segura("ABCDEFGH1!")

def test_senha_sem_especial():
    assert not verificar_senha_segura("Abcdefgh1")

def test_senha_segura():
    assert verificar_senha_segura("SenhaSegura123!")

