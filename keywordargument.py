def printer(**kwargs):
	print(kwargs["key"])

printer(key=1234)

def printtuple(*args):
	print(args)

printtuple(3,4,2,"hello", "high five")