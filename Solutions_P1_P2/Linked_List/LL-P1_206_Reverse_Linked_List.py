"""
+
Перевернуть связанную строку. Представим что элементы с 1 по 5 связанны между собой
NULL (None) это конец
Например:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""



class List1():
    def __init__(self, x):
        self.value = x
        self.next = None


a1 = List1(1)
a2 = List1(2)
a3 = List1(3)
a4 = List1(4)
a5 = List1(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5


class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            next_e = head.next # Запоминаем следующий элеменБ потому что будем перезаписывать curr_node.next
            head.next = prev  # Сама перезапись происходит тут
            prev = head  # Перезаписываем prev_node для того чтобы на каждой итерации было новое значение предыдущего
            head = next_e  # Шаг вперед
        return prev

s = Solution()
h = s.reverseList(a1)

while h:
    print(h.value)
    h = h.next


