from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if not password_confirmation:
            raise UserInputError("Password confirmation is required")
        
        if password_confirmation != password:
            raise UserInputError("Password and password confirmation do not match")
        
        valid_characters = "abcdefghijklmnopqrstuvwxyz"

        for char in username:
            if char not in valid_characters:
                raise UserInputError("Username must contain lowercase letters a-z")
        
        if len(username) < 3:
            raise UserInputError("Username must be at least 3 characters long")
        
        if self._user_repository.find_by_username(username):
            raise UserInputError("Given username already exists")
        
        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")

        has_letter = False
        has_number = False
        
        for char in password:
            if char in valid_characters:
                has_letter = True
            elif char.isdigit():
                has_number = True
            else:
                # Character is neither a lowercase letter nor a digit
                raise UserInputError("Password must consist of lowercase letters a-z and numbers 0-9")
            
            # Stop early if both conditions are met
            if has_letter and has_number:
                break
        
        # Final check if password meets both criteria
        if not has_letter or not has_number:
            raise UserInputError("Password must contain both letters (a-z) and numbers (0-9)")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


user_service = UserService()
