from main import get_temperature
from unittest import mock
import pytest

temperaturas = [(60, 15)]


@pytest.mark.parametrize('faren, celsius', temperaturas)
def test_get_temperature_by_lat_lng(faren, celsius):
    moc_patch = 'main.get_temperature'

    with mock.patch(moc_patch) as mp:
        mp.temprature.return_value = celsius
        resultado = get_temperature(64.1405435, -21.951502)

    print(celsius)
    print(resultado)

    assert resultado == celsius
