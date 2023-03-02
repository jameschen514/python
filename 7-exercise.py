
gas = input("What type of gas do you need? (regular, plus, or premium) ").strip()

amount = float(input("How many gallons do you need? "))

regular = 2.25
plus = 2.50
premium = 2.75

lower = gas.lower()

if lower == "regular":
    cost = regular * amount
    print("Regular gas would cost: {}".format(cost))
elif lower == "plus":
    cost = plus * amount
    print("Regular gas would cost: {}".format(cost))
elif lower == "premium":
    cost = premium * amount
    print("Premium gas would cost: {}".format(premium * amount))
else:
    print("You've entered an invalid gas type.")