"""
Проверка является ли число счастливым.
Например:
Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

s = 82




def solve(s):
    try:
        str_s = str(s)
        result = []
        for i in str_s:
            a = int(i) * int(i)
            result.append(a)
        if sum(result) != 1:
            return solve(sum(result))
        else:
            return True
    except:
        return False

print(solve(s))







