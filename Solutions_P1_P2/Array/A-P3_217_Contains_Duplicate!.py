

inp = [1,2,3,4]





def solve():
    for i in range(0, len(inp)):
        for x in range(i+1, len(inp)):
            if inp[i] == inp[x]:
                return True
    return False

# print(solve())


