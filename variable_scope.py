
animal = 'wombat'  # global

def spam():
#    global animal  #  naughty naughty programmer! no biscuit!!
    animal = "koala"  # local
    print("animal:", animal)
    country = 'Burkina Faso' # local

spam()
print("animal:", animal)
