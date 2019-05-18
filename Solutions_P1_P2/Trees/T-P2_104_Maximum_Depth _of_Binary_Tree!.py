
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

def maxDepth(root):
    stack = [root]
    h = 0
    while stack:
        nextlevel = []
        while stack:
            top = stack.pop(-1)
            if top.left:
                nextlevel.append(top.left)
            if top.right:
                nextlevel.append(top.right)
        stack = nextlevel
        h += 1
    return h


print(maxDepth(a0))








