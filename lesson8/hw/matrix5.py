def create_arithmetic_matrix(given_set, m, n, d):
    # Initialize the matrix with size m x n
    matrix = [[0] * n for _ in range(m)]

    # Fill the first column with the given set
    for i in range(m):
        matrix[i][0] = given_set[i]

    # Fill the rest of the columns to form an arithmetic progression
    for col in range(1, n):
        for row in range(m):
            matrix[row][col] = matrix[row][col - 1] + d

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Example usage
given_set = [2, 4, 6, 8]
m = len(given_set)
n = 5
d = 3

matrix = create_arithmetic_matrix(given_set, m, n, d)
print_matrix(matrix)
