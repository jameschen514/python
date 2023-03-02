
person = ''
age = '0'

while age != '':
    age = input("How old are they? ").strip()

    if not age:
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

"""

prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished."

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    
    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

"""