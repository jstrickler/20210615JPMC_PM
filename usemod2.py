# 1. find john.py and execute (functions are now in memory)
# 2. copy spam and toast to current global namespace
from projectone.db.oracle.general.gis.misc import john


# 1. create 'john' object as namespace for contents of john.py

def spam():
    print("I am not the spam() you think I am")

spam()
john.spam()
# toast()


#  from mymod import thing1, thing2, ...
# OR
#  import mymod
#  mymod.thing1 ...

import sys
for path in sys.path:
    print(path)

