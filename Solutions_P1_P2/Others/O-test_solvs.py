import string
import requests
import time




class LinkedList():
    def __init__(self, x):
        self.val = x
        self.link = None


class Solv():
    def __init__(self, n=5, m=7):
        self.list_n = []
        self.list_m = []
        for i in range(n):
            a = LinkedList(i)
            self.list_n.append(a)
        for x in range(m):
            b =LinkedList(x)
            self.list_m.append(b)
        for a1 in range(len(self.list_n)-1):
            self.list_n[a1].link = self.list_n[a1+1]
        for b1 in range(len(self.list_m)-1):
            self.list_m[b1].link = self.list_m[b1+1]

    def printLinkedLists(self):
        if len(self.list_n) > 0:
            head = self.list_n[0]
            while head:
                print(head.val)
                head = head.link

    def replace(self, a):
        head = self.list_n[0]
        while head:
            if head.link.val == 2:
                next_e = head.link.link
                head.link = a
                a.next = next_e
                break
            head = head.link


# s = Solv()
# a = s.list_n
# b = s.list_m
# a = LinkedList(6)
# x = s.replace(a)
# s.printLinkedLists()



a1 = LinkedList(1)
a2 = LinkedList(7)
a3 = LinkedList(3)
a4 = LinkedList(4)
a5 = LinkedList(8)

b1 = LinkedList(2)
b2 = LinkedList(5)
b3 = LinkedList(9)
b4 = LinkedList(7)
b5 = LinkedList(10)

a1.link = a2
a2.link = a3
a3.link = a4
a4.link = a5
# a5.link = a3

b1.link = b2
b2.link = b3
b3.link = b4
b4.link = b5

num1 = [1,2,3,4,5,6]
num2 = [8, 1, 5, 2, 12]
n1 = 4
n2 = 3

text = "keks"


head = a1

emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]

x = -158

scb = ")()()"

J = "jJ"
S = "ssJjJjJsss"

tag = 115

arr = [8, 1, 5, 7, 12, 2]

n = 15

xl = "XIV"

t = 9




class Solver:
    listArray = []

    def __init__(self, n=1):
        for i in range(n):
            print('append element...')
            self.listArray.append(LinkedList(i))
        for i in range(n - 1):
            self.listArray[i].link = self.listArray[i + 1]


    def printLinkedList(self):
        if len(self.listArray) > 0:
            head = self.listArray[0]
            while head:
                print(head.val)
                head = head.link

    def solveTask(self, *args, **kwargs):
        pass

# s = Solver(5)
# s.printLinkedList()

import collections

lis = [1,1,1,2,2]

def soool():
    counted = collections.Counter(lis)
    print(counted)
    for i in counted:
        if counted[i] % 2 != 0:
            return i


print(soool())

t = 300

def solat(t):
    n = 0
    while n < t:
        resp = requests.get(api)
        content = resp.content["status"]
        if content == "In progress":
            time.sleep(20)
            n += 20
            continue
        if content == "Complited":
            return "Complited"
        if content == "Failed":
            return "Failed"
    return "Failed"





