locations = ["New York", "New Jersey", "Pennsylvania", "Delaware", "Virginia"]
print(locations)


print(sorted(locations))
"""
def sorted(lst, **kwargs):
	current_lst = lst
	if kwargs["reverse"] == True:
		current_lst.sort(reverse=True)
	else:
		current_lst.sort()
	print(current_lst)
	
sorted(locations, reverse=True)
"""
print(sorted(locations, reverse=True))