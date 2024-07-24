def factorial_sum(n):
    # Initialize the sum and the current factorial value
    total_sum = 0.0
    current_factorial = 1.0

    # Iterate over numbers from 1 to n
    for i in range(1, n + 1):
        # Calculate the factorial iteratively
        current_factorial *= i
        # Add the current factorial to the sum
        total_sum += current_factorial

    # Print the result as a real number
    return total_sum


# Example usage
n = 5
result = factorial_sum(n)
print(f"The sum of factorials from 1! to {n}! is: {result:.6f}")
