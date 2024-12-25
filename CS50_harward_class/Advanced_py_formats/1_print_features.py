a, b = 3.333333, 40000000
print(f"a is: {a:.2f}, b is: {b:,}")

#To assign while printing, use a feature from python 3.8 onwards
s = 1
print(s:= 2)
print(s)

#returning the exact string object back:
a = "hello\n"
f"{a!r}"
#uses an f-string with the !r conversion flag, which calls repr() on the variable a. It outputs the string representation of a that can be used to recreate the object, including quotes for strings.
print(1, f"{a!r}")