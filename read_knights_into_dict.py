from pprint import pprint
knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line  = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        # knight_data.setdefault(name, (title, color, quest, comment))
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

for name, data in sorted(knight_data.items()):
    print(data[0], name)

print(knight_data['Bedevere'][2])
