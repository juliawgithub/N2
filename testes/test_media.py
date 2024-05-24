import pytest
from stat_funcs import StatsN2

def test_media():
    resultado = StatsN2.media([4, 2])
    assert resultado == 2

def test_media_sem_lista():
    resultado = StatsN2.media(None)
    assert resultado == 0

@pytest.mark.parametrize("lista, resultado_esperado", [
    ([4, 2], 3),
    ([10, 20, 30], 20)
])

def test_media_esperado(lista, resultado_esperado):
    resultado = StatsN2.media(lista)
    assert resultado == resultado_esperado

@pytest.mark.xfail
def test_media_fail():
    resultado = StatsN2.media([4, 2])
    assert resultado == 2

