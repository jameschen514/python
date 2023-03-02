
print("Pastrami has ran out.")

sandwich_orders = ["Turkey", "Pastrami", "Roast Beef", "Pastrami", "Meat Ball", "Pastrami"]

index = 0

while index < len(sandwich_orders):
    if sandwich_orders[index] == "Pastrami":
        sandwich_orders.pop(index)
    else:
        index += 1

print(sandwich_orders)

finished_sandwiches = []

index = 0

while index < len(sandwich_orders):
    print("I made you a {} sandwich".format(sandwich_orders[index]))
    finished_sandwiches.append(sandwich_orders[index])
    print("{} is made.".format(sandwich_orders[index]))
    index += 1

print(sandwich_orders)