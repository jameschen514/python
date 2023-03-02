
toppings = []
topping = ''

while topping != 'quit':
    topping = input("What kind of topping would you like? ")
    toppings.append(topping)
    print("{} is added to your pizza.".format(topping))

toppings.pop()
print(toppings)
