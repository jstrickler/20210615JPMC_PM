from collections import Counter

food_counts = {}
with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()
        if food not in food_counts:
            food_counts[food] = 0

        food_counts[food] += 1

for food, count in food_counts.items():
    print(food, count)

with open('DATA/breakfast.txt') as breakfast_in:
    foods = (line.rstrip() for line in breakfast_in)    # GENERATOR!
    # foods = [line.rstrip() for line in breakfast_in]  # LIST!

    counts = Counter(foods)
    print(counts.most_common())



