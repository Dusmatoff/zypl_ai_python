def DigitCountSum(k):
    # Initialize the count of digits and the sum of digits
    c = 0
    s = 0
    temp = k

    # Calculate the number of digits and the sum of digits
    while temp > 0:
        digit = temp % 10
        s += digit
        c += 1
        temp //= 10

    # Print the results
    print(f"Number of digits: {c}")
    print(f"Sum of digits: {s}")


# Example usage with five given integers
numbers = [123, 4567, 89, 1001, 23456]

for number in numbers:
    print(f"\nFor the number {number}:")
    DigitCountSum(number)
