
class List():
    def __init__(self, x):
        self.val = x
        self.link = None

a =

a1 = List(1)
a2 = List(2)
a3 = List(7)
a4 = List(4)
a5 = List(5)
a6 = List(6)

a1.link = a2
a2.link = a3
a3.link = a4
a4.link = a5
a5.link = a6

b1 = List(9)
b2 = List(8)
b3 = List(7)
b4 = List(4)
b5 = List(5)
b6 = List(6)

b1.link = b2
b2.link = b3
b3.link = b4
b4.link = b5
b5.link = b6



def solve(a1, b1, skipa=2, skipb=3):
    n = 0
    m = 0
    while a1 and n < skipa:
        a1 = a1.link
        n += 1

    while b1 and m < skipb:
        b1 = b1.link
        m += 1

    len_a = 0
    len_b = 0

    a1_s = a1
    b1_s = b1

    while a1:
        a1 = a1.link
        len_a += 1

    while b1:
        b1 = b1.link
        len_b += 1

    if len_a < len_b:
        while a1_s and b1_s:
            if a1_s.val != b1_s.val:
                b1_s = b1_s.link
            else:
                return a1_s.val
    else:
        while a1_s and b1_s:
            if a1_s.val != b1_s.val:
                a1_s = a1_s.link
            else:
                return b1_s.val

# print(solve(a1, b1))
