"""
Найти мажорный элемент из списка.
(Мажорный элемент это значит элемент который всегда встречается более чем n/2 случаях,
где n это количество элементов в массиве)
Например:
Input: [2,2,1,1,1,2,2]
Output: 2
"""

import collections


my_list = [1,1,1,1,0,0,0,0,0,1,1]



def solve(my_list):
    max_key = ""
    max_val = 0
    counted = collections.Counter(my_list)
    for i in counted:
        if counted[i] > max_val:
            max_val = counted[i]
            max_key = str(i)
    return max_key


print(solve(my_list))










def solve1():
    res = []
    counted = Counter(my_list)
    keys = list(counted.keys())
    for i in counted:
        if counted[i] > counted[i+1]:
            res.append(i)

    first_key_value = counted[keys[0]]
    second_key_value = counted[keys[1]]

    if first_key_value > second_key_value:
        return keys[0]
    else:
        return keys[1]


# print(solve1())
