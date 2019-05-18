"""
Найти индексы двух чисел сумма коих является указанным числом
Например:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

nums = [7, 1, 4, 5, 6, 15, 8]

target = 15

# What you want to return: couple of indexes or elements?
# Do you want to return all matches or just first couple?

def solve():
    res = []
    for i in range(0, len(nums)):
        for a in range(i+1, len(nums)):
            if nums[i] + nums[a] == target:
                res.append([i, a])
                # res.append([nums[i], nums[a]])
    return res

print(solve())



