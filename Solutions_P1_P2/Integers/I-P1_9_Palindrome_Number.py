

num = 1112

def solve():
    num_l = list(str(num))
    if num_l[0] == "-":
        return False
    mid = len(num_l) // 2
    right = num_l[mid:]
    left = num_l[:mid]
    if len(right) > len(left):
        right.pop(0)
    left.reverse()
    if right == left:
        return True
    else:
        return False

print(solve())


