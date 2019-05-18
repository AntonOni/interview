"""
-
Даны 2 листа. Найти множество чисел повторяющиеся в этих 2ух листах
Например:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9] - повторяются в num1 и num2
"""

list_1 = [1, 4, 9, 9, 8, 5, 0, 0, 6, 3]
list_2 = [10, 9, 0, 0, 6, 12, 89]

import collections


def solve():
    res = []
    counts = collections.Counter(list_1)
    for i in list_2:
        if counts[i] > 0:
            res.append(i)
            counts[i] -= 1
    return res

print(solve())

