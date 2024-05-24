import pytest
from stat_funcs import StatsN2

def test_dpadrao():
    resultado = StatsN2.dpadrao([4, 3, 5, 7])
    assert resultado == 1.713

@pytest.mark.parametrize("lista, resultado_esperado", [
    ([4, 3, 5, 7], 1.713),
    ([10, 20, 30, 40], 12.909),
    ([2, 4, 6, 8, 10], 2.828)
])
def test_dpadrao_esperado(lista, resultado_esperado):
    resultado = StatsN2.dpadrao(lista)
    assert resultado == resultado_esperado

@pytest.mark.xfail
def test_dpadrao_fail():
    resultado = StatsN2.dpadrao(4)
    assert resultado == 2

