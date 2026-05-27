# 8.12 Sandwiches

def make_sandwich(*toppings):
    """Print a summary of the sandwich toppings orderd."""
    print("\nMaking a sandwich with the following toppings:")
    
    for topping in toppings:
        print(f"- {topping}")



make_sandwich("ham", "cheese")

make_sandwich("turkey", "lettuce", "tomato", "mayo")

make_sandwich("cheese", "ham", "tomato", "red onion", "garlic sauce")
