# app/auth.py

class AuthSystem:
    def __init__(self):
        self.users = {}  # username -> password

    def signup(self, username, password):
        if username in self.users:
            return "User already exists"
        if len(password) < 6:
            return "Password too short"
        self.users[username] = password
        return "Signup successful"

    def login(self, username, password):
        if username not in self.users:
            return "User not found"
        if self.users[username] != password:
            return "Incorrect password"
        return "Login successful"
