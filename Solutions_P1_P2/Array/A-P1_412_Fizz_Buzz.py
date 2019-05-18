"""
+
Написать программу которая распечатывает строки от 1 до n.
"""

n = 15

def solve():
    res = []
    for i in range(1, n+1):
        if i % 5 == 0 and i % 3 == 0:
            res.append("FizzBuzz")
        elif i % 5 == 0:
            res.append("Buzz")
        elif i % 3 == 0:
            res.append("Fizz")
        else:
            res.append(str(i))
    return res

print(solve())

