from collections import namedtuple

old_person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

print(old_person[0], old_person[1], len(old_person))
print(old_person)

t = 1, 2, 3
tt = 1, 2
ttt = 1,

Person = namedtuple("Person", "first_name last_name product dob")

person = Person('Bill', 'Gates', 'Microsoft', '1955-10-24')
print(person.first_name, person.last_name)

print(person)
print(person[0], person[-1])

# ITERABLE -- can be iterated over with 'for' loop
first_name, last_name, product, dob = old_person  # UNPACKING


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for first_name, last_name, product, dob in people:
    print(first_name, last_name)
print()

for person in people:
    print(person[0], person[1])
print()

data = [('red', 3), ('purple', 6), ('brown', 1), ('purple', 2),
        ('blue', 5)]

for color, number in data:
    print(color * number)
print()

