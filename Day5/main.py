

if __name__ == '__main__':
    num_people = int(input('input:\n'))

    pairs = []
    for i in range(0, num_people):
        pairs.append(input("").split(' '))


    results = ""
    for p in pairs:
        bmi = float(p[0]) / (float(p[1])**2)
        if bmi < 18.5:
            results += 'under '
        elif bmi < 25.0:
            results += 'normal '
        elif bmi < 30:
            results += 'over '
        else:
            results += 'obese'

    print(results[:-1])
