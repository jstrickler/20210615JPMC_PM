x = 5   # create int obj with value 5, and *bind* 'x' to it
y = 10  # create int obj and bind to 'y'
result = x + y  # create int obj and bind to 'result'

a = 10   # 'a' refers to (is bound to) int obj
b = a    # 'b' refers to same object as 'a'
print(a, id(a), b, id(b))
a = 123  # create new int obj and bind 'a'
print(a, b)
print(a, id(a), b, id(b))

c = 10
c = 5.9
d = c
c = "cole slaw"

# int c = new int(10);

#  a-z A-Z 0-9 _

# local variables, functions: lower_case_words
# global variables: UPPER_CASE_WORDS
# classes: UpperCamelCase

m = None   # like null (more or less)

current_class = "Python Intro"
while_whatever = 12

print(type(m), type(x), type(a))

blood_type = "B negative";

print(blood_type)

print(type(m), type(x), type(a))

d = "100"
e = 123
# print(d + e)
print(d + str(e))
print(int(d) + e)

# str() int() float() bool()
# dict() list() tuple() set()







