# 9.11 Imported Admin

class Users:
    """A simple user model"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)

    def greet_user(self):
        print(f"Your name is {self.first_name} {self.last_name}.")


# Create instances
user1 = Users("Joavi", "Amaya")


class Admin(Users):
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


admin = Admin("Ida", "Einarsen")