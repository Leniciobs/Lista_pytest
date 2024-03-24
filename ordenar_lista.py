# ordenacao.py

def ordenar_crescente(lista):
    return sorted(lista)

def ordenar_decrescente(lista):
    return sorted(lista, reverse=True)

# test_ordenacao.py
import pytest
from ordenar_lista import ordenar_crescente, ordenar_decrescente

def test_ordenar_crescente():
    assert ordenar_crescente([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert ordenar_crescente([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ordenar_crescente([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]

def test_ordenar_decrescente():
    assert ordenar_decrescente([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [9, 6, 5, 5, 4, 3, 2, 1, 1]
    assert ordenar_decrescente([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert ordenar_decrescente([5, 2, 4, 6, 1, 3]) == [6, 5, 4, 3, 2, 1]
