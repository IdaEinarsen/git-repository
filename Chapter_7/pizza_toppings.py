# 7.4 Pizza Toppings

prompt = "Enter a pizza topping (enter 'quit' to finish): "

while True:
    topping = input(prompt)

    if topping.lower() == "quit":
        break
    else:
        print(f"I'll add {topping} to your pizza.")