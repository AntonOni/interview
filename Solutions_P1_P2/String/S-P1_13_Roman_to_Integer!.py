"""
+
Перевести римские числа к нормальному виду
Наример:
Input: "III"
Output: 3
Input: "IV"
Output: 4
"""

inp = "MDCCCXLIILC"


def romanToInt(inp):
    res = 0
    n = len(inp) - 1
    number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    exeption = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    while n >= 0:
        if inp[n-1] + inp[n] in exeption:
            res += exeption[inp[n-1] + inp[n]]
            inp = inp[:n-1]
            n -= 2
        elif inp[n] in number:
            res += number[inp[n]]
            inp = inp[:n]
            n -= 1
        else:
            return "Incorrect"
    return res

print(romanToInt(inp))


def solve(inp):
    i = len(inp)-1
    result = 0
    while i >= 0:
        if inp[i] == "V" and inp[i-1] == "I":
            a = 4
            result += a
            inp = inp[:i-1]
            i = i - 2
        elif inp[i] == "X" and inp[i-1] == "I":
            a = 9
            result += a
            inp = inp[:i-1]
            i = i - 2
        elif inp[i] == "L" and inp[i-1] == "X":
            a = 40
            result += a
            inp = inp[:i-1]
            # splited.remove(splited[i-1])
            # splited.remove(splited[i-1])
            i = i - 2
        elif inp[i] == "C" and inp[i-1] == "X":
            a = 90
            result += a
            inp = inp[:i-1]
            i = i - 2
        elif inp[i] == "D" and inp[i-1] == "C":
            a = 400
            result += a
            inp = inp[:i-1]
            i = i - 2
        elif inp[i] == "M" and inp[i-1] == "C":
            a = 900
            result += a
            inp = inp[:i-1]
            i = i - 2
        elif inp[i] == "I":
            a = 1
            result += a
            inp = inp[:i]
            i = i - 1
        elif inp[i] == "V":
            a = 5
            result += a
            inp = inp[:i]
            i = i - 1
        elif inp[i] == "X":
            a = 10
            result += a
            inp = inp[:i]
            i = i - 1
        elif inp[i] == "L":
            a = 50
            result += a
            inp = inp[:i]
            i = i - 1
        elif inp[i] == "C":
            a = 100
            result += a
            inp = inp[:i]
            i = i - 1
        elif inp[i] == "D":
            a = 500
            result += a
            inp = inp[:i]
            i = i - 1
        elif inp[i] == "M":
            a = 1000
            result += a
            inp = inp[:i]
            i = i - 1
        else:
            return "Wrong symbol inputed. You need to use only symbols from list"
    return print(result)

solve(inp)