# 4.11 My pizzas, Your Pizzas
type_pizzas = ['hawaii', 'hakis', 'kebab', 'vesuvio']
friend_pizzas = ['hawaii', 'hakis', 'kebab', 'vesuvio']
print(type_pizzas)
print(friend_pizzas)
type_pizzas.append('chicago')
friend_pizzas.append('alfungi')
print (type_pizzas)
print(friend_pizzas)

print("My favorite pizzas are:")
for pizza in type_pizzas:
    print(pizza.title())

print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
# I added chicago to my list and al fungi to my friends list and 
# then printed each list with a line saying favorite pizzas.


