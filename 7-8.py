sandwich_orders = ["Turkey", "Roast Beef", "Meat Ball"]

finished_sandwiches = []

index = 0

while index < len(sandwich_orders):
    print("I made you a {} sandwich".format(sandwich_orders[index]))
    finished_sandwiches.append(sandwich_orders[index])
    print("{} is made.".format(sandwich_orders[index]))
    index += 1