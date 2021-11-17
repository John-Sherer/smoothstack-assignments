import numpy as np


def exercise_one():
    print('2.')
    zeroes = np.zeros(10)
    print(zeroes)

    print('\n3.')
    ones = np.ones(10)
    print(ones)

    print('\n4.')
    fives = np.ones(10) * 5
    print(fives)

    print('\n5.')
    spread = np.arange(10, 51)
    print(spread)

    print('\n6.')
    even_spread = np.arange(10, 51, 2)
    print(even_spread)

    print('\n7.')
    matrix = np.random.rand(3, 3) * 8
    print(matrix)

    print('\n8.')
    identity = np.eye(3)
    print(identity)

    print('\n9.')
    print(np.random.random(1))


if __name__ == '__main__':
    exercise_one()
