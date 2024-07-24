def number_to_text(n):
    if n < 10 or n > 90 or n % 10 != 0:
        return "Invalid number. It should be between 10 and 90 and multiple of 10."

    match n:
        case 10:
            return "десять задач"
        case 20:
            return "двадцать задач"
        case 30:
            return "тридцать задач"
        case 40:
            return "сорок задач"
        case 50:
            return "пятьдесят задач"
        case 60:
            return "шестьдесят задач"
        case 70:
            return "семьдесят задач"
        case 80:
            return "восемьдесят задач"
        case 90:
            return "девяносто задач"
        case _:
            return "Invalid number. It should be between 10 and 90."

for n in range(10, 100, 10):
    print(f"{n}: {number_to_text(n)}")
