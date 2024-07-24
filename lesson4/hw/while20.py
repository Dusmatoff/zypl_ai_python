def contains_digit_two(n):
    # Initialize a flag for the presence of the digit "2"
    has_two = False

    # Loop through the digits of the number
    while n > 0:
        # Get the last digit
        digit = n % 10

        # Check if the digit is "2"
        if digit == 2:
            has_two = True
            break

        # Remove the last digit
        n //= 10

    # Print the result
    if has_two:
        print("TRUE")
    else:
        print("FALSE")


# Example usage
n = 12345
contains_digit_two(n)

n = 6789
contains_digit_two(n)
