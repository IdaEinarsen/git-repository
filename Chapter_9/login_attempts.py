# 9.5 Login Attempts

class User:
    """A simple user model"""

# Attributes 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0   #Default V

    def describe_user(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Instance
user1 = User("John", "Smith")

# Increment login attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print login attempts
print("Login attempts:", user1.login_attempts)

# Reset attempts
user1.reset_login_attempts()


print("Login attempts after reset:", user1.login_attempts)

