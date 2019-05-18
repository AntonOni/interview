"""
Удалить указанный элемент из связанного листа
"""


class LinkedList():
    def __init__(self, x):
        self.value = x
        self.next = None


a1 = LinkedList(1)
a2 = LinkedList(2)
a3 = LinkedList(3)
a4 = LinkedList(4)

a = LinkedList(7)

a1.next = a2
a2.next = a3
a3.next = a4

head = a1

j = 2



def delete(head):
    current = head # current добавлен потому что в течении первого while указатель сдвинулся
    while head:
        if head.next.value == 2:
            head.next = head.next.next
            break
        head = head.next

    while current:
        print(current.value)
        current = current.next


# delete(head)

def insert(head, a):
    current = head # current добавлен потому что в течении первого while указатель сдвинулся
    while head:
        if head.next.value == 4:
            next_e = head.next
            head.next = a
            a.next = next_e
            break
        head = head.next

    while current:
        print(current.value)
        current = current.next

# insert(head, a)


def replace(head, a):
    # current = head # current добавлен потому что в течении первого while указатель сдвинулся
    while head:
        if head.next.value == 2:
            next_e = head.next.next
            head.next = a
            a.next = next_e
            break
        head = head.next

    # while current:
    #     print(current.value)
    #     current = current.next

# replace(head, a)
