import pytest
from app.src.app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Todo List' in response.data
