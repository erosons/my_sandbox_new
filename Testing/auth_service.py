"""
Component testing focuses on testing a group of related
functionalities or a class in isolation, but it might involve
more than one function or method. It tests a component as a whole,
usually with its own internal dependencies mocked or stubbed.
Scenario: Testing a class that performs user authentication by verifying credentials.
The class interacts with a user repository but the repository’s behavior is simulated for the test.
"""

# auth_service.py
class UserRepository:
    def get_user(self, username):
        raise NotImplementedError

class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authenticate(self, username, password):
        user = self.user_repository.get_user(username)
        return user and user["password"] == password
