"""
Проверить является ли строка полиндромом
Например:
Input: "A man, a plan, a canal: Panama"
Output: true
"""

import string

# Do you have spaces?
# Do you have capital letters?
# Do you have any dots or special symbols?

s = "A man, a plan, a canal: Panama"

def solve_1(s):
    list_s = list(s.lower())
    for i in s:
        if i.isalpha() is False:
            list_s.remove(i)
    mid = len(list_s)//2
    right = list_s[mid:]
    left = list_s[:mid]
    if len(right) > len(left):
        right.pop(0)
    left.reverse()
    if right == left:
        return True
    else:
        return False


print(solve_1(s))