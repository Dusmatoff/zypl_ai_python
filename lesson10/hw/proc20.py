import math


def TriangleP(a, h):
    # Calculate the side length b using the Pythagorean theorem
    b = math.sqrt((a / 2) ** 2 + h ** 2)

    # Calculate the perimeter of the equilateral triangle
    perimeter = 3 * b

    # Return the perimeter
    return perimeter


# Example usage with three sets of base and height
triangles = [
    (6, 5),
    (10, 8),
    (15, 12)
]

for a, h in triangles:
    perimeter = TriangleP(a, h)
    print(f"Base: {a}, Height: {h} -> Perimeter: {perimeter:.2f}")
