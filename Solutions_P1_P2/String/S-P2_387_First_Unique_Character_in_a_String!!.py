"""
Дана строка. Найти первый неповторяющийся символ в этой строке и распечатать его индекс.
Если такого символа нет распечатать -1.
Например:
s = "loveleetcode",
return 2 (2 это индекс буквы v, которая является первым неповторяющимся символом в слове)
"""


s = "loveleetcode"




def solve_():
    list_s = list(s)
    for i in range(0, len(list_s)):
        poped = list_s.pop(i)
        if poped in list_s:
            list_s.insert(i, poped)
        else:
            return poped, i

print(solve_())




# def solve_1():
#     list_s = list(s)
#     n = 0
#     while n < len(list_s)-1:
#         poped = list_s.pop(n)
#         if poped in list_s:
#             list_s.insert(n, poped)
#             n += 1
#         else:
#             return poped, n
#
# print(solve_1())