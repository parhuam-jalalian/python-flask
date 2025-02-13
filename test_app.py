import pytest
from app import app, generate_html, greet

def test_generate_html():
    message = "Test Message"
    html = generate_html(message)
    assert message in html
    assert "Version Number: 0001" in html
    assert "<html>" in html
    assert "</html>" in html

def test_greet():
    assert greet() == "Welcome to CI/CD"

def test_hello_world():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert "Welcome to CI/CD" in response.data.decode()
