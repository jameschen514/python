
person = ''
age = '0'
active = True

while active == True:
    age = input("How old are they? ").strip()
    age = age.lower()

    if not age or age == 'quit':
        active = False
        break
    else:
        age = int(age)

    if age <= 3:
        print("Ticket is free")
    elif age >= 3 and age < 12:
        print("Ticket is: $10")
    elif age >= 12:
        print("Ticket is: $15")
    else:
        print("Invalid age is entered.")
        active = False
