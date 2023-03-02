pizzas = ["Extra Cheese", "Pepparoni", "Cillion"]

for pi in pizzas:
	print("{} yum good".format(pi))

print("Pizza is really good.  It's so good that so good doesn't justify it.")


#*****************************************
# 4-11
# James Chen

friend_pizzas = pizzas

pizzas.append("Hawaiian")

friend_pizzas.append("Buffalo")

#for pizza in pizzas:
#	print("My favorite pizza are {}".format(pizza))

for pizza in pizzas:
	print("My favorite pizzas are {}".format(pizza))

for friend_pizza in friend_pizzas:
	print("My favorite pizzas are {}".format(friend_pizza))
#print("{}".format(pizza))