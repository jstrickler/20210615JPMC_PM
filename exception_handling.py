
try:
    with open("wombat.txt") as wombat_in:
        pass
except FileNotFoundError as err:
    print(err)
except PermissionError as err:
    print(err)

values = 0, 2, 8.6, 0, 9, 4.3

for v in values:
    try:
        result = 10 / v
    except ZeroDivisionError as err:
        print(err)
        exit()
    else:
        print(result)
    finally:
        # pass  no-op
        print("FINALLY!")






