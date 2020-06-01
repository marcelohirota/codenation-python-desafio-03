import pytest
from main import get_temperature
from unittest.mock import patch


# Values to be used on test

parametrized_values = [
    (-14.235004, -51.92528, 62, 16)
]

# Parameters that are going to be used

params = 'lat, lng, temperature, expected'

# Testing temperature by location


@patch('main.requests.get')
@pytest.mark.parametrize(params, parametrized_values)
def test_get_temperature_by_lat_lng(mock_requests, lat, lng, temperature, expected):

    temp = {'currently': {'temperature': temperature}}

    mock_requests.return_value.json.return_value = temp

    result = get_temperature(lat, lng)

    assert result == expected
