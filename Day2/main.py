def exercise_three():
    print("Coding Exercise 3:")

    print("1.")
    print('Hello World'[-3])

    print("\n2.")
    print('thinker'[2:5])
    print("if s = 'hello', the output of s[1] is 'e'")

    print("\n3.")
    print("if s = 'Sammy', the output of s[2:] is 'mmy'")

    print("\n4.")
    letter_set = set('Mississippi')
    print(letter_set)

    print("\n5.")
    num_lines = int(input("input data:\n"))
    results = ""
    phrases = []
    for i in range(0, num_lines):
        phrases.append(input())

    print("\nanswer:")

    for phrase in phrases:
        phrase = phrase.lower()
        index = 0
        rev_index = len(phrase) - 1
        result = 'Y'
        while index < rev_index:
            if not phrase[index].isalpha():
                index += 1
            elif not phrase[rev_index].isalpha():
                rev_index -= 1
            elif phrase[index] != phrase[rev_index]:
                result = 'N'
                rev_index = -1
            else:
                index += 1
                rev_index -= 1
        results += result + " "
    print(results[:-1])

    print("\n\n")


def exercise_four():
    print("Coding Exercise 4:")
    print("1.")
    assorted_list = [12, "twelve", 1.2]
    for item in assorted_list:
        print(item)

    print("\n2.")
    nested_list = [1, 1, [1, 2]]
    print("Use multiple indices, as in 'nested_list[2][1]")
    print(nested_list[2][1])

    print("\n3.")
    print("The result is ['b', 'c']")
    print(['a', 'b', 'c'][1:])

    print("\n4.")
    week = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
    for day in week:
        print(day, week[day])

    print("\n5.")
    print("If D = {'k1': [1, 2, 3]}, then D[k1][1] is 2")
    D = {'k1': [1, 2, 3]}
    print(D['k1'][1])

    print("\n6.")
    print("You can")
    tuple_version = tuple([1, [2, 3]])
    for item in tuple_version:
        print(item)
    # The following line would cause an error
    # tuple_version[0] = 0

    print("\n7.")
    letter_set = set('Mississippi')
    print(letter_set)

    print("\n8.")
    print("Yes, using the .add() method.")
    letter_set.add("X")
    print(letter_set)

    print("\n9.")
    print("The output will be coerced into a set, and remove duplicates as follows:")
    print(set([1, 1, 2, 3]))

    print("\nQuestion 1:")
    output_string = ""
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            output_string += str(i) + ","
    print(output_string[:-1])

    print("\nQuestion 2:")
    x = int(input("input:\n"))
    print(factorial(x))

    print("\nQuestion 3:")
    i = int(input("input:\n"))
    dictionary = {}
    for i in range(1, i+1):
        dictionary[i] = i*i
    print(dictionary)

    print("\nQuestion 4:")
    user_list = input("input:\n").split(",")
    user_tuple = tuple(user_list)
    print(user_list, "\n", user_tuple)

    print("\nQuestion 5:")
    object1 = StringObject()
    object2 = StringObject()

    object1.getString()
    object2.getString()

    object1.printString()
    object2.printString()


def factorial(x):
    if x == 2:
        return 2
    return x * factorial(x - 1)

class StringObject:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("input:\n")

    def printString(self):
        print(self.string.upper())

if __name__ == '__main__':
    exercise_three()
    exercise_four()
