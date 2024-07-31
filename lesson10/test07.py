def print_me(s):
    my_str = str(s)
    s2 = '-'.join(my_str)
    print(f"*** {s2} ***")

my_input = input("Сатр: ")
print_me(my_input)