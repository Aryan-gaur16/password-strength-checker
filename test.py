import pytest
from app import app
from checker import check_password_strength

# ---- UNIT TESTS ----
# these tests test the checker module directly (unit testing)

# test that a short password is weak
def test_weak_password_unit():
    result = check_password_strength("abc")
    assert result['strength'] == 'Weak'

# test that a password with upper, lower and numbers is medium
def test_medium_password_unit():
    result = check_password_strength("Hello123")
    assert result['strength'] == 'Medium'

# test that a password with everything is strong
def test_strong_password_unit():
    result = check_password_strength("Hello123!")
    assert result['strength'] == 'Strong'

# test that score is between 0 and 5
def test_score_range():
    result = check_password_strength("Hello123!")
    assert 0 <= result['score'] <= 5

# test that feedback is a list
def test_feedback_is_list():
    result = check_password_strength("abc")
    assert isinstance(result['feedback'], list)

# test that a weak password gives feedback
def test_weak_password_has_feedback():
    result = check_password_strength("abc")
    assert len(result['feedback']) > 0

# test that a strong password has no feedback
def test_strong_password_no_feedback():
    result = check_password_strength("Hello123!")
    assert len(result['feedback']) == 0

# test that password is returned in result
def test_password_in_result():
    result = check_password_strength("Hello123!")
    assert result['password'] == "Hello123!"


# ---- INTEGRATION TESTS ----
# these tests test the full api including checker module together

# set up the test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# test the home route works
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

# test the health route works
def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200

# test a weak password through the full api
def test_weak_password_api(client):
    response = client.post('/check', json={"password": "abc"})
    data = response.get_json()
    assert response.status_code == 200
    assert data['strength'] == 'Weak'

# test a medium password through the full api
def test_medium_password_api(client):
    response = client.post('/check', json={"password": "Hello123"})
    data = response.get_json()
    assert response.status_code == 200
    assert data['strength'] == 'Medium'

# test a strong password through the full api
def test_strong_password_api(client):
    response = client.post('/check', json={"password": "Hello123!"})
    data = response.get_json()
    assert response.status_code == 200
    assert data['strength'] == 'Strong'

# test when no password is provided
def test_no_password(client):
    response = client.post('/check', json={})
    assert response.status_code == 400

# test when empty password is sent
def test_empty_password(client):
    response = client.post('/check', json={"password": ""})
    data = response.get_json()
    assert response.status_code == 200
    assert data['strength'] == 'Weak'