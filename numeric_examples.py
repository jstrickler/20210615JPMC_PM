i1 = 10
i2 = 0b10
i3 = 0x10
i4 = 0o10  # 010

print(i1, i2, i3, i4)

x = 232095842035820395820395820385209385029835029385029835029835029835028935029835029835029835029835028350283502893502983509283509823059820359820395820983502983502983058203598253

print(x + 1)

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 0.42093020932032
print(f1, f2, f3, f4)
f5 = 1.23903e33
print(f5)
f6 = 1.49049034909488390282987301059193838283080813081380
print(f6)
print()

a = 23
b = 17
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)   # rounded to whole number (towards -inf)
print(a // -17)
print(a % b)
print(a ** b)
print(divmod(a, b))

a = "100"
b = "DeadBeef"

print(int(a) + 1)
print(int(b, 22) + 1)
print(int(a, 13))

print(int('abcdefghijklmnopqrstuvwxyz', 36))

m = 1_234_730_039

print(m)

a = 23
b = 7
print()

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # floored division
print(a % b)   # modulo (remainder)
print(a ** b)  # exponentiation
print()

x = 5
x *= 10
x += 25
x /= 3
print(x)

# not available:  ++ --

# PEMDAS

# int() float() str() bool() complex()

a = "123"
print(int(a) + 1)
b = "DeadBeef"
print(int(b, 16) + 1)














