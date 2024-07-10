number = 123

# Проверка, что число является трехзначным
if 100 <= number <= 999:
    # Преобразуем число в строку
    str_number = str(number)

    # Извлекаем цифры числа
    digit1 = str_number[0]
    digit2 = str_number[1]
    digit3 = str_number[2]

    # Проверяем, все ли цифры разные
    if digit1 != digit2 and digit1 != digit3 and digit2 != digit3:
        print(f"Все цифры числа {number} разные.")
    else:
        print(f"Цифры числа {number} не все разные.")
else:
    print("Число должно быть трехзначным.")
