# 7.9 No Pastrami

sandwich_orders = [ "pastrami", "new yorker", "clubhouse", "pastrami", "subway melt", "urban melt", "pastrami", "turkey stack"]
finished_sandwiches = []

message = "Out of pastrami"
print(message)

# Removing all pastrami sandwiches from orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Continue making the other orders and sending them to finished
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"A {current_sandwich} is ready")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been ordered today :")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches)

