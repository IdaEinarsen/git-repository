# 8.13 User Profile

def build_profile(first, last, **user_info):
    """Build a dictionary about everthing we know about a user. """
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("Ida", "Einarsen",
                             location="Övertorneå",
                             field= "Application development",
                             age= 30)
print(user_profile)