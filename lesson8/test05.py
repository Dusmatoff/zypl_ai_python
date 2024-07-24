l = (1, 2, 3, 4, 5)
A = {"a", "b", "c", "z", l}
B = {"f", "d", "a", "z"}

print("A => ", A)
X = A.discard(l)
print("A => ", A)
