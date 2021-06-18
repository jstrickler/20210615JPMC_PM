c1 = ['red', 'mauve', 'purple', 'brown', 'black', 'pink', 'white']
c2 = ['blue', 'orange', 'purple', 'pink', 'pink', 'pink', 'green']

things = {'NJ', 'VA', 'VA', 'TX'}

s1 = set(c1)
s2 = set(c2)
s1.add('orange')
s2.add('ecru')
print("s1:", s1)
print("s2:", s2)

print("common:", s1 & s2)  # intersection
print("not common:", s1 ^ s2) # xor
print("both:", s1 | s2) # union
print("only in s1:", s1 - s2)
print("only in s2:", s2 - s1)

with open('DATA/breakfast.txt') as breakfast_in:
    foods = [line.rstrip() for line in breakfast_in]

print("all foods:", foods)
ufoods = set(foods)
print("unique foods:", ufoods)
