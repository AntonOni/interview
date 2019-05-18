"""
+
Дан массив чисел с повторяющимися элементами.
Все элементы повторяются кроме одного. Найти этот один элемент
Например:
Input: [4,1,2,1,2]
Output: 4
"""
import collections


list_1 = [1, 4, 9, 9, 8, 5, 0, 0, 6, 3]


def solve_1(mylist):
    res = []
    counted = collections.Counter(mylist)
    for i in counted:
        if counted[i] == 1:
            res.append(i)
    return res

print(solve_1(list_1))



#
# def solve_2():
#     uniq = []
#     for i in lists:
#         if i not in uniq:
#             uniq.append(i)
#         elif i in uniq:
#             uniq.remove(i)
#     return uniq
#
# # print(solve_2())
#
# def solve_3():
#     duplicate = list.copy()
#     for n in list:
#         c = 0
#         for d in duplicate:
#             if n == d:
#                 c += 1
#         if c == 1:
#             return n
#
# # print(solve_3())