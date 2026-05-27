# 7.6 Three Exits


# Version 1 using a break statement

prompt = "Enter you're mcdonalds order (enter 'quit' to finish): "

while True:
    topping = input(prompt)

    if topping.lower() == "quit":
        break
    else:
        print(f" {topping}, would you like anything else ? ")

