# 4.10 Slices
type_pizza = ['hawaii', 'hakis', 'kebab', 'vesuvio', 'romeo', 'margarita', 'chicago', 'milano','alfungi']
print("The first three items in the list are:")
for pizza in type_pizza[:3]:
    print(pizza.title())
print("Three items from the middle of the list are:")
for pizza in type_pizza[3:6]:
    print(pizza.title())
print("The last three items in the list are:")
for pizza in type_pizza[6:]:
    print(pizza.title())

# I used the 4.1 program and added some type of pizza and then used print
# to print the three first, three in middle and three last pizza types
