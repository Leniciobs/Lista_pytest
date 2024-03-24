# diferenca_datas.py
from datetime import datetime

def diferenca_entre_datas(data1, data2, unidade_tempo):
    formato_data = '%Y-%m-%d'
    formato_data_hora = '%Y-%m-%d %H:%M:%S'

    if ' ' in data1:
        formato_data = formato_data_hora
    if ' ' in data2:
        formato_data = formato_data_hora

    data1 = datetime.strptime(data1, formato_data)
    data2 = datetime.strptime(data2, formato_data)

    diferenca = data2 - data1

    if unidade_tempo == 'dias':
        return diferenca.days
    elif unidade_tempo == 'meses':
        meses = (data2.year - data1.year) * 12 + data2.month - data1.month
        return meses
    elif unidade_tempo == 'anos':
        anos = data2.year - data1.year
        return anos
    elif unidade_tempo == 'horas':
        return diferenca.days * 24 + diferenca.seconds // 3600
    elif unidade_tempo == 'minutos':
        return diferenca.days * 24 * 60 + diferenca.seconds // 60
    else:
        raise ValueError("Unidade de tempo inválida. Por favor, escolha entre 'dias', 'meses', 'anos', 'horas' ou 'minutos'.")


# test_diferenca_datas.py
import pytest
from diferenca_datas import diferenca_entre_datas

def test_diferenca_datas_dias():
    assert diferenca_entre_datas('2024-03-20', '2024-03-24', 'dias') == 4

def test_diferenca_datas_meses():
    assert diferenca_entre_datas('2024-01-01', '2024-04-01', 'meses') == 3

def test_diferenca_datas_anos():
    assert diferenca_entre_datas('2020-01-01', '2024-01-01', 'anos') == 4

def test_diferenca_datas_horas():
    assert diferenca_entre_datas('2024-03-24 10:00:00', '2024-03-24 14:30:00', 'horas') == 4

def test_diferenca_datas_minutos():
    assert diferenca_entre_datas('2024-03-24 10:00:00', '2024-03-24 14:30:00', 'minutos') == 270

if __name__ == "__main__":
    pytest.main()
