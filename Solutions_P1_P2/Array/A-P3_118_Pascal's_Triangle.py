

n = 5

def triangle(n):
    result = []
    pend = [1]
    for i in range(0, n):
        result.append(pend)
        pend = [1] + [pend[k] + pend[k+1] for k in range(len(pend) - 1)] + [1]
    return result
print(triangle(n))

a =