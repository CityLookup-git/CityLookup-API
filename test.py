import pytest
import json
import os

# Constants for mock setup
TEST_DATASET_FOLDER = 'datasets'
TEST_GEOJSON_FILE = os.path.join(TEST_DATASET_FOLDER, 'test.geojson')
# OpenAddresses dataset structure
TEST_GEOJSON_CONTENT = {
    "type": "Feature",
    "properties": {
        "hash": "testhash",
        "number": "1",
        "street": "Test Street",
        "unit": "",
        "city": "Test",
        "district": "",
        "region": "TST",
        "postcode": "0000",
        "id": ""
    },
    "geometry": {
        "type": "Point",
        "coordinates": [0.0, 0.0]
    }
}

@pytest.fixture(scope='module')
def app():
    # Set up: create mock dataset
    with open(TEST_GEOJSON_FILE, 'w') as file:
        json.dump(TEST_GEOJSON_CONTENT, file)

    # App loads data on run/import to make sure it is ready before executing anything else
    # That is why it is imported here instead of the beginning of this file
    from app import app as flask_app

    app = flask_app
    app.config['TESTING'] = True
    yield app

    # Teardown: remove mock dataset
    os.remove(TEST_GEOJSON_FILE)

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_street_names_success(client):
    """Test the /get_street_names endpoint with a valid city parameter."""

    # Using city 'Test' from mock dataset
    response = client.get('/get_street_names?city=test')
    data = response.get_json()

    assert response.status_code == 200
    assert 'streets' in data
    assert isinstance(data['streets'], list)  # Streets should be a list

def test_get_street_names_error(client):
    """Test the /get_street_names endpoint with no city parameter."""
    
    response = client.get('/get_street_names')
    data = response.get_json()

    assert response.status_code == 400
    assert 'error' in data
    assert data['error'] == 'City parameter is required'