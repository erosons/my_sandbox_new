# user_service.py
import sqlite3

class UserRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_user(self, username):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT username, password FROM users WHERE username=?", (username,))
        row = cursor.fetchone()
        return {"username": row[0], "password": row[1]} if row else None

class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authenticate(self, username, password):
        user = self.user_repository.get_user(username)
        return user and user["password"] == password
