x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

x = 10
z = lambda a: a * x
print(z(5))

lst = [('1', 1), ('3', 3), ('2', 2), ('4', 4)]

lst.sort(key=lambda x: x[1])
print(lst)