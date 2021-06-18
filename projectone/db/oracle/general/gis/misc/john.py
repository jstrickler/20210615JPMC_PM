# pseudo-constant
ANIMALS = ['wombat', 'koala', 'quokka']

def main():
    spam()
    toast()

    x = 5
    x = x * 10
    print("x is", x)
    print("Hi Mom!")


class Blurf:
    pass

def spam(): # "public"
    print("Hello from spam()")

# pseudo-private
def _ham(): # "private"
    print("   ...and _ham()")

def toast():  # "public"
    print("Hello from toast()")
    _ham()


if __name__ == '__main__':
    main()