"""
Найти сколько раз символы из J встречаются в S
Например:
Input: J = "aA", S = "aAAbbbb"
Output: 3

"""

L = "aAAbbbb"
S = "aA"

def solve():
    result = 0
    for i in L:
        if i in S:
            result += 1
    return result

print(solve())