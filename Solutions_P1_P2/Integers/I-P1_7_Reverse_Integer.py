"""
Перевернуть число
Например:
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
"""

n = -670

def solve():
    n_list = list(str(n))
    minus = []
    if n_list[0] == "-":
        minus_el = n_list.pop(0)
        minus.append(minus_el)
    n_list.reverse()
    if len(minus) > 0:
        n_list.insert(0, minus[0])
    final = int("".join(n_list))
    if 2 ** 31-1 > final > -2 ** 31:
        return final
    else:
        return False

print(solve())

