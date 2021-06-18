
mary_in = open('DATA/mary.txt')
# work with file
mary_in.close()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:  # mary_in.readline() read 1 line
        line = raw_line.rstrip() # remove \n \t \r ' ' \b
        print(line)
    # mary_in.__exit__() -> mary_in.close()
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    entire_file = mary_in.read()  # read file into string
    print("RAW:")
    print(repr(entire_file))
    print("COOKED:")
    print(entire_file)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)

with open('DATA/alice.txt') as alice_in:
    count = 0
    for line in alice_in:
        if 'alice' in line.lower():
            count += 1
print(f"{count} lines contained 'alice'")

with open('DATA/alice.txt', "r") as alice_in:
    all_alice = alice_in.read()
    count = all_alice.lower().count('alice')
    print(f"{count} occurrances of 'alice'")

# modes:
# "r"  read
# "w"  write
# "a"  append
# "x"  exclusive
with open('DATA/words.txt') as words_in:
    with open('qwords.txt', 'w') as words_out:
        for line in words_in:
            if 'q' in line:
                words_out.write(line)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit)

