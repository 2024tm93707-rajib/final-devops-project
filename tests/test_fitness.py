import pytest
from app.services.fitness_service import calculate_bmi

def test_bmi_valid():
    assert calculate_bmi(70, 1.75) == 22.86

def test_bmi_zero_height():
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)
