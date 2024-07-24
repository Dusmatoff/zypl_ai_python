def find_even_numbers(arr):
    even_numbers = [arr[i] for i in range(len(arr)-1, -1, -1) if arr[i] % 2 == 0]
    k = len(even_numbers)
    return even_numbers, k

arr = [10, 21, 4, 45, 66, 93, 11]
even_numbers, k = find_even_numbers(arr)
print(f"Even numbers in reverse index order: {even_numbers}")
print(f"Count of even numbers: {k}")
