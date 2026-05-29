
from user_module import User 

class Admin(User):
    """Admin configuration"""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.privileges = [
            "can delete post",
            "can ban user",
            "can add post"
        ]

    def describe_admin(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)

    def display_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print("_", privilege)