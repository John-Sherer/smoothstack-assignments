from random import randrange

def exercise_seven():
    print('1.')
    results = list(range(1500 + 35 - 1500 % 35, 2701, 35))
    print(results)

    print('\n2.')
    print('celsius to fahrenheit:')
    celsius = 100
    fahrenheit = celsius * (9/5.0) + 32
    print('{} degree celsius = {} degree fahrenheit'.format(celsius,fahrenheit))
    fahrenheit = 80
    celsius = (fahrenheit - 32) * (5/9.0)
    print('{} degree fahrenheit = {} degree celsius'.format(celsius, fahrenheit))

    print('\n3.')
    random_answer = randrange(9) + 1
    guess = int(input("Guess the number:"))
    while guess != random_answer:
        if guess < 1 or guess > 9:
            print("Guess must be between 1 and 9, inclusive")
        else:
            print("Sorry, incorrect.")
        guess = int(input("Guess the number:"))
    print("Well guessed!")
    return
    # exit(0) could be used here as well


def exercise_seven_continued():
    print('\n4.')
    for i in range(1, 10):
        output = ""
        for j in range(1, 6-abs(i-5)):
            output += "*"
        print(output)

    print('\n6.')
    reversible = input("input string to reverse:\n")
    backwards = ""
    for i in range(0, len(reversible)):
        backwards += reversible[-(i+1)]
    print(backwards)

    print('\n7.')
    sequence = input("input a sequence of comma separated numbers:\n").split(',')
    odds = 0
    evens = 0
    for i in sequence:
        if int(i) % 2 == 0:
            evens += 1
        else:
            odds += 1
    print('Number of even numbers :', evens)
    print('Number of odd numbers :', odds)

    print('\n8.')
    sample_list = [100, 3.14, 'One hundred', True, [0, 1], (0, 1), {0, 1}, {0: 0, 1: 10}]
    for item in sample_list:
        print("Item = '{}', type = '{}'".format(item, type(item)))

    print('\n8.')
    output_string = ""
    for i in range(0, 7):
        if i == 3 or i == 6:
            continue
        output_string += str(i) + " "
    print(output_string[:-1])


if __name__ == '__main__':
    exercise_seven()
    exercise_seven_continued()
