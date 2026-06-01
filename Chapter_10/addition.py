# 10.6 Addition

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

try:
    total = int(number1) + int(number2)
    print(f"The total is {total}.")
except ValueError:
    print("Please enter valid numbers.")

# Valid : Enter the first number: 5, Enter the second number: 12, The total is 17.

# ValueError: Enter the first number: banana, Enter the second number: 2, 
# Please enter valid numbers.