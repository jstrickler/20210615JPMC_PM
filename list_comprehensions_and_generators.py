fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    if f.startswith('p'):
        f0.append(f.upper())
print("f0:", f0, '\n')

#  [EXPR for VAR in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
suits = 'Clubs Diamonds Hearts Spades'.split()
print(ranks)
print(suits)
from collections import namedtuple
import random
Card = namedtuple("Card", "rank suit")

cards = [Card(rank, suit) for suit in suits for rank in ranks]
random.shuffle(cards)
print(cards, '\n')
f0 = []
for f in fruits:
    f0.append(f.upper())

#     expr      loop    iterable
f1 = [f.upper() for f in fruits if f.startswith('p') if len(f) > 8]
print("f1:", f1, '\n')

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

last_names = [p[1] for p in people if p[-1] > '1970']
print("last_names:", last_names, '\n')

full_names = [f"{p[0]} {p[1]}" for p in people]
print("full_names:", full_names, '\n')

full_name_gen = (f"{p[0]} {p[1]}" for p in people)
print(full_name_gen)
for full_name in full_name_gen:
    print(full_name)
print("Round 2:")
for full_name in full_name_gen:
    print(full_name)