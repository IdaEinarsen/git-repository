# 3.10 Every Function

animals = ['cat', 'dog', 'bird', 'chicken', 'goat', 'fish']
message = f"My favorite animal is {animals[1]}."
print(animals)
print(animals[1].title())
print(message)
# Created a list of animals and made a message of my favorite animal

print(animals)
animals[4] = 'cow'
print(animals)
# I Changed animal 4 in index from goat to cow

animals.append('goat')
animals.append('horse')
print(animals)
animals.insert(4, 'frog')
print(animals)
# I added goat,horse by using append and i added frog in index 4 using insert

print(animals)
del animals[3]
print(animals)
# I deleted animal 3 in index using del

popped_animals = animals.pop()
print(animals)
print(popped_animals)
# I popped out horse from the list and also printed what i popped out 

print(animals)
animals.remove('bird')
print(animals)
# i removed bird from the list using .remove

print(sorted(animals))
print(animals)

animals.reverse()
print(animals)
animals.reverse()
print(animals)

animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)
# I sorted and reversed the list using sorted(), .sort, reverse= and .reverse

print(f"I think i used all functions while making this list with {len(animals)} animals.")

# 3.11 Intentional Error
# I tried to get an error in exercise 3.9 by trying to pull a index number that didn't exist
# and got error : IndexError: list index out of range
