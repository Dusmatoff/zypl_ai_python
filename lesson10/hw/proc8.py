def AddRightDigit(d, k):
    # Convert k to a string and append d (also converted to a string)
    result = int(f"{k}{d}")
    return result

# Example usage with given numbers d1 and d2
k = 123
d1 = 4
d2 = 7

# Add d1 and print the result
result1 = AddRightDigit(d1, k)
print(f"After adding {d1} to {k}: {result1}")

# Add d2 and print the result
result2 = AddRightDigit(d2, result1)
print(f"After adding {d2} to {result1}: {result2}")
