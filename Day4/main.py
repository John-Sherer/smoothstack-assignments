def exercise_eight():
    print('1.')
    func()

    print('\n2.')
    func1('Google')

    print('\n3.')
    print(func3('hello', 'goodbye', False))

    print('\n4.')
    print(func4(3, 4))

    print('\n5.')
    print(is_even(9), is_even(202))

    print('\n6.')
    print(strictly_greater(10, 5), strictly_greater(20, 20))

    print('\n7.')
    print(sum_arguments(5, 2, 3))

    print('\n8.')
    print(filter_even(1, 2, 3, 4, 5, 6, 7, 8))

    print('\n9.')
    print(alternate_capitalization("Some crazy looking text"))

    print('\n10.')
    print(conditional_pick_number(4, 8), conditional_pick_number(9, 8))

    print('\n11.')
    print(same_starting_char("apple", "Arnold"), same_starting_char("Pear", "Rebecca"))

    print('\n12.')
    print(mirror_about_seven(5), mirror_about_seven(10))

    print('\n13.')
    print(capitalize_first_and_fourth("capitalize these!"), capitalize_first_and_fourth("me!"))


def func():
    print('Hello World')


def func1(name):
    print('Hi My name is ' + name)


def func3(x, y, z):
    if z:
        return x
    return y


def func4(x, y):
    return x * y


def is_even(x):
    return x % 2 == 0


def strictly_greater(x, y):
    return x > y


def sum_arguments(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result


def filter_even(*numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result


def alternate_capitalization(string):
    result = ""
    # Ignore non-alpha
    even = False
    for s in string:
        if s.isalpha():
            if even:
                result += s.upper()
            else:
                result += s.lower()
            even = not even
        else:
            result += s
    return result


def conditional_pick_number(x, y):
    if x % 2 == 0 and y % 2 == 0:
        if x < y:
            return x
        return y
    if x > y:
        return x
    return y


def same_starting_char(string1, string2):
    return string1[0].lower() == string2[0].lower()


def mirror_about_seven(x):
    dist = x - 7
    return 7 - dist * 2


def capitalize_first_and_fourth(string):
    if len(string) >= 4:
        return string[0].upper() + string[1:3] + string[3].upper() + string[4:]
    return string[0].upper() + string[1:]


def exercise_nine():
    print('\n2.')
    # Order number, title & author, quantity, and price per item
    ledger = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
              [98762, 'Programming Python, Mark Lutz', 5, 56.80],
              [77226, 'Head First Python, Paul Barry', 3, 32.95],
              [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

    tuple_ledger = map(order_to_tuple, ledger)
    print(list(tuple_ledger))

    print('\n3.')
    ledger2 = [[34587, ('Learning Python, Mark Lutz', 4, 40.95), ('Programming Python, Mark Lutz', 5, 56.80)],
               [77226, ('Head First Python, Paul Barry', 3, 32.95), ('Einfuhrung in Python3, Bernd Klein', 3, 24.99)]]
    tuple_ledger2 = map(order_to_tuple2, ledger2)
    print(list(tuple_ledger2))


def order_to_tuple(order_list):
    result = (order_list[0], order_list[2] * order_list[3])
    return result


def order_to_tuple2(order_list):
    amount = 0
    for item in order_list[1:]:
        amount += item[1] * item[2]
    result = (order_list[0], amount)
    return result


if __name__ == '__main__':
    exercise_eight()
    exercise_nine()
