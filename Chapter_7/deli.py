# 7.8 Deli

sandwich_orders = ["new yorker", "clubhouse", "subway melt", "urban melt", "turkey stack"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"A {current_sandwich} is ready")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been ordered today :")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches)



