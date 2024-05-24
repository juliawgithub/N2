import pytest
from stat_funcs import StatsN2

def test_multimodal():
    resultado = StatsN2.amodal([4, 3, 5, 7])
    assert resultado == "Não existe moda"

def test_nao_multimodal():
    resultado = StatsN2.amodal([4, 2, 9, 9])
    assert resultado == "Existe moda"

@pytest.mark.parametrize("lista, resultado_esperado", [
    ([4, 2, 9, 10], "Não existe moda"),
    ([4, 2, 9, 9], "Existe moda"),
    ([1, 2, 3, 4], "Existe moda")
])

def test_amodal_esperado(lista, resultado_esperado):
    resultado = StatsN2.amodal(lista)
    assert resultado == resultado_esperado

@pytest.mark.xfail
def test_amodal_fail():
    resultado = StatsN2.amodal([4, 2, 9, 10])
    assert resultado == "Existe moda"