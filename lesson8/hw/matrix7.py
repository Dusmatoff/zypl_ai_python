def print_kth_row(matrix, k):
    # Adjust k for 0-based indexing
    row_index = k - 1

    # Check if k is within the valid range
    if row_index < 0 or row_index >= len(matrix):
        print("Invalid row index")
        return

    # Print the k-th row
    row = matrix[row_index]
    print(" ".join(map(str, row)))


# Example usage
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
k = 3

print_kth_row(matrix, k)
