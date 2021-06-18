d1 = dict()  # empty dict
# d = dict(other_dict)

things = [1, 2, 3]  # literal list
things = list()  # list constructor
things = []  # empty literal list

d2 = {}  # empty literal dict

state_capitals = {'TX': 'Austin', 'NC': 'Raleigh', 'IL': 'Springfield',
      'NY': 'Albany'}

print(state_capitals['TX'])
print(state_capitals.get('CA'))
print(state_capitals.get('CA', 0))

state_capitals['VA'] = 'Richmond'
state_capitals['NJ'] = 'Trenton'

print(state_capitals)

x = state_capitals.setdefault('CA', 'Sacramento')
print(x)
print(state_capitals)

print(state_capitals.setdefault('NC', 'Durham'))

for state, capital in state_capitals.items():
    print(state, capital)

del state_capitals['NJ']
print(state_capitals)
print()

state_capitals['TX'] = 'Dallas'
print(state_capitals)

more_capitals = {'MA': 'Boston', 'NV': 'Carson City', 'NM': 'Albuquerque',
                 'NC': 'Charlotte'}

state_capitals.update(more_capitals)
print(state_capitals)

print(state_capitals.keys(), '\n')
print(state_capitals.values(), '\n')






