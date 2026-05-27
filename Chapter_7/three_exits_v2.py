# 7.6 Three exits 

# Version 2 using conditional test in while statement

prompt = "\nEnter a pizza topping :"
prompt += "\n Enter 'quit' to end the program"

topping = ""
while topping != 'quit':
    topping = input(prompt)
    
    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")

