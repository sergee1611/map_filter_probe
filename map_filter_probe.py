def square(x):
    return x ** 2


def is_odd(x):
    return x % 2


list_1 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
square_list = map(square, list_1)
filtered_list = filter(is_odd, square_list)
print(list(filtered_list))
