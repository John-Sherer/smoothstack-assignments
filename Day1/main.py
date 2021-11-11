def exercise_two():
    print("Coding Exercise 2:")
    print("1.")
    result1 = 50 + 50
    print(result1)
    result2 = 100 - 10
    print(result2)

    print("\n2.")
    # 30+*6 will not execute, because +* is not a valid operation
    print(6 ^ 6)  # Bitwise XOR
    print(6 ** 6)  # Exponential
    print(6 + 6 + 6 + 6 + 6 + 6)  # Operations in sequence

    print("\n3.")
    print("Hello World")
    number = 10
    print("Hello World : {}".format(number))

    print("\n4.")
    # Start by reading user input
    user_input = input("input data:\n").split()
    while not (len(user_input) == 3):
        user_input = input("invalid input, please provide three integers (p, r and l):\n").split()

    p0 = int(user_input[0])
    r = 1 + int(user_input[1]) / 100 / 12
    months = int(user_input[2])
    # General formula for Pn where n = month: R^n(P0 - M/R - M/R^2 - ... - M/R^n) = R^n * P0 - sum{1 to n}(M/R^n)
    # If Pl = 0 (last payment reduced principal to 0), then R^l * P = M * sum{1 to l}(M/R^n)
    # Therefore, M = (R^l * P0) / sum{1 to l}(M/R^n)

    # Couldn't get this accurate, so instead, we brute force
    m = p0
    guess_months = 0
    while guess_months <= months:
        m -= 1
        p = p0
        guess_months = 0
        while p > 0:
            p *= r
            p -= m
            guess_months += 1
        # print("M: {}, months: {}".format(m, guessMonths))
    print("\nanswer:\n{}".format(m+1))


if __name__ == '__main__':
    exercise_two()
