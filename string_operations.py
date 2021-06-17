actor = "Chris Hemsworth"

print(len(actor))
print(actor.upper())
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
print("Still:", actor)
x = 12321 + 12323523
print(x)
print(len(str(x)))
#  s.islower() s.isupper() s.isalpha() etc etc
#  s.startswith('....')  s.endswith('....')
#  '...' in s
print(actor.find('ems'))

#  \s+
s = "  Here he comes to      save    the    day!   "
print(s.split())

rec = "foo;bar;blah;baz"

print(rec.split(';'))

line = "Twas brillig and the slithy toves\n"
print(line.rstrip())

s = "    \t \t   kookaburra      \n"
print("|" + s.strip() + "|")
print()

s = "qaummmmmaquuuuuuaaaqThe kumquat hagen-daazmuaqqqqqqqmmmmm"
#                   ['u', 'm', 'q', 'a']
print("|" + s.lstrip("umqa") + "|")
print("|" + s.rstrip("umqa") + "|")
print("|" + s.strip("umqa") + "|")

line = "Twas brillig and the slithy toves\n"
print(line.rstrip("\r\n"))

print(s.replace('hag', ''))

s = "Missississississippi"
print(s.replace('iss', 'X', 1))




