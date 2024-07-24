def find_first_less_than_last(arr):
    # Access the last element of the array
    last_element = arr[-1]

    # Iterate through the array up to the second-to-last element
    for i in range(len(arr) - 1):
        # Check if the current element is less than the last element
        if arr[i] < last_element:
            # Print the first such element and exit the function
            print(arr[i])
            return

    # If no such element is found, print 0
    print(0)


# Example usage
array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 25]
find_first_less_than_last(array)

array = [30, 40, 50, 60, 70, 80, 90, 100, 110, 20]
find_first_less_than_last(array)

array = [100, 110, 120, 130, 140, 150, 160, 170, 180, 90]
find_first_less_than_last(array)
