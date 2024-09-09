class UserRepository:
    def __init__(self, database):
        self.database = database

    def add_user(self, user_id, user_name):
        if self.database.get(user_id):
            raise ValueError("User already exists")
        self.database.save(user_id, user_name)

    def get_user(self, user_id):
        return self.database.get(user_id)
