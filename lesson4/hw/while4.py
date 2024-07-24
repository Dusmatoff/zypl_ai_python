def is_power_of_three(n):
    # Check if n is less than or equal to zero
    if n <= 0:
        return False

    # Continue dividing n by 3 while n is greater than 1 and divisible by 3
    while n > 1:
        # If n is not divisible by 3, return False
        if n % 3 != 0:
            return False
        # Divide n by 3
        n //= 3

    # If n is reduced to 1, it is a power of 3
    return True

# Example usage
n = 27
result = is_power_of_three(n)
print(f"Is {n} a power of 3? {result}")

n = 28
result = is_power_of_three(n)
print(f"Is {n} a power of 3? {result}")
