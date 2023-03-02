person1 = { "name" : "James", "fav_number" : 2}
person2 = { "name" : "John", "fav_number" : 4}
person3 = { "name" : "Stan", "fav_number" : 6}
person4 = { "name" : "Jackey", "fav_number" : 8}
person5 = { "name" : "Bucket", "fav_number" : 10}

people = { "people" : [person1, person2, person3, person4, person5]}

index = 0

for person in people["people"][index]["name"]:
    print("Name {}\t\tFavorite number: {}".format(people["people"][index]["name"], people["people"][index]["fav_number"]))
    index = index + 1

indexj = 0

for key, value in people["people"][0].items():
    print("{} {}".format(key, value))
    indexj = indexj + 1
