def dictionary(a, b, c):
    total = a + b + c
    print(f"The total is: {total}")

if __name__ == "__main__":
    dict_values = {'b': -4, 'c': 100, 'a': -42 }
    dictionary(*dict_values)
    dictionary(**dict_values)