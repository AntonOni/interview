"""
+
Данны 2 строки. Написать функцию которая проверяет что одна строка является анограммой другой
(Анограмма - слово или словосочетание, образованное путём перестановки букв)
Например:
Input: s = "anagram", t = "nagaram"
Output: true
"""

s = "anagram"
t = "anamagr"

# Одинаковой ли длинны
# Всю ли длинну хотят

def solve():
    list_1 = list(s)
    list_2 = list(t)
    for i in list_1:
        if i in list_2:
            list_2.remove(i)
    if len(list_2) == 0:
        return True
    else:
        return False


print(solve())


def solve_1():
    s_list = list(s)
    s_list.sort()
    t_list = list(t)
    t_list.sort()
    t_list_set = set(t_list)
    s_list_set = set(s_list)
    result = t_list_set - s_list_set # Лист от листа отнять нельзя, но можно отнять сет от сета.
                                     # А сет просто убирает повторяющиеся элементы массива
    if len(result) == 0:
        return True
    else:
        return False

# print(solve_1())
