
x = [5, 10, 2, 99, 4]
print(len(x), min(x), max(x), sum(x))
print(sorted(x))

print(reversed(x))
x.insert(3, 7)
x.append(8)

for i in reversed(x):
    print(i, end=' ')
print('\n')
print("x is still:", x)


rnums = reversed(x)
print(rnums)
for num in rnums:
    print(num)

cities = ['Plano', 'Seattle', 'Houston', 'Durham']
states = ['TX', 'WA', 'TX', 'NC']
places = zip(cities, states)
print(places)
print(list(places))
print(list(places), '\n')

# not pythonic:
# for i in range(len(cities)):
#     print(i, cities[i])
for i, city in enumerate(cities):
    print(i, city)
print()

print(list(enumerate(cities)))

enum_cities = enumerate(cities)
for i, city in enum_cities:
    print(i, city)
print()

location = '123 Elm St.', 'Madison', 'Wisconsin'
for i, field in enumerate(location):
    print(i, field)
data = list(enumerate(location))
print(data)

a = "moo"
b = "cow"
print(a + b)

a = ['m', 'o', 'o']
b = ['c', 'o', 'w']
print(a + b)

print("woo" * 5)
print(['True'] * 5)
print((1.2, 3.4) * 5)
print(['a', 'b', 'c'] * 3)
print((1.2,) * 5)
print((1.2) * 5)