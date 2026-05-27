# 7.6 Three exits 

# Version 3 using active variable

prompt = "\nEnter a topping for your pizza:"
prompt += "\n Enter 'quit' to end program"

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")