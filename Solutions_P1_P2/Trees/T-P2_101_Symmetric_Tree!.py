


class TreeEl():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Один это влево, два это вправо корень всегда 0

a0 = TreeEl(0)
a1 = TreeEl(1)
a2 = TreeEl(1)
a11 = TreeEl(11)
a12 = TreeEl(11)
a21 = TreeEl(11)
a22 = TreeEl(11)


a0.left = a1
a0.right = a2
a1.left = a11
a1.right = a12
a2.left = a21
a2.right = a22


# def isSymmetric1(root):
#     # if not root:
#     #     return True
#
#     stack_left = [root]
#     stack_right = [root]
#     while stack_left and stack_right:
#         current_left = stack_left.pop(-1)
#         current_right = stack_right.pop(-1)
#         if current_left.val != current_right.val:
#             return False
#         if current_left.left:
#             if not current_right.right:
#                 return False
#             stack_left.append(current_left.left)
#             stack_right.append(current_right.right)
#         if current_left.right:
#             if not current_right.left:
#                 return False
#             stack_left.append(current_left.right)
#             stack_right.append(current_right.left)
#     return stack_left == [] and stack_right == []



def isSymmetric(root):
    left_stack = [root.left]
    right_stack = [root.right]

    while left_stack and right_stack:
        left = left_stack.pop(-1)
        right = right_stack.pop(-1)

        if left is None or right is None: # Если один из элементов либо оба являются None (крайние узлы)
            if left != right: # Если один из узлов не ровняется другому - провал
                return False
            else:
                continue # Если ровняется - вернутся к началу цикла

        elif left.val != right.val:
            return False

        else:
            left_stack.append(left.left)
            left_stack.append(left.right)
            right_stack.append(right.right)
            right_stack.append(right.left)
    return True

print(isSymmetric(a0))


"""
    1
   / \
  2   2
 / \ / \
3  4 4  3

"""







