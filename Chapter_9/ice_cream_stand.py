# 9.6 Ice Cream Stand

class Restaurant:
    """A simple restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


# Ice cream stand class
class IceCreamStand(Restaurant):
    """Represents an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        # Attribute for flavors
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Butter"]

    def display_flavors(self):
        print("Ice Cream Flavors:")
        for flavor in self.flavors:
            print("-", flavor)


# instance
ice_cream_shop = IceCreamStand("BrainFreeze", "Ice Cream")

# Call methods
ice_cream_shop.describe_restaurant()
ice_cream_shop.display_flavors()
