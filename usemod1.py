# from pkg.pkg import module
# find (using sys.path) projectone/misc and load john.py from it
from projectone.db.oracle.general.gis.misc import john


# creates module object named 'john'
# find john.py and execute it
# put contents in a namespace 'john'
def spam():
    print("I am the other spam!")

john.spam()
john.toast()
print(john.ANIMALS[0])
b = john.Blurf()
spam()
# john._ham()