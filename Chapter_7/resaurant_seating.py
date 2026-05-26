# 7.2 Restaurant Seating

guests = input("How many people are in you're dinner group?: ")
guests = int(guests)

if guests >= 7: 
    print("\n You have to wait for a table.")
else:
    print("\n You're table is ready.")