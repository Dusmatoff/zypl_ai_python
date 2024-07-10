a = 12
b = 9
c = -7

positive_count = 0
negative_count = 0

if a > 0:
    positive_count += 1
elif a < 0:
    negative_count += 1

if b > 0:
    positive_count += 1
elif b < 0:
    negative_count += 1

if c > 0:
    positive_count += 1
elif c < 0:
    negative_count += 1

print(f"Количество положительных чисел: {positive_count}")
print(f"Количество отрицательных чисел: {negative_count}")
