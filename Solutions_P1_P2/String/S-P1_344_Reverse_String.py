"""
+
Дана строка. Переверните стоку
Например:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

string = "hello"

def solve_1():
    rev_str = []
    for x in range(len(string) - 1, -1, -1):
        rev_str.append(string[x])
    return rev_str


def solve_2():
    list_new = []
    for i in string:
        list_new.insert(0, i)
    return list_new


def solve_3():
    list_s = list(string)
    list_s.reverse()
    my = "".join(list_s)
    return my

print(solve_3())

# print(solve_1())

# print(solve_2())

list1 = [1,3]
list2 = [4,5]


newlist = [(tuple(list1), tuple(list2))]
print(newlist)