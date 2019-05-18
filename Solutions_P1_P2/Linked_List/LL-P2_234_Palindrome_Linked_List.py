"""
Определить является ли палиндромом линкед лист
Например:
Input: 1->2->2->1
Output: true
"""


class LinkedList():
    def __init__(self, x):
        self.value = x
        self.next = None

a1 = LinkedList(1)
a2 = LinkedList(2)
a3 = LinkedList(3)
a4 = LinkedList(2)
a5 = LinkedList(1)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

head = a1




def solve(head):
    # current = head
    res = []
    while head:
        res.append(head.value)
        head = head.next
    mid = len(res)//2
    right = res[mid:]
    left = res[:mid]
    if len(right) > len(left):
        right.pop(0)
    left.reverse()

    # while current:
    #     print(current.value)
    #     current = current.next

    if right == left:
        return True
    else:
        return False



print(solve(head))




