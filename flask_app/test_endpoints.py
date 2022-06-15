from flask_app import create_app

def test_if_user_is_not_logged(flask_app):
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 302

        
def test_if_a_list_of_endpoints_is_returning_200(flask_app):
    with flask_app.test_client() as test_client:
        endpoints_list = ['/register', '/login', '/monsters', '/home/builds', '/monsters/fatalis']
        for i in range(len(endpoints_list)):
            response = test_client.get(endpoints_list[i])
            assert response.status_code == 200
            
def test_register_user(flask_app):
    with flask_app.test_client() as test_client:
        data = {
            "email": "teste@pytest.com",
            "password": "testando092",
            "username": "pytest"
        }
        response = test_client.post('/register', json=data)
        assert response.status_code == 200