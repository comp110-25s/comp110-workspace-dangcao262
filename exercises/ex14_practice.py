a: int = 0
b: int = a
b += 1
print(f"a is {a}")
print(f"b is {b}")

c: list[int] = [b, 4]
d: list[int] = c

d.append(13)

print(c)
