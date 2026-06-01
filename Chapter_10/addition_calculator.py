# 10-7. Addition Calculator

while True:
    number1 = input("Enter the first number (or 'quit' to quit): ")

    if number1.lower() == "quit":
        break

    number2 = input("Enter the second number (or 'quit' to quit): ")

    if number2.lower() == "quit":
        break

    try:
        total = int(number1) + int(number2)
        print(f"The total is {total}.")
    except ValueError:
        print("Please enter valid numbers.")

# I had some problems with this one because i didn't see that i put
# try in the wrong "slot/position" so i sat here for 30 minutes struggling.

# NOTE TO SELF, WORDS MIGHT BE RIGHT, BUT IN THE WRONG PLACE!
