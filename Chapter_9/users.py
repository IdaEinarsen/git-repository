# 9.3 Users

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
user1 = Users("Ida", "Einarsen")
user2 = Users("Freddie", "Johnson")

# Call methods
user1.describe_user()
user1.greet_user()

# Space between user 1 and user 2 

print()

user2.describe_user()
user2.greet_user()
        