

list1 = ["flo","fliwer","flowht"]


def solve(list1):
    list1.sort(key=len)
    word = list1[0]
    n = 0
    while n <= len(word):
        for i in list1:
            if word[:n] != i[:n]:
                return word[:n-1]
        n += 1
    return word

print(solve(list1))

