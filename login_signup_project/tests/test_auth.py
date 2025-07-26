# tests/test_auth.py

import unittest
from app.auth import AuthSystem

class TestAuthSystem(unittest.TestCase):
    def setUp(self):
        self.auth = AuthSystem()

    def test_signup_success(self):
        result = self.auth.signup("alice", "password123")
        self.assertEqual(result, "Signup successful")

    def test_signup_user_exists(self):
        self.auth.signup("bob", "securepass")
        result = self.auth.signup("bob", "newpass")
        self.assertEqual(result, "User already exists")

    def test_signup_short_password(self):
        result = self.auth.signup("charlie", "123")
        self.assertEqual(result, "Password too short")

    def test_login_success(self):
        self.auth.signup("david", "mypassword")
        result = self.auth.login("david", "mypassword")
        self.assertEqual(result, "Login successful")

    def test_login_user_not_found(self):
        result = self.auth.login("eve", "doesntmatter")
        self.assertEqual(result, "User not found")

    def test_login_wrong_password(self):
        self.auth.signup("frank", "correctpass")
        result = self.auth.login("frank", "wrongpass")
        self.assertEqual(result, "Incorrect password")

if __name__ == "__main__":
    unittest.main()
