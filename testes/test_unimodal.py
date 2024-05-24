import pytest
from stat_funcs import StatsN2

def test_unimodal():
    resultado = StatsN2.unimodal([4,2, 2, 9, 10])
    assert resultado == 2

def test_nao_unimodal():
    resultado = StatsN2.unimodal([4, 2, 2, 9, 10, 9])
    assert resultado == "Não é unimodal"

@pytest.mark.parametrize("lista, esperado", [
    ([4, 2, 2, 9, 10], 2),
    ([4, 2, 2, 9, 10, 9], "Não é unimodal")
])
def test_unimodal_esperado(lista, esperado):
    resultado = StatsN2.unimodal(lista)
    assert resultado == esperado

@pytest.mark.xfail
def test_unimodal_sem_lista_fail():
    resultado = StatsN2.unimodal(None)
    assert resultado == "Não é unimodal"