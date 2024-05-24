import pytest
from stat_funcs import StatsN2

def test_multimodal():
    resultado = StatsN2.multimodal([4,2, 2, 9, 9, 10])
    assert resultado == 2, 9

def test_nao_multimodal():
    resultado = StatsN2.multimodal([4, 2, 9, 10])
    assert resultado == "Não é multimodal"

@pytest.mark.parametrize("lista, resultado_esperado", [
    ([4, 2, 9, 10], "Não é multimodal"),
    ([1, 2, 3, 4], "Não é multimodal")
])

def test_multimodal_esperado(lista, resultado_esperado):
    resultado = StatsN2.multimodal(lista)
    assert resultado == resultado_esperado

@pytest.mark.xfail
def test_multimodal_fail():
    resultado = StatsN2.multimodal([4, 2, 2, 9, 9, 10])
    assert resultado == [2, 9]