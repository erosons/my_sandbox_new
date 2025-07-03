# test_user_service_integration.py
import pytest
import sqlite3
from integration_user_service import AuthService, UserRepository

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('test_user', 'test_password')")
    connection.commit()
    yield connection
    connection.close()

def test_authenticate(db_connection):
    repo = UserRepository(db_connection)
    service = AuthService(repo)
    
    assert service.authenticate("test_user", "test_password") == True
    assert service.authenticate("test_user", "wrong_password") == False
    assert service.authenticate("unknown_user", "any_password") == False
