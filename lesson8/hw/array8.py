def find_odd_numbers(arr):
    odd_numbers = [x for x in arr if x % 2 != 0]
    k = len(odd_numbers)
    return odd_numbers, k

arr = [10, 21, 4, 45, 66, 93, 11]
odd_numbers, k = find_odd_numbers(arr)
print(f"Odd numbers: {odd_numbers}")
print(f"Count of odd numbers: {k}")
