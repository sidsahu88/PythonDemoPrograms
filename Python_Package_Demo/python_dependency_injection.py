from typing import Protocol

# Define a protocol for User Repository for dependency injection
class UserRepo(Protocol):
    def get_user(self, user_id) -> dict:
        ...

class UserRepository(UserRepo):
    def get_user(self, user_id):
        return {"user_id": user_id, "name": "John Doe"}

class MockUserRepository(UserRepo):
    def get_user(self, user_id):
        return {"user_id": user_id, "name": "Mock User"}
    
class UserService:
    def __init__(self, user_repository: UserRepo):
        self.user_repository = user_repository
    
    def get_user_details(self, user_id):
        return self.user_repository.get_user(user_id)
    

if __name__ == "__main__":
    user_repo = UserRepository()
    user_service = UserService(user_repo)
    print(user_service.get_user_details(1))

    mock_user_repo = MockUserRepository()
    mock_user_service = UserService(mock_user_repo)
    print(mock_user_service.get_user_details(2))