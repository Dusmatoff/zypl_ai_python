def arithmetic_operation(n, a, b):
    if b == 0 and n == 4:
        return "Error: Division by zero is not allowed."

    match n:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case 4:
            return a / b
        case _:
            return "Invalid operation number. It should be between 1 and 4."


# Примеры использования
n = 1
a = 10
b = 5
print(f"Operation {n} with {a} and {b} results in: {arithmetic_operation(n, a, b)}")

n = 2
a = 10
b = 5
print(f"Operation {n} with {a} and {b} results in: {arithmetic_operation(n, a, b)}")

n = 3
a = 10
b = 5
print(f"Operation {n} with {a} and {b} results in: {arithmetic_operation(n, a, b)}")

n = 4
a = 10
b = 5
print(f"Operation {n} with {a} and {b} results in: {arithmetic_operation(n, a, b)}")

n = 4
a = 10
b = 0
print(f"Operation {n} with {a} and {b} results in: {arithmetic_operation(n, a, b)}")
