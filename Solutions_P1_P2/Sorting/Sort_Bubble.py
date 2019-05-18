


numbers = [11, 0, 1, 3, 98, -1]


def bubble(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for x in range(0, i):
            if numbers[x] > numbers[x+1]:
                numbers[x], numbers[x+1] = numbers[x+1], numbers[x]
                # tmp = num1[x + 1]
                # num1[x + 1] = num1[x]
                # num1[x] = tmp

    return numbers

print(bubble(numbers))

