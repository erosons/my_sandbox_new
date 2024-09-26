# test_auth_service.py
import pytest
from auth_service import AuthService

class MockUserRepository:
    def get_user(self, username):
        if username == "valid_user":
            return {"username": "valid_user", "password": "correct_password"}
        return None

def test_authenticate():
    mock_repo = MockUserRepository()
    auth_service = AuthService(mock_repo)
    
    assert auth_service.authenticate("valid_user", "correct_password") == True
    assert auth_service.authenticate("valid_user", "wrong_password") == False
    assert auth_service.authenticate("unknown_user", "any_password") == False
