def arithmetic_mean_of_subarray(arr, k, l):
    # Adjust indices for 0-based indexing
    start_index = k - 1
    end_index = l

    # Extract the subarray from index k to l
    subarray = arr[start_index:end_index]

    # Calculate the sum of the subarray
    subarray_sum = sum(subarray)

    # Calculate the number of elements in the subarray
    num_elements = len(subarray)

    # Calculate the arithmetic mean
    if num_elements == 0:
        return 0  # Handle the edge case where there are no elements
    arithmetic_mean = subarray_sum / num_elements

    # Return the arithmetic mean
    return arithmetic_mean


# Example usage
array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
k = 3
l = 7
mean = arithmetic_mean_of_subarray(array, k, l)
print(f"The arithmetic mean of elements from index {k} to {l} is: {mean:.2f}")

# Another example
k = 1
l = 10
mean = arithmetic_mean_of_subarray(array, k, l)
print(f"The arithmetic mean of elements from index {k} to {l} is: {mean:.2f}")
