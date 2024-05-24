import pytest
from stat_funcs import StatsN2

@pytest.mark.parametrize("lista, esperado", [
    ([4, 3, 5, 7], "Distribuição positiva"),
    ([7, 5, 3, 4], "Distribuição negativa"),
    ([4, 4, 4, 4], "Distribuição normal")
])

def test_skew_esperado(lista, esperado):
    resultado = StatsN2.skew(lista)
    assert resultado == esperado

def test_skew_positiva():
    resultado = StatsN2.skew([4, 3, 5, 7])
    assert resultado == "Distribuição positiva"

def test_skew_negativa():
    resultado = StatsN2.skew([7, 5, 3, 4])
    assert resultado == "Distribuição negativa"

def test_skew_zero():
    resultado = StatsN2.skew([4, 4, 4, 4])
    assert resultado == "Distribuição normal"

@pytest.mark.xfail
def test_skew_negativa_fail():
    resultado = StatsN2.skew([7, 5, 3, 4])
    assert resultado == "Distribuição negativa"
