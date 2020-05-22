from main import get_temperature
import requests
import pytest

# Testando a conexão com a API (status 200 para conexão feita)


def test_valid_connection():
    lat = -14.235004
    lng = -51.92528
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)
    response = requests.get(url)
    assert response.status_code == 200


def test_get_temperature_by_lat_lng():
    pass
