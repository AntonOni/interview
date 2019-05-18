"""
+
Дан массив чисел с нулями. Нужно передвинуть все нули в конец массива.
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

list1 = [0, 1, 0, 3, 12, -1, 4, 0, 9]

# How many zeroes you want into your list?
# In what side you want to move it?



def mover_r(list1):
    n = 0
    while n < len(list1):
        if list1[n] == 0:
            for i in range(n, len(list1)-1):
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
        n += 1
    return list1

# print(mover_r(list1))


def move_l(list1):
    n = 0
    while n < len(list1)-1:
        if list1[n] == 0:
            for i in range(n, 0, -1):
                list1[i], list1[i - 1] = list1[i - 1], list1[i]
        n += 1
    return list1

# print(move_l(list1))


def solve():
    for i in range(len(list1)-1):
        if list1[i] == 0:
            poped = list1.pop(i)
            list1.insert(0, poped)
    return list1

# print(solve())

def solve1():
    for i in range(len(list1)-1):
        if list1[i] == 0:
            poped = list1.pop(i)
            list1.append(poped)
    return list1


# print(solve1())








