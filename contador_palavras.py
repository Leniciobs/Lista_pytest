import re

def contar_palavras(texto):
    texto_sem_pontuacao = re.sub(r'[^\w\s]', '', texto) 
    palavras = texto_sem_pontuacao.split()
    return len(palavras)

import pytest
from contador_palavras import contar_palavras

def test_contar_palavras_texto_vazio():
    assert contar_palavras("") == 0

def test_contar_palavras_um():
    assert contar_palavras("palavra") == 1

def test_contar_palavras_muitas():
    assert contar_palavras("Este é um exemplo de texto com várias palavras.") == 7

def test_contar_palavras_com_espacos():
    assert contar_palavras("    Olá     mundo!    ") == 2

def test_contar_palavras_muitas():
    assert contar_palavras("Este é um exemplo de texto com várias palavras.") == 9
