import pytest
from stat_funcs import StatsN2

def test_mediana():
    resultado = StatsN2.mediana([4,2, 8, 9, 10])
    assert resultado == 2

def test_mediana_sem_lista():
    resultado = StatsN2.mediana(None)
    assert resultado == 0

def test_mediana_resto_0():
    resultado = StatsN2.mediana([4,2,6,2])
    assert resultado == 2

def test_mediana_resto_diferente_de_0():
    resultado = StatsN2.mediana([7.5,7.5,7.5,7.5])
    assert resultado == 7.5

@pytest.mark.parametrize("lista, resultado_esperado", [
    ([4, 2, 8, 9, 10], 8),
    ([4, 2, 6, 2], 2),
    ([5.5, 5.5, 5.5, 5.5], 5.5)
])

def test_mediana_esperado(lista, resultado_esperado):
    resultado = StatsN2.mediana(lista)
    assert resultado == resultado_esperado

@pytest.mark.xfail
def test_mediana_fail():
    resultado = StatsN2.mediana([4, 2, 8, 9, 10])
    assert resultado == 2