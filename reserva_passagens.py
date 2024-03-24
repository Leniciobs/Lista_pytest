class Voo:
    def __init__(self, numero_voo, origem, destino, data, hora, assentos_disponiveis):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.data = data
        self.hora = hora
        self.assentos_disponiveis = assentos_disponiveis

class Reserva:
    def __init__(self, numero_voo, nome_passageiro, assento):
        self.numero_voo = numero_voo
        self.nome_passageiro = nome_passageiro
        self.assento = assento

class SistemaReservas:
    def __init__(self):
        self.voos = []
        self.reservas = []

    def adicionar_voo(self, voo):
        self.voos.append(voo)

    def fazer_reserva(self, numero_voo, nome_passageiro, assento):
        for voo in self.voos:
            if voo.numero_voo == numero_voo and voo.assentos_disponiveis > 0:
                self.reservas.append(Reserva(numero_voo, nome_passageiro, assento))
                voo.assentos_disponiveis -= 1
                return True
        return False

    def cancelar_reserva(self, numero_voo, nome_passageiro):
        for reserva in self.reservas:
            if reserva.numero_voo == numero_voo and reserva.nome_passageiro == nome_passageiro:
                self.reservas.remove(reserva)
                for voo in self.voos:
                    if voo.numero_voo == numero_voo:
                        voo.assentos_disponiveis += 1
                return True
        return False

# test_sistema_reservas.py

import pytest
from reserva_passagens import Voo, Reserva, SistemaReservas

@pytest.fixture
def sistema_reservas():
    return SistemaReservas()

def test_adicionar_voo(sistema_reservas):
    voo = Voo(numero_voo="001", origem="Aeroporto A", destino="Aeroporto B", data="2024-12-01", hora="08:00", assentos_disponiveis=100)
    sistema_reservas.adicionar_voo(voo)
    assert len(sistema_reservas.voos) == 1

def test_fazer_reserva_sucesso(sistema_reservas):
    voo = Voo(numero_voo="001", origem="Aeroporto A", destino="Aeroporto B", data="2024-12-01", hora="08:00", assentos_disponiveis=100)
    sistema_reservas.adicionar_voo(voo)
    assert sistema_reservas.fazer_reserva(numero_voo="001", nome_passageiro="João", assento="A1") == True
    assert len(sistema_reservas.reservas) == 1
    assert sistema_reservas.voos[0].assentos_disponiveis == 99

def test_fazer_reserva_falha(sistema_reservas):
    assert sistema_reservas.fazer_reserva(numero_voo="001", nome_passageiro="João", assento="A1") == False

def test_cancelar_reserva_sucesso(sistema_reservas):
    voo = Voo(numero_voo="001", origem="Aeroporto A", destino="Aeroporto B", data="2024-12-01", hora="08:00", assentos_disponiveis=100)
    sistema_reservas.adicionar_voo(voo)
    sistema_reservas.fazer_reserva(numero_voo="001", nome_passageiro="João", assento="A1")
    assert sistema_reservas.cancelar_reserva(numero_voo="001", nome_passageiro="João") == True
    assert len(sistema_reservas.reservas) == 0
    assert sistema_reservas.voos[0].assentos_disponiveis == 100

def test_cancelar_reserva_falha(sistema_reservas):
    assert sistema_reservas.cancelar_reserva(numero_voo="001", nome_passageiro="João") == False
