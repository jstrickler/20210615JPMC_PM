list1 = list()

#  [1, 2, 3]

cities = ["Plano", "Sacramento", "Schaumberg", "Durham"]

print(cities)

print(cities[0], cities[2])
cities.append("Las Vegas")
cities.append("Des Moines")
print(cities)
cities.insert(0, "Trenton")
cities.insert(5, "Houston")
print(cities)
cities[2] = "San Francisco"
print(cities)
print(len(cities))

more_cities = ["Dallas", "New York", "Boston"]

cities.extend(more_cities)  # add objects individually
print(cities)

# L.append(obj) L.insert(pos, obj) L.extend(iterable_of_objects)

del cities[3]  # completely remove 4th element
print(cities)

c = cities.pop(4)
print("popped:", c)
print(cities)
cities.insert(1, c)
print(cities)
cities.pop(8)
print(cities)
c = cities.pop()
print("popped:", c)
print(cities)

cities.insert(0, cities.pop(1))
print(cities)
cities.insert(1, cities.pop(2))
print(cities)

cities.remove('Trenton')
print(cities)

food = ["spam", "spam", "spam", "spam", "spam",
        "spam", "spam", "spam", "spam", 'eggs', "spam"]

print(food.count('spam'), food.count('eggs'))

# del L[pos]  L.pop(pos) L.pop()  L.remove(value)
print(cities)
print(cities[0])
print(cities[-1])
print(cities[len(cities)-1])

food.remove('spam')
print(food)

food.remove('spam')
print(food)

print(cities[-2])

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

#  [start:stop]
print(fruits[0:3])
print(fruits[7:10])
print(fruits[:5])  # first 5
print(fruits[-4:])  # last 4

founder = "Guido Van Rossum"
print(founder[6:9])
print(founder[:5])
#  "Guido Van Rossum"
print(founder[-6:-2])
print(founder[len(founder)-6:len(founder)-2])
print(founder[10:14])

print(founder[-6:])
print(founder[6:])

value = "-1234"
print(value[1:])

print(founder[22:99])
print()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

for fruit in fruits:
    # fruit = next(fruits)
    print(fruit.upper())
print()

for city in cities:
    if city.startswith('D'):
        print(city)
print()

data = [
    ['Durham', 'Raleigh', 'Chapel Hill'],
    ['Los Angeles', 'Oxnard', 'Oakland', 'Sacramento'],
    ['Albany', 'New York', 'Ossining'],
]

for sublist in data:
    print("==>")
    for city in sublist:
        print(city)




