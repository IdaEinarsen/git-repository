# 9.2 Three Restaurants

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")

# Instances 

restaurant1 = Restaurant("Pizza Palace", "Italian")
restaurant2 = Restaurant("Sushi World", "Japanese")
restaurant3 = Restaurant("Taco Town", "Mexican")

# Call methods for restaurants

restaurant1.describe_restaurant()
restaurant1.open_restaurant()


restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()