from django.contrib.auth.models import User
from django.test import Client

def test_registration():
    client = Client()
    response = client.post('/signup/', {'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200

    # Check if user is created
    assert User.objects.filter(username='testuser').exists()

def test_login():
    client = Client()
    response = client.post('/login/', {'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200

    # Check if user is authenticated
    assert '_auth_user_id' in client.session
