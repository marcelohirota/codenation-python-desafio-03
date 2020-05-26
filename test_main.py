import pytest
import requests
from main import get_temperature
from unittest.mock import patch


# Values to be used on test

parametrized_values = [
    (-14.235004, -51.92528, 62, 16)
]

# Testing temperature by location


@pytest.mark.parametrize('lat, lng, temperature, expected', parametrized_values)
def test_get_temperature_by_lat_lng(lat, lng, temperature, expected):
    mock_get_patcher = patch('main.requests.get')

    temp = {'currently': {'temperature': temperature}}

    mock = mock_get_patcher.start()

    mock.return_value.json.return_value = temp

    result = get_temperature(lat, lng)

    mock_get_patcher.stop()

    assert result == expected

# Testing connection with API (code 200 for a valid connection)


def test_valid_connection():
    response = requests.get('https://api.darksky.net/v1/status.txt')

    assert response.status_code == 200
