numbers = []

for number in range(1, 11):
	result = number ** 3 
	numbers.append(result)
	print(result)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)