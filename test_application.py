import pytest
from Application import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    # Check that home page loads some expected text (adjust to match index.html)
    assert b'Welcome' in response.data or b'Index' in response.data

def test_register_get(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert b'Register' in response.data

def test_register_post_valid(client):
    response = client.post('/register', data={'name': 'Chetan', 'email': 'Chetan@gmail.com'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Chetan' in response.data
    assert b'Chetan@gmail.com' in response.data

def test_register_post_invalid(client):
    response = client.post('/register', data={'name': '', 'email': ''})
    assert response.status_code == 200
    assert b'Please Enter name and email.' in response.data

def test_list_members(client):
    # Ensure members page loads
    response = client.get('/members')
    assert response.status_code == 200
    assert b'Members' in response.data
