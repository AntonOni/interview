"""
Определить если ли в линкед листе цикл
"""

class LinkedList():
    def __init__(self, x):
        self.value = x
        self.next = None


a1 = LinkedList(1)
a2 = LinkedList(2)
a3 = LinkedList(3)
a4 = LinkedList(4)
a5 = LinkedList(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a1



def solve(head):
    res = []
    while head:
        res.append(head)
        head = head.next
        if head in res:
            return True
    return False

print(solve(a1))