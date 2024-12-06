import pytest
from unittest.mock import Mock
import requests

# Mocked server URL
BASE_URL = "http://127.0.0.1:8000/users"

def test_users_api_unauthorized(mocker):
    """
    Test the /users endpoint with invalid credentials and expect a 401 response with an empty text body.
    """
    # Mock the requests.get method
    mock_get = mocker.patch("requests.get")
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    mock_get.return_value = mock_response

    # Send a GET request
    response = requests.get(BASE_URL, params={"username": "admin", "password": "admin"})

    # Assertions
    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response body, got {response.text.strip()}"

def test_users_api_success(mocker):
    """
    Test the /users endpoint with valid credentials and expect a 200 response with an empty text body.
    """
    # Mock the requests.get method
    mock_get = mocker.patch("requests.get")
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    mock_get.return_value = mock_response

    # Send a GET request
    response = requests.get(BASE_URL, params={"username": "admin", "password": "qwert"})

    # Assertions
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response body, got {response.text.strip()}"
