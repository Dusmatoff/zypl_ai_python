import math


def TrianglePS(a):
    # Calculate the perimeter
    p = 3 * a

    # Calculate the area
    s = (a ** 2 * math.sqrt(3)) / 4

    # Return the perimeter and area
    return p, s


# Example usage
a1 = 5
a2 = 10
a3 = 7

p1, s1 = TrianglePS(a1)
p2, s2 = TrianglePS(a2)
p3, s3 = TrianglePS(a3)

print(f"Equilateral triangle with side {a1}:")
print(f"Perimeter: {p1}")
print(f"Area: {s1:.2f}")

print(f"\nEquilateral triangle with side {a2}:")
print(f"Perimeter: {p2}")
print(f"Area: {s2:.2f}")

print(f"\nEquilateral triangle with side {a3}:")
print(f"Perimeter: {p3}")
print(f"Area: {s3:.2f}")
