sandwich_orders = ["turkey", "pastrami", "roast beef", "pastrami", "meat ball", "pastrami"]

finished_sandwiches = []

print("I'm sorry we're all out of pastrami today")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print()

print(sandwich_orders)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your {} sandwich.".format(current_sandwich))
    finished_sandwiches.append(current_sandwich)

print()

for sandwich in finished_sandwiches:
    print("I made a {} sandwich".format(sandwich))