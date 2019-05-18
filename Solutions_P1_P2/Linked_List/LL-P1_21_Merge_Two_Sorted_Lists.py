"""
Соеденить два линкед листа.
Например:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class List():
    def __init__(self, x):
        self.val = x
        self.link = None


a1 = List(1)
a2 = List(2)
a3 = List(3)

a1.link = a2
a2.link = a3

b1 = List(1)
b2 = List(5)
b3 = List(6)

b1.link = b2
b2.link = b3






head = a1


def mergeTwoLists1(a1, b1):
    dummy = List(0)
    while a1 and b1:
        if a1.val < b1.val:
            dummy.link = a1
            a1 = a1.link
        else:
            dummy.link = b1
            b1 = b1.link
        dummy = dummy.link
    dummy.link = a1 or b1
    return dummy.link

# while head:
#     print(head.val)
#     head = head.link

mergeTwoLists1(a1, b1)



#
# def merger(a1, b1):
#
#     if a1 is None:
#         return b1
#
#     elif b1 is None:
#         return a1
#
#     elif a1.value < b1.value:
#         a1.link = merger(a1.link, b1)
#         return a1
#
#     else:
#         b1.link = merger(a1, b1.link)
#     return b1
#
#
# head = merger(a1, b1)
#
#
#
#
# # recursively
# def mergeTwoLists(l1, l2):
#     if not l1 or not l2:
#         return l1 or l2
#     if l1.val < l2.val:
#         l1.next = mergeTwoLists(l1.next, l2)
#         return l1
#     else:
#         l2.next = mergeTwoLists(l1, l2.next)
#         return l2










