import pytest
from stat_funcs import StatsN2

def test_media_ponderada():
    resultado = StatsN2.media_ponderada([2, 3, 2, 3])
    assert resultado == 2

def test_media_ponderada_sem_lista():
    resultado = StatsN2.media_ponderada(None)
    assert resultado == 0

@pytest.mark.xfail
def test_media_ponderada_fail():
    resultado = StatsN2.media_ponderada([2, 3, 2, 3])
    assert resultado == 2

@pytest.mark.parametrize("lista, pesos, resultado_esperado", [
    ([2, 3, 2, 3], None, 2),
    ([1, 2, 3], [1, 2, 3], 2.333)
])

def test_media_ponderada_esperada(lista, pesos, resultado_esperado):
    resultado = StatsN2.media_ponderada(lista, pesos)
    assert resultado == resultado_esperado