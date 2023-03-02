
times = 3

number = []

while times < 4:
    resp = input("Enter a number: ").strip()
    print("Number is: {}".format(float(resp)))
    print("Number is squared: {}".format(float(resp)*float(resp)))
    print("Number is cube: {}".format(float(resp) * float(resp) * float(resp)))
    times += 1