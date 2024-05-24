from stat_funcs import StatsN2
import pytest

@pytest.fixture()
def fixture_unimodal(request):
    return StatsN2.unimodal([1, 2, 3, 3, 4])
@pytest.fixture()
def fixture_multimodal(request):
    return StatsN2.multimodal([1, 2, 2, 3, 3, 4, 4, 4])

def test_unimodal(fixture_unimodal):
    assert fixture_unimodal == 3

def test_multimodal(fixture_multimodal):
    assert fixture_multimodal == [4]





