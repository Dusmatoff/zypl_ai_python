def number_to_text(n):
    if n < 100 or n > 999:
        return "Invalid number. It should be a three-digit number."

    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    h = n // 100
    t = (n % 100) // 10
    u = n % 10

    result = hundreds[h]

    if t == 1:
        result += " " + teens[u]
    else:
        if t > 0:
            result += " " + tens[t]
        if u > 0:
            result += " " + units[u]

    return result.strip()

# Примеры использования
numbers = [256, 814, 100, 999, 305, 720, 118]
for number in numbers:
    print(f"{number}: {number_to_text(number)}")
