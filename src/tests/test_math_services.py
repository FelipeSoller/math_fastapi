import pytest
from src.app.services.math_services import NumbersService

def test_sum():
    service = NumbersService()
    result = service.sum([1, 2, 3])
    assert result == 6

def test_average():
    service = NumbersService()
    result = service.average([2, 4, 6])
    assert result == 4

def test_average_empty_list():
    service = NumbersService()
    with pytest.raises(ValueError, match="A lista de números não pode estar vazia"):
        service.average([])
