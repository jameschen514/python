
#################################################################
#
#  James Chen
#  5-2 exercise
#
#################################################################

sports = 'foOtball'

if sports == 'football':
    print("Sport is {}".format(sports))
elif sports == 'fOotball':
    print("Sport is {}".format(sports))
elif sports.lower() == 'football':
    print("Sport is lowered {}".format(sports.lower()))
else:
    pass


fingers = 5

if fingers < 5:
    print("You have less than five fingers")
elif fingers > 1:
    print("You have more than one finger")
elif fingers == 5:
    print("You have five fingers")
else:
    pass

finger = 5

if finger > 0 and finger == 2:
    print("You have two fingers")
elif finger > 0 or finger < 3:
    print("You have more than 1 finger but less 3")
else:
    pass

items = ["strawberry", "pineapple", "banana"]

if "apple" in items:
    print("Apple is on the list")
elif "pear" in items:
    print("Pear is on the list")
elif "orange" not in items:
    print("Orange is not in the list")
else:
    print(items)




