import pytest
from stat_funcs import StatsN2

def test_variancia():
    resultado = StatsN2.variancia([4,2, 9, 10])
    assert resultado == 10.8125

@pytest.mark.parametrize("lista, resultado_esperado", [
    ([4, 2, 9, 10], 10.8125),
    ([1, 2, 3, 4], 1.25),
    ([10, 20, 30, 40], 125.0)
])

def test_variancia_esperado(lista, resultado_esperado):
    resultado = StatsN2.variancia(lista)
    assert resultado == resultado_esperado

@pytest.mark.xfail
def test_variancia_fail():
    resultado = StatsN2.variancia([4, 2, 9, 10])
    assert resultado == 5