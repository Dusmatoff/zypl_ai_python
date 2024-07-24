def RectPS(x1, y1, x2, y2):
    # Calculate width and height of the rectangle
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    # Calculate perimeter and area
    p = 2 * (width + height)
    s = width * height

    # Print the results
    print(f"Perimeter: {p}")
    print(f"Area: {s}")


# Example usage
# Rectangle 1
x1, y1, x2, y2 = 1, 2, 4, 6
RectPS(x1, y1, x2, y2)

# Rectangle 2
x1, y1, x2, y2 = -3, -2, 2, 1
RectPS(x1, y1, x2, y2)

# Rectangle 3
x1, y1, x2, y2 = 0, 0, 10, 5
RectPS(x1, y1, x2, y2)
