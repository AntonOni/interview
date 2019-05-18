"""
Даны 3 вида скобок. (), [], {}. Нужно определить корректность их написания
Например:
Input: "(((())))"
Output: true
Input: "(]"
Output: false
"""

scobs = "([)]"


def solve_1():
    brackets = {"(": ")", "[": "]", "{": "}"}
    opened = ["(", "[", "{"]
    stack = []
    for i in scobs:
        if i in opened:
            stack.append(i)
        elif len(stack) > 0 and i == brackets[stack[-1]]:
            stack.pop(-1)
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

print(solve_1())


def solve():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    for i in scob_list:
        if i == "(":
            counter1 += 1
        elif i == ")":
            counter1 -= 1
        elif i == "[":
            counter2 += 1
        elif i == "]":
            counter2 -= 1
        elif i == "{":
            counter3 += 1
        elif i == "}":
            counter3 -= 1
        if counter1 < 0 or counter2 < 0 or counter3 < 0:
            return False
    if counter1 + counter2 + counter3 == 0:
        return True
    else:
        return False





