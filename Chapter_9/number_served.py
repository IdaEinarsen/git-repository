# 9.4 Number Served

class Restaurant:
    """A simple restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant("Pizza Palace", "Italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


restaurant.describe_restaurant()
restaurant.open_restaurant()

# Print the number of customers served.
print("Customers served:", restaurant.number_served)

# Change the value to 25
restaurant.number_served = 25


print("Customers served:", restaurant.number_served)

