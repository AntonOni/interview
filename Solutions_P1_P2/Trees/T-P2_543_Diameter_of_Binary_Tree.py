
class TreeEl():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Один это влево, два это вправо корень всегда 0

a0 = TreeEl(0)
a1 = TreeEl(1)
a2 = TreeEl(2)
a11 = TreeEl(11)
a12 = TreeEl(12)
a21 = TreeEl(21)
a22 = TreeEl(22)
a222 = TreeEl(222)


a0.left = a1
a0.right = a2
a1.left = a11
a1.right = a12
a2.left = a21
a2.right = a22
a22.right = a222

ans = 0


def depth(p):
    global ans
    if not p:
        return 0
    left = depth(p.left)
    right = depth(p.right)
    ans = max(ans, left + right)
    return 1 + max(left, right)






"""
a0
a1
a11
None == 0
None == 0
return 1
a12
None == 0
None == 0
return 1
ans a1 = 2 return 3
a2
a21
None == 0
None == 0
return 1
a22
None == 0
None == 0
return 1
ans a2 = 2 return 3
ans a0 = 6 return 4
"""


depth(a0)
print(ans)


n = 5

def soso(n):
    if n == 0:
        return 1
    return soso(n-1)*n


# class Solution():
#     ans = 0
#     def diameterOfBinaryTree(self, root):
#         self.ans = 1
#         def depth(node):
#             if not node:
#                 return 0
#             L = depth(node.left)
#             R = depth(node.right)
#             self.ans = max(self.ans, L+R+1)
#             return max(L, R) + 1
#
#         depth(root)
#         return self.ans - 1
#



