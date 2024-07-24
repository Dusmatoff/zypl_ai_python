def PowerA234(A, B, C, D):
    # Calculate the second, third, and fourth powers of A
    B = A ** 2
    C = A ** 3
    D = A ** 4

    # Return the results
    return B, C, D


# Example usage
A = 2
B, C, D = PowerA234(A, None, None, None)

print(f"Second power of {A}: {B}")
print(f"Third power of {A}: {C}")
print(f"Fourth power of {A}: {D}")
