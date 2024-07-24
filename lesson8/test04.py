A = {"a", "b", "c"}
B = {"f", "d", "a"}

X = A.difference(B)
print(X)

Y = A - B
print(Y)

X = B.difference(A)
print(X)

Y = B - A
print(Y)
