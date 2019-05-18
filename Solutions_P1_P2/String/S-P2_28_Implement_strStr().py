"""
Найти индекс где входит подсторока в строку первый раз. Если не входит нигде вернуть -1
Например:
Input: haystack = "hello", needle = "ll"
Output: 2
Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

string = "mahahamahauahamahaayahamahdaa"
part = "mahd"



def solve(string, part):
    try:
        return string.index(part)
    except:
        print("Not found")

print(solve(string, part))



def second():
    for i in range(len(string) - len(part)):
        n = 0
        for x in range(0, len(part)):
            if string[i + x] == part[x]:
                n += 1
        if n == len(part):
            return i

# print(second())


# print(solve())







