"""
+
Дан неупорядоченный массив от 0 до n. Найти недостоющий элемент.
Например:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""

my_list = [9,6,4,2,3,5,7,0,1]


# Is list starts from 0?
# Is list sorted?
# Is it just one missing symbol?


def solve():
    res = []
    max_el = max(my_list)
    min_el = min(my_list)
    for i in range(min_el, max_el):
        if i not in my_list:
            res.append(i)
    return res

print(solve())