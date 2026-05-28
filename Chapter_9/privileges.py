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

class Privileges:

    def __init__(self):
        self.privileges = [
            "can delete post",
            "can ban user",
            "can add post"
        ]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print("_", privilege)
    


class Admin(Users):
    """Admin configuration"""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.privileges = Privileges()



admin = Admin("Ida", "Einarsen")

# Admin instance
admin = Admin("Ida", "Einarsen")

# Show admin info
admin.describe_user()

# Show privileges
admin.privileges.show_privileges()