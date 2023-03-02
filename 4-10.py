numbers = []

for number in range(1, 11):
	result = number ** 3 
	numbers.append(result)
	print(result)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)

#**********************************
# 4-10
# James Chen

print(cubes[0:3])

print(cubes[5:8])

print(cubes[-3:])

