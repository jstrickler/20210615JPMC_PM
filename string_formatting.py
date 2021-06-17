a = "wombat"
b = "burrow"

print("The", a, "lives in the", b)  # 2.0+   manual formatting
print("The %s lives in the %s" % (a, b))  # 2.0+  legacy Python 2

print("The {} lives in the {}".format(a, b))  # 3.0+
print(f"The {a} lives in the {b}")  # 3.6+ (f-string)

c = 23.39023902
print(c)
print(f"{c:.1f}")
print("{:.3f}".format(c))
big_num = 420942848271107
print(f"{big_num:,d}")

#   {:d}  {:f}  {:.3f} {:5d} {:05d}
#  {:10.10s} {:>10s} {:^10s}
x = "antidisestablishmentarianism"
print(f"|{x:10.10s}|")
y = "wombat"
print(f"|{y:10s}|")
print(f"|{y:<10s}|")
print(f"|{y:^10s}|")
print(f"|{y:>10s}|")
